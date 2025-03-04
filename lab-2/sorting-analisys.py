import random
import time
import matplotlib.pyplot as plt
import matplotlib.animation as animation

def quick_sort_visual(arr, low, high, frames):
    if low < high:
        pi = partition(arr, low, high)
        frames.append(arr.copy())
        quick_sort_visual(arr, low, pi-1, frames)
        quick_sort_visual(arr, pi+1, high, frames)

def partition(arr, low, high):
    pivot = arr[high]
    i = low - 1
    for j in range(low, high):
        if arr[j] <= pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i]
    arr[i+1], arr[high] = arr[high], arr[i+1]
    return i + 1

def merge_sort_visual(arr, frames):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort_visual(arr[:mid], frames)
    right = merge_sort_visual(arr[mid:], frames)
    merged = merge(left, right)
    frames.append(merged.copy())
    return merged

def merge(left, right):
    merged = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1
    merged.extend(left[i:])
    merged.extend(right[j:])
    return merged

def heap_sort_visual(arr, frames):
    n = len(arr)
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
        frames.append(arr.copy())
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        frames.append(arr.copy())
        heapify(arr, i, 0)

def heapify(arr, n, i):
    largest = i
    left = 2*i + 1
    right = 2*i + 2
    if left < n and arr[left] > arr[largest]:
        largest = left
    if right < n and arr[right] > arr[largest]:
        largest = right
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]
        heapify(arr, n, largest)

def bitonic_sort_visual(arr, frames, low, high, ascending=True):
    if high - low <= 1:
        return
    mid = (high - low) // 2
    bitonic_sort_visual(arr, frames, low, low+mid, True)
    bitonic_sort_visual(arr, frames, low+mid, high, False)
    bitonic_merge_visual(arr, frames, low, high, ascending)

def bitonic_merge_visual(arr, frames, low, high, ascending):
    if high - low <= 1:
        return
    mid = (high - low) // 2
    for i in range(low, low + mid):
        if (arr[i] > arr[i + mid]) == ascending:
            arr[i], arr[i + mid] = arr[i + mid], arr[i]
    frames.append(arr.copy())
    bitonic_merge_visual(arr, frames, low, low+mid, ascending)
    bitonic_merge_visual(arr, frames, low+mid, high, ascending)

def generate_random(size):
    return [random.randint(0, 1000) for _ in range(size)]

def animate_sort(frames_list, titles, times):
    fig, axs = plt.subplots(2, 2, figsize=(12, 8))
    axs = axs.flatten()
    bar_rects_list = []

    max_frames = max(len(frames) for frames in frames_list)
    for i in range(len(frames_list)):
        if len(frames_list[i]) < max_frames:
            last_frame = frames_list[i][-1]
            frames_list[i].extend([last_frame]*(max_frames - len(frames_list[i])))

    for i, (frames, title) in enumerate(zip(frames_list, titles)):
        axs[i].set_title(f"{title}\nTime: {times[i]:.4f}s")
        axs[i].set_xlim(0, len(frames[0]))
        axs[i].set_ylim(0, max(frames[0]) + 10)
        bar_rects = axs[i].bar(range(len(frames[0])), frames[0], color='skyblue')
        bar_rects_list.append(bar_rects)

    def update_fig(frame_idx):
        for i, frames in enumerate(frames_list):
            for rect, val in zip(bar_rects_list[i], frames[frame_idx]):
                rect.set_height(val)
        return [rect for rects in bar_rects_list for rect in rects]

    anim = animation.FuncAnimation(fig, update_fig, frames=max_frames, interval=50, repeat=False)
    plt.tight_layout()
    plt.show()

data_size = 32  # power of 2
arr = generate_random(data_size)

algorithms = [
    ("QuickSort", lambda a, f: quick_sort_visual(a, 0, len(a)-1, f)),
    ("MergeSort", lambda a, f: merge_sort_visual(a, f)),
    ("HeapSort", lambda a, f: heap_sort_visual(a, f)),
    ("BitonicSort", lambda a, f: bitonic_sort_visual(a, f, 0, len(a), True))
]

frames_list = []
times = []

for name, algo in algorithms:
    arr_copy = arr.copy()
    frames = [arr_copy.copy()]
    start_time = time.time()
    algo(arr_copy, frames)
    end_time = time.time()
    frames_list.append(frames)
    times.append(end_time - start_time)

animate_sort(frames_list, [name for name, _ in algorithms], times)
import time
import matplotlib.pyplot as plt

def iterative_fib(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a

def measure_time(iterations):
    times = []
    for i in range(iterations):
        start_time = time.time()
        iterative_fib(i)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_results(times):
    plt.plot(range(len(times)), times, label='Iterative Space-Optimized Method')
    plt.xlabel('n-th Fibonacci Term')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Iterative Space-Optimized Method')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    iterations = 10000
    times = measure_time(iterations)
    plot_results(times)
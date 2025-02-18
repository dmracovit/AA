import time
import matplotlib.pyplot as plt

def fast_doubling(n):
    def fib_pair(n):
        if n == 0:
            return (0, 1)
        a, b = fib_pair(n >> 1)
        c = a * (2 * b - a)
        d = a * a + b * b
        if n & 1:
            return (d, c + d)
        else:
            return (c, d)
    return fib_pair(n)[0]

def measure_time(iterations):
    times = []
    for i in range(iterations):
        start_time = time.time()
        fast_doubling(i)
        end_time = time.time()
        times.append(end_time - start_time)
    return times

def plot_results(times):
    plt.plot(range(len(times)), times, label='Fast Doubling Method')
    plt.xlabel('n-th Fibonacci Term')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Fast Doubling Method')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    iterations = 10000
    times = measure_time(iterations)
    plot_results(times)
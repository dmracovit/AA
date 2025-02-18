import time
import matplotlib.pyplot as plt

def fibonacci_generator():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

def get_fibonacci(n):
    fib_gen = fibonacci_generator()
    for _ in range(n + 1):
        fib_num = next(fib_gen)
    return fib_num

def measure_time(iterations):
    times = []
    for i in range(iterations):
        start_time = time.perf_counter()  
        get_fibonacci(i)
        end_time = time.perf_counter()
        times.append(end_time - start_time)
    return times

def plot_results(times):
    plt.plot(range(len(times)), times, label='Generative Approach Using Python Generators')
    plt.xlabel('n-th Fibonacci Term')
    plt.ylabel('Time (seconds)')
    plt.title('Time Complexity of Generative Approach Using Python Generators')
    plt.legend()
    plt.show()

if __name__ == "__main__":
    iterations = 10000
    times = measure_time(iterations)
    plot_results(times)
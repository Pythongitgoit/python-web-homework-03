import multiprocessing
import time


def factorize_sync(*numbers):
    result = []
    for num in numbers:
        divisors = [i for i in range(1, num + 1) if num % i == 0]
        result.append(divisors)
    return result


def factorize_parallel(*numbers):
    num_cores = multiprocessing.cpu_count()
    pool = multiprocessing.Pool(num_cores)
    result = pool.map(factorize_number, numbers)
    pool.close()
    pool.join()
    return result


def factorize_number(num):
    return [i for i in range(1, num + 1) if num % i == 0]


if __name__ == "__main__":
    start_time = time.time()
    a, b, c, d = factorize_sync(128, 255, 99999, 10651060)
    end_time = time.time()
    print(f"Послідовний код виконувався: {end_time - start_time:.5f} секунд")

    start_time = time.time()
    e, f, g, h = factorize_parallel(128, 255, 99999, 10651060)

    end_time = time.time()
    print(f"Багато ядерна версія виконувала: {end_time - start_time:.5f} секунд")

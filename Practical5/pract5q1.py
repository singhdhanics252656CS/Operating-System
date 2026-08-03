import threading

def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    print(f"Factorial of {n} = {result}")

numbers = [4, 5, 6]
threads = []

for n in numbers:
    t = threading.Thread(target=factorial, args=(n,))
    threads.append(t)
    t.start()

for t in threads:
    t.join()

print("All threads completed.")

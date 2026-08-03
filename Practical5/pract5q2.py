import threading

def print_even():
    print("Even numbers:")
    for i in range(2, 11, 2):
        print(i)

def print_odd():
    print("Odd numbers:")
    for i in range(1, 11, 2):
        print(i)

def reverse_string(text):
    print("Reversed string:", text[::-1])

t1 = threading.Thread(target=print_even)
t2 = threading.Thread(target=print_odd)
t3 = threading.Thread(target=reverse_string, args=("Multithreading",))

t1.start()
t2.start()
t3.start()

t1.join()
t2.join()
t3.join()

print("All threads completed.")

print("S113 Dhani Singh")

import threading
import time
import random

BUFFER_SIZE = 5

buffer = [None] * BUFFER_SIZE
front = 0
rear = 0

mutex = threading.Lock()

empty = threading.Semaphore(BUFFER_SIZE) 
full = threading.Semaphore(0)           

ITEMS = 10


def producer():
    global rear

    for item in range(1, ITEMS + 1):
        empty.acquire()

        with mutex:
            buffer[rear] = item
            print(f"Producer produced {item} at position {rear}")

            rear = (rear + 1) % BUFFER_SIZE

        full.release()

        time.sleep(random.uniform(0.5, 1))


def consumer():
    global front

    for _ in range(ITEMS):
        full.acquire()

        with mutex:
            item = buffer[front]
            buffer[front] = None

            print(f"Consumer consumed {item} from position {front}")

            front = (front + 1) % BUFFER_SIZE

        empty.release()

        time.sleep(random.uniform(0.5, 1.5))

producer_thread = threading.Thread(target=producer)
consumer_thread = threading.Thread(target=consumer)

producer_thread.start()
consumer_thread.start()

producer_thread.join()
consumer_thread.join()

print("\nProducer-Consumer execution completed.")

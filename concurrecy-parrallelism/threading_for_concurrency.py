# Using threading for concurrency
import threading
import time

def task(name, duration):
    print(f"Task {name} starting...")
    time.sleep(duration)
    print(f"Task {name} completed.")

if __name__ == "__main__":
    start_time = time.time()

    # Creating threads
    thread1 = threading.Thread(target=task, args=("Task 1", 2))
    thread2 = threading.Thread(target=task, args=("Task 2", 3))
    thread3 = threading.Thread(target=task, args=("Task 3", 1))

    # Starting threads
    thread1.start()
    thread2.start()
    thread3.start()

    # Waiting for threads to complete
    thread1.join()
    thread2.join()
    thread3.join()

    end_time = time.time()
    total_time = end_time - start_time
    print(f"Total time taken: {total_time} seconds")
    print(f"All tasks completed.")
    
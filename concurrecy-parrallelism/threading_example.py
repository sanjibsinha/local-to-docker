import threading
import time

def square_list(numbers):
    result = []
    for n in numbers:
        result.append(n*n)
    return result

def task_thread(numbers):
    print(f"Thread Name: {threading.current_thread().name}")
    squares = square_list(numbers)
    #print("Squares:", squares) # Removing print for brevity, large output
    return squares # Returning for potential use later

if __name__ == "__main__":
    numbers_list = [i for i in range(100000)] # A large list of numbers
    start_time = time.time()

    # Creating threads
    thread1 = threading.Thread(target=task_thread, args=(numbers_list,), name="Thread-1")
    thread2 = threading.Thread(target=task_thread, args=(numbers_list,), name="Thread-2")

    # Starting threads
    thread1.start()
    thread2.start()

    # Waiting for threads to finish
    thread1.join()
    thread2.join()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    print("Both threads are finished")
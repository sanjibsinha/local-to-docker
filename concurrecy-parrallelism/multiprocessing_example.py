# Mutiprocessing : CPU bound tasks
import multiprocessing
import time

def squares_list(numbers):
    result = []
    for i in numbers:
        result.append(i * i)
    return result

def task_process(numbers):
    print(f"Process ID: {multiprocessing.current_process().pid}")
    squares = squares_list(numbers)
    print(f"Squares: {squares}")

if __name__ == "__main__":
    numbers_list = [i for i in range(100000)] # A large list of numbers
    start_time = time.time()

    #Creatng processes
    process1 = multiprocessing.Process(target=task_process, args=(numbers_list,))
    process2 = multiprocessing.Process(target=task_process, args=(numbers_list,))

    # Starting processes
    process1.start()
    process2.start()

    # Waiting for processes to complete
    process1.join()
    process2.join()

    end_time = time.time()
    print(f"Total time taken: {end_time - start_time:.2f} seconds")
    print(f"All tasks completed. Both processes finished.")
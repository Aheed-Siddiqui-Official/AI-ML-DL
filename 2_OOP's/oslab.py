import multiprocessing
import os
import time

def child_task():
    print(f"Child Process: PID={os.getpid()}, Parent PID={os.getppid()}")
    time.sleep(20)

if __name__ == '__main__':
    # Creating a new process
    p = multiprocessing.Process(target=child_task)
    p.start()
    
    print(f"Parent Process: PID={os.getpid()}")
    
    # Wait for the child to finish (optional)
    # p.join()
    time.sleep(20)

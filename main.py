# Junnan Shimizu
# Project 7 - Semaphores + Dining Philosophers Problem
# 4/13/22

import threading

import philosopher
import semaphore
from buffer import Buffer

my_buffer = Buffer(10)


def producer():
    for item in range(100):
        print("adding item:", item, "\tbuffer length:", len(my_buffer.queue))
        my_buffer.place(item)


def consumer():
    for index in range(100):
        item = my_buffer.remove()
        print("removing item:", item, "\tbuffer length:", len(my_buffer.queue))


if __name__ == '__main__':
    t1 = threading.Thread(target=producer)
    t2 = threading.Thread(target=consumer)

    t1.start()
    t2.start()

    t1.join()
    t2.join()

    # fork1 = semaphore.Semaphore(1)
    # fork2 = sempahore.Semaphore(1)
    # fork3 = threading.Semaphore(1)
    # fork4 = threading.Semaphore(1)
    # fork5 = threading.Semaphore(1)
    #
    # p1 = philosopher.Philosopher(1, fork1, fork5)
    # p2 = philosopher.Philosopher(2, fork2, fork1)
    # p3 = philosopher.Philosopher(3, fork3, fork2)
    # p4 = philosopher.Philosopher(4, fork4, fork3)
    # p5 = philosopher.Philosopher(5, fork5, fork4)
    #
    # t1 = threading.Thread(target=p1.run_all)
    # t2 = threading.Thread(target=p2.run_all)
    # t3 = threading.Thread(target=p3.run_all)
    # t4 = threading.Thread(target=p4.run_all)
    # t5 = threading.Thread(target=p5.run_all)
    #
    # t1.start()
    # t2.start()
    # t3.start()
    # t4.start()
    # t5.start()
    #
    # t1.join()
    # t2.join()
    # t3.join()
    # t4.join()
    # t5.join()



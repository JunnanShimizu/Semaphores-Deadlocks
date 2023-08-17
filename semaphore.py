# Junnan Shimizu
# Project 7 - Semaphores + Dining Philosophers Problem
# 4/13/22

import threading


class Semaphore:
    def __init__(self, counter):
        self.counter = 1
        self.counter = counter
        self.condition = threading.Condition(threading.Lock())

    def acquire(self):
        self.condition.acquire()
        while self.counter < 1:
            self.condition.wait()
        self.counter = self.counter - 1
        self.condition.release()

    def release(self):
        self.condition.acquire()
        self.counter = self.counter + 1
        self.condition.notify(1)
        self.condition.release()

# Junnan Shimizu
# Project 7 - Semaphores + Dining Philosophers Problem
# 4/13/22

import threading
import time
import random
import semaphore


class Buffer:

    def __init__(self, size):
        self.size = size
        self.queue = []
        self.lock = threading.Lock()
        self.full = semaphore.Semaphore(0)
        self.empty = semaphore.Semaphore(self.size)

    def place(self, item):
        self.empty.acquire()

        self.lock.acquire()
        self.queue.append(item)
        self.lock.release()

        self.full.release()

    def remove(self):
        self.full.acquire()

        self.lock.acquire()
        item = self.queue.pop(0)
        self.lock.release()

        self.empty.release()

        return item

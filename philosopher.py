# Junnan Shimizu
# Project 7 - Semaphores + Dining Philosophers Problem
# 4/13/22

import random
import threading
import time

import semaphore


class Philosopher (threading.Thread):
    def __init__(self, number, left_fork, right_fork):
        super().__init__()
        self.id = number
        self.left_fork = left_fork
        self.right_fork = right_fork
        self.has_left = False
        self.has_right = False

    def get_id(self):
        return self.id

    def get_left_fork(self):
        return self.left_fork

    def get_right_fork(self):
        return self.right_fork

    def think(self):
        print(self.get_id(), "is thinking...")
        time.sleep(random.uniform(.2, .6))

    def eat(self):
        print(self.get_id(), "is eating...")
        time.sleep(random.uniform(.2, .6))

    def pick_left(self):
        print(self.get_id(), "picking up left fork")
        self.left_fork.acquire()
        self.has_left = True
        time.sleep(.3)

    def pick_right(self):
        print(self.get_id(), "picking up right fork...")
        self.right_fork.acquire()
        self.has_right = True
        time.sleep(.3)

    def drop_left(self):
        print(self.get_id(), "putting down left fork...")
        self.left_fork.release()
        self.has_left = False

    def drop_right(self):
        print(self.get_id(), "putting down right fork...")
        self.right_fork.release()
        self.has_right = False

    def run_all(self):
        for _ in range(5):
            self.think()
            self.pick_left()
            self.pick_right()
            self.eat()
            self.drop_right()
            self.drop_left()
        print(self.get_id(), "is done!")

    def run_even(self):
        for _ in range(5):
            self.think()
            self.pick_right()
            self.pick_left()
            self.eat()
            self.drop_right()
            self.drop_left()
        print(self.get_id(), "is done!")

    def run_odd(self):
        for _ in range(5):
            self.think()
            self.pick_left()
            self.pick_right()
            self.eat()
            self.drop_left()
            self.drop_right()
        print(self.get_id(), "is done!")


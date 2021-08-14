import random
import time
from threading import Thread
import logging


class QuadraticError(Exception):
    pass


class MyThread(Thread):
    def __init__(self, name, a=1, b=1, c=0):
        Thread.__init__(self)
        self.name = name
        self.a = a
        self.b = b
        self.c = c

    def quadratic(self):
        logging.info(f"Thread {self.name} - f = {self.a} * x**2 + {self.b} * x + {self.c}")
        d = self.b ** 2 - 4 * self.a * self.c
        if d > 0:
            x1 = (-self.b + d ** 0.5) / (2 * self.a)
            x2 = (-self.b - d ** 0.5) / (2 * self.a)
            logging.info(f"Thread {self.name}: root1 = {x1}, root2 = {x2}")
            return x1, x2
        elif d == 0:
            x = -self.b / (2 * self.a)
            logging.info(f"Thread {self.name}: root = {x}")
            return x
        elif d < 0:
            logging.info("There are no real roots.")
            return None

    def run(self):
        amount = random.randint(3, 10)
        time.sleep(amount)
        logging.info("%s is running" % self.name)
        try:
            if self.a != 0:
                self.quadratic()
            else:
                raise QuadraticError
        except QuadraticError:
            logging.error("Error. First operator in quadratic equation can not be zero.")
        except TypeError:
            logging.error("Error. Operator must be int or float")

        logging.info("Thread %s: finishing" % self.name)


format_ = "%(asctime)s: %(message)s"
logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")

thread_1 = MyThread("Thread 1", a='zero', b=5, c=3)
thread_2 = MyThread("Thread 2", a=1, b=4, c=3)
logging.info("Threads starting")
thread_1.start()
thread_2.start()

# 14:56:43: Threads starting
# 14:56:51: Thread 2 is running
# 14:56:51: Thread Thread 2 - f = 1 * x**2 + 4 * x + 3
# 14:56:51: Thread Thread 2: root1 = -1.0, root2 = -3.0
# 14:56:51: Thread Thread 2: finishing
# 14:56:52: Thread 1 is running
# 14:56:52: Thread Thread 1 - f = 2 * x**2 + 5 * x + 3
# 14:56:52: Thread Thread 1: root1 = -1.0, root2 = -1.5
# 14:56:52: Thread Thread 1: finishing


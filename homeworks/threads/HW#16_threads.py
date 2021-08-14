# 1. Написати програму яка буде обраховувати два квадратних рівняня одночасно, всі параметри рівняння задати в змінні.

import logging
import threading
import time


def thread_function(name, a, b, c):
    logging.info("Thread %s: starting", name)
    time.sleep(2)
    d = b**2 - 4*a*c
    logging.info(f"Thread {name} - f = {a} * x**2 + {b} * x + {c}")
    if d > 0:
        x1 = (-b + d ** 0.5) / (2*a)
        x2 = (-b - d ** 0.5) / (2*a)
        logging.info(f"Thread {name}: root1 = {x1}, root2 = {x2}")
    elif d == 0:
        x = -b / (2*a)
        logging.info(f"Thread {name}: root = {x}")
    elif d < 0:
        logging.info("there are no real roots")
    logging.info("Thread %s: finishing", name)


format_ = "%(asctime)s: %(message)s"
logging.basicConfig(format=format_, level=logging.INFO, datefmt="%H:%M:%S")
x1 = threading.Thread(target=thread_function, args=(1, 2, 5, 3))
x2 = threading.Thread(target=thread_function, args=(2, 1, 4, 3))
x1.start()
x2.start()

# 13:49:08: Thread 1: starting
# 13:49:08: Thread 2: starting
# 13:49:10: Thread 2 - f = 1 * x**2 + 4 * x + 3
# 13:49:10: Thread 1 - f = 2 * x**2 + 5 * x + 3
# 13:49:10: Thread 2: root1 = -1.0, root2 = -3.0
# 13:49:10: Thread 1: root1 = -1.0, root2 = -1.5
# 13:49:10: Thread 2: finishing
# 13:49:10: Thread 1: finishing




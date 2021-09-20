
# Task2
# Напишіть два генератори:
# 1. на кожній ітерації видає наступний член арифметичної прогресії з кроком d, до тих пір поки число не стане
# більшим ніж n
# 2. на кожній ітерації видає наступний член ряду фібоначі до тих пір поки число не стане більшим ніж k
#
# напишіть event_loop для конкурентного прогресу роботи цих двох генераторів
# (щоб генератори по черзі видавали по 1 числу)


def func_1(number, d, n):
    while number < n:
        number += d
        print("gen 1")
        print("number = ", number)
        yield


def func_2(number, k):
    while number < k:
        print('func_2')
        a, b = 0, 1
        for i in range(number):
            a, b = b, a + b
        print("number 2 = ", a)
        number += 1
        yield


def event_loop():
    gen_1 = func_1(3, 1, 15)
    gen_2 = func_2(2, 8)
    queue = [gen_1, gen_2]

    while True:
        try:
            gen = queue.pop(0)
            next(gen)
            queue.append(gen)
        except StopIteration:
            return 1


if __name__ == '__main__':
    event_loop()

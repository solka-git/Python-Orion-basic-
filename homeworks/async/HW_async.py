# Task1
# написати корутину для знаходження накопичувального середнього арифметичного
# корутина на кожній "ітерації" приймає число, додає його до накопичувальної суми і повертає середнє арифметичне
#
# Приклад роботи
#
# >>> average.send(1)
# 1.0
# >>> average.send(3)
# 2.0
# >>> average.send(6)
# 3.3333333333333335
# >>> average.send(10)
# 5.0

def coroutine(func):
    def wrap(*args, **kwargs):
        gen = func(*args, **kwargs)
        gen.send(None)
        return gen
    return wrap


@coroutine
def average():
    sum = 0
    iter = 0
    arg = yield
    while True:
        iter += 1
        sum += arg
        arg = yield sum / iter


gen = average()
list = [1, 2, 3, 4, 5]

for i in list:
    average = gen.send(i)
print(average)


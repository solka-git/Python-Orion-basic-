"""
Task 2
в файлі task2 збережений список, відкрийте цей файл, прочитайте вміст, і
знайдіть середнє арифметичне чисел що знаходяться в списку

"""
import pickle


def arithmetic_mean(filename):
    with open(filename, "rb") as file:
        obj = pickle.load(file)
        summ = 0
        for i in obj:
            summ += int(i)
        return round(summ/len(obj), 2)


print('Arithmetic mean of numbers in task2: ', arithmetic_mean('task2'))

# Arithmetic mean of numbers in task2:  187.53





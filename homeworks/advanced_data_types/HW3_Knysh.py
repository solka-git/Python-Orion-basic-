# 1. Define the id of next variables:
int_a = 55
str_b = 'cursor'
set_c = {1, 2, 3}
lst_d = [1, 2, 3]
dict_e = {'a': 1, 'b': 2, 'c': 3}

print("int_a id =", id(int_a))
print("str_b id =", id(str_b))
print("set_c id =", id(set_c))
print("lst_d id =", id(lst_d))
print("dict_e id =", id(dict_e))

# 2. Append 4 and 5 to the lst_d and define the id one more time.

print("lst_d id =", id(lst_d))
lst_d.append(4)
lst_d.append(5)
print("lst_d id =", id(lst_d))

# 3. Define the type of each object from step 1.

print("int_a type =", type(int_a))
print("str_b type =", type(str_b))
print("set_c type =", type(set_c))
print("lst_d type =", type(lst_d))
print("dict_e type =", type(dict_e))

# 4*. Check the type of the objects by using isinstance.

print("int_a type = int is ", isinstance(int_a, int))
print("str_b type = str is", isinstance(str_b, str))
print("set_c type = set is", isinstance(set_c, set))
print("lst_d type = list is", isinstance(lst_d, list))
print("dict_e type = dict is", isinstance(dict_e, dict))

#
# String formatting:
# Replace the placeholders with a value:

print(f"Anna has 55 apples and 3 peaches.")
#
# 5. With .format and curly braces {}

print("Anna has {} apples and {} peaches.".format(55, 3))

# 6. By passing index numbers into the curly braces.

print("Anna has {0} apples and {1} peaches.".format(55, 3))

# 7. By using keyword arguments into the curly braces.

print("Anna has {ff} apples and {three} peaches.".format(ff=55, three=3))

# 8*. With indicators of field size (5 chars for the first and 3 for the second)

print("Anna has {0:5} apples and {1:3} peaches.".format("red", "yellow"))

# 9. With f-strings and variables

print(f"Anna has {int_a} apples and {lst_d[2]} peaches.")

# 10. With % operator

print("Anna has %d apples and %s peaches." % (int_a, "yellow"))

# 11*. With variable substitutions by name (hint: by using dict)
#
# Comprehensions:
# (1)
# lst = []
# for num in range(10):
#     if num % 2 == 1:
#         lst.append(num ** 2)
#     else:
#         lst.append(num ** 4)
# print(lst)
#
# (2)
# list_comprehension = [num // 2 if num % 2 == 0 else num * 10 for num in range(10)]
#
# 12. Convert (1) to list comprehension
# 13. Convert (2) to regular for with if-else
#
# (3)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
# print(d)
#
# (4)
# d = {}
# for num in range(1, 11):
#     if num % 2 == 1:
#         d[num] = num ** 2
#     else:
#         d[num] = num // 0.5
# print(d)
#
# (5)
# dict_comprehension = {x: x**3 for x in range(10) if x**3 % 4 == 0}
#
# (6)
# dict_comprehension = {x: x**3 if x**3 % 4 == 0 else x for x in range(10)}
#
# 14. Convert (3) to dict comprehension.
# 15*. Convert (4) to dict comprehension.
# 16. Convert (5) to regular for with if.
# 17*. Convert (6) to regular for with if-else.
#
# Lambda:
#
# (7)
# def foo(x, y):
#     if x < y:
#         return x
#     else:
#         return y
#
# (8)
# foo = lambda x, y, z: z if y < x and x > z else y
#
# 18. Convert (7) to lambda function
# 19*. Convert (8) to regular function
#
# lst_to_sort = [5, 18, 1, 24, 33, 15, 13, 55]
#
# 20. Sort lst_to_sort from min to max
# 21. Sort lst_to_sort from max to min
# 22. Use map and lambda to update the lst_to_sort by multiply each element by 2
# 23*. Raise each list number to the corresponding number on another list:
# list_A = [2, 3, 4]
# list_B = [5, 6, 7]
# 24. Use reduce and lambda to compute the numbers of a lst_to_sort.
# 25. Use filter and lambda to filter the number of a lst_to_sort with elem % 2 == 1.
# 26. Considering the range of values: b = range(-10, 10), use the function filter to return only negative numbers.
# 27*. Using the filter function, find the values that are common to the two lists:
# list_1 = [1,2,3,5,7,9]
# list_2 = [2,3,5,6,7,8]
#
#
#
#

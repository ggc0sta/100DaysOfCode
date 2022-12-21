"""
List comprehension is a shortcut to writing lists

new_list = [new_item for item in list]
"""

# Long version
numbers = [1, 2, 3]
new_list = []
for n in numbers:
    add_1 = n + 1
    new_list.append(add_1)

# List comprehension version
numbers = [1, 2, 3]
new_list = [n + 1 for n in numbers]

name = "Angela"
new_list = [letter for letter in name]
# print(new_list)


# Double items in range
my_range = range(1, 5)
my_new_range = [n * 2 for n in my_range]
print(my_new_range)


"""
Conditional List Comprehension

new_list = [new_item for item in list if test]

"""

# Extract only short names (4 chars)
names = ["Alex", "Beth", "Caroline", "Dave", "Lola", "Freddie", "Elanor"]
short_names = [n for n in names if len(n) <= 4]
print(short_names)

# Make long names UPPERCASE
long_names = [name.upper() for name in names if len(name) > 4]
print(long_names)


# Exercises
# 1. Square numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
squared_numbers = [num ** 2 for num in numbers]
print(squared_numbers)

# 2. Filtering even numbers
numbers = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
result = [num for num in numbers if num % 2 == 0]
print(result)



import random

num_list = []
list_length = 24

while len(num_list) <= list_length:
    new_num = random.randrange(1,100)
    num_list.append(new_num)

num_list.sort(reverse=True)

print(num_list)

"""

[96, 88, 85, 77, 75, 73, 72, 72, 68, 63, 62, 61, 55, 50, 43, 40, 39, 33, 33, 22, 18, 13, 11, 10, 7]
ian@Mac Lab 1 fix % /usr/local/bin/python3 "/Users/ian/Desktop/School Stuff/Spring 2026/COMP 467/Lab 1 fix/main.py"

[98, 97, 97, 94, 93, 90, 87, 86, 80, 79, 70, 63, 63, 61, 60, 47, 42, 41, 34, 29, 27, 25, 16, 3, 1]
ian@Mac Lab 1 fix % /usr/local/bin/python3 "/Users/ian/Desktop/School Stuff/Spring 2026/COMP 467/Lab 1 fix/main.py"

[97, 86, 83, 82, 80, 75, 64, 62, 42, 41, 33, 30, 30, 28, 27, 27, 25, 25, 24, 17, 17, 16, 10, 7, 6]
ian@Mac Lab 1 fix % 

"""
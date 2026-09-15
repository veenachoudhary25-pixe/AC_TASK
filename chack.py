# class Feature_list():
#     def __init__(self,list):
#         self.list = list
# class f:      
#     def __init__(self):
#         self.feature = Feature_list()
#     def feature_list(self):
#         print(", ".join(self.feature))

# list = ["apple", "banana", "mango"]


# c = [1,2,3]

# # n = int(input())
# # print(5+n)
# def sum(a,b):
#     c = 5
#     return c

# num=sum(9,3)
# print(c)

# f = open("open.txt","w")

# # line1 = f.readline()
# # print(line1)
# # a = input()
# # f.write(a)
# from pathlib import Path

# path = Path('/home/ng/Task/guest_book.txt')

# prompt = "\nHi, what's your name? "
# prompt += "\nEnter 'quit' if you're the last guest. "

# guest_names = []
# while True:
#     name = input(prompt)
#     if name == 'quit':
#         break

#     print(f"Thanks {name}, we'll add you to the guest book.")
#     guest_names.append(name)

# # Build a string where "\n" is added after each name.
# file_string = ''
# for name in guest_names:
#     file_string += f"{name}\n"

# path.write_text(file_string)

# def name(a,b):
#     def name_(c,d):
#         print(c,d)
#     name_(a,b)
#     c = f"{a} is {b}"
#     return c
# name = name("jkd","fjdk")
# # print(f"j {name}")
# filename = '/home/ng/Task/open.txt'

# with open(filename, "w") as file_object:

#     h = []

#     for line in file_object:
#         h.append(line)

# print(h)
# try:
#     h = int(input("-"))
#     n = int(input("-"))
#     print(h/n)
# except ( ZeroDivisionError,ValueError):
#     print("it is encorrect!")
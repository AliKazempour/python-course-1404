# first program

# printing text
# print("Hello world!")
# print(2)

# Variable Types

# age = 18  # int
# weight = 96.5 # float
# name = "Ali" # String
# is_good = True # bool

# print(type(age))
# print(type(weight))
# print(type(name))
# print(type(is_good))

# first_name,last_name,age = "Ali","Kazempour",20
# print(first_name)

# x = "Hello python"
# print(type(x))
# x = 22.5
# print(type(x))

# x = 5
# print(type(x))

# x = str(x)
# print(type(x))


a = 10
b = 3

# print(a+b)  # 13
# print(a*b)  # 30
# print(a - b) # 7
# print(a / b) # 3.333...
# print(a//b)
# print(a**b)  # 1000
# print(a % b) # 1

# a = 10
# b = 5
# print(a==b)  # False
# print(a >b)  # True
# print(a>=b)  # True
# print(a<=b) # False
# print(a!=b) # True

# p = True
# q = False
# # print(not(p))

# print (p and q) # False
# print( p or q) # True

# print((2+2==5) and (2*3==6))

# first_name = "Ali"
# last_name = "Kazempour"
# full_name = first_name + " " + last_name
# print(full_name)

# PI = 3.14159
# first_name = input("please enter your first_name : ")
# age = int(input("Please enter your age : "))
# avg = float(input())
# print(first_name)
# print(age)
# print(avg)


# Q1
# ghaede = float(input("please enter a number : "))
# height = float(input("please enter a number : "))
# mojaver = float(input("please enter a number : "))
# s = ghaede * height
# p = 2*(ghaede + mojaver)
# print(s)
# print(p)


# Q3
# x1 = float(input("please enter a number for x1 : "))
# y1 = float(input("please enter a number for y1 : "))
# x2 = float(input("please enter a number  for x2 : "))
# y2 = float(input("please enter a number for y2 : "))

# delta_x = x1 - x2
# delta_y = y1 - y2

# answer = ((delta_x)**2 + (delta_y)**2)**(0.5)
# print(answer)


# grade = float(input("please enter a number : "))
# if grade >=60:
#     print("Pass")
# else:
#     print("Fail")


# weight = float(input("please enter your weight  : "))
# if weight >=90 :
#     print("You are fat")
# else:
#     print("You are not fat")


# x = 7
# if x > 10:
#     print("x is greater than 10")
# elif x > 5:
#     print("x is greater than 5 but less than or equal to 10")
# else:
#     print("x is 5 or less")

# marks = 85
# if marks >= 90:
#     print("Grade: A")
# elif marks >= 80:
#     print("Grade: B")
# elif marks >= 70:
#     print("Grade: C")
# else:
#     print("Grade: D or below")


# x = 1
# if x > 10:
#     pass
# else:
#     print("Fail")


# Q2
# a = int(input("please enter a number for a : "))
# b = int(input("please enter number for b : "))
# c = int(input("please enter number for c :"))

# if a+b>c and a+c>b and b+c>a:
#     print("We can make triangle")
# else :
#     print("We can't")


# Q4

# ax^2 + bx + c = 0
a = int(input("please enter a number for a : "))
b = int(input("please enter a number for b : "))
c = int(input("please enter a number for c : "))
delta = b**2 - 4*a*c
if delta > 0 :
    x1 = (-b + delta**0.5)/2*a
    x2 = (-b-delta**0.5)/2*a
    print(x1)
    print(x2)
elif delta ==0:
    x = -b/2*a
    print(x)
else:
    print("No real roots")


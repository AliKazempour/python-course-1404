# for(int i = 1;i<21;i++) # C++
# print(i)


# i+=1 or i = i + 1

# printing numbers from 1 to 20

# for i in range(1,21):
#     print(i)

# for j in range(100):
#     print(j)


# 2 , 4 , 6 , 8 , ...... , 50

# for i in range(2,51,2):
#     print(i)


# 3 , 6 , 9 , ...... , 102
# for i in range(3,103,3):
#     print(i)


# for i in range(10): # 0 , 1 , 2 , ..... , 9
#     if i == 5:
#         break
#     # print("Number:", i)


# for i in range(10):
#     if i == 5:
#         continue
#     print("Number:", i)


# for i in range(10):
#     if i == 5:
#         pass
#     print("Number:", i)


# n = int(input("please enter a number : "))
# for i in range(1,n+1):
#     if i % 2 == 0 :
#         print(i)


# n = int(input("please enter a number : "))
# for i in range(1,n+1):
#     if i % 2 == 1 :
#         print(i)

# n = int(input("please enter a number : "))
# for i in range(1,n+1):
#     if i % 2 == 0:
#         pass
#     else:
#         print(i)


# 1 + 2 + 3 + 4 + ..... + n = n*(n+1)/2
# n = int(input("please enter a number for n : "))  # 1 + 2 + 3 + 4
# sum = 0
# for i in range(1,n+1):
#     print("Sum:",sum)
#     print("i:",i)
#     sum = sum + i
#     print(sum)
# print(sum)


# Q2
# number = int(input("please enter a number : "))
# if number % 2 == 0 :
#     sum = 0
#     for i in range(2,number+1,2):
#         sum = sum + i
#     print(sum)
# else:
#     sum = 0
#     for i in range(2,number,2):
#         sum = sum + i
#     print(sum)

# ----------------------------------------------

# number = int(input("please enter a number : "))
# sum = 0
# for i in range(2,number+1,2):
#     sum = sum + i
# print(sum)

# --------------------------------------------

# 1 - 2 + 3 - 4 + 5 - 6 + .....
# road1
# sum_even = 0
# sum_odd = 0
# n = int(input("please enter a number : "))
# for i in range(2, n+1, 2):
#     sum_even = i + sum_even
# for i in range(1, n+1, 2):
#     sum_odd = i + sum_odd
# print(sum_odd - sum_even)


# road2
# number = int(input("please enter a number : "))
# sum = 0
# for i in range(1,number+1):
#     if i % 2 == 1 :
#         sum = sum + i
#     else:
#         sum = sum - i
# print(sum)



# Q3
# n = int(input())
# result = 1
# for i in range(1,n+1):
#     result = result*i
# print(result)

# Q4
# x = int(input("please enter a number for x :"))
# n = int(input("please enter a number for  n :"))
# result = 1
# for i in range(n):
#     result = result * x
# print(result)

# nested loop
for i in range(3):
    for j in range(3):
        print(f"i={i}, j={j}")
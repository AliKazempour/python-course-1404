# count = 0
# while count < 5:
#     print("Count is : ", count)
#     count+=1
#     # count = count + 1

# Q6-Session2
# sum = 0
# number = int(input("please enter a number : "))
# while number != 0:
#     sum = sum + number
#     number = int(input("please enter a number : "))
# print(sum)

# Q5-Session2
# number = int(input("please enter a number : "))
# while number > 0 :
#     yekan = number % 10
#     print(yekan)
#     number = number // 10


# number = int(input("please enter a number : "))
# is_prime = True
# if number < 2 :
#     is_prime = False
# elif number == 2 :
#     is_prime = True
# else:
#     for i in range(3,int(number**0.5)+1,2):
#         if number % i == 0:
#             is_prime = False
#             break

# if is_prime:
#     print(number," is a prime number")
# else:
#     print(number," is not a prime number")


# ------------------------------

# name = 'Ali'
# family = "Kazempour"
# text = '''python is one of the best
# programming language in the world'''
# new_text = """python is
# very easy """

# first_name = "Ali"
# last_name = "Kazempour"
# full_name = first_name + " " + last_name
# print(full_name)


# word = "Hello"
# print(word*3)


# text = "Python"
# print(text[-2]) # o
# print(text[:4]) # Pyth
# print(text[1:6:2]) # yhn
# print(text[-5:-1]) #ytho
# print(text[::-1]) # nohtyP


# new_text = "Converts All characters to lowercase"
# print(new_text.capitalize())
# print(new_text.title())
# print(new_text.swapcase())


# sentence = "Python is fun"
# print(sentence.find("is")) # 7
# print(sentence.find("python")) # -1
# print(sentence.find("Python")) # 0
# print(sentence.replace("Python","C++").replace("fun","hard"))


# name = input("please enter your name : ")
# age = int(input("please enter your age : "))
# print(f"{name} is {age} years old . ")

# name = input("please enter your name : ")
# family = input("please enter your family : ")
# age = int(input("please enter your age : "))
# print(f"{name} {family} is {age} years old . ")


# text =  "Python is fun"
# print("Python" in text)


# data = "   Some sample DATA "
# cleaned = data.lower().replace("data", "information")
# print(cleaned)

# empty_list = []
# new_list = ["Ali","Kazempour",20,True,"Zahra",False,19.5]
# print(new_list[0])
# print(new_list[-1])
# new_list[0] = "Abbas"
# new_list[-3] = "Kimia"
# print(new_list)
# new_list.append("apple")
# new_list.insert(0,"Reza")
# new_list.remove(19.5)
# print(new_list)
# # new_list.pop(1)
# # new_list.pop()
# del new_list[0]
# print(new_list)

# new_list = [10,40,25,15,-9,0,75,16,10000]
# new_list.sort()
# print(new_list)


# new_list = [10,40,25,15,-9,0,75,16,10000]
# new_list.sort(reverse=True)
# print(new_list)

# numbers  = [10,40,25,15,-9,0,75,16,10000]
# sorted_numbers = sorted(numbers)
# print(sorted_numbers)

# numbers  = [10,40,25,15,-9,0,75,16,10000]
# numbers.reverse()
# print(numbers)

# list = ["ali", "reza", "reza", 20, 19.75, True, 20, 20, 40, "reza"]
# print(list.index("reza"))
# print(list.count("reza"))
# print(list.count(20))

# new_list = [10, 40, 25, 15, -9, 0, 75, 16, 10000]

# updated_list = list + new_list
# print(updated_list)
# new_list.extend(list)
# print(new_list)
# new_list.clear()
# print(new_list)


# list1 = [1, 2, 3]
# list2 = [4, 5, 6]
# combined = list1 + list2
# print(combined)


# list = ["Ali","Reza",20]
# update = list*3
# print(update)


# matrix = [
#     [4,5,6,7],
#     ["Ali","Reza","Mohammad",20],
#     [1,2]
# ]
# print(matrix[2])
# print(matrix[2][1]).


# fruits = ["apple","orange","banana","cucumber"]
# for fruit in fruits:
#     print(fruit)


#-----------------------------------------

# numbers = [10, 20, 30, 45, 50, 60, 70, 80, 90, 100]
# print(sum(numbers))
# sum = 0
# for number in numbers:
#     sum = sum + number
# print(sum)


#---------------------------------------------

# my_list = [1,2,3,4,5,1,1,2,3]
# element_to_count = int(input("please enter a element from list : "))
# count = 0
# print(my_list.count(element_to_count))
# for element in my_list:
#     if element == element_to_count:
#         count+=1
# print(f"count of {element_to_count} is {count}")


#---------------------------------

my_numbers  = [10,20,30,40,50]
sum = 0
for num in my_numbers:
    sum+=num
avg = sum / len(my_numbers)
print(f"avg is {avg}")


#-------------------------------


numbers = [0, 1, 2, 3, 4, 5]
print(numbers[1:6:2])  # Output: [1, 3, 5]
# print(numbers[:3])   # Output: [0, 1, 2]
# print(numbers[3:])   # Output: [3, 4, 5]
# print(numbers[-3:])  # Output: [3, 4, 5]
print(numbers[::-1])  # Output: [5, 4, 3, 2, 1, 0]

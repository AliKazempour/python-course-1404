# new_tuple = (1,2,3,4)
# my_tuple = 1, 2, 3
# my_tuple = tuple([1,2,3,4])
# my_tuple = (1,)

# print(new_tuple[0])
# print(new_tuple[:2])

# tuple1 = (1, 2, 3)
# tuple2 = (4, 5, 6)
# tuple3 = tuple1 + tuple2
# print(tuple3)

# print(new_tuple*3)
# print(5 in new_tuple) # False
# print(2 in new_tuple) # True

# my_tuple = (1,2,3,4,4,5,6,7,4,4,4)
# # print(my_tuple.count(4))  # 5

# new_tuple = (1,2,3,4,5)
# print(new_tuple.index(1)) # 0
# print(new_tuple.index(3)) # 2
# print(new_tuple.index(4)) # 3


# my_tuple = (10,20,30,40,50)
# total = 0
# for number in my_tuple:
#     total = total + number
# print(total)


# my_tuple = (10,20,30,40,50,60,70)
# total = 0
# for number in my_tuple:
#     total+=number
# avg = total / len(my_tuple)
# print(avg)


##############################################################

# my_set = {1,2,3,4,5}
# new_set = set([1,2,3])
# empty_set = set()

# my_set = {1,2,3,4,5}
# for item in my_set:
#     print(item)


# my_set = {1, 2, 3}
# print(2 in my_set) # True
# print(5 in my_set) # False

# my_set = {1, 2, 3}
# my_set.add(4)
# print(my_set)  # Output: {1, 2, 3, 4}

# my_set = {1, 2, 3}
# my_set.update([4, 5, 6])
# print(my_set)  # Output: {1, 2, 3, 4, 5, 6}

# my_set = {1, 2, 3, 4, 5, 6}
# my_set.remove(2)
# my_set.discard(10)
# print(my_set)


# my_set = {1, 2, 3}
# item = my_set.pop()
# print(item)  # Output: (an arbitrary item from the set)
# print(my_set)  # Output: (set after popping the item)


# my_set = {1, 2, 3}
# my_set.clear()
# print(my_set)  # Output: set()

# set1 = {1, 2, 3}
# set2 = {3, 4, 5}
# print(set1 | set2)
# union_set = set1.union(set2)
# print(union_set)
# print(set1 & set2)
# intersection_set = set1.intersection(set2)
# print(intersection_set)

# print(set1 - set2) # {1, 2}
# print(set2 - set1) # {4, 5}
# difference_set = set1.difference(set2)
# print(difference_set) # {1, 2}

# print(set1 ^ set2) # {1, 2, 4, 5}
# symmetric_difference_set = set1.symmetric_difference(set2)
# print(symmetric_difference_set)

# set1 = {1, 2, 3, 6}
# set2 = {1, 2, 3, 4, 5}
# print(set1.issubset(set2))  # Output: False
# print(set2.issuperset(set1))  # Output: False

# set1 = {1, 2, 3}
# set2 = {4, 5, 6}
# print(set1.isdisjoint(set2))  # Output: True

#######################################################
# Empty dictionary
# my_dict = {}

# Dictionary with integer keys
# my_dict = {1: 'apple', 2: 'orange'}

# Dictionary with mixed keys
# my_dict = {'name': 'John', 1: [2, 4, 3]}
# my_dict = {
#     'name': 'Ali',
#     'family': 'Kazempour',
#     'age': 20,
#     'grades': [10, 19, 20, 20, 19.5]
# }
# Using the dict() method
# my_dict = dict({1:"Ali",2:"Kazempour"})


# Using the dict() method with pairs
# my_dict = dict([("first_name","Ali"),("age",20)])

# Accessing values using keys
# my_dict = {'name': 'Ali', 'age': 20}

# print(my_dict['name']) # Ali
# print(my_dict['age']) # 20 
# my_dict['address'] = "Pirouzi"
# my_dict['age'] = 21
# print(my_dict)
# my_dict.pop("age")
# my_dict.popitem()
# del my_dict['name']
# my_dict.clear()
# print(my_dict)

# my_dict = {'name': 'Ali', 'age': 25, 'job': 'Engineer'}
# keys = my_dict.keys()
# print(keys)
# values = my_dict.values()
# print(values)
# items = my_dict.items()
# print(items)

# my_dict = {
#     "name" : "Ali",
#     "age" : 20 ,
#     "email" : "alikazempoor83@gmail.com",
#     "phone_number" : "09231697327"
# }

# extra_info = {
#     "last_name" : "Kazempour",
#     "email" : "alikazempoor1383@gmail.com",
#     "job" : "Engineer"
# }

# # my_dict.update(extra_info)
# # print(my_dict)

# print(my_dict.get("age")) # 20
# print(my_dict.get("Job")) # None
# print(my_dict.get("Job","Engineer")) # Engineer

####################################
# method 1
# numbers = [10,20,30,40,50,60,10,20,30,40,50,70,10,20]
# number_count = {}

# for number in numbers:
#     if number in number_count:
#         number_count[number] +=1
#     else:
#         number_count[number] = 1

# # print(number_count)
# for element , count in number_count.items():
#     print(f"count of {element} : {count}")
 
######################################

# method 2 
# numbers = [10,20,30,40,50,60,10,20,30,40,50,70,10,20]
# number_count = {}
# for number in numbers:
#     number_count[number] = number_count.get(number,0) + 1

# print(number_count)
# for element , count in number_count.items():
#     print(f"count of {element} : {count}")


##########################################################
# method 3
numbers = [10,20,30,40,50,60,10,20,30,40,50,70,10,20]
number_count = {}
for i in numbers:
    number_count[i] = numbers.count(i)
print(number_count)
for element , count in number_count.items():
    print(f"count of {element} : {count}")    

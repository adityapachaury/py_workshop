# # # # # ###creating an empty dict
# # # # # my_dict = {}

# # # # ###creating dictionory with key-value pairs
# # # # # student = {
# # # # #     "name": "Alice",
# # # # #     "age": 25,
# # # # #     "grade": "A"
# # # # # }

# # # # # ##1. Acccessing dictionary values
# # # # # name = student["name"]
# # # # # age = student["age"]
# # # # # print(name, age)

# # # # # ##2.Modyfying Dictionary values:
# # # # # student["age"] = 25
# # # # # ##3.adding new key-value
# # # # # student["city"] = "Aligarh"
# # # # # print(student)


# # # # # ##4.Iterating Through a Dictionary:
# # # # # for key, value in student.items():
# # # # #     print(f"{key}: {value}")

# # # # # for key in student.keys():
# # # # #     print(f"{key}")
# # # # # for value in student.values():
# # # # #     print(f"{value}")

# # # # # ##5. check if key exists
# # # # # if "age" in student:
# # # # #     print("Age exists in the dictionary.")

# # # # # ##6.squares
# # # # # squares = {num: num**2 for num in range(1, 6)}
# # # # # qube = {num: num**3 for num in range(1, 6)}
# # # # # print(squares)
# # # # # print(qube)

# # # # student = {
# # # #     "name": "Alice",
# # # #     "age": 25,
# # # #     "grade": "A"
# # # # }
# # # # del student["age"]
# # # # print(student)
# # # # grade = student.get("grade", "N/A")
# # # # print(grade)
# # # # student["city"] = "Aligarh"
# # # # print(student) 
# # # # student.get("name")
# # # # print(student.get("name"))
# # # # print(student.get("Army"))

# # # dict1  = {0:10, 1:20}
# # # dict1[2] = 30
# # # print(dict1)


# # # dic1 = {1:10,  2:20}
# # # dic2= {3:30,  4:40}
# # # dic3 = {5:50,  6:60}
# # # dic1.update(dic2)
# # # dic1.update(dic3)
# # # print(dic1)

# # # # #############################################
# # d = {"x": 10, "y": 20, "z": 30}
# # for key, value in d.items():
# #     print(f"{key}: {value}")

# # ##############################################
# # num = {num: num*num for num in range(1,6)}
# # print(num)


# # ##############################################
# # num1 = {x: x**2 for x in range(1,16)}
# # print(num1)

# # ##############################################
# # color_dict = {
# #     'red': '#FF0000',
# #     'green': '#008000',
# #     'black': '#000000',
# #     'white': '#FFFFFF'
# # }
# # for key in sorted(color_dict):
# #     print("%s: %s" %key)

# # ##############################################
# # my_dict1 = {
# #     'data1': 100,
# #     'data2': -54,
# #     'data3': 247
# # }
# # sum_dic = sum(my_dict1.values())
# # print(sum_dic)


# ######################
# d = {1: 10, 2: 20, 3:30, 4:40, 5:50, 6:00}
# num = int(input("Enter you key: "))
# if num in d.values():
#     print("it exists.")
# else:
#     print("it's no exists")

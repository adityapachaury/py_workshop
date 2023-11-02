# #####2.
# dic1 = {
#     "name": "Aditya",
#     "Roll.No.": "03",
#     "Sec": "EA"
# }
# print(dic1)




# #########4.
# my_dict1 = {
#     "Aditya": 10,
#     "Nishant": 9,
#     "Div": 7,
#     "Vikash": 8,
#     "Manish": 4,
#     "Nikhil": 6
# }
# min_dict = min(my_dict1.values())
# max_dict = max(my_dict1.values()) 

# print(min_dict)
# print(max_dict)


# ########3
# name1 = ["Aditya", "Ashish", "Ronit"]
# marks = [20, 20, 20]
# print(dict(zip(name1,  marks))) 


# #####1.
# #creating a class
# class Student:
#    def __init__(self, name, marks):
#        self.name = name
#        self.marks = marks
# stud1 = Student("Aditya", "26")
# stud2 = Student("Ashish", "25")
# stud3 = Student("Krishna", "24")
# stud4 = Student("Ronit", "25")
# stud5 = Student("Suraj", "26")

# print(f"{stud1.name}: {stud1.marks}, {stud2.name}: {stud2.marks}, {stud3.name}: {stud3.marks},  {stud4.name}: {stud4.marks}, {stud5.name}: {stud5.marks}")

# ####################
# class Exam:
#     def __init__(self, Aditya, Ashish, Ronit, Krishna, Suraj):
#         self.Aditya = Aditya
#         self.Ashish = Ashish
#         self.Ronit = Ronit
#         self.Krishna = Krishna
#         self.Suraj = Suraj

# Marks = Exam(26, 25, 23, 25, 24)
# dict1 = vars(Marks)
# print(dict1)
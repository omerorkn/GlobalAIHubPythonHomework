#__author__ = omerorkn

#Obtain information from user
value1 = input("Please login your name :")
value2 = input("Please login your school name :")
value3 = int(input("Please login your age :"))
value4 = float(input("Please login your grade point average :"))
value5 = int(input("Please login your year of experience in Python "))

#Values' types
type1 = type(value1)
type2 = type(value2)
type3 = type(value3)
type4 = type(value4)
type5 = type(value5)

#All informations on the screen
print(50*"=")
print(f"Name :{value1} --> data type :{type1}")
print(50*"=")
print("School : {} --> data type :{}".format(value2,type2))
print(50*"=")
print(f"Age :{value3} --> data type :{type3}")
print(50*"=")
print("GPA : {} --> data type :{}".format(value4,type4))
print(50*"=")
print(f"Python Experience(Year) :{value5} --> data type :{type5}")
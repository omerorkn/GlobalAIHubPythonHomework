#__author__ = omerorkn

import os,time

#Intro
print("Welcome to Global AI HUB User Identification Program!")
time.sleep(3)
input("Please press enter to continue...")

#For screen cleaning
clear = "cls" if os.name == "nt" else "clear"
os.system(clear)

#User's info
name = input("Please login your name :")
last_name = input("Please login your last name :")
age = int(input("Please login your age :"))
bdate = int(input("Please login your year of birth date :"))
info_list = [name , last_name , age , bdate]
print("Wait a few seconds...")
time.sleep(2)
os.system(clear)

#Infos in a list with a 'for' loop
for i in info_list:
	print(i)
	time.sleep(1)

print("Please wait us to decide your condition...!")
time.sleep(2)

#User's info on the screen 
print(""" 				---USER INFO---

			Your Name : {}
			Your Last Name : {}
			Your Age : {}
			Your Birth Year : {}
	""".format(name,last_name,age,bdate))

#Final result with an 'if' 
if (age < 18):
	print("You can't go out because it's too dangerous! ")
	time.sleep(3)
	input("Please press enter to exit...")
	time.sleep(1)
	exit()
elif (age >= 18):
	print("You can go out to the street! ")
	time.sleep(3)
	input("Please press enter to exit...")
	time.sleep(1)
	exit()

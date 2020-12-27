#__author__ = omerorkn


import os,time


#All attributes and methods(OOP Logic)
class StudentSystem():
	def __init__(self,sysname):
		self.sysname = sysname
		self.names = []
		self.courses = []
		self.grades = {"midterm":38,"final":66,"project":89}
		self.score = (self.grades["midterm"]*0.3) + (self.grades["final"]*0.5) + (self.grades["project"]*0.2)
		self.mistake_counter = 0

	def sign_up(self,name):
		if (name in self.names):
			print("This name is in our system already!")
			time.sleep(2.5)
		else:
			self.names.append(name)
			print("Your name added to our system succesfully, you can sign-in!")
			time.sleep(2.5)



	def failed(self):
		return "You failed in class"


	def sign_in(self,name):
		if (name in self.names):
			print("Successfully signed in!")
			print("Welcome {}".format(name))
			time.sleep(2.5)
			course_counter = int(input("How many courses you can take? :"))
			if(course_counter>2 and course_counter<6):
				print("It's a valid number of lessons")
				print("You should type lessons you want on next screen, you can skip extra field(s) with 'enter' button ")
				time.sleep(5)
				os.system(clear)
				course1 = input("Course 1 :")
				self.courses.append(course1)
				course2 = input("Course 2 :")
				self.courses.append(course2)
				course3 = input("Course 3 :")
				self.courses.append(course3)
				course4 = input("Course 4 :")
				self.courses.append(course4)
				course5 = input("Course 5 :")
				self.courses.append(course5)
				lesson_choice = input("Please choose a lesson for look up your grade :")
				time.sleep(1)
				os.system(clear)

				if (lesson_choice in self.courses):
					print("""Your Midterm Exam Grade : {}\nYour Final Exam Grade : {}\nYour Project Exam Grade : {}""".format(self.grades["midterm"],self.grades["final"],self.grades["project"]))
					time.sleep(2)
					
					if(self.score > 90):
						print("Your score is : {}".format(self.score)) 
						print("Congrats! You got an AA")
						time.sleep(4)
						exit()
					elif(self.score > 70 and self.score < 90):
						print("Your score is : {}".format(self.score)) 
						print("You got a BB")
						time.sleep(4)
						exit()
					elif(self.score > 50 and self.score < 70):
						print("Your score is : {}".format(self.score)) 
						print("You got a CC")
						time.sleep(4)
						exit()
					elif(self.score > 30 and self.score < 50):
						print("Your score is : {}".format(self.score)) 
						print("You got a DD")
						time.sleep(4)
						exit()
					elif(self.score < 30):
						print("Your score is : {}".format(self.score)) 
						print("You got a FF :( You failed...")
						time.sleep(4)
						exit()
					else:
						print("Calculation Error!")
						time.sleep(3)
						
				else:
					print("Wrong lesson choice it doesn't exist :(")
			elif(course_counter < 3):
				print(self.failed())
				time.sleep(2.5)
				os.system(clear)
			else:
				print("You can choose maximum 5 course!")
				time.sleep(2)
				os.system(clear)
		else:
			if(self.mistake_counter <= 2):
				self.mistake_counter += 1
				print("Your name isn't in our database. Please first sign-up our system.")
				print("You're directing to menu..")
				time.sleep(3.5)
				os.system(clear)
			elif (self.mistake_counter >= 3):
					print("Please try again later...")
					time.sleep(3)
					exit()



e1 = StudentSystem("-----Global AI HUB Student Management System-----")

#Screen cleaner
clear = "cls" if os.name == "nt" else "clear"
mistake_counter = 0

while True:
	print(e1.sysname)
	print("""
	
		[1] Sign-Up
		[2] Sign-in & Choose Course

		""")
	choice = int(input("Make your choice: "))
	if choice == 1:
		name = input("Please write your name and surname :")
		e1.sign_up(name)
		os.system(clear)
	elif choice == 2:
		name = input("Please write your name and surname correctly :")
		os.system(clear)
		e1.sign_in(name)
	else:
		print("Wrong choice! Please select 1 or 2")
		time.sleep(3)
		os.system(clear)
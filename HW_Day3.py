#__author__ = omerorkn

import os,time,random

clear = "cls" if os.name == "nt" else "clear"

#Intro
print("-----Global AI HUB Hangman Game-----")
name = input("What is your name?:")
print("Welcome {}!".format(name))
input("Please press enter to continue...") 
time.sleep(1.5)
os.system(clear)

#Our words
words = ["machine","deep","learning","global","artificial",
		"intelligence","community","neural","data","science",
		"electronics","hardware","software","engineering"]


lifes = 10



#Before the game screen
print("""NOTE: You have 10 lives in game, be careful :)
WARNING: Your game word's letters will be in a irregular letter order, good luck! {}""".format(name))
input("Please press enter to play...")
time.sleep(1)

print("Let's play!")
time.sleep(1)
os.system(clear)


#Random word choice
game_word = random.choice(words)
word_length = len(game_word)
aaa = ("_ " * word_length)
print(aaa)

#For game word's letters
letters = []

#guess = input("Please type a letter in lower case form :")



#All game stuff
while (lifes > 0):
	guess = input("Please type a letter in lower case form :")
	same_count = game_word.count(guess)
	for i in game_word:
		letters.append(i)
	
	if (guess in letters):
		print("""The word has {} letter of "{}" """.format(same_count,guess))
		bbb = "_ " * (word_length - 1) + guess
		print(bbb)
		word_length -=1
		print("{} word(s) left to victory!".format(word_length))
		
		if (word_length == 0 and lifes > 0):
			print("Congrats! You won!!!")
			print("""Secret word was "{}" and you got this!\nSee you {}! """.format(game_word,name))
			time.sleep(8)
			exit()
	
	else: 
		aaa = ("_ " * word_length)
		print(aaa)
		lifes -= 1
		print("{} lifes remaining!".format(lifes))
		if (lifes == 0):
			print("""You haven't any lives :(\nSee you soon {}""".format(name))
			time.sleep(6)
			exit()
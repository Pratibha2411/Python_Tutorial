# Comment-In, Comment-Out & Learn More

# Just a Simple Program Like: Hello World
print("Hey Everyone, \n Lets Learn Python")

# ---------------------------
# Drawing Shapes with basic Python program
# print("   /|")
# print("  / |")
# print(" /  |")
# print("/___|")


# print("|\   ")
# print("| \  ")
# print("|  \ ")
# print("|___\")


# print(" ___")
# print("|   |")
# print("|   |")
# print("|___|")
# ---------------------------------


# ____________________________________
# Variables & Data Types
# without variable
# print("I'm TaNu, 28 y/o.")
# print("A is for Am & U is for You.")
# print("Its my story 'soul loves souls'.")
# print("I'm Tanu, showing error here can not put Tanu coz: Typo in Tanu.")

# with variable
# can not change everything manually so we use Variables: string,int-numbers etc
# character_name = "TANU"
# character_age = "28"

# character_age = 28 #wrong

# is_Male = True

# is_Female = true  #wrong

# print("I'm " + character_name + character_age + " y/o.")
# print("A is for Am & U is for You.")
# print("Its my story 'souls under souls'.")
# character_name = "Prati"
# print("I'm " + character_name + " showing error here can not put " + character_name + " coz: Typo in Tanu.")


#  ------------------------------
# string in Python
# print("Hey All,Howdy?")

# print("Hey All,\nHowdy?")

# print("Hey All,\"Howdy?")

# print("Hey All,Howdy\Howru?")

# phrase = "Hey Everyone!!!"

# print("Hey All,Howdy?")
# print(phrase)

# adding concatination by using (+ "___")
# print(phrase + " Howdy All?? ")

# String function in Python
# # Using Function (block of code) for modifying string & to get information about string & etc etc

# phrase = "Hey Everyone!!!"

# print(phrase.lower())

# print(phrase.upper())

# print(phrase.isupper())

# print(phrase.upper().isupper())

# print(len(phrase))

# print(phrase[0])

# print(phrase[4])

# print(phrase.index("H"))

# print(phrase.index("E"))

# print(phrase.index("Every"))

# print(phrase.replace("Everyone","All"))

# these were Basic function of Strings in Pyhton for more Google them
# ------------------------------------------

# _________________________________________
# # Numbers & function of numbers in Python

# print(2)
# print(2.89474)
# print(-2.6667777777777)
# print(2 + 6)
# print(2 * 6)
# print(2 / 6)

# print(2 % 6)
# # give uh reminder

# print(2 + 6.234565 * 4)

# print((2 + 6.234565) * 4)

# # to specify order of operations use perenthesis
# print(2 + 6.234565 * 4)

# my_num = -3

# print(my_num)

# print(str(my_num) + " Fav Number")
# converted number into string ^ then able to add string after that

# print(abs(my_num))
# # this will give absolute value

# print(pow(4, 3))
# will give us power solution

# print(max(4,11))
# print(min(4,11))
# print(round(5.1224))

# # Importing Some Math function in python to use more specific math calculation
# from math import *  # here math is know as module in pyhton

# my_num1 = -7

# print(floor(9.24))
# print(ceil(9.24))
# print(sqrt(36))

# # Now search math function on google
# ___________________________

# # ____________________________
# # Getting Input From Users

# # name = input("Enter Your Name: ")
# # print("Heyaaa " + name + "!")

# # taking more than 1 input form user & prompt it
# name = input("Enter Your Name: ")
# age = input("Enter Your Age: ")
# print("Heyaaa " + name + "! You're " + age)

#
# # ________________________

# # _____________________
# # Basic Calculator in Pyhton

# # num1 = input("enter a number: ")
# # num2 = input("enter another number: ")
# # result = num1 + num2
# # print(result)
# # # if you will do something like this getting input from user it'll prompt the number as string coz python assumes that the number is string by default which is giver by user'

# # num1 = input("enter a number: ")
# # num2 = input("enter another number: ")
# # result = int(num1) + int(num2)
# # print(result) # we have to convert numbers (pyhon is assuming'em, as a string) in numbers.
# # but here we can not get decimal number as input this is the problem

# num1 = input("enter a number: ")
# num2 = input("enter another number: ")
# result = float(num1) + float(num2)
# print(result)
# # even if one of the number is decimal it will still work so we'll use float

# # num1 = input("enter a number: ")
# # num2 = input("enter another number: ")
# # result = int(num1) * int(num2)
# # print(result)
# # ____________________

# # _________________________
# # Mad Libs Game

# gender = input("Enter a Gender: ")
# plural_Noun = input("Enter a Plural Noun: ")
# Define_someone = input("Enter something to Define Someone: ")
#
# print("Rose is Redient {gender} " + gender)
# print("{plural Noun} is an Anime Character " + plural_Noun)
# print("Haruhico is Super {Define someone} " + Define_someone)
# # Make Your own Mad libs game with creativity
# # -----------------------------------------

# # -------------------------------
# # Lists in Python

# familyMembers = ["Mum", "Papa", "Bruh","Sis"]

# # print(familyMembers)

# # print(familyMembers[2]) # indexing to get specific value

# # print(familyMembers[0])
# # print(familyMembers[-2])
# # print(familyMembers[-1])

# # print(familyMembers[1:])
# # print(familyMembers[1:3]) # will not take value of 3rd element

# familyMembers[2] = "Bro"
# # print(familyMembers)
# # print(familyMembers[2])
# # ______________________________________

# # _______________________________________
# # List Function

# god_number = [7,9,1,5,568,9774,23]
# familyMembers = ["Akki","Tanu","Mai","Aash","Tanu","haruhiko","Mummy","Father"]

# # print(familyMembers)
# # familyMembers.extend(god_number) #add two lists together

# # print(familyMembers)

# # familyMembers.append("Business")
# # print(familyMembers)

# # familyMembers.insert(1, "America")
# # print(familyMembers)

# # familyMembers.remove("Tanu")
# # print(familyMembers)

# # familyMembers.clear()
# # print(familyMembers)

# # familyMembers.pop()
# # print(familyMembers)

# # print(familyMembers.index("Tanu"))

# # print(familyMembers.count("Tanu"))

# # familyMembers.sort()
# # print(familyMembers)

# # god_number.sort()
# # print(god_number)

# # god_number.reverse()
# # print(god_number)

# # familyMembers2 = familyMembers.copy()
# # print(familyMembers2)

# # _______________________________________

# # -----------------------------------------
# # Tupple in Python
# # type of Data-Structure which means a conatiner who stores different values
# # tupples are immutable(tupples can not be changed & modified)
# # how to create tupple:
#
# coordinates = (4, 9, 676, 5)
# coordinates[1] = 7 #eroor coz tupple are immutable
#
# print(coordinates[2])
#
# # difference btw tupple & list Google Search
# # list aren't immutable, tupples are'
# coordinates = [(2,6),(6,8),(7,9),(34,67)]
#
# # like this you may also make a list of tuples who is immutable
# # ________________________________________

# ____________________________________________
# Functions in Python:
# Function:collection of code which performs a specific task.


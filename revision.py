import os
import random 
def clear_console():
    if os.name == 'nt':  # For Windows
        os.system('cls')
    else:  # For macOS and Linux
        os.system('clear')
# # print("namastey duniya")
# input("enter something here!")
# print("namastey" +"raju bhai"+ input("kaise hai aap?") )#yaha phele input function run hoga badme print function okay bro?
# print(len(input("what is your name?")))
 

# BMI calculator 

# height = input("enter your height")
# weight = input("enter your weight")

# h = float(height)
# w = float(height)
# bmi = w/(h*h)
# print(f'{bmi} this is your bmi')
clear_console()

# print("WELCOME TO THE TIP CALCULATOR")

# totalBill = input("what is the bill ")
# percentage = input("what percentage of tip you like to give? ")

# per = float(percentage)/100

# people = input("how many people to split the bill ? ")

# tip = float(totalBill)*per

# payment = tip + float(totalBill)

# pay = payment/int(people)
# print(f'Each person Should pay:-{pay}')


# print("LEAP YEAR OR NOT")

# year = int(input("Enter a year!"))

# if (year % 4 == 0):
#     print("leap year")
# elif (year % 100 == 0):
#     print("leap year")
# if (year % 400 == 0):
#     print("leap year")
# else:
#     print('not a leap year')


# print("WELCOME TO PYTHON DELIVERIES")
# size = input("What size pizza do you want ? S, M, L?")
# add_pepperoni = input("Do you want peperonies? press 'Y' for yes and press 'N' for no. ")
# extra_cheese = input("Do you want extra cheese?press 'Y' for yes and press 'N' for no.")

# bill = 0 
# if size == 's' or size == 'S':
#     bill += 15
# elif size == 'm' or size == 'M':
#     bill += 20
# else:
#     bill += 25
# if add_pepperoni == 'y' or add_pepperoni == 'Y':
#     if size == 's' or size == 'S':
#         bill +=2
#     else:
#         bill += 3
# if extra_cheese == 'y' or extra_cheese == 'Y':
#     bill += 1
# print(f' Your final bill is {bill}')    
#print( random.randint(20, 50))

# fruits = ["apple", "mango", "ananass"]
# # print(fruits[2])
# # fruits[2] = "grapes"
# # print(fruits[2])
# # fruits.append("momos")
# # print(fruits)
# fastFood = ['spring rolls', 'patties', 'chawmin']
# fruits.extend(fastFood)
# print(fruits)
# name = 'arpan arpan sharma manju'
# names = name.split(" ")
# print(names)
# print( len(fruits))

# names_String = input("Give me everybody's names seperated by a comma")
# names = names_String.split(",")
# name_count = len(names)

# rand = random.randint(0, name_count - 1)
# print(names[rand] + " is going to buy the lunch!$")

#nested list 
# fruits = ['mango', 'banana', 'apple', 'pine apple']
# vegetables = ['potato', 'tomato', 'ladyfinger', 'eggplant', 'onion']

# dry =  [fruits, vegetables]
# print(dry)
# column = int(str(position[0]))
# rows = int(str(position[-1]))
# print(f'{rows}\n {column}')

# Stone paper scissors 

user_choice = int(input("what do you choose ?"))
print("✊  - Stone (Rock) press 0 for stone\n✋  - Paper press 1 for paper\n✌️  - Scissors press 2 for scissors")
computer_choice = random.randint(0,2)

if user_choice >= 3 or user_choice < 0:
    print("Invalid choice, you loose!")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN")
elif user_choice == 0 and computer_choice == 2:
    print("YOU WIN") 
#guess a number

import random

number = random.randint(1,50)

print("welcome to the game :=) \n if you guess the right number you win 2000$!!! \n the right number is between 1 and 50 \n ready go !!")

user_input = 0
#print("you won!")

while True:
 
    user_input = int(input("enter the number: "))
     
    if user_input < number:
         
        print("the number you entered is less than the right number try again")
         
    elif user_input >  number:
         
        print("the number you entered is greater than the right number try again")
     
    else:
        print("Congratulations you won 2000$")
         
        break;

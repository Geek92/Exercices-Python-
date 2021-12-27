import random


def there_is_a_winner(player, oponent):
    
    if (player == 'R' and oponent == 'C') or (player == 'C' and oponent == 'P') or (player == 'P' and oponent == 'R'):
        
        return True
    else:
        return False
    
    

user_win  = False

computer_win = False

while user_win != True or computer_win != True:
    
    user = input("rock (R), Paper(P), Scissors(S): ").upper()

    computer = random.choice(["R","P","C"])
    
    user_win = there_is_a_winner(user,computer)
    
    computer_win = there_is_a_winner(computer,user)
    
    
    if user == computer:
        
        print("it\'s a Tie!")
    
    if  user_win == True:
        
        print("you won!!")
        
        break
        
    if computer_win == True:
        
        print("you lost!!")
        
        break
        
print(f"USER: {user} COMPIUTER: {computer}")



    

    
import random

def guess_the_number(number):
    
    print(f"guess my secret number it is between 1 and {number}")
    
    minimum = 1
    
    while  minimum <= number:
        
        computer_answer = random.randint(minimum,number)
    
        human_answer = input(f" is your number {computer_answer}? ")
        
        
        if human_answer.lower() == 'yes':
            
            print("it was too easy for me next time try to choose a more complicated number :=))")
            
            break;
        
        elif human_answer.lower() == 'greater':
            
            
            minimum = computer_answer + 1 
        
        elif human_answer.lower() == 'less':
            
            number = computer_answer - 1               
            
           
guess_the_number(1000)     
    
    
    
    

test = int(input())

for i in range(test):
    
    number = int(input())
    
    result = 1
    
    if number <= 1:
        print(1)
    else:
        while number > 1:
            result *= number
            number-= 1
        print(result) 
            

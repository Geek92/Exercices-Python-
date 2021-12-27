

x,y = map(int,input().split())

rest  = 0

number = x if x > y else y

divisor = y if x > y else x

#rest = number % divisor
    
while  divisor > 0:
    
    divisor = number % divisor
    
    number = divisor
    
print (number)


        

    
    
    
    
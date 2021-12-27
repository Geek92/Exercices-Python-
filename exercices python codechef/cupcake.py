


test = int(input())

for x in range(test):

    number = int(input())

    divisor = number

    totalRest = 0

    packageSize = 0

    if number == 1 or number == 2:
        print(number)

    else:
        while divisor >=1:
            
            rest =  number % divisor
            
            if rest > totalRest:
                
                totalRest = rest
                
                packageSize = divisor
            
            divisor -= 1

        print(packageSize)
            
    

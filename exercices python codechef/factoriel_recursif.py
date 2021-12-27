def factoriel(number):
        
        if number <= 1:
            return 1
        else:
            return number * factoriel(number - 1)

test = int(input())

for x in range(test):

    number = int(input())
    
    print(factoriel(number))


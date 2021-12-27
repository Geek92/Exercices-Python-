import math

test = int(input())

for t in range(test):
    number = int(input())
    count = 0
    valeurs = map(int,[math.pow(2,i-1) for i in range(12,0,-1)])  
    liste = list(valeurs)
    #print(liste)
    for x in liste:
        if number >= x:
            while number >= x:
                number = number - x 
                count += 1
    print(count)

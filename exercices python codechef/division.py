import collections


test = int(input())

for _ in range(test):
    
    liste = input()

    val = len(liste)

    liste1 = list()

    liste2 = list()

    result = 'YES'

    if val % 2 == 0:
        
        liste1 = [liste[i] for i in range(0,val//2)]
        
        liste2 = [liste[i] for i in range(val//2, val)]

    else:
        liste1 = [liste[i] for i in range(0,val//2)]
        liste2 = [liste[i] for i in range((val//2) + 1, val)]

    occorences = collections.Counter(liste2)

    for item in liste1:
        
        if occorences[item] != 1:
            
            result = 'NO'

    print(liste1, liste2)
    #print(result)

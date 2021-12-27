
T = int(input("inserez le nombre de test"))


for x in range (0,T):
    
    count = 0
    
    list_values = map(int, input("entrez la valeur de la chaine:"))
    
    liste = list(list_values)
    
    print(liste)
        
    for i in liste:
        
        if i == 4:
            count = count + 1 

    print(count)
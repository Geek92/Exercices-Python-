
def somme (x,y):
    return x + y
    
maxi = 1

liste = list(map(int, input().split()))
  
liste1 = [maxi + y for y in liste]
  
maxi = max(liste1)

print(maxi)
        

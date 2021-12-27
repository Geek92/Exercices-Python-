
test = int(input())


for _ in range(test):
    
    N = int(input("insert N "))
    
    maxi = int(input("insert maxi"))
    
    for _ in range(N - 1):

        liste = list(map(int, input().split()))
  
        liste1 = [maxi + y for y in liste]
  
        maxi = max(liste1)
    
    print(maxi)

    
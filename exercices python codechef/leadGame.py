# cook your dish here

rounds = int(input())

cumulative_score1,cumulative_score2 = 0,0

liste = list()

for i in range(rounds):
     
    score1,score2 = map(int, input().split())
    
    cumulative_score1 += score1 
    
    cumulative_score2 += score2 
    
    leader = 1 if cumulative_score1 > cumulative_score2 else 2
    
    liste.append(leader)
    
    lead = abs(cumulative_score1 - cumulative_score2)
    
    liste.append(lead)

print(liste)
Max = max(liste)
print(liste[liste.index(Max) - 1], Max)

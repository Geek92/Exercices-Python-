
test = int(input())

for t in range(test):
    
    quantity, price = map(int,input().split())
    
    totalExpense = 0.000000
    
    if quantity <= 1000:
        
        totalExpense = quantity * price
    else:
        
        initialPrice =  quantity * price
        
        discount = initialPrice * 0.1
        
        totalExpense = initialPrice - discount
        
    print(totalExpense)
        
        
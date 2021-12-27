
def sum(number):
    if number == 1:
        return number
    else:
        return number + sum(number-1)


def main():

    test = int(input())
    
    for t in range(test):
        
        x,y = map(int,input().split())

        result = y

        for i in range(x):
    
            result = sum(result)

        print(result)
    
if __name__ == "__main__":
    main()

# iteration = 2
# 
# for i in range(iteration):
#     return()





    
    
    
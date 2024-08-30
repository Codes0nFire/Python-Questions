#Find Out the second highest element  in an array

def secondhigh(arr):
    high=float("-inf")
    shigh=float("-inf")
    
    for elem in arr:
        if(elem > high):
            shigh=high
            high=elem
        elif(elem>shigh and elem != high):
            shigh=elem

    return shigh
        
userinput=list(map(int,input().split()))
print(secondhigh(userinput))
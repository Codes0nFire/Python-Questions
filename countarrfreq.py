#Count frequency of each elm in an array

def maxsum(arr):
    
    obj={}
    
    for elem in arr:
        obj[elem]=0
    for elem in arr:
        obj[elem]=obj[elem]+1
    
    return obj
    
    
    
arr=list(map(int,input().split()))

print(maxsum(arr))
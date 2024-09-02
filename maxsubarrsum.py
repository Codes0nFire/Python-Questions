#Find the maximum sum in subaaray of given array

def maxsum(arr):
    
    sum=0
    max=float("-inf")

    for elem in arr:
        sum=sum+elem
        if(sum>max):
            max=sum
        if(sum<0):
            sum=0
    return max
    
arr=list(map(int,input().split()))

print(maxsum(arr))
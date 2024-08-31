# Find the sum of digits of number given if the sum is odd then check is it prime or not based on that return 1 or 0 and if thats even then check if its plaindrome or not if yes retun 1 if no return 0


def mix(number):
    mysum=sum(number)
    
    if(mysum%2 == 0 ):
        return checkpalindrome(number)
    else:
        return checkprime(number)
    


def sum(number):
    sum=0
    n=number
    while(n>0):
        ld=n%10
        sum=sum+ld
        n=n//10
    return sum

        
    

def checkprime(number):
    for i in range(2,number):
        if(number%i ==0):
            return 0
    return 1
    

def checkpalindrome(number):
    copy=number
    rev=0
    
    while(number>0):
        ld=number%10
        rev=rev*10+ld
        number=number//10
    
    if(rev==copy):
        return 1
    else:
        return 0
        
        
    
    


userinput=int(input("Enter the Number :"))
print(mix(userinput))


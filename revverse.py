#Reverse the given string without split function

def reverse(s):
    arr=[]
    temp=""
    for i in range(len(s)):
        if s[i] != " ":
            
            temp=temp+s[i]     
        else:
            arr.append(temp)
            temp=""
        if(i==len(s)-1):
            arr.append(temp)
            temp=""
    
    arr=arr[::-1]
    return " ".join(arr)
        
        
        
    


print(reverse("how are you from"))
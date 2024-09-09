#Reverse Each word of the given string without split function




def rev(s):
    arr=[]
    l=[]
    emp=""
    
    for i in range(len(s)):
        if(s[i] != " "):
            emp=emp+s[i]
        else:
            l.append(emp)
            emp=""
        if(i == len(s)-1):
            l.append(emp)
            emp=""
        
    
    for elem in l:
        elem=elem[::-1]
        arr.append(elem)
    
    return " ".join(arr)


print(rev("am i reversed?"))        
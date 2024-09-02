#count frequncy of each elem in string

def counter(s):
    
    obj={}
    
    # for elem in s:
    #     if(elem in obj):
    #         obj[elem]=obj[elem]+1
    #     if(elem not in obj):
    #         obj[elem]=1
    # return obj
    
    for i in s:
        obj[i]=0
    for i in s:
        obj[i]=obj[i]+1
    return obj

    # for sorting use sorted function
    # sorted(obj.items(), key=lambda item: item[1], reverse=True)
        
        
        
    
mystr=input("Enter String : ")

print(counter(mystr))
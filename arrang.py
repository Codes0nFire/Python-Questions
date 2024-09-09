#Remove Special chars  and arrang numbers in left and chars in right

def rev(s):
    num=""
    alp=""
    
    for elem in s:
        if(elem.isalpha()):
            alp=alp+elem
        if(elem.isdigit()):
            num=num+elem
    return num+alp
    


print(rev("0--i-o-z-00--000--0888--8io++ip"))        
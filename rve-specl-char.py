#Remove Special chars from the given string

def rev(s):
    emp=""
    for elem in s:
        if(elem.isalpha() or elem.isdigit()):
            emp=emp+elem
    return emp
    


print(rev("000--000--0888--8io++ip"))        
# convert the string to its mirror string like for a ,z is mirror word



def rev(s):
    emp=""
    for elem in s:
        emp=emp+chr((ord("z")-ord(elem)+97))
    return emp
    
    


print(rev("azby"))        

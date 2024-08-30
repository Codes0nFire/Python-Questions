# Reverse the given String by user 

def reversed(string):
    str=list(string)
    
    start=0
    end=len(str)-1
    
    while (start< end):
        str[start],str[end]=str[end],str[start]
        start=start+1
        end=end-1
    
    result="".join(str)
    
    return result

userinput=input("Ente the string to be reversed : ")

print(reversed(userinput))


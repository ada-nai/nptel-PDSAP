#Problem 2.1
def intreverse(num):
    rem = 0
    rev = 0
    while num > 0:  
        rem = num%10 #Obtain remainder   
        rev = rev*10+rem #Multiply remainder by 10  
        num = num//10 #Integer division
    return rev

    

print(intreverse(45))
def isprime(num):
    if num < 0:
        return False
    if num == 2 or num == 1:
        return True
    for i in range(2,num):
        if num%i == 0:
            return False
    return True

def sumprimes(li):
    sum = 0
    for number in li:
        if isprime(number):
            sum += number
    return sum

#print(isprime(3))
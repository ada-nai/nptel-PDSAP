#Problem 1.3
def f(n): 
    s = 0
    for i in range(1, n+1):
        if n%i == 0:
           s = s+1
    return(s%2 == 1)

print(f(15))
print(f(2))
print(f(8))
print(f(36))
print(f(25))
print(f(23))
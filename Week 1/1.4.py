#Problem 1.4
import expectException

def f(m):
    if m == 0:
      return(0)
    else:
      return(m+f(m-1))

print(f(4))
print(f(100))


  
# Function to check parentheses 
def matched(s): 
    if s[0] == ")" or s[len(s)-1] == "(":
        return False
    count = 0
    for i in s:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1
    if count == 0:
        return True
    else:
        return False

print(matched("zb%78"))
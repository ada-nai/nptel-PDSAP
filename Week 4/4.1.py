def mystery(l):
    if l == []:
        return l
    else:
        return (l[-1:]+mystery(l[:-1]))

print(mystery([31,32,71,18,51]))
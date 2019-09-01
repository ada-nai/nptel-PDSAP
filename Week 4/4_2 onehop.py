#Problem 4.2

#using list comprehensions
#run two loops; one for first hop, next for second hop 
#compare the one-hop conditions and append to list
#python is beautiful
def onehop(l):
    one_hop = [(i,y) for(i,j) in l for(x,y) in l if((i,j) != (x,y) and (j == x) and (i != y))]
    return list(sorted(set(one_hop)))

print(onehop([(1,3),(1,2),(2,3),(2,1),(3,2),(3,1)]))
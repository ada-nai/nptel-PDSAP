# Problem 4.1

def frequency(ref_list):
    #sort the list to get numbers in order
    ref_list = sorted(ref_list) 
    dic = {}
    #calculating occurrences of numbers
    for i in ref_list:
        if i in dic:
            dic[i] += 1
        else:
            dic[i] = 1
    lis = list(dic.items())
    #reordering to list of tuples of form (frequency, number)
    new = [(f, num)for num, f in lis]
    new = sorted(new)
    #creating dict with keys by occurrence
    fin = {}
    for f, num in new:
        if f in fin:
            fin[f].append(num)
        else:
            fin[f] = [num]
    #dict to list (indexing) and getting first and last element
    fl = list(fin.keys())
    minfreq = fin[fl[0]]
    maxfreq = fin[fl[-1]]
    return (minfreq, maxfreq)

print(frequency([13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12]))
print(frequency([13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14]))
print(frequency([13, 12, 11, 13, 14, 13, 7, 11, 13, 14, 12, 14, 14, 7]))
    
# Problem 3.2

def accordian(ref_list):
    temp = []
    for i in range(1, len(ref_list)):
        temp.append(abs(ref_list[i]-ref_list[i-1])) # absolute difference list
    #print(temp)
    diff = []
    for j in range(1, len(temp)):
        diff.append(temp[j]-temp[j-1]) # difference of abs list
    #print(diff)
    if (diff[0] < 0 and diff[1] > 0):
        for k in range(0, len(diff), 2):
            if (diff[k] >= 0):
                return False
            else:
                for k in range(1, len(diff), 2):
                    if (diff[k] <= 0):
                        return False

        return True
    if (diff[0] > 0 and diff[1] < 0):
        for k in range(0, len(diff), 2):
            if (diff[k] <= 0):
                return False
            else:
                for k in range(1, len(diff), 2):
                    if (diff[k] >= 0):
                        return False

        return True
    return False
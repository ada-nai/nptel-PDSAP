# Problem 3.1
def expanding(ref_list):
    temp = []
    for i in range(1, len(ref_list)):
        temp.append(abs(ref_list[i] - ref_list[i-1]))   #Taking the difference and appending to temp
    if(temp == sorted(temp)):   #Check if the absolute differences are strictly increasing
        for j in range(1, len(temp)):
            if temp[j] == temp[j-1]:    #Check for equal differences 
                return False
        return True
        
    else: return False

expanding([1, 3, 7, 2, -3])
  
        
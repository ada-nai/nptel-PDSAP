#Problem 3.3

def rotate(ref_list):
    ref_list = ref_list[::-1]
    ref_list = list(zip(*ref_list))
    res = [list(ele) for ele in ref_list]
    return res

print(rotate([[1, 2],[3, 4]]))
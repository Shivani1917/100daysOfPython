#  Program to sort list 1 by list 2

def sort_list(list1, list2):
 
    zip_pairs = zip(list2, list1)
 
    z = [x for _, x in sorted(zip_pairs)]
 
    return z
 
 
x = ["a",  "d", "e", "f", "g", "h", "i"]
y = [0,  0,   1,   2,   2,   0,   1]
 
print(sort_list(x, y))
#  Program to find Occurrences of elements

a = [1,2,3,4,[],5,[],[],8]

while [] in a:
    a.remove([])

print("List after empty list removal : " + str(a))

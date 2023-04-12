# Program to Break list into Chunks of list

a = []
n = int(input("Enter number of elements: "))

print("Enter elements of the list")
for i in range(0, n):
    element = int(input())
    a.append(element)

print(a)

chunk_size = int(input("Chunk on which new list form: "))

def formChunkList(a, chunk_size):
    ele = []
    for i in range (0, len(a), chunk_size):
        chunk_list = a[i:i+chunk_size]
        ele.append(chunk_list)
    return ele

print("The chunked list ", formChunkList(a,chunk_size))

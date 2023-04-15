#  Program to find maximum of each key in list

def findMaxKeyPair(data):
    maxPerKey = {}
    for item in data:
        for key, value in item.items():
            if key not in maxPerKey:
                maxPerKey[key] = value
            else:
                if value > maxPerKey[key]:
                    maxPerKey[key] = value
    return maxPerKey

lisOfDicts = [
    {"a": 1, "b": 5, "c": 3},
    {"a": 2, "b": 7, "c": 1},
    {"a": 3, "b": 3, "c": 9},
]

result = findMaxKeyPair(lisOfDicts)
print("The maximum of each key in list: ",result)

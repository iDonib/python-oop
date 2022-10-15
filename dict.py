def displayDuplicates(x):
    dupe = []
    for i in range(len(x)):
        k = i+1
        for j in range(k, len(x)):
            if x[i] == x[j] and x[i] not in dupe:
                dupe.append(x[i])
        
    return dupe

a = [55,6,5,8,6,55,6,66,66,5, 6,5,66]
print(displayDuplicates(a))

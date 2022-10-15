def remove_items(lists):
    for i in range(len(lists)-1, -1, -1):
        if lists[i] >= 50:
            del list[i]
    return lists

list = [50,25,68,88,1,2]
print(remove_items(list))
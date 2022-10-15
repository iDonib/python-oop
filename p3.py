for i in range(1,6):
    for j in range(6-i):
        print(" ", end=" ")
    
    for k in range(i):
        print(i, end=" ")
    
    for k in range(i-1):
        print(i, end=" ")

    print()
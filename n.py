print("N")
for row in range(5):
    for col in range(5):
        if (row in {0,4}) and (col in {0,4}):
            print("*", end=" ")
        elif (row ==1) and (col in {0,1,4}):
            print("*", end=" ")
        elif (row ==2) and (col in {0,2,4}):
            print("*", end=" ")
        elif (row ==3) and (col in {0,3,4}):
            print("*", end=" ")
        
        else:
            print(" ", end=" ")
    print()

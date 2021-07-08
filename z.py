print("I")
for row in range(9):
    for col in range(5):
        if (row in {0,8}):
            print("*", end=" ")
        elif (row ==2) and (col in {3}):
            print("*", end=" ")
        elif (row ==4) and (col in {2}):
            print("*", end=" ")
        elif (row ==6) and (col in {1}):
            print("*", end=" ")
        
        else:
            print(" ", end=" ")
    print()

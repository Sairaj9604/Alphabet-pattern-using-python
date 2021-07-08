print("V")
for row in range(5):
    for col in range(5):
        if (row in {0}) and (col in {0,4}):
            print("*", end=" ")
        elif (row ==2) and (col in {1,3}):
            print("*", end=" ")
        
        elif (row ==4) and (col in {2}):
            print("*", end=" ")
        
        else:
            print(" ", end=" ")
    print()

print("W")
for row in range(7):
    for col in range(5):
        if (row not in {4,5}) and (col in {0,4}):
            print("*", end=" ")
        elif (row ==5) and (col !=2):
            print("*", end=" ")
        elif (row ==4) and (col in {0,2,4}):
            print("*", end=" ")
        
        else:
            print(" ", end=" ")
    print()

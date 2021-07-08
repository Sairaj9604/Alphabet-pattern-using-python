print("Y")
for row in range(8):
    for col in range(5):
        if (row  in {0}) and (col in {0,4}):
            print("*", end=" ")
        elif (row ==2) and (col in {1,3}):
            print("*", end=" ")
        elif (row ==4) and (col in {2}):
            print("*", end=" ")
        elif (row not in {0,1,2,3,4}) and (col ==2):
            print("*", end=" ")
        
        else:
            print(" ", end=" ")
    print()

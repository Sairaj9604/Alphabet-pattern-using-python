print("Q")
for row in range(7):
    for col in range(5):
        if (row in {0}) and (col in {1,2,3}):
            print("*", end=" ")
        elif (row in {1,2,3}) and (col in {0,4}):
            print("*", end=" ")
        elif (row in {4}) and (col in {0,2,4}):
            print("*", end=" ")
        elif (row in {5}) and (col not in {0,4}):
            print("*", end=" ")
        elif (row in {6}) and (col in {4}) :
            print("*", end=" ")
        else:
            print(" ", end=" ")
    print()

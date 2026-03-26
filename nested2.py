for i in range(6):
    for j in range(7):
        if i == 0 or i == 3 or j == 0 or j == 6:
            print("AR", end=" ")
        else:
            print(" ", end=" ")
    print()
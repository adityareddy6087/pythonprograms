for i in range(1,9):
    for j in range(1,8):
        if i==6:
            if j==7:
                break
            continue
        print(i)
        print(j)
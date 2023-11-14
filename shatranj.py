row= int(input("enter number row:"))
col= int(input("enter number col:"))


for n in range(row):
    for m in range(col):
        if (n+m)  %2==0:
            print("#",end="")
        else:
            print("*",end="")

    print()

drink = input()
if drink == "t" or drink == "c":
    refills = int(input())
    if refills > 10:
        refills = int(input())
    print(1+refills)

else:
    print(1)

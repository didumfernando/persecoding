count = 0
for i in range(2):
    num = str(input())
    print(num[-1:])
    print(num[:1])
    if int(num[:1]) + 1 == int(num[-1:]) or int(num[:1]) - 1 == int(num[-1:]):
        count += 1
print(count)
    

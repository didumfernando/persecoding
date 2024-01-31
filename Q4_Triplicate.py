first = input()
second = input()
third = input()

if first == second == third:
    print("OK")
elif second != first and third != first:
    print("BOTH MISMATCH")

elif second != first:
    print("ENTRY 2 MISMATCH")

else:
    print("ENTRY 3 MISMATCH")

a = 0
c = 0

s = 1
while s < 5:
    a += 1
    a = int(input("a = "))
    s += 1
    if a >= 10:
        print("тяж",  a) 
    elif a <= 3:
        print("лёгк",  a)
    elif a >= 4 and a <= 9:
        c += 1
print("хороших",  c )

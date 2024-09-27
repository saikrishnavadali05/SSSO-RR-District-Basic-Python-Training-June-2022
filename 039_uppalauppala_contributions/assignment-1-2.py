
tup = eval(input("Enter input for tuple:"))
tup2 = ()
tup3 = ()
i = 0
while i < len(tup):
    if i % 2 == 0:
        tup2 += (tup[i],)
    else:
        tup3 += (tup[i],)
    i += 1
print(tup2)
print(tup3)

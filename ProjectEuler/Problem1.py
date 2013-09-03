a = 0
for x in range(3,1000):
    if x%5 == 0 or x%3 == 0:
        a = a+x
    elif x%5 != 0 or x%3 != 0:
        a = a+0
print a
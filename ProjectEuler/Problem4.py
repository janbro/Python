ans=0
def palendrime(num):
    revnum=str(num)[::-1]
    if revnum==num:
        if(num>ans):
            return num
    else:
        return 1

for y in range(100,1000):
    for x in range(100,1000):
        z=x*y
        if(float(palendrime(str(z)))>ans):
            ans=float(palendrime(str(z)))
print ans
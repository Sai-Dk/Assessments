Ip=input()
ls=Ip.split(".")
       
a=int(ls[0])
b=int(ls[1])
c=int(ls[2])
d=int(ls[3])

def check(j):
    j=int(j)
    if j >= 0 and j <= 255:
        return True
    else:
        return False
 
if check(a) and check(b) and check(c) and check(d):
    print(Ip, "is valid")
else:
    print(Ip, "is invalid")
       


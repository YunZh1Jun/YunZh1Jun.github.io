import gmpy2
a=5
b=8
m=26
n=gmpy2.invert(a,m)
print(n)
enc='IHHWVCSWFRCP'
dec=''
for i in enc:
    if i.isalpha():
        e=(n*(ord(i)-ord('A')-b))%m
        dec+=chr(ord('A')+e)
    else:
        dec+=i
print(dec)

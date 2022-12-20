a=5
b=8
m=26
enc=''
plain='AFFINE CIPHER'
for i in plain:
    if i.isalpha():
        e=(a*(ord(i)-ord('A'))+b)%m
        enc+=chr(ord('A')+e)
    else:
        enc+=i
print(enc)
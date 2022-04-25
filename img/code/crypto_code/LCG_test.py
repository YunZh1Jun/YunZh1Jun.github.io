import random
p = 4646704883
x = random.randint(0,p)
y = random.randint(0,p)
print(x)
print(y)
for i in range(10):
    x = (2 * x + 3) % p
    y = (3 * y + 9) % p
    rlt = x ^ y
    print(rlt)

'''
output:
x = 4176266457
y = 211689793
4181201166
3577931257
185789797
3597291091
3253305450
2858406768
2755347051
4023894776
3972770629
1123136706
'''
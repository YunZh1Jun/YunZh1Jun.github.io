flag=b'flag{1fsr_c4n_n0t_pr3v3nt_0xb14cb12d~}'
assert flag.startswith(b"flag{")
assert flag.endswith(b"}")
assert len(flag) == 38

masklength = 0xffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffffff

class LFSR:
    def __init__(self,seed,mask):
        self.mask = mask
        self.state = seed

    def next(self):
        output = (self.state << 1) & masklength
        i = (self.state & mask) & masklength
        lastbit = 0
        while i!=0:
            lastbit ^= (i & 1)
            i = i >> 1
        output ^= lastbit
        self.state = output
        return lastbit

R = int(flag[5:-1].hex(),16)
mask = int(bin(int(b'the_little_boy:0xb14cb12d'.hex(),16))[2:130]*2,2)
lfsr = LFSR(R,mask)

cipher = []
for i in range(100):
    tmp=0
    for j in range(8):
        out = lfsr.next()
        tmp=(tmp << 1)^out
    cipher.append(tmp)

print(bytes(cipher))
#b'\xab\xcf\xa8\xdc\xa8\x00\x95\xfc\xc5\x16`\x91%X^\xde\xaf\x0e\xd0\xba\x0fCg\rwz\xc1{\xfdX\x1b\xf1\x85\x94\xddK)\x8d\x1e\xb3s\xf8\x18\x00q\xc78hT\x11\x9c\xf7\x9c\x0e\x96o3\x12\xffl\xf1\x1d\xacD\xf2F6\x8d\xa3\x06\x17\xe5\xdc\xe4<\x8eAa\x8d\x04\xdd\xab\xd2\xd9~\x17\x81}\x16\x92wWF\x87\xb5[@\\\x84\xe3'
#flag{1fsr_c4n_n0t_pr3v3nt_0xb14cb12d~}
def ct_crc32(ch,size):
    crc = 0xffffffff
    for i in range(size):
        crc = crc_table[(crc ^ ch[i])&0xff] ^ (crc >> 8)
    return crc

crc_table = []
for i in range(256):
    c = i
    for j in range(8):
        if c & 1 == 1:
            c = 0xedb88320 ^ (c >> 1)
        else:
            c = c >> 1
    crc_table.append(c)
for i in range(8):
    print(hex(crc_table[i]))
#include <stdio.h>
#include <stdint.h>


#define DELTA 0x9e3779b9
#define MX (((z>>5^y<<2) + (y>>3^z<<4)) ^ ((sum^y) + (key[(p&3)^e] ^ z)))


void xxtea(uint32_t* v, int n, uint32_t* key)
{
    uint32_t y, z, sum;
    unsigned p, rounds, e;

    if (n > 1)             // encrypt
    {
        rounds = 6 + 52/n;
        sum = 0;
        z = v[n-1];
        do
        {
            sum += DELTA;
            e = (sum >> 2) & 3;
            for (p=0; p<n-1; p++)
            {
                y = v[p+1];
                z = v[p] += MX;
            }
            y = v[0];
            z = v[n-1] += MX;
        }
        while (--rounds);
    }
    else if (n < -1)      // decrypt
    {
        n = -n;
        rounds = 6 + 52/n;
        sum = rounds * DELTA;
        y = v[0];
        do
        {
            e = (sum >> 2) & 3;
            for (p=n-1; p>0; p--)
            {
                z = v[p-1];
                y = v[p] -= MX;
            }
            z = v[n-1];
            y = v[0] -= MX;
            sum -= DELTA;
        }
        while (--rounds);
    }
}

// test
int main()
{
    // 两个32位无符号整数，即待加密的64bit明文数据
    uint32_t v[2] = {0x12345678, 0x78563412};
    // 四个32位无符号整数，即128bit的key
    uint32_t k[4]= {0x1, 0x2, 0x3, 0x4};
    //n的绝对值表示v的长度，取正表示加密，取负表示解密
    int n = 2;

    printf("Data is : %x %x\n", v[0], v[1]);
    xxtea(v, n, k);
    printf("Encrypted data is : %x %x\n", v[0], v[1]);
    xxtea(v, -n, k);
    printf("Decrypted data is : %x %x\n", v[0], v[1]);

    return 0;
}
/*
Data is : 12345678 78563412
Encrypted data is : ef86c2bb 25f31b5e
Decrypted data is : 12345678 78563412
*/

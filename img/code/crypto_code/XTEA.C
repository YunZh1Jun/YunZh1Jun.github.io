#include <stdio.h>
#include <stdint.h>


void decrypt(uint32_t* v, uint32_t* key) {
    uint32_t v0 = v[0], v1 = v[1];
    uint32_t delta = 0x9E3779B9;
    uint32_t sum = delta * 32;

    for (int i=0; i<32; i++) {
        v1 -= (((v0 << 4) ^ (v0 >> 5)) + v0) ^ (sum + key[(sum>>11) & 3]);
        sum -= delta;
        v0 -= (((v1 << 4) ^ (v1 >> 5)) + v1) ^ (sum + key[sum & 3]);
    }

    v[0]=v0;
    v[1]=v1;
}

// test
int main()
{
    // 两个32位无符号整数，即待加密的64bit明文数据
    uint32_t v[2] = {0x12345678, 0x78563412};
    // 四个32位无符号整数，即128bit的key
    uint32_t k[4]= {0x1, 0x2, 0x3, 0x4};

    printf("Data is : %x %x\n", v[0], v[1]);
    encrypt(v, k);
    printf("Encrypted data is : %x %x\n", v[0], v[1]);
    decrypt(v, k);
    printf("Decrypted data is : %x %x\n", v[0], v[1]);

    return 0;
}
/*
Data is : 12345678 78563412
Encrypted data is : ae685ec7 59af4238
Decrypted data is : 12345678 78563412
*/

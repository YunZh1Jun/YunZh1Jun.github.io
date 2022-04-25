#include <stdio.h>
#include <stdint.h>

void encrypt (uint32_t* v, uint32_t* k) {
    uint32_t sum = 0;  // 注意sum也是32位无符号整型
    uint32_t v0 = v[0], v1 = v[1];
    uint32_t delta = 0x9e3779b9;
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];

    for (int i=0; i<32; i++) {
        sum += delta;
        v0 += ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        v1 += ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
    }

    v[0]=v0; 
    v[1]=v1;
}

void decrypt (uint32_t* v, uint32_t* k) {
    uint32_t v0 = v[0], v1 = v[1];
    uint32_t delta = 0x9e3779b9;
    uint32_t sum = delta * 32;
    uint32_t k0 = k[0], k1 = k[1], k2 = k[2], k3 = k[3];

    for (int i=0; i<32; i++) {
        v1 -= ((v0<<4) + k2) ^ (v0 + sum) ^ ((v0>>5) + k3);
        v0 -= ((v1<<4) + k0) ^ (v1 + sum) ^ ((v1>>5) + k1);
        sum -= delta;
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
Encrypted data is : 9a65a69a 67ed00f6
Decrypted data is : 12345678 78563412
*/

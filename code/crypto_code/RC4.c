/*初始化函数*/
void rc4_init(unsigned char*s,unsigned char*key, unsigned long Len)
{
    int i=0,j=0;
    unsigned char k[256]={0};
    unsigned char tmp=0;
    for(i=0;i<256;i++) {
        s[i]=i;
        k[i]=key[i%Len];
    }
    for(i=0;i<256;i++) {
        j=(j+s[i]+k[i])%256;
        tmp=s[i];
        s[i]=s[j];//交换s[i]和s[j]
        s[j]=tmp;
    }
}

/*加解密*/
void rc4_crypt(unsigned char*s,unsigned char*Data,unsigned long Len)
{
    int i=0,j=0,t=0;
    unsigned long k=0;
    unsigned char tmp;
    for(k=0;k<Len;k++)
    {
        i=(i+1)%256;
        j=(j+s[i])%256;
        tmp=s[i];
        s[i]=s[j];//交换s[x]和s[y]
        s[j]=tmp;
        t=(s[i]+s[j])%256;
        Data[k]^=s[t];
    }

/*
  v7[0] = 0xE0B25F3D8FFA94B6LL;
  v7[1] = 0xE79D6C9866D20FEALL;
  v7[2] = 0x6D6FBEC57140081BLL;
  v7[3] = 0xF6F3BDA88D097B7CLL;
v7=v8[j]+v7+a1[j]%256
v4=a1[j]
a1[j]=a1[v7]
a1[v7]=v4
*/
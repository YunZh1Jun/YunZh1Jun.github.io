key =  '1010101111001111101010001101110010101000000000001001010111111100110001010001011001100000100100010010010101011000010111101101111010101111000011101101000010111010000011110100001101100111000011010111011101111010110000010111101111111101010110000001101111110001'
mask = '1110100011010000110010101011111011011000110100101110100011101000110110001100101010111110110001001101111011110010011101000110000011101000110100001100101010111110110110001101001011101000111010001101100011001010101111101100010011011110111100100111010001100000'

tmp = key
R = ''
for i in range(256):
    output = '?'+key[:255]
    ans= int(tmp[-1-i])^int(output[-6])^int(output[-7])^int(output[-11])^int(output[-13])^int(output[-14])^int(output[-15])^int(output[-18])^int(output[-21])^int(output[-22])^int(output[-23])^int(output[-24])^int(output[-26])^int(output[-27])^int(output[-28])^int(output[-29])^int(output[-31])^int(output[-32])^int(output[-35])^int(output[-39])^int(output[-40])^int(output[-42])^int(output[-43])^int(output[-44])^int(output[-45])^int(output[-46])^int(output[-48])^int(output[-50])^int(output[-52])^int(output[-55])^int(output[-56])^int(output[-60])^int(output[-61])^int(output[-63])^int(output[-64])^int(output[-68])^int(output[-70])^int(output[-71])^int(output[-72])^int(output[-76])^int(output[-78])^int(output[-79])^int(output[-80])^int(output[-82])^int(output[-85])^int(output[-87])^int(output[-88])^int(output[-92])^int(output[-93])^int(output[-95])^int(output[-96])^int(output[-98])^int(output[-99])^int(output[-100])^int(output[-101])^int(output[-102])^int(output[-104])^int(output[-106])^int(output[-108])^int(output[-111])^int(output[-112])^int(output[-117])^int(output[-119])^int(output[-120])^int(output[-124])^int(output[-126])^int(output[-127])^int(output[-128])^int(output[-134])^int(output[-135])^int(output[-139])^int(output[-141])^int(output[-142])^int(output[-143])^int(output[-146])^int(output[-149])^int(output[-150])^int(output[-151])^int(output[-152])^int(output[-154])^int(output[-155])^int(output[-156])^int(output[-157])^int(output[-159])^int(output[-160])^int(output[-163])^int(output[-167])^int(output[-168])^int(output[-170])^int(output[-171])^int(output[-172])^int(output[-173])^int(output[-174])^int(output[-176])^int(output[-178])^int(output[-180])^int(output[-183])^int(output[-184])^int(output[-188])^int(output[-189])^int(output[-191])^int(output[-192])^int(output[-196])^int(output[-198])^int(output[-199])^int(output[-200])^int(output[-204])^int(output[-206])^int(output[-207])^int(output[-208])^int(output[-210])^int(output[-213])^int(output[-215])^int(output[-216])^int(output[-220])^int(output[-221])^int(output[-223])^int(output[-224])^int(output[-226])^int(output[-227])^int(output[-228])^int(output[-229])^int(output[-230])^int(output[-232])^int(output[-234])^int(output[-236])^int(output[-239])^int(output[-240])^int(output[-245])^int(output[-247])^int(output[-248])^int(output[-252])^int(output[-254])^int(output[-255])
    R += str(ans)
    key = str(ans) + key[:255]

from Crypto.Util.number import long_to_bytes
R = int(R[::-1], 2)
print(b'flag{'+long_to_bytes(R)+b'}')
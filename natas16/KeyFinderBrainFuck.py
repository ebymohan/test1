def standardize(text):
    out=''''''
    for i in range(0, text.__len__()):
        text=text.lower()
        if(text[i].isalpha()):
            out=out+text[i]
    return out


ptext=''''''
ctext='''-zb-ra--m---------q-h---wfoq-zc-/frmfycu/sp_ptr'''

#plaintext= '''orestishackingforfunandprofit'''
key=[8, 13, 5, 20, 2, 10, 12, 24, 1, 17, 0, 8, 13, 5, 20, 2, 10, 12, 24, 1, 17, 0, 8, 13, 5, 20, 2, 10, 12]
#[1, 17, 0, 8, 13, 5, 20, 2, 10, 12, 24]
ciphertext=standardize(ctext)
#output=''''''
keylength=11    #has to be initialized for decrypt function






#Tested Working Fine
def encrypt(plaintext, key):
    output=''''''
    for i in range (0, plaintext.__len__()):
        keydigit=key[i%key.__len__()]
        o= ord(plaintext[i]) + keydigit
        if (o>122):
            temp=o-122
            o=96+temp
        output=output+chr(o)
    return output


def cryptanalysis(plaintext, ciphertext):
    length=plaintext.__len__()
    output = [0]*length
    for i in range(0, plaintext.__len__()):
        flag=1
        count=0
        while(flag==1):
            o=ord(plaintext[i]) + count
            if (o > 122):
                temp = o - 122
                o = 96 + temp
            if (chr(o)==ciphertext[i]):
                flag=0
                output[i]=count
            count=count+1
    return(output)



#out=cryptanalysis(plaintext,ciphertext)
#print('''key value''',out)
#bruteforcekey=out


#Tested Working Fine
#key=[8, 13, 5, 20, 2, 10, 12, 24, 1, 17, 0, 8, 13, 5, 20, 2, 10, 12, 24, 1, 17, 0, 8, 13, 5, 20, 2, 10, 12]
#1st try 8, 13, 5, 20, 2, 10, 12, 24, 1, 17, 0
#2nd try 13, 5, 20, 2, 10, 12, 24, 1, 17, 0, 8
#3rd try 5, 20, 2, 10, 12, 24, 1, 17, 0, 8, 13
#and so on ....
def rollingdecrypt(ciphertext, rolligkey):
    possiblesolution = [''''''] * keylength
    for j in range (0, keylength):

        output=''''''
        key= rolligkey[j:(j + keylength)]
        for i in range (0, ciphertext.__len__()):
            keydigit=key[i%key.__len__()]
            o= ord(ciphertext[i]) + (26 - keydigit)
            if (o>122):
                temp=o-122
                o=96+temp
            output=output+chr(o)
        possiblesolution[j]=output
    return possiblesolution

out=rollingdecrypt(ciphertext,key)
print('''decrypted value''',out)


#Inititialize @ ptext,ctext or plaintext,ciphertext depending on stangardization is required

ptext=''''''
ctext='''Mya qutf de buj otv rms dy srd vkdof :)'''

#plaintext= '''orestishackingforfunandprofit'''
#ciphertext='''pieagnmjkoijegnbwzwxmlegrwsnn'''

key=[1, 17, 0, 8, 13, 5, 20, 2, 10, 12, 24]

def standardize(text):
    out=''''''
    for i in range(0, text.__len__()):
        text=text.lower()
        if(text[i].isalpha()):
            out=out+text[i]
    return out


ciphertext=standardize(ctext)
plaintext=standardize(ptext)



#Tested Working Fine
def decrypt(ciphertext, key):
    output=''''''
    for i in range (0, ciphertext.__len__()):
        keydigit=key[i%key.__len__()]
        o= ord(ciphertext[i]) + (26 - keydigit)
        if (o>122):
            temp=o-122
            o=96+temp
        output=output+chr(o)
    return output

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

#Tested Working Fine
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





#out=encrypt(plaintext,key)
#print('''encrypted value''',out)

out=decrypt(ciphertext,key)
print('''decrypted value''',out)

#out=cryptanalysis(plaintext,ciphertext)
#print('''key value''',out)


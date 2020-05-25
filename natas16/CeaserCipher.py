
msg='''Jub'f yhexvat va gur funqbjf? Jub'f npghnyyl uvqvat haqre gubfr fpnel pybnxf? Jung'f tbvat ba ng /funqbjOnaxUD?'''
#msg='''SYNTPrfneVfPbbyOhgAbgFrpher'''
def add(c, s):
    result=''
    if (c.isupper()):
        result += chr((ord(c) + s - 65) % 26 + 65)
    else:
        result += chr((ord(c) + s - 97) % 26 + 97)
    return result
def sub(c, s):
    result = ''
    if (c.isupper()):
        result += chr((ord(c) - s - 65) % 26 + 65)
    else:
        result += chr((ord(c) - s - 97) % 26 + 97)
    return result
ans=''''''
for j in range (1,26): #0 will mean the input is same as output
    for i in range(0, msg.__len__()):
        #ans=''''''
        if (i%2==0):
            ans= ans+add(msg[i],j)
        else:
            ans= ans + sub(msg[i], j)
    if ans.upper().find("FLAG") != -1:
        print(ans+ '''<= This looks promising''')
    else:
        print (ans)
    ans=('''''')


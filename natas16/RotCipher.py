
#msg='''vOAM5ZcReMNzJqOfxLauakHx'''
msg='''SYNTPrfneVfPbbyOhgAbgFrpher'''
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
for j in range (0,25):
    for i in range(0, msg.__len__()):
        #ans=''''''
        ans= ans+add(msg[i],j)

    print(ans)
    ans=('''''')


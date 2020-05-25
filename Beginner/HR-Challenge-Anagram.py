#input1='fcrxzwscanmligyxyvym'
#input2='jxwtrhvujlmrpdoqbisbwhmgpmeoke'
input1='showman'
input2='woman'
str1=input1
str2=input2
count=0
r=len(str1)
for i in range (0,len(str1)):
    char=str1[i]
    if char not in str2:
        count+=1
    else:
        str2=str2.replace(char,"",1)

count+=len(str2)
print(count)






fin= open("10CommonWords.txt","r")
fout=open("10CommonWords-ShortestFirst.txt","w+")
outlist=[]
outlist.insert(1,fin.readline().strip())
temp=fin.readline().strip()
if temp.__len__() > outlist[0].__len__():
    outlist.insert(1, temp)
else:
    outlist.insert(0, temp)
for line in fin:
    for i in range  (0,outlist.__len__()):
        if line.__len__() > outlist[i].__len__() and (line.__len__() <= outlist[i+1].__len__()):
            outlist.insert(i+1,line.strip())
            break
        else:
            outlist.insert(i, line.strip())
            break

for line in outlist:
    #print(line)
    pass
print(outlist)


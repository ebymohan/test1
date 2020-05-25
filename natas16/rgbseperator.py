from PIL import Image
import re


iname="BiaSciLab_Avatar.jpg"
input=Image.open(iname)
size=(x,y)=input.size
print(input.size)
print (input.mode)

outputr=input
outputg=input
outputb=input

for i in range (0,x):
    for j in range (0,y):
        r, g, b = input.getpixel((i, j))
        outputr.putpixel((i, j), (r, 0, 0))
        outputg.putpixel((i, j), (0, g, 0))
        outputb.putpixel((i, j), (0, 0, b))

outputr.show()
#outputg.show()
#outputb.show()
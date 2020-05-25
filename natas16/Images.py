from PIL import Image


lenna=Image.open("Lenna.png")
print (lenna.mode)
x,y=lenna.size
out=Image.new("RGB",(100,100),'cyan')

for j in range (0,100):
    out.putpixel((48, j), (ord('e'),0,0))
    out.putpixel((49, j), (ord('b'),0,0))
    out.putpixel((50, j), (ord('y'),0,0))
    out.putpixel((51, j), (ord('m'),0,0))

out.show()


out.save('eby.jpg')
for i in range(0,x):
    for j in range(0,y):
        r,g,a=lenna.getpixel((i,j))
        if (a == 254):
            print("transparent pixel @",i," ",j)



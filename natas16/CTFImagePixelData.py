from PIL import Image
import re


iname="Whats.jpg"
input=Image.open(iname)
size=(x,y)=input.size
print(input.size)
print (input.mode)
ra=""
ga=""
ba=""
rgb=""
px=input.load()
for i in range (0,x):
    for j in range (0,y):
        r,g,b=input.getpixel((i,j))
        ra=ra+chr(r)
        ga=ga+chr(g)
        ba=ba+chr(b)
        rgb=rgb+chr(r)+chr(g)+chr(b)

print ("ra values", ra)
print ("ga values", ga)
print ("ba values", ba)
print ("rgba values", rgb)

print("searching red")
if re.search('key', ra, re.IGNORECASE) or re.search('flag', ra, re.IGNORECASE):
    print ('Red Pixel Array contains Key/Flag Process ra')
    keyindex=re.search('key', ra, re.IGNORECASE)
    if (keyindex):
        start,end=keyindex.span()
        print('Matched string:', ra[start:start+64])

    flagindex = re.search('flag', ra, re.IGNORECASE)
    if (flagindex):
        start,end=flagindex.span()
        print('Matched string:', ra[start:start+64])

    tokenindex = re.search('t0k3n', ra, re.IGNORECASE)
    if (tokenindex):
        start,end=tokenindex.span()
        print('Matched string:', ra[start:start+64])

print("searching blue")
if re.search('key', ga, re.IGNORECASE) or re.search('flag', ga, re.IGNORECASE):
    print('Green Pixel Array contains Key/Flag Process ga')
    keyindex=re.search('key', ga, re.IGNORECASE)
    if (keyindex):
        start,end=keyindex.span()
        print('Matched string:', ga[start:start+64])

    flagindex = re.search('key', ga, re.IGNORECASE)
    if (flagindex):
        start,end=flagindex.span()
        print('Matched string:', ga[start:start+64])

    tokenindex = re.search('t0k3n', ga, re.IGNORECASE)
    if (tokenindex):
        start,end=tokenindex.span()
        print('Matched string:', ra[start:start+64])

print("searching green")
if re.search('key', ba, re.IGNORECASE) or re.search('flag', ba, re.IGNORECASE):
    print('Blue Pixel Array contains Key/Flag Process ba')
    keyindex=re.search('key', ba, re.IGNORECASE)
    if (keyindex):
        start,end=keyindex.span()
        print('Matched string:', ba[start:start+64])

    flagindex = re.search('flag', ba, re.IGNORECASE)
    if (flagindex):
        start,end=flagindex.span()
        print('Matched string:', ba[start:start+64])

    tokenindex = re.search('t0k3n', ba, re.IGNORECASE)
    if (tokenindex):
        start,end=tokenindex.span()
        print('Matched string:', ra[start:start+64])

print("searching rgb")
if re.search('key', rgb, re.IGNORECASE) or re.search('flag', rgb, re.IGNORECASE):
    print ('RGB Pixel Array contains Key/Flag Process ra')
    keyindex=re.search('key', rgb, re.IGNORECASE)
    if (keyindex):
        start,end=keyindex.span()
        print('Matched string:', rgb[start:start+64])

    flagindex = re.search('flag', rgb, re.IGNORECASE)
    if (flagindex):
        start,end=flagindex.span()
        print('Matched string:', rgb[start:start+64])

    tokenindex = re.search('t0k3n', rgb, re.IGNORECASE)
    if (tokenindex):
        start,end=tokenindex.span()
        print('Matched string:', ra[start:start+64])
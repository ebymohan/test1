'''Sample Input 12345678 Output twelve million threehundredfortyfive thiousand six hundred seventy eight'''

teens=['one ','two ','three ','four ','five ','six ','seven ','eight ','nine ','ten ','eleven ','twelve ','thirteen ','fourteen ','fifteen ','sixteen ','seventeen ','eighteen ','nineteen ']
def lessthanhundred(num):
    output=''
    #tens=['twenty','thirty','fourty','fifty','sixty','seventy','eighty','ninty']
    if (num == 0):
        output = ''
    elif (num<20):
        output=teens[num-1]
    elif (num<100):
        if(num>89):
            output="ninty "
        elif(num>79):
            output="eighty "
        elif (num > 69):
            output = "seventy "
        elif (num > 59):
            output = "sixty "
        elif (num > 49):
            output = "fifty "
        elif (num > 39):
            output = "fourty "
        elif (num > 29):
            output = "thirty "
        elif (num > 19):
            output = "twenty "
        tens=num%10
        if(tens != 0):
            output=output+" "+teens[tens-1]
    return output

def lessthanthousand(num):
    output=''

    if(num==0):
        output='zero'
    else:
        temp = num // 100
        if (temp!=0):
            output = output+teens[temp-1]+"hundred "
            temp=num%100
            output=output+lessthanhundred(temp)
        else:
            output = lessthanhundred(num)
    return output

num=int(input('Enter the input'))
output=''
#100,000,000
millions=num//1000000
thousands=(num%1000000)//1000
lasts=(num%1000)
if(num>=1000000):
    output = lessthanthousand(millions) + "million "
if(num>=1000 and thousands!=0):
    output=output+ lessthanthousand(thousands) + "thousand "
if(num>0 and lasts !=0):
    output=output+lessthanthousand(lasts)
if (num==0):
    output="zero"
print(output.capitalize())







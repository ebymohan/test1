import random
import sys
import os

name='eby'
print(("Hello World"+ name)*5 )

sample_list=['eby','chi','bar2']
sample_list.append('che')
#print (sample_list.index('bar2'),end=" ")


#print (sample_list[sample_list.index('bar2')])

another_list=['Chilanka','Chinjado','kunjukutty']

listoflists=[sample_list,another_list]


#print(listoflists)

#print (listoflists[0][1])

del listoflists[0][1]

#print(listoflists)
#print (sample_list)
sample_list.insert(1,'chi')

#print(listoflists)

sample_tuple=('Eby','Mohan')

print(sample_tuple)
sample_list.__add__(sample_tuple)

print(sample_list)

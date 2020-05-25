import sys
import os

#print('Enter the file name')
#file_name=sys.stdin.readline()
#file_name='test'
file_name=input("Enter the file name")
file_name.strip()

new_file=open(file_name,'w+')
print('enter the file content to add')
content=sys.stdin.readline()
#content='sample content'
#new_file.write(bytes(content,'UTF-8'))
new_file.write(content)

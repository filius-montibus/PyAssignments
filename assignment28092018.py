#Question1: Reverse the whole list using list methods.
li=[1,2,3,'a','b','c']
print('Orignal List :',li)
li.reverse()
print('Reversed List :',li)
print('-'*50)

#Question2:Print all the uppercase letters from a string.
s="This is a Sentence Answer to the Question"
for i in s:
	if i==i.upper():
		print(i,end=' ')
print()
print('-'*50)

#Question3:Split the user input on comma's and store the values in a list as integers.
lis=list(map(int,input('enter numeric elements :').split(',')))
print('The list is :',lis)
print('-'*50)

#Question4:Check whether a string is palindromic or not.
st=str(input("Enter a string :"))
r_st=st[::-1]
if st==r_st:
	print('The string is palindrome.')
else:
	print('The string is not palindrome.')
print('-'*50)

#Question5:Make a deepcopy of a list and write the difference between shallow copy and deep copy.
from copy import deepcopy
l1=['java','pyhton','C++',23,45,77,'perl']
l2=deepcopy(l1)
print('Original list :',l1,'id=',id(l1))
print('Deepcopy list :',l2,'id=',id(l2))

#In case of deep copy, a copy of object is copied in other object,in case of shallow copy, a reference of object is copied in other object.

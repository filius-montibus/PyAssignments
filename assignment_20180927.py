#List
#Q.1-Create a list with user defined inputs.
l1=list(input('Enter list items :').split(','))
print('List :',l1)
print('-'*50)

#Q.2-Add the following list to above created list:[‘google’,’apple’,’facebook’,’microsoft’,’tesla’]
l2=['google','apple','facebook','microsoft','tesla']
l1.extend(l2)
print('Extended list is :',l1)
print('-'*50)

#Q.3-Count the number of time an object occurs in a list.
l3=['blue', 'red', 'blue', 'yellow', 'blue', 'red']
print('Custom list :',l3)
a=str(input('Enter the element :'))
c=l3.count(a)
print('Occurance is=',c)
print('-'*50)

#Q.4-create a list with numbers and sort it in ascending order.
l4=list(map(float,input('Enter numeric elements :').split(',')))
print('Unsorted list :',l4)
l4.sort()
print('Sorted list :',l4)
print('-'*50)

#Q.5-Given are two one-dimensional arrays A and B which are sorted in ascending order. Write a program to merge them into a single sorted array C that contains every item from arrays A and B, in ascending order.
A=[1,2,4,5,8,9,12,15,19]
B=[7,11,13,16,18]
C=A.copy()
C.extend(B)
C.sort()
print('A=',A)
print('B',B)
print('C',C)
print('-'*50)

#Q.6-Count even and odd numbers in that list.
count_odd = 0
count_even = 0
for x in C:
        if x%2==0:
    	     count_even+=1
        elif x%2==1:
    	     count_odd+=1
print("Number of even numbers :",count_even)
print("Number of odd numbers :",count_odd)
print('-'*50)

#Tuples
#Q.1-Print a tuple in reverse order.
t1=('java','C',21,77,'pyhton')
print('Original tuple :',t1)
t1=t1[::-1]
print('Reversed tuple',t1)
print('-'*50)

#Q.2-Find largest and smallest elements of a tuples.
t2=(456, 700, 200, 999, 100, 777, 1014, 567, 783, 384)
print('Tuple is',t2)
print('Max element : ', max(t2))
print('Min element : ', min(t2))
print('-'*50)

#Strings
#Q.1- Convert a string to uppercase.
s1='this is a string'
print(s1)
print(s1.upper())
print('-'*50)

#Q.2- Print true if the string contains all numeric characters.
ss=str(input('Enter string :'))
if ss.isnumeric()==True:
    print('True')
else:
    print('False')
print('-'*50)

#Q.3- Replace the word "World" with your name in the string "Hello World".
s2='Hello World'
print(s2)
print (s2.replace('World', 'Vishvajeet'))

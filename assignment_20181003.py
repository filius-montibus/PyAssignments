# Q.1- Create a function to calculate the area of a sphere by taking radius from user. 
import math
rad=float(input('Enter the radius '))
def area(x):
	ar=4*math.pi*x*x
	return(ar)
print('Area of the sphere =',area(rad))
print('-'*50)

# Q.2- Write a function “perfect()” that determines if parameter number is a perfect number. Use this function in a program that determines and prints all the perfect numbers between 1 and 1000.
nu = int(input("Enter any number: "))
def perfect(n):
	sum1 = 0
	for i in range(1, n):
	    if(n % i == 0):
	        sum1 = sum1 + i
	if (sum1 == n):
		return  True
	else:
		return False

if perfect(nu):
	print(nu,' is a perfect number')
else:
	print(nu,' is not a perfect number')

print('Perfect numbers between 1 and 1000 are:')
k =[]
for i in range(1, 1001):
 	if perfect(i):
 		k.append(i)

print(k)
print('-'*50)

# Q.3- Print multiplication table of n using loops, where n is an integer and is taken as input from the user.
n=int(input('Enter the number '))
for i in range(0,11):
	nu=i*n
	print(n,'*',i,'=',nu)
print('-'*50)

# Q.4- Write a function to calculate power of a number raised to other ( a^b ) using recursion.
a=int(input('First number a = '))
b=int(input('First number b = '))

def pow(x, y):
        if y == 1:
        	return x
        else:
                y-=1
                return x*pow(x,y)

print (a,'^',b,'=',pow(a,b))

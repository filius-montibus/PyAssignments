# Q.1- Name and handle the exception occured in the following program:
#     a=3
#     if a<4:
#        a=a/(a-3)
#        print(a)
 
#A.1-The error present here is ZeroDivisionError
a=3
try:
     if a<4:
       a=a/(a-3)
       print(a)

except ZeroDivisionError as e:
	print('Error occurred -',e)
print('-'*50)    

# Q.2- Name and handle the exception occurred in the following program:
#
#	 l=[1,2,3]
#	 print(l[3])

#A.2- The exception occuring in the above program is IndexErront
l=[1,2,3]
try:
	print(l[3])
except IndexError as e:
	print('Error occured, ',e)
print('-'*50)

# Q.3- What will be the output of the following code:
#
# Program to depict Raising Exception
# try:
#     raise NameError("Hi there")  # Raise Error
# except NameError:
#     print("An exception")
#     raise  # To determine whether the exception was raised or not

#A.3-The code will have following output
print('An exception\nNameError: Hi there')
print('-'*50)    

# Q.4- What will be the output of the following code:
#
#      # Function which returns a/b
#     def AbyB(a , b):
#         try:
#             c = ((a+b) / (a-b))
#         except ZeroDivisionError:
#             print("a/b result in 0")
#         else:
#             print(c)
#   
#     # Driver program to test above function
#     AbyB(2.0, 3.0)
#     AbyB(3.0, 3.0)

#A.4-The output of the code will be
print('-5.0\na/b result in 0')
print('-'*50)    

# Q.5- Write a program to show and handle following exceptions:
# 1. Import Error
# 2. Value Error
# 3. Index Error

#A.5.1
import sys
try:
    print(sys.version)
except ImportError as error:
    print(error)
print('-'*5)
#A.5.2
lst=['dog','cat','horse','elephant']
try:
	lst.remove(21)
except ValueError as err:
	print('ValueError occured -',err)
print('-'*5)
#A.5.3
l=[2,4,5,6,8]
try:
	l[6]
except IndexError as e:
	print(e)
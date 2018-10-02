#Decision and Flow Control
#Q.1- Take an input year from user and decide whether it is a leap year or not.
yr=int(input('Enter a year for leap year evaluation='))
if yr%4==0:
    if yr%100==00:
        if yr%400==0:
            print(yr,' is a Leap year.')
        else:
            print(yr,' is not a leap year.')
    else:
        print(yr,' is a leap year.')
else:
    print(yr,' is not a leap year.')
print('-'*50)

#Q.2- Take length and breadth input from user and check whether the dimensions are of square or rectangle.
l=int(input('Enter length :'))
b=int(input('Enter breadth :'))
if l==b:
    print('The dimensions are of square.')
else:
    print('The dimensions are of rectangle.')
print('-'*50)

#Q.3- Take the input age of 3 people and determine oldest and youngest among them.
p1=int(input('Enter the age of first person-'))
p2=int(input('Enter the age of second person-'))
p3=int(input('Enter the age of third person-'))
if p1>p2 and p1>p3:
    print(p1,'is largest.')
elif p2>p3 and p2>p1:
    print(p2,'is largest.')
else:
    print(p3,'is largest.')
print('-'*50)

#Q.4- Ask user to enter age, sex ( M or F ), marital status ( Y or N ) and then using following rules print their place of service.
#1. if employee is female, then she will work only in urban areas.
#2. if employee is a male and age is in between 20 to 40 then he may work in anywhere
#3. if employee is male and age is in between 40 t0 60 then he will work in urban areas only.
#4. And any other input of age should print "ERROR".
sex=str(input('Enter sex (M/F)-'))
age=int(input('Enter age-'))
mar=str(input('Enter marital status (Y/N)-'))
if sex=='F':
    print( 'You may work only in urban areas.')
elif sex=='M':
    if age>20 and age<40:
        print('You may work in anywhere.')
    elif age>40 and age<60:
        print('You may work in urban areas only.')
    else:
        print('ERROR')
else:
    print('ERROR')
print('-'*50)

#Q.5- A shop will give discount of 10% if the cost of purchased quantity is more than 1000.Ask user for quantity, suppose one unit will cost 100. Judge and print total cost for user.
cost=int(input('Enter the cost='))
quant=int(input('Enter Quantity='))
if quant>=1000:
    tot=cost*quant
    print('Your total is=',tot-(tot*0.1))
elif quant<1000:
    print('Your total is=',cost*quant)
print('='*50)

#Loops
#Q.1- Take 10 integers from user and print it on screen.
i=0
l=[]
while i<10:
    a=int(input('Enter integer-'))
    l.append(a)
    i+=1
print('Your integers are ',l)
print('-'*50)

#Q.2- Write an infinite loop.An infinite loop never ends. Condition is always true.
i=1
while i>0:
    print('Loop',end=' ')
    i+=i
print('-'*50)

#Q.3- Create a list of integer elements by user input. Make a new list which will store square of elements of previous list.
i=0
lst1=[]
lst2=[]
while i<5:
    a=int(input('Enter integer-'))
    lst1.append(a)
    i+=1
print('Firsst list',lst1)

for i in lst1:
    b=i**2
    lst2.append(b)
print('Seconfd list',lst2)
print('-'*50)

#Q.4- From a list containing ints, strings and floats, make three lists to store them separately
ls=[22,'yahoo','google',27,'apple',34,'microsoft',9.0,7.7,64,2.1,13.36]
lstring=[]
lfloat=[]
linteger=[]
for i in ls:
    if isinstance(i, int):
        linteger.append(i)
    elif isinstance(i, float):
        lfloat.append(i)
    elif isinstance(i, str):
        lstring.append(i)
print('Original list :',ls)
print('Integer list :',linteger)
print('Float list :',lfloat)
print('String list :',lstring)
print('-'*50)


#Q.5- Using range(1,101), make a list containing only prime numbers.
prime=[]
for i in range (1,101):
    if i>1:
        for j in range(2,i):
            if i%j==0:
                break
        else:
            prime.append(i)

print('Prime list',prime)
print('-'*50)

#Q.6- Print the following patterns:
#*
#**
#***
#****
count=1
while count<=5:
    print('*'*count)
    count+=1

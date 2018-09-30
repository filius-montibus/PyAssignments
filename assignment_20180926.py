#Q.1-Print anything you want on screen.
print('My first Python script.')

#Q.2-Join two strings using '+'.E.g.-"Acad"+"View”
s1='The quick brown'
s2='fox jumps over the fence.'
print(s1+s2)

#Q.3-Take the input of 3 variables x, y and z . Print their values on screen.
x=input('Enter first variable :')
y=input('Enter second variable :')
z=input('Enter third variable :')
print('x=',x,'y=',y,'z=',z)

#Q.4-Print “Let’s get started” on screen.
print('“Let’s get started”')

#Q.5-Print the following values using placeholders. s=”Acadview” course=”Python” fees=5000
s='Acadview'
course='Python'
fees=5000
print ('%s %s %d' % (s, course, fees))

#Q.6-Find the area of circle pi = 3.14 Take radius as input from user Print the area of circle
pi=3.14
r=int(input('Enter radius='))
ar=pi*r**2
print('Area of circle is=',ar)

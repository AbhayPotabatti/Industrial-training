#python  program to find area of traingle

a=5
b=6
c=7

#Uncomment below to take inpute from the user
#a = float (input('Enter first side: '))
#b = float (input('Enter second side:'))
#c = float (input('Enter third side:'))

#calculate the semi-perimeter 
s=(a+b+c)/

#calculate the semi perimeter 
s=(a+b+c)/2

#calculate the area

area =(s*(s-a)*(s-b)*(s-c))**0.5
print('The area of the traingle is %0.2f',%area)

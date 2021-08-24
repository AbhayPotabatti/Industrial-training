#Name error

name = "exception handling"
try:
    pritn(name)
except:
    print("This is name error")    

#Overflow error

i=1
f=3.0**i

try:
    for i in range(11):
     print(i,f)
     f=f**2

except:
    print("This is overflow bcz of too much large result")

#Syntax error

#amount=10000
#try:
 #   if(amount>2999)
 #    print("U r eligible to purchase gold")
#except:
 #   print("This is syntax error")

 #indentation error

#   print("hello")        

#value error


i="string"
try:
    print(int (i))
except:
    print("This is value error")

#type error

b=40
try:
    print("Type error"+b)
except:
    print("This is type error")
    

# Unbound Local Error
x = 5
try:
    def local():
        print(x)
        x = 7
    local()
except:
    print("This is Unbound Local Error")

#zero division error

try:
    print(7/0)

except:
    print("This is zero division error")    






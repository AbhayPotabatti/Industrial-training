   x = "global variable"
def foo():
    global x #global variable access in function
    y = "local variable"
    x = x * 2
    print(x)
    print(y)
   
foo() 

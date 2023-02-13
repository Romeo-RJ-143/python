def hello():
    global x #global variable
    x = "hello" #local variable
    print(x)
def hello1():
    print(x)
hello()
hello1()

#int + int = int
#int + float = float
#float + float = float
#float + int = int
#str + int = error
#str + float = error

#Implicit type conversion
'''
python automatically convert one data type
to another
'''
a = 10 #int
b = 20.3 #float
c = a + b #float
'''
print(type(a))
print(type(b))
print(type(c))
'''

#Explicit type conversion
'''
user convert datatype
'''
a = 100
b = "40"
c = int(b) 
d = a + c
print(type(d))

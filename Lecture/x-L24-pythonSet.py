my_set = {1,2,9,6,8}
print(my_set)
my_set = {1,1.0,"hello world",2,2} 
print(my_set)
a = {"a","b","c"}
print(a[0]) #not support indexing
my_set = {1,2,9,6,8}
#my_set.add(3)
my_set.update([10,11,12])
print(my_set)
my_set = {1,2,9,6,8}
my_set.remove(2)
print(my_set)

#Set Operation
#union - set of all elements in both

a = {0,1,2}
b = {3,4,5}
print(a|b)

#intersection - elements that are common

a = {0,1,2,3,4}
b = {0,2,4,9,8,7}
print(a&b)


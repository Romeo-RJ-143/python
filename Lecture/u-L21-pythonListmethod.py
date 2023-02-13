#append()
fruit = ["graps", "apple", "mango"]
print(fruit)
fruit.append("bnana")
print(fruit)

#extend()
lang = ["English", "Hindi"]
lang1 = ["French", "German"]
#lang.extend(lang1)
lang1.extend(lang)
print(lang1)

#index() - tell the position (0,1,2)
lang = ["English", "Hindi","French"]
print(lang.index("Hindi"))

#insert()
lang = ["English", "Hindi","French"]
lang.insert(2,"German")
print(lang)

#count()
list_int = [1,2,9,1,4,2,1,5,9,6,1]
print(list_int.count(1))

#remove()
lang = ["English", "Hindi","French"]
print(lang)
lang.remove("Hindi")
print(lang)

#pop()
lang = ["English", "Hindi","French"]
print(lang)
lang.pop(2)
print(lang)

#reverse()
lang = ["English", "Hindi","French"]
print(lang)
lang.reverse()
print(lang)

#sort()
list_int = [1,4,9,8,7,5,1,4,3]
list_int.sort() # sort in asscending order
print(list_int)

list_int.sort(reverse=True) # sort in discending order
print(list_int)

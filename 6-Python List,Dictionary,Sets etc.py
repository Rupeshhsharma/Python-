# ===========================================
# Python Data Structures and Boolean
# ===========================================

# Topics:
# - Boolean
# - Boolean and Logical Operators
# - Lists
# - Comparison operators
# - Dictionaries
# - Tuples
# - Sets

# ===========================================
# Boolean Variables
# ===========================================

# Boolean values are the two constant objects False and True.
# They represent truth values and behave like integers 0 and 1.

print(True, False)  #True False
print(type(True))   #Bool
print(type(False))   #Bool

my_str = 'Rupesh123'
print("Is title case:", my_str.istitle()) #True

print(my_str.isalnum())  # check if all chars are numbers/alphabetic
print(my_str.isalpha())  # check if all chars are alphabetic
print(my_str.isdigit())  # test if string contains only digits
print(my_str.istitle())  # test if string contains title case
print(my_str.isupper())  # test if string contains upper case
print(my_str.islower())  # test if string contains lower case
print(my_str.isspace())  # test if string contains spaces
print(my_str.endswith('k'))  # test if string ends with 'k'
print(my_str.startswith('R'))  # test if string starts with 'R'
True
False
False
True
False
False
False
False
True

# ===========================================
# Boolean and Logical Operators
# ===========================================

print(True and True)   #True
print(True and False)  #False
print(True or False)   #True
print(True or True)    #True

str_example = 'Hello World'
my_str = 'Rupesh'
# Note: str_example.isnum() should be str_example.isalnum()
print(my_str.isalpha() or str_example.isalnum())
True
# ===========================================
# Lists
#A list is a data structure in Python that is a mutable, or changeable, ordered sequence of elements.Each element or value that is inside of a list is called an item.
#Just as strings are defined as characters between quotes, lists are defined by having values between square brackets [ ]
# ===========================================

# Mutable vs Immutable
str1 = "Rupesh"
print(str1) #Rupesh
print(type(str1)) #str

str1 = "Sharma"
print(str1) #Sharma

# Strings are immutable
# str1[2] = "jk"  # This would cause a TypeError

# Lists are mutable
lst = [1, 2, 3, 4, "Rupesh", "Hello"]
print(lst) # 1, 2, 3, 4, "Rupesh", "Hello"
lst[4] = "Sharma"
print(lst[4]) #Sharma

lst = list((1, 2, 3, 4, 5))
print(lst) #[1, 2, 3, 4, 5]
print(type(lst)) #list

for i in lst:
    print(i ** 2)
1
4
9
16
25  

print("Minimum value:", min(lst)) #1
print(type([]))

lst_example = []
print(type(lst_example))#List

lst = list()
print(type(lst))#List

lst = ['Mathematics', 'chemistry', 100, 200, 300, 204]
print(len(lst)) #6
print(type(lst)) #List

# ===========================================
# Append Method
# ===========================================

lst = [1, 2, 3, 4, 5]
lst.append("Rupesh")
print(lst)
#[1, 2, 3, 4, 5,"Rupesh"]
lst.append(["John", "Bala"])
print(lst)
[1, 2, 3, 4, 5,"Rupesh",["John", "Bala"]]
print(lst[2:6])
# [3, 4, 5,"Rupesh",["John", "Bala"]]
# ===========================================
# Insert Method
# ===========================================

lst.insert(2, "Sharma")
print(lst) #[1, 2, "Sharma", 4, 5,"Rupesh",["John", "Bala"]]

# ===========================================
# Extend Method
# ===========================================

lst = [1, 2, 3, 4, 5, 6]
lst.append([8, 9])
print(lst) #[1, 2, 3, 4, 5, 6,[8, 9]]

lst = [1, 2, 3, 4, 5, 6]
lst.extend([8, 9])
print(lst) # [1, 2, 3, 4, 5, 6,8,9]

# ===========================================
# List Operations
# ===========================================

lst = [1, 2, 3, 4, 5]
print("Sum:", sum(lst)) #15
print("Repetition:", lst * 5)
#[1, 2, 3, 4, 5, 1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5,1, 2, 3, 4, 5]
for i in lst:
    print(i / 5)
0.2
0.4
0.6
0.8
1.0
# ===========================================
# Pop Method
# ===========================================

print(lst.pop())  # removes last element
print(lst)
print(lst.pop(2))  # removes element at index 2
print(lst)

# ===========================================
# Count, Length, Index, Min, Max
# ===========================================

lst = [1, 1, 2, 3, 4, 5]
print("Count of 1:", lst.count(1))
print("Length:", len(lst))
print("Index of 1 between 1 and 4:", lst.index(1, 1, 4))
print("Min:", min(lst))
print("Max:", max(lst))

# ===========================================
SETS
A Set is an unordered collection data type that is iterable, mutable, and has no duplicate elements. Python's set class represents the mathematical notion of a set.This is based on a data structure known as a hash table
# ===========================================
## Defining an empy set

set_var= set()
print(set_var)
print(type(set_var))
set()
<class 'set'>
set_var={1,2,3,4,3}
set_var
{1, 2, 3, 4}
set_var={"Avengers","IronMan",'Hitman'}
print(set_var)
type(set_var)
{'IronMan', 'Hitman', 'Avengers'}
set
 
## Inbuilt function in sets

set_var.add("Hulk")
.
print(set_var)
{'IronMan', 'Hitman', 'Avengers', 'Hulk'}
set1={"Avengers","IronMan",'Hitman'}
set2={"Avengers","IronMan",'Hitman','Hulk2'}
set2.intersection_update(set1)
set2
{'Avengers', 'Hitman', 'IronMan'}
##Difference 
set2.difference(set1)
{'Hulk2'}
set2
{'Avengers', 'Hitman', 'Hulk2', 'IronMan'}
## Difference update

set2.difference_update(set1)
print(set2)
{'Hulk2'}

-------------------------------------------------------------------Dictionaries---------------------------------------------------------------------------
A dictionary is a collection which is unordered, changeable and indexed. In Python dictionaries are written with curly brackets, and they have keys and values.

dic={}
type(dic)
dict
type(dict())
dict
set_ex={1,2,3,4,5}
type(set_ex)
set
## Let create a dictionary

my_dict={"Car1": "Audi", "Car2":"BMW","Car3":"Mercidies Benz"}
type(my_dict)
dict
##Access the item values based on keys

my_dict['Car1']
'Audi'
# We can even loop throught the dictionaries keys

for x in my_dict:
    print(x)
Car1
Car2
Car3
# We can even loop throught the dictionaries values

for x in my_dict.values():
    print(x)
Audi
BMW
Mercidies Benz
# We can also check both keys and values
for x in my_dict.items():
    print(x)
('Car1', 'Audi')
('Car2', 'BMW')
('Car3', 'Mercidies Benz')
## Adding items in Dictionaries

my_dict['car4']='Audi 2.0'
my_dict
{'Car1': 'Audi', 'Car2': 'BMW', 'Car3': 'Mercidies Benz', 'car4': 'Audi 2.0'}
my_dict['Car1']='MAruti'
my_dict
{'Car1': 'MAruti', 'Car2': 'BMW', 'Car3': 'Mercidies Benz', 'car4': 'Audi 2.0'}
-----------------------------------------------------------------------Nested Dictionary--------------------------------------------------------------------------
car1_model={'Mercedes':1960}
car2_model={'Audi':1970}
car3_model={'Ambassador':1980}

car_type={'car1':car1_model,'car2':car2_model,'car3':car3_model}
print(car_type)
{'car1': {'Mercedes': 1960}, 'car2': {'Audi': 1970}, 'car3': {'Ambassador': 1980}}
## Accessing the items in the dictionary

print(car_type['car1'])
{'Mercedes': 1960}
print(car_type['car1']['Mercedes'])
1960
------------------------------------------------------------------------------------Tuples---------------------------------------------------------------------------------------------
## create an empty Tuples

my_tuple=tuple()
type(my_tuple)
tuple
my_tuple=()
type(my_tuple)
tuple
my_tuple=("Krish","Ankur","John")
my_tuple=('Hello','World')
print(type(my_tuple))
print(my_tuple)
<class 'tuple'>
('Hello', 'World')
type(my_tuple)
tuple
## Inbuilt function
my_tuple.count('Krish')
1
my_tuple.index('Ankur')
1

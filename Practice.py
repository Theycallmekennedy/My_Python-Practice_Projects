import random
# #print('Hello world')
'''title = 'Kennedy is a programer'
print(title[0])

X="apple "
Y="banana "
Z="cucumber "
title=["Kennedy", "is", "a", "programmer"]
w,x,y,z=title
print(w,x,y,z)
print(X + Y + Z)
'''

'''x = "awesome"
def myfunc():
 x = "great"
print("Python is " + x)
    
my_list=[1,2,3]
my_list[1]=4
print(my_list)
'''
'''y=random.random()
print(y)

x=random.randint(1, 10)
print(x)

my_list = [1, 2, 3, 4, 5]
x = random.choice(my_list)
print(x)

my_list = [1, 2, 3, 4, 5]
x = random.shuffle(my_list)
print(my_list)

my_list = [1, 2, 3, 4, 5]
x = random.sample(my_list, 4)
print(x)

x=5
x = float(x)
print(x)
'''

'''i = """Kennedy is a start up tech guy,
he is also passionate about music,
also he is skilled in music production and audio engineering."""
print(i)
'''
'''for a in "Hi Kennedy":
    print(a)


j = "Kennedy the super star"
print(len(j)

txt = "The best things in life are free!"
print(txt[2:5])
if "joy" in txt:
    print('Yes it is')
else:
    print("no it isn't")
    
b = "They Call Me Kennedy"
print(b[4:8])


def myFunction():
    return True

if myFunction():
    print('YES!')
    
else:
    print('NO!')

#print(myFunction())

x = 'Hello'
print(isinstance(x,str))

print(bool("Kennedy"))

fruits=["cucumber", "apple", "orange", "mango", "grape", "pineapple"]
second_fruit=fruits[-1]
print(fruits)
print(fruits[-4:-2])
print(type(fruits))
print(second_fruit)
print(len(fruits))
'''

'''current_year = 2023
user_birth_year_input = input("What year were you born? ")
user_birth_year = int(user_birth_year_input)
x = current_year - user_birth_year
print(x)
print(f'You are {x} years old')
'''


'''name = input("What is your name? ")
print(name)
Age = input("How old are you? ")
print(Age)
'''

'''course = "Python Programming Language"
contain = 'Python' in course
print(contain)
'''

'''if "it's_cold":
    print("It is a cold day")
elif "it's hot":
    print("It is a hot day")
else:
    print("It is a beautiful day")
    
i = 5
while i < 10:
    print(i)
    i+=1
'''
    
'''for j in range(1, 10):
   print(j)
   
for j in range(5):
    print(j)
    
for i in range(1,2,5):
    print(i)
'''

quantity=2
specification=512
item_number=24

'''print(f'I want to buy {quantity} laptops with a hard disk {specification} and number {item_number}')
txt= 'I want to buy {0} laptops with a hard disk {1} and number {2}'
print(txt.format(quantity, specification, item_number))
'''

'''x=("cucumber", "apple", "orange", "mango", "grape", "pineapple")
y=list(x)
y[-1]= 'banana'
x=tuple(y)
print(x)

x=("cucumber", "apple", "orange", "mango", "grape", "pineapple")
y=list(x)
y.append('banana')
x=tuple(y)
print(x)

x=("cucumber", "apple", "orange", "mango", "grape", "pineapple")
y=list(x)
y.remove('grape')
x=tuple(y)
print(x)

x=("cucumber", "apple", "orange", "mango", "grape", "pineapple")
del (x)
print(x)
'''

my_tuple= (1, 2, 3, 4, 5)
updated_tuple= tuple(value * 2 for value in my_tuple)
print(updated_tuple)
updated_tuple= my_tuple + (6,7)
print(updated_tuple)


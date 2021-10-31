if True:
    print('Its true')

if 3 > 2:
    print('3 is greater than 2')

hungry = False

if hungry:  # No need to do hungry == True/False
    print('FEED ME!')
else:
    print('I am not hungry')

loc = 'Bank'

if loc == 'Auto Shop':
    print('Cars are cool!')
elif loc == 'Bank':
    print('Money is cool')
elif loc == 'Store':
    print('Welcome to the store')
else:
    print('I do not know much')

name = 'Sammy'

if name == 'Frankie':
    print('Hello Frankie')
elif name == 'Sammy':
    print('Hello Sammy')
else:
    print('What is your name')

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

for num in my_list:
    print(num)

for num in my_list:
    # check for even
    if num % 2 == 0:
        print(num)
    else:
        print(f'Odd Number: {num}')

list_sum = 0

for num in my_list:
    list_sum += num

print(f'Total Sum = {list_sum}')

my_string = 'Hello World'
for letter in my_string:
    print(letter)

my_message = 'Entered into loop'

# _ (underscore) here is a common syntax in for loop in python because we don't need a variable here.
for _ in my_string:
    print(my_message)

my_tuple = (1, 2, 3)

for item in my_tuple:
    print(item)

# If you are iterating through a sequence that contains itself tuples, the item can be used with tuple.
my_tuple_list = [(1, 2), (3, 4), (5, 6), (7, 8)]

for tup in my_tuple_list:
    print(tup)

# Tuple Unpacking
for a, b in my_tuple_list:
    print(f'{a}   {b}')

myList = [(1, 2, 3), (4, 5, 6), (7, 8, 9)]

for a, b, c in myList:
    print(f'{a}     {b}    {c}')

# Iterating through dictionary
d = {'k1': 1, 'k2': 2, 'k3': 3}

# By default, when you iterating through a dictionary, then you will iterate through your keys only
for item in d:
    print(item)

# If you want to iterate though both key and value
for a, b in d.items():
    print(f'key = {a}, value = {b}')

# Iterate through only keys
for key in d.keys():
    print(key)

# Iterate through only values
for value in d.values():
    print(value)

x = 0

while x < 5:
    print(f'The current value of x is {x}')
    x += 1
else:
    print('x is not less than 5')

y = [1, 2, 3]

for item in y:
    pass  # That means do nothing at all

testString = 'Sammy'

for letter in testString:
    if letter == 'a':
        continue
    print(letter)

for letter in testString:
    if letter == 'a':
        break
    print(letter)

# Useful operators in Python
for num in range(10):
    print(num)  # prints the number from 0 to 9 (excludes 10)

print('##################')

for num in range(3, 10):
    print(num)  # prints the number from 3 to 9 (excludes 10)

print('##################')

for num in range(0, 10, 2):
    print(num)  # the third operator is a step operator
    # so, this prints 0 to 8 (steps by value 2)

# If we want to capture the output into a list of range() function, then following is the way
generated_list = list(range(0, 10, 2))
print(f'Generated list : {generated_list}')

index_count = 0

for letter in 'abcde':
    print('At index {} the letter is {}'.format(index_count, letter))
    index_count += 1

my_word = 'abcde'
index = 0

for _ in my_word:
    print(my_word[index])
    index += 1

# So, above operation can be done using enumerate() function
for item in enumerate('abcde'):
    print(item)  # This returns tuples

# Now, we can also tuple unpacking as shown above.
for index, letter in enumerate('abcde'):
    print(f'index = {index}, letter = {letter}')

myList1 = [1, 2, 3]
myList2 = ['a', 'b', 'c']

for item in zip(myList1, myList2):
    print(item)

zip_list = list(zip(myList1, myList2))
print(f'After listing the zipped output = {zip_list}')

# What if the above lists are asymmetrical i.e not having the same length across all of them ?
# Ans - Then it just applies zip() to the smallest length of list and ignores all

myList3 = [1, 2, 3, 4, 5, 6, 7, 8]
myList4 = ['a', 'b', 'c']

for item in zip(myList3, myList4):
    print(item)

print(x in [1, 2, 3])

print(1 in [1, 2, 3])

print('a' in 'a world')

key_dict = {'myKey': 100, 'myKey1': 200, 'myKey2': 300, 'myKey3': 400}

print('myKey' in key_dict)

print('myKey' in key_dict.keys())

print(100 in key_dict.values())

min_max_list = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

print(min(min_max_list))

print(max(min_max_list))

from random import shuffle
from random import randint

shuffle(min_max_list)
print(min_max_list)

print(randint(0, 100))

user_input = input('Enter a number')
print(f'The entered user input is = {user_input}')

# The user input always takes it as a string. You can cast it to int, float based on your requirement
print(f'After casting user input to int = {int(user_input)}, The type of the user input is {type(int(user_input))}')

print(f'After casting user input to float = {float(user_input)}, The type of the user input is {type(float(user_input))}')

print(f'After casting user input to float = {bool(user_input)}, The type of the user input is {type(bool(user_input))}')

# List Comprehension
result_list = [char for char in 'word']

print(f'The resultant list = {result_list}')

num_list = [num for num in range(0,10)]
print(f'The num list = {num_list}')

even_list = [num for num in range(0,20) if num % 2 == 0]
print(even_list)

celcius = [0,10,20,34.5]

farenheit = [((9/5)*temp + 32) for temp in celcius]
print(f'Farenheits after converting from Celcius using list comprehension = {farenheit}')

# The above celcius to farenheit conversion can be done using a for loop also and add the same to a list
farenheit_list = []
for cel in celcius:
    cel = (9/5)*cel + 32
    farenheit_list.append(cel)

print(f'Farenheits after converting from celcius using for loop = {farenheit_list}')

# We can also do if else looping inside a list comprehension. But that is not recommended as it reduces the code
# readability
result_list1 = [num if num % 2 == 0 else 'ODD' for num in range(0,20)]
print(result_list1)

# Nested for loop in list comprehension
myList5 = [x*y for x in [1,2,3] for y in [10,100,1000]]
print(myList5)

# The same can also be done using nested for loop approach
myList6 = []

for x in [1,2,3]:
    for y in [10,100,1000]:
        myList6.append(x*y)

print(myList6)




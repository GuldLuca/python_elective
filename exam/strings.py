#String examples

#grap characters

firstString = "Hi there"

print(firstString[3])

#Reverse indexing

print(firstString[-2])



#Slicing

firstString = "123456789"

print(firstString[3:])
print(firstString[:5])
print(firstString[2:6])
print(firstString[::3])

#reverse the string
print(firstString[::-1])


#Properties and methods
#Strings are immutable, can't assign items

#String concatenation

name = "Luca"

change_one = name[:3]

print(change_one)

new_name = change_one + "ca"

print(new_name)

name = new_name

print(name)

#Multiple concatenation

print(name*10)


#Be aware of data types

print(5 + 7)
#print("5" + 7) cant concat string and int
print("5" + "7")

#build-in functions

string_ex = "Hi there"

print(string_ex.upper())

print(string_ex.lower())

#Split based on white space into list
print(string_ex.split())

#Specified what to split on, is not included in list
print(string_ex.split('i'))


#Print formatting - strings

#.format() inserting in same order

print('This string stops here, but {}'.format('this is inserted'))

# for yoda-version index the parameters taken in format method in the curly braces
print('{2} {1} {0}'.format('Corona', 'is', 'unpreferred'))

#With variable assignments
print('{i} {c} {u}'.format(c = 'Corona', i = 'is', u = 'unpreferred'))

#Float formatting "{value:width.precision f}"

some_result = 100.23/777

print('the result was {r:10.3f}'.format(r = some_result))

#f strings

name = "Luca"
age = "under 67"

print(f"Hello, my name is {name}. I'm {age} years old.")










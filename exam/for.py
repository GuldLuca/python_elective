this_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine", "ten"]

#variable name after for can be anything it represent the items
#for every item in the object, do something
for string_number in this_list:
    print(string_number)

#for loop with if statement
for i in this_list:
    if len(i) > 4:
        print("[" + i + "] is a long word.")
    else:
        print("[" + i + "] is a short word.")

#with strings
this_string = "Luca"

for i in this_string:
    print(i)

#You don't need to assign a variable and you don't need that iterator name
for _ in "luca":
    print("what's up?")

#With numbers
that_list = [0, 1, 2, 3, 4, 5]

sum_of_that_list = 0

for i in that_list:
    sum_of_that_list = sum_of_that_list + i

print(sum_of_that_list)

#With tuples

#tuples in a list
a_list = [(10, 3, 5), (2, 65, 1), (1, 9, 0)]
print(len(a_list))

for i in a_list:
    print(i)

#Tuple unpacking. Dublicating the structure of the items (tuples) in the list sequence and then unpack them. 
#a is the first item in each tuple, b is second, c is third. 3 iterators.
for a, b, c in a_list:
    print("Tuple unpacking:")
    print(a)
    print("middle item in tuple skipped.")
    #print(b)
    print(c)

#for dictionary

this_dict = {"key_one" : 10, "key_two" : 15, "key_three" : 20}

#This iterates only through the keys, therefore the keys is returned, not the values
for i in this_dict:
    print(i)

#To get both keys and values, change to .values() if only values is needed
for i in this_dict.items():
    print(i)

#Or use the same unpacking technique as for tuples
for key, value in this_dict.items():
    #print(key)
    print(value)

  
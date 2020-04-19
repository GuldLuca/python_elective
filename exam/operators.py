# Range, start=where to start from, stop=where to stop but not include, step=every what is handled

a_list = [1, 2, 3,]

for i in range(3, 10, 2):
    print(i)

#Casting result to a list
print(list(range(3, 10, 2)))


#Enumerate function

index_count = 0
a_string = "luca"

for i in a_string:
    print(a_string[index_count])
    index_count += 1

#Returns a tuple with index-counter and item/element at index position. You can use tuple unpacking
for index, letter in enumerate(a_string):
    print(index)
    print(letter)
    print("\n")


#Zip function, returns list of tuples, the lists is paired up. Can only go so far as the length of the shortest list

a_list = [1, 2, 3]
b_list = ["a", "b", "c"]
c_list = [4, 5, 6]

for i in zip(a_list, b_list, c_list):
    print(i)

#cast to a list
list(zip(a_list, b_list, c_list))


#in operator

a_dict = {"no" : 1, 1 : "first"}

print(4 in a_list)
print("a" in b_list)
print("first" in a_dict)
print("first" in a_dict.values())


#min, max functions || random library

this_list = [1, 2, 3, 4, 5]

print(min(this_list))
print(max(this_list))

from random import shuffle

#Shuffle dosen't return anything like the sort function, therefor the following approach, nonetype
that_list = ["a", "b", "c", "d"]
shuffle(that_list)
print(that_list)


#grab random int, from to int

from random import randint

print(randint(0,100))


#input, paranthesis is what to represent user with, accepts anythin passed to it as a string

name_res = input("Hi there, what's your name?")
num_res = input("Age?")

print(name_res)
print(type(num_res))
int_num_res = int(num_res)
print(type(int_num_res))

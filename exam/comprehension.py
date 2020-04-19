a_string = "luca"

a_list = []

for i in a_string:
    a_list.append(i)

print(a_list)

#Alternative is list comprehension

#Flattenout for loop. Element for element in some string or what should be in the list
b_list = [i for i in a_string]
print(b_list)

#With range
#Operations can be done to the first i, fx square. 
#You are appending the first i and what is done to it, also if statements with even numbers
c_list = [i**2 for i in range(0,21) if i%2 == 0]
print(c_list)

#More complex example with convert
celcius = [0, 15, 30, 50, 75, 100]
fahrenheit = [((9/5)*temp + 32) for temp in celcius]
print(fahrenheit)

#If-else, but not really readable, different order

results = [x if x%2==0 else "ODD" for x in range(0,11)]
print(results)

#Nested loops, can be confusing, not readable really

#d_list = []

#for i in [2, 4, 6]:
#    for n in [1, 10, 100]:
#        d_list.append(i*n)

#print(d_list)

d_list = [i*n for i in [2, 4, 6] for n in [1, 10, 100]]
print(d_list)

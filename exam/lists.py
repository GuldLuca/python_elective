#Creating a list

that_list = [1, 2, 3]

that_list = [1, "luca", 10,5]

#has len() method

len(that_list)

#Indexing 
that_list = ["first", "second", "third"]

print(that_list[1])

print(that_list[1][4])

#Slicing

print(that_list[:-1])

#Concat

this_list = [1, 2, 3]

print(that_list + this_list)

#Mutable - change elements already in the list

cat_list = that_list + this_list

print(cat_list)

cat_list[-2] = "SECOND"

print(cat_list)

#Add to end of list

cat_list.append("FOURTH")

print(cat_list)

#Remove from end of list

former_item = cat_list.pop() 

print(cat_list)
print(former_item)

#Remove from where ever in list

cat_list.pop(-3)

print(cat_list)

#Sort

what_list = ["hi", "there", "you", "yes", "you"]
wow_list = [4, 8, 2, 5, 1, 2]

what_list.sort()

print(what_list)

#Don't, cause .sort() dosen't return anything, it is of NoneType
#sorted_list = what_list.sort()

#Instead if you want

what_list.sort()
sorted_list = what_list

#Reverse list

wow_list.reverse()

print(wow_list)

#Reverse order of list to decreasing

wow_list.sort()
wow_list.reverse()
print(wow_list)


#Create empty set

this_set = set()

#Add to set. Returned in curly braces but not a dict

this_set.add(5)
this_set.add(3)
this_set.add(3) #Won't be represented in set, cause already there

print(this_set)

#Can't carry multiple occuerence of same object even when based on a list
this_list = [3, 3, 3, 3, 3, 5, 9, 1, 1, 5, 3, 2, 7]

print(this_list)
print(set(this_list))




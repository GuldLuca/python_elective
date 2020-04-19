#Create dictionary

this_dict = {"first_key" : "first_value", "second_key" : "second_value"}
print(this_dict)

#Grab values

print(this_dict["first_key"])

#Realistic example

merch_prices = {"mug" : 30, "t-shirt" : 60, "poster" : 100, "stickers" : 10}

print(merch_prices["poster"])

#Can hold many data types and data structures

that_dict = {"string_key" : 555, 10 : "int_key", 4.5 : "float_key", "list_value" : [1, 2, 3], "dict_value" : {1 :"dict"}}
print(that_dict)

#Get something that's nested - square brackets for each level
print(that_dict["dict_value"][1])

#Change string value inside inside dict
print(that_dict["dict_value"][1].upper())

#Add to dict

merch_prices["backpack"] = 50
print(merch_prices)

#Override value in existing key
merch_prices["t-shirt"] = 55
print(merch_prices)

#Grab all keys

print(merch_prices.keys())

#Grab all values

print(merch_prices.values())

#Grab all keys and values. Will be returned as tuples

print(merch_prices.items())

#Remove from dict

del merch_prices["backpack"]
print(merch_prices)





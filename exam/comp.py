#To check for equality
print(5==5)
print("No"=="Yes")
print("No"=="no")
print("5"==5)
print(5.0 ==5)

#Check to not equal
print("No" != "No")
print("No" != "Yes")

#Greater than, smaller than
print("hiyaya" < "hi")
print(5>1)

#Equal to or greater/smaller than
print(10 >= 5)
print(10 <= 10)
print(10 >= 20)

#More than one comparison - and, or, not

#and - both sides needs to be true for true to be returned
#print(5 < 10 > 0)          <--- please don't --->
print(5 < 10 and 10 > 0)

#Can use paranthesis around each comparison between logical operators
print(("luca" == "luca") and (5 < 1))

#or - just one side needs to be true to return true
print(0 < 10 or 2>0)

#not keyword - return opposite boolean
print(not ("luca" == "luca"))
print(not 10<5)


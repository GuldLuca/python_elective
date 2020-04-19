k = 5

#Simple while loop, while k is smaller than 10, print the text and then increase k by 1 until condition is false
while k < 10:
    print(f"{k} is smaller than 10")
    k += 1

else:
    print(f"{k} is not smaller than 10")


#Pass: Doesn't do anything, something must be placed in the enclosing loop. Pass is often used as a placeholder.
#Great for building the architecture
l = ["a", "b", "c"]

for i in l:
    pass

#Continue:  goes to the top of the closest enclosing loop

for i in l:
    if i == "b":
        continue #this goes up to the for i in l loop, therefore skips the print and just continues.
    print(i)

#Break: breaks out of the current closest enclosing loop
k = 5

while k > 1:

    if k == 3:
        break #breaks and stops the loop
    print(k)
    k -= 1


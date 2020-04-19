#Be aware of writing correct filename and to place file in the same directory as scripts, else FileNotFoundError wil occur
this_file = open("test.txt")

#print everything from file with a pointer that goes through file and stops at the end
print(this_file.read())

#If you try to read it again, the pointer is still at the end of the file. Therefore nothing is printed/returned.
# There is no more content to read
#print(this_file.read())

#To reset pointer

this_file.seek(0)
#print(this_file.read())

#content = this_file.read()

#this_file.seek(0)

#Returns lines of file, lines seperated by \n in list
print(this_file.readlines())

#File location, provide full file path (in OS syntax)

#If you open a file, remember to close
this_file.close()

#Or

#with open("test.txt") as this_file:
#    content = this_file.read()

#print(content)

#Write to file
#Mode (permissions): r= read only, w= write only (overwrite or create new), a = append only (add to end of file)
#r+ = reading and writing, w+ = writing and reading (overwrites existing files or creates new)

#Read only mode
with open("new_file.txt", mode="r") as that_file:
    print(that_file.read())
    that_file.seek(0)


#Append only mode
with open("new_file.txt", mode="a") as that_file:
    that_file.write("\nThis is continued")

#Read with appended content
with open ("new_file.txt", mode="r") as this_file:
    print(this_file.read())

#Writing to file
with open("what_the_file.txt", mode="w") as a_file:
    a_file.write("I just made this!")

#Read with write to file, have created a new file, cause file didn't exist already
with open("what_the_file.txt", mode="r") as a_file:
    print(a_file.read())


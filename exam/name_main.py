#In python there is no main script that will
#be run in the top of script
# built-in variable called __name__
#in the background when fx python3 name_main.py is called
# python assigns __name__ = "__main__"
#You can check for equality with if

if __name__ == "__main__":
    #func_one
    #func_two
    #this code should only be executed
    #when __name__ == "__main__"
    #When this script is called by commandline
    #python3 name_main.py
    pass

def func():
    print("FUNC() in name_main.py")

print("TOP LEVEL in name_main.py")

if __name__== "__main__":
    print("name_main.py is being run directly")

else:
    print("name_main.py has been imported")
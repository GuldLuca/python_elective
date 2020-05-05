import name_main 

print("TOP LEVEL in main_name.py")

name_main.func()

if __name__ == "__main__":
    print("main_name.py his being run directly")

else:
    print("main_name.py has been imported")
# Scope, life-time of a variable 
# Local scope: Only available locally in a function
# Global scope: Available through execution of program

name = "Fredrik"

def main():
    global name
    name = "kalle"
    print(name)


main()


#Python doesn't have block scope, but this is used in most other languages, such as c#, c++, java
# if name == "Fredrik":
#     last_name = "Johansson"
#     print(last_name)
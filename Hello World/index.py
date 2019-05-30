name = input("Enter your name: ")
if len(name)<3:
    print("the character of name must have at least 3.")
elif len(name)>50:
    print("the character of name maximum is 50.")
else:
    print("Good name.")
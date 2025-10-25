correct_password = int(input("choose a password: "))


password = int(input("Enter the password: ")) #will ask the user to enter a password


while password !=1 correct_password:
    print("Incorrect password. Please try again.")
    password = input("Enter the password: ") #will keep asking until password is correct


print("Access granted. Welcome!") #outputs "Access granted. Welcome!"


import getpass

users_db = {"admin": "123456", "test": "test@123"}

username = input("Enter User name: ")
while username not in users_db:
    print("Incorrect Username")
    username = input("Please Enter correct User name: ")

password_attempts = 3
while password_attempts > 0:
    password = getpass.getpass("Enter password: ")
    if password == users_db[username]:
        print("Verified..!!")
        break
    else:
        password_attempts -= 1
        print("Incorrect password. Please try again.")
        if password_attempts == 0:
            print("You have exhausted all password attempts. Exiting.")
            exit()

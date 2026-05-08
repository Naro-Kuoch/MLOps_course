    #username must not be empty and not contain space
    #email must contain @ and . 
    #pwd must be at least 8 characters, one number, one letter and one special char
def validate_username(username):
    if username == '' or " " in username:
        raise ValueError("Username must not be empty and must not contain spaces")
    return username
def validate_email(email):
    if email == '' or " " in email:
        raise ValueError("Email must not be empty and must not contain spaces")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    return email
def validate_password(pwd):
    if len(pwd) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in pwd):
        raise ValueError("Password must contain at least one number")
    if not any(char.isalpha() for char in pwd):
        raise ValueError("Password must contain at least one letter")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in pwd):
        raise ValueError("Password must contain at least one special character")
    return pwd
def enter_data():
    username = input("Enter your name: ")
    username = validate_username(username)
    email = input("Enter your email: ")
    email = validate_email(email)
    pwd = input("Enter your password: ")
    pwd = validate_password(pwd)
    return {
        "username": username,
        "email": email,
        "pwd": pwd
    }
r = enter_data()
print(r)


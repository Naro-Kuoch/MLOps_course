# username must not be empty and must not contain spaces.
# email must contain an '@' symbol and a domain dot.
# password must be at least 8 characters long, and include a number, a letter, and a special character.

def validate_username(username):
    """Validate that the username is non-empty and contains no spaces."""
    if username == '' or " " in username:
        raise ValueError("Username must not be empty and must not contain spaces")
    return username

def validate_email(email):
    """Validate that the email is non-empty and follows a simple email format."""
    if email == '' or " " in email:
        raise ValueError("Email must not be empty and must not contain spaces")
    if "@" not in email or "." not in email:
        raise ValueError("Invalid email format")
    return email

def validate_password(pwd):
    """Validate that the password meets basic strength requirements."""
    if len(pwd) < 8:
        raise ValueError("Password must be at least 8 characters long")
    if not any(char.isdigit() for char in pwd):
        raise ValueError("Password must contain at least one number")
    if not any(char.isalpha() for char in pwd):
        raise ValueError("Password must contain at least one letter")
    if not any(char in "!@#$%^&*()-_=+[]{}|;:'\",.<>?/" for char in pwd):
        raise ValueError("Password must contain at least one special character")
    return pwd
def validate_age(age):
    """Validate that the age is a positive integer."""
    if not age.isdigit() or int(age) <= 0:
        raise ValueError("Age must be a positive integer")
    return int(age)

def enter_data():
    """Prompt the user for registration details and validate each field."""
    username = input("Enter your name: ")
    username = validate_username(username)

    email = input("Enter your email: ")
    email = validate_email(email)

    pwd = input("Enter your password: ")
    pwd = validate_password(pwd)
    age = input("Enter your age: ")

    return {
        "username": username,
        "email": email,
        "pwd": pwd,
        "age": age
    }





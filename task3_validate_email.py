import re

def validate_email(email):
    # Regular expression for email validation
    pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
    return bool(re.match(pattern, email))

# Input email from the user
email_input = input("Enter an email address: ")
if validate_email(email_input):
    print("The email address is valid.")
else:
    print("The email address is invalid.")

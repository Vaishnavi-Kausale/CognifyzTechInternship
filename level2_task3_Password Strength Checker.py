import re

def check_password_strength(password):
    # Initialize strength criteria
    length_criteria = len(password) >= 8
    uppercase_criteria = bool(re.search(r'[A-Z]', password))
    lowercase_criteria = bool(re.search(r'[a-z]', password))
    digit_criteria = bool(re.search(r'[0-9]', password))
    special_char_criteria = bool(re.search(r'[!@#$%^&*(),.?":{}|<>]', password))

    # Count how many criteria are met
    strength_score = sum([
        length_criteria,
        uppercase_criteria,
        lowercase_criteria,
        digit_criteria,
        special_char_criteria
    ])

    # Determine the strength level
    if strength_score == 5:
        return "Strong"
    elif strength_score >= 3:
        return "Medium"
    else:
        return "Weak"

def main():
    print("Password Strength Checker")
    password = input("Enter your password: ")
    
    strength = check_password_strength(password)
    print(f"Your password strength is: {strength}")
    print("Tips for a stronger password:")
    if len(password) < 8:
        print("- Use at least 8 characters.")
    if not re.search(r'[A-Z]', password):
        print("- Include at least one uppercase letter.")
    if not re.search(r'[a-z]', password):
        print("- Include at least one lowercase letter.")
    if not re.search(r'[0-9]', password):
        print("- Include at least one digit.")
    if not re.search(r'[!@#$%^&*(),.?\":{}|<>]', password):
        print("- Include at least one special character.")

# Run the password strength checker
main()

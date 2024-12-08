def is_palindrome(s):
    # Normalize the string (remove spaces and make lowercase)
    s = s.replace(" ", "").lower()
    return s == s[::-1]  # Check if the string is the same reversed

# User inputs the string to check
input_str = input("Enter a string: ")
if is_palindrome(input_str):
    print("The string is a palindrome.")
else:
    print("The string is not a palindrome.")

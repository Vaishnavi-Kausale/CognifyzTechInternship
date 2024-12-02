# CognifyzTechInternship
# Level First_Task First 
# Function to reverse a string
def reverse_text(input_text):
    
    # Initialize an empty string for the reversed result
    reversed_result = ""
    
    # Loop through the string in reverse order
    for char in input_text:
        reversed_result = char + reversed_result  # Add each character to the front of the result

    return reversed_result


# Example to demonstrate the function
if __name__ == "__main__":
    my_string = "hello"
    
    # Call the function and store the reversed string
    reversed_string = reverse_text(my_string)
    
    print("Original String:", my_string)
    print("Reversed String:", reversed_string)

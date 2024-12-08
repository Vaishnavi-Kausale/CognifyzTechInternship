import random

def number_guesser():
    print("Welcome to the Number Guesser Game!")
    
    # Get the range from the user
    try:
        lower_bound = int(input("Enter the lower bound of the range: "))
        upper_bound = int(input("Enter the upper bound of the range: "))
        
        if lower_bound >= upper_bound:
            print("Invalid range! The lower bound must be less than the upper bound.")
            return
        
        # Generate a random number within the specified range
        secret_number = random.randint(lower_bound, upper_bound)
        attempts = 0
        
        print(f"I have chosen a number between {lower_bound} and {upper_bound}. Try to guess it!")

        while True:
            try:
                # Get the user's guess
                guess = int(input("Enter your guess: "))
                attempts += 1
                
                if guess < lower_bound or guess > upper_bound:
                    print(f"Please guess a number within the range {lower_bound} to {upper_bound}.")
                elif guess < secret_number:
                    print("Too low!")
                elif guess > secret_number:
                    print("Too high!")
                else:
                    print(f"Congratulations! You guessed the number in {attempts} attempts.")
                    break
            except ValueError:
                print("Invalid input. Please enter a number.")
    except ValueError:
        print("Invalid range. Please enter numeric values for the bounds.")

# Run the game
number_guesser()

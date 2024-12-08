def count_word_occurrences(file_path):
    try:
        # Read the file content
        with open(file_path, 'r') as file:
            text = file.read().lower()

        # Remove punctuation and split into words
        words = text.split()
        cleaned_words = [word.strip('.,!?;:"()[]{}') for word in words]

        # Count word occurrences
        word_count = {}
        for word in cleaned_words:
            word_count[word] = word_count.get(word, 0) + 1

        # Sort and display the word counts
        print("Word occurrences (in alphabetical order):")
        for word in sorted(word_count):
            print(f"{word}: {word_count[word]}")

    except FileNotFoundError:
        print("The specified file does not exist. Please provide a valid file path.")
    except Exception as e:
        print(f"An error occurred: {e}")

def main():
    print("Word Occurrence Counter")
    file_path = input("Enter the path to the text file: ")
    count_word_occurrences(file_path)

# Run the word occurrence counter
main()

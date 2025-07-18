# List and Dictionary Comprehension
# Comprehenion is a QUICK WAY to build up list or dict from already existing data

# List Comprehension

def main():
    words = get_words("speech.txt")

    # List Comprehension
    # Performing some transformation on list
    # Filtering our list further with if condition
    lowercase_words = [word.lower() for word in words if len(word) > 4]

    # Dictionary Comprehension
    # Doing the same thing as that for loop and if condition, but in less code
    counts = {word: lowercase_words.count(word) for word in lowercase_words}

    for word in lowercase_words:
        print(
            f"""| {word} | {counts[word]}  |\n+----------------+\n""", end=""
        )

# Helping function created in GROK, high level stuff (ik, can't code the below function yet...)
def get_words(file_path):
    """
    Reads a text file and returns a list of words.

    Args:
        file_path (str): Path to the text file.

    Returns:
        list: List of words from the file.

    Raises:
        FileNotFoundError: If the specified file does not exist.
        IOError: If there's an error reading the file.
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            text = file.read()
            # Split on whitespace and remove punctuation
            words = ''.join(char if char.isalnum() or char.isspace() else ' ' for char in text).split()
            return words
    except FileNotFoundError:
        raise FileNotFoundError(f"The file {file_path} was not found.")
    except IOError as e:
        raise IOError(f"Error reading file {file_path}: {str(e)}")



main()

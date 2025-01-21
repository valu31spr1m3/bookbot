def count_characters():

    """
    Reads the content of a text, converts it to lowercase,
    counts the frequency of each character in the text, and prints the result.
    """
    # Specify the relative or absolute path to the text file you want to process
    text_path = "books/frankenstein.txt"

    # Open the file and read its entire contents as a single string; convert to lowercase
    with open(text_path) as f:
        file_contents = f.read().lower()

    # Initialize an empty dictionary to keep track of character counts
    char_count = {}

    # Iterate over each character in the string
    # - If the character is new, set its count to 1
    # - If it already exists, increment its existing count
    for character in file_contents:
        char_count[character] = char_count.get(character, 0) + 1

    # Print the dictionary containing all character counts
    print(char_count)

count_characters()
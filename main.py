def count_characters():
    """
    Reads the content of a text file, converts it to lowercase,
    counts the frequency of each character and the number of purely alphabetical words,
    then prints a report sorted by character frequency.
    """

    # Path to the text file you want to analyze
    text_path = "books/frankenstein.txt"

    # Open the file, read its entire contents, and convert to lowercase
    with open(text_path) as f:
        file_contents = f.read().lower()

    # Count how many words are purely alphabetical (i.e., no punctuation, digits, etc.)
    words = file_contents.split()
    word_count = 0
    for word in words:
        if word.isalpha():
            word_count += 1

    # Initialize a dictionary to keep track of the frequency of every character
    char_count = {}

    # Iterate over each character in the text:
    # - If it's new, start its count at 1
    # - Otherwise, increment its existing count
    for character in file_contents:
        char_count[character] = char_count.get(character, 0) + 1

    def split_big_dict(big_dict):
        """
        Converts a dictionary of form {'a': 3476, 'b': 2587}
        into a list of dictionaries, each containing two key-value pairs:
          - 'char': the original dictionary's key
          - 'num': the integer frequency of that key
        Example:
            Input:  {'a': 3476, 'b': 2587}
            Output: [{'char': 'a', 'num': 3476}, {'char': 'b', 'num': 2587}]
        """
        small_dicts_ls = []
        for k, v in big_dict.items():
            small_dicts_ls.append({'char': k, 'num': v})
        return small_dicts_ls

    # Transform the character-frequency dictionary into a list of smaller dictionaries
    dicts_ls = split_big_dict(char_count)

    # Define a helper function to sort by the 'num' key in each smaller dictionary
    def sort_on(entry):
        return entry['num']

    # Sort the list of dictionaries in descending order by frequency
    dicts_ls.sort(reverse=True, key=sort_on)

    # Print a brief report
    print(f"--- Begin report of {text_path} ---")
    print(f"{word_count} words found in the document (only counting purely alphabetical words).")

    # Print the frequency of each alphabetical character (ignore punctuation, spaces, digits, etc.)
    for item in dicts_ls:
        if item['char'].isalpha():
            print(f"The '{item['char']}' character was found {item['num']} times")

    print("--- End report ---")

count_characters()
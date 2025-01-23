def count_characters():
    """
    Reads the content of a text file, converts it to lowercase,
    counts the frequency of each character and the number of purely alphabetical words,
    then prints a report sorted by character frequency.
    """

    # Path to the text file you want to analyze
    text_path = "books/frankenstein.txt"

    # Dictionary to store character counts (e.g., {'a': 1200, 'b': 980, ...})
    char_count = {}

    # Counter for purely alphabetical words (excludes punctuation, digits, etc.)
    word_count = 0

    # Open the file in read mode
    with open(text_path) as f:
        for line in f:
            line = line.lower()

             # Split the line into words and increment the count for words that are purely alphabetical
            words = line.split()
            word_count += sum(1 for word in words if word.isalpha())

        
            # Count the frequency of each alphabetical character in the line
            for character in line:
                if character.isalpha():
                    char_count[character] = char_count.get(character, 0) + 1

    # Print a brief report
    print(f"--- Begin report of {text_path} Version 2.0 ---")
    print(f"{word_count} words found in the document (only counting purely alphabetical words).")

    # Sort characters by their frequency in descending order and print the results
    sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)
    for char in sorted_char_count:
        print(f"The '{char[0]}' character was found {char[1]} times")

    
    
    print("--- End report ---")    

count_characters()
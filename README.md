BookBot is my first project!

Optimizing main.py => main_v2.py

1.    Counting Words Simplification:
    Your loop for counting purely alphabetical words can be replaced with a generator expression. 
    This reduces redundancy and might improve readability.

    >>> word_count = sum(1 for word in words if word.isalpha())

2.    Splitting Dictionary Function:
    The split_big_dict function is unnecessary. 
    Python's list comprehension can create the list of dictionaries without requiring a separate function.

    >>> Instead of converting to a list of dictionaries, sort char_count.items() directly. You can use:
        sorted_char_count = sorted(char_count.items(), key=lambda x: x[1], reverse=True)

        The .items() method of a dictionary transforms its key-value pairs into a sequence of tuples, 
        where each tuple represents one key-value pair.

        key=lambda x: x[1] tells sorted() to sort the items based on the second element of each tuple — the character counts. 
        When combined with reverse=True, this ensures the sorting goes from highest to lowest counts.

3.    Sorting Dictionaries:
    Consider skipping the intermediate list and sort directly over the dictionary items. This eliminates one transformation step.

4.   File Reading:
    You're reading the file's entire content at once with .read(), which could be memory-intensive for large files. 
    Iterating line-by-line and incrementally updating your counts might be more efficient.

    >>> with open(text_path) as f:
        for line in f:
            line = line.lower()
            words = line.split()
            word_count += sum(1 for word in words if word.isalpha())

            for character in line:
                char_count[character] = char_count.get(character, 0) + 1



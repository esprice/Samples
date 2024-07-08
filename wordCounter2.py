def word_counter(filename):
    word_count = {}
    
    # Open the file and read its contents
    with open(filename, 'r') as file:
        text = file.read()
    
    # Tokenize the text into individual words
    words = text.lower().split()
    
    # Count the occurrences of each word
    for word in words:
        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1
    
    # Sort the dictionary by keys (words) in alphabetical order
    sorted_word_count = sorted(word_count.items())
    
    # Output the word count
    print("Word Count:")
    for word, count in sorted_word_count:
        print(f"{word}: {count}")

# Add text file to search
word_counter(".txt")



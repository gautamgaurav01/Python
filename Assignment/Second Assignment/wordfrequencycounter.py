# word count in file
with open("file.txt") as f:
    file = f.read()
    word = file.split()
    total_word = len(word)
    print(f"The words in file are {total_word}")
    for x in range(total_word):
        freq = 0
        for y in range(total_word):
            if word[x] == word[y]:
                freq += 1
        if word[x] not in word[:x]:
            print(f"The word {word[x]} repeat {freq} times")

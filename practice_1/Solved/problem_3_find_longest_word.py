def longest_word(words):
    longest = max(words, key=len)
    return longest, len(longest)

print(longest_word(["Honorificabilitudinitatibus", "longest", "word"]))  # Output: ('Honorificabilitudinitatibus', 27)
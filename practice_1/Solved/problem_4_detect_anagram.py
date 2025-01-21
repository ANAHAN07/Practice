def is_anagram(term_1, term_2):
    return sorted(term_1) == sorted(term_2)

print(is_anagram("listen", "silent"))       # Output: True

print(is_anagram("anagrams", "analyze"))    # Output: False
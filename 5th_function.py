def are_anagrams(word1, word2):
    return sorted(word1) == sorted(word2)
result = are_anagrams("ata", "ata")
print(f"Слова 'ata' и 'apa' являются анаграммами: {result}")
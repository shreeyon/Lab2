sentence = input("Enter a sentence: ")
vowels = set("aeiouAEIOU")
used_vowels = set()

for char in sentence:
    if char in vowels:
        used_vowels.add(char.lower())

print(used_vowels)

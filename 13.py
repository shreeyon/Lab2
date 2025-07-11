text = input("Enter text: ")

freq = {}

for ch in text:
    if ('A' <= ch <= 'Z') or ('a' <= ch <= 'z'):
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1

for char in freq:
    print(f"{char}: {freq[char]}")

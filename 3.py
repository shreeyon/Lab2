sen = input("Enter a sentence: ")
words = sen.split()
counts = []  

for i in words:
    if i not in counts:
        count = 0
        for j in words:
            if j == i:
                count += 1
        print(f"{i}: {count}")
        counts.append(i)

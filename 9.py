import random

numbers = set()

while len(numbers) < 10:
    numbers.add(random.randint(1, 100))

print("Set with 10 unique elements:", numbers)

numbers.remove(min(numbers))
numbers.remove(max(numbers))

print("Set after removing smallest and largest:", numbers)

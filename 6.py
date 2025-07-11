n = int(input("Enter number of elements: "))
numbers = []

print("Enter the numbers:")
for _ in range(n):
    num = float(input())
    numbers.append(num)

numbers = tuple(numbers)

# Average
average = sum(numbers) / n

# Median
sorted_nums = sorted(numbers)
mid = n // 2
if n % 2 == 1:
    median = sorted_nums[mid]
else:
    median = (sorted_nums[mid - 1] + sorted_nums[mid]) / 2

# Mode
freq = {}
for num in numbers:
    if num in freq:
        freq[num] += 1
    else:
        freq[num] = 1

max_count = 0
mode = None
for num in freq:
    if freq[num] > max_count:
        max_count = freq[num]
        mode = num

if max_count == 1:
    mode = None  # no mode if all unique

print("\nResults:")
print(f"Tuple: {numbers}")
print(f"Average: {average}")
print(f"Median: {median}")
if mode is None:
    print("Mode: No mode (all numbers are unique)")
else:
    print(f"Mode: {mode}")

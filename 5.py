lst = [10, 3, 5, 8, 7, 12, 4, 2]
result = []

for i in range(len(lst)):
    if i % 2 == 0:
        num = lst[i]
        if num > 1:
            is_prime = True
            for j in range(2, num):
                if num % j == 0:
                    is_prime = False
                    break
            if is_prime:
                result.append(num)

print(result)

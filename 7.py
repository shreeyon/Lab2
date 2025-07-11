n = int(input("Enter number of points: "))
points = []

print("Enter points as x y (separated by space):")
for _ in range(n):
    x, y = map(float, input().split())
    points.append((x, y))

if n < 2:
    print("The points form a straight line.")
else:
    x0, y0 = points[0]
    x1, y1 = points[1]

    is_line = True

    for i in range(2, n):
        x, y = points[i]
        # Check if (y1 - y0)*(x - x0) == (y - y0)*(x1 - x0)
        if (y1 - y0) * (x - x0) != (y - y0) * (x1 - x0):
            is_line = False
            break

    if is_line:
        print("The points form a straight line.")
    else:
        print("The points do NOT form a straight line.")

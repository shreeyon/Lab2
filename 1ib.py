a=int(input("How many numbers do you want to add in list: "))
l=[]
for i in range (0,a):
    num=int(input(f"Enter a number {i+1}: "))
    l.append(num)
    
l.sort()
print("Sorted data is:")
print(l)
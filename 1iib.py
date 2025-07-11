a=int(input("How many numbers do you want to add in list: "))
l=[]
for i in range (0,a):
    num=int(input(f"Enter a number {i+1}: "))
    l.append(num)
    
for i in range(0,a):
    for j in range(i+1,a):
        if(l[i]>l[j]):
            temp=l[i]
            l[i]=l[j]
            l[j]=temp
print("Sorted data is:")
print(l)
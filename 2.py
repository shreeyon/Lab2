l1=[1,2,3,4,5,6]
l2=[3,5,7,9,11]
merge=l1+l2
result=[]
for i in merge:
    if (i not in l1) or (i not in l2):
        result.append(i)
print(result)
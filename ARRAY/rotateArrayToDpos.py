n=int(input())
d=int(input())
list1=[]
for i in range(n):
 value=int(input())
 list1.append(value)
print(list1[d:]+list1[:d])
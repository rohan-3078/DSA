n=int(input())
k=int(input())
list1=[]
for i in range(n):
 value=int(input())
 list1.append(value)
for i in range (k):
 new = list1[n-1:n]+list1[0:n-1]
 list1 = new
#  last=list1[n-1]
#  for j in range(n-1,0,-1):
#    list1[j]=list1[j-1]
#  list1[0] = last
# print(list1)
print(new)

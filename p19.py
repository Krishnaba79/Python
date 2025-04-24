"""list Function
append
clear
count
extend
index
insert
pop
remove
reverse
sort
len

del
range
pointer\references"""

#sorting

"""list = [5, 4, 7, 2, 1, 8, 3, 6]
print(list)
list.sort()
list.sort(reverse=True)
print(list)

list = ['a', 'c', 'e', 'b', 'd']
print(list)
list.sort(reverse=True)
print(list)

list = ["Hii", "Hello", "Hat", "Home",]
print(list)
list.sort()
print(list)"""

#copy list

l1 = [2, 3, 4, 5]
l2 = l1.copy()

l2.append(10)

print("L 1 is:", l1)
print("L 2 is:", l2)

"""#reverse function

l1 = [5,4,2,9,7,1,6,3]
print(l1)

l1.reverse()
print(l1)

#count function

l1=[1,2,4,3,1,3,5,6,7,3,1]
print("Count is:",l1.count(1))

#clear function

l1=[1,2,4,3,1,3,5,6,7,3,1]
l1.clear()
print(l1)

#index function

l1=[1,2,4,3,1,3,5,6,7,3,1]   l1=["Apple","Mango"]
print(l1.index(1))   print(l1.index("Mango"))

#range function

l1 = list(range(1,100))
print(l1)

for i in [1,3,4,2,5]:
    print(i)

l1=list(range(2,20,2))
print(l1)

#string

h="Hello Hiral"
for i in h:
    print(i)


l1 = [1,2,3]
l2 = [5,6,7]

l2.append(l1)
print(l2)
print(len(l2))
print(l2[-1])
print(l2[-1][1])


l1=[[1,2,3],[4,5,6],[7,8,9]]
print(l1[0][1])
print(l1[1][1])
print(l1[2][1])

l1 = [5, 9, 2, 1, 6]
for i in l1:
    print(i)"""

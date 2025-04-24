# creat a list using[]
# can update list value
a = [1,2,3,4,5]
a[0]=8        # list is changeble
print(a)
print(a[0])

# we can create a list with items of different types
c = [45,"harry",False,6.9]
print(c)

#list slicing
friends = ["lija","krishna","princy","dharm","aarya"]
print(friends[0:4])
print(friends[-3:-2])

#list method
# ascending order:sort
l1=[5,4,6,8,1]                               
l1.sort()
print(l1)
'''[l1_sorted=l1.sort()
   print(l1_sorted
   its wrong]'''

# reverse order:reverse
l2=[2,3,4,5,6]
l2.reverse()
print(l2)

# append: means add at the end of list
l3=[1,2,3,4,5]
l3.append(8)
print(l3)

#insert:this will add at index when you choose
l4=[1,2,3,4,5]
l4.insert(3,8)        # 3 number as given is the index number and the number 8 is add in this index
print(l4)

#pop : delete element at index  and return its value
l5=[1,2,3,4,5,6]
l5.pop(2)
print(l5)

#remove : remove element from list
l6=[1,2,3,4,56,6]
l6.remove(56)
print(l6)




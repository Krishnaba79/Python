a= {1,2,3,4,4,5}               # cant't add repetation value
print(type(a))
print(a)


#important = this systax will create an empty dictionary and not an empty set
a={}
print(type(a))

# an empty set can be created using the below synrax:
b= set(1,2,3)
print(type(b))
#METHOD:
#add:
b.add(4)
b.add(5)
b.add((6,7,8))
print(b)  
# can't add list and dictionary in sets

#len: print the length of set
print(len(b))

#remove:
b.remove(5)
print(b)

#pop:remove any value of the sets
print(b.pop())
print(b)

#clear:to clear sets means its do empty sets

#union:returns a new set with all items from both sets


#intersection: return a set which contains only items in both sets


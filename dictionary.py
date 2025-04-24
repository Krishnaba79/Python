mydict = {
    "fast":"in aquick manner",  # first is key(like:fast) and second is value(like in quick manner)
    "lija" : "a student",
    "anotherdict": {'harry':'player'}    #neasted dictionary
}
mydict["lija"]= ("a proffesor")     # its a changeble and overwrite on old value of lija key
print(mydict["fast"])  
print(mydict["anotherdict"]["harry"])  
print(mydict["lija"])

#METHODS:
#keys:print the keys of the dictionary as a list
print(mydict.keys())
print(list(mydict.keys()))

#values:print the value of the dictionary as a list
print(mydict.values())

#items:print the key and value as a tuples
print(mydict.items())

#update:to update dictionary
updatedict = {
    "kasvala":"sirname"
}
print(mydict.update(updatedict))
print(mydict)

#get:
print(mydict.get("harry"))# return none as harry 2 is not present in the dict
#print(mydict["harry2"])  # thows an eror as harry2 is not present in the dict


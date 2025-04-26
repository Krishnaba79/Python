# 1 Create a function 
def demo(name,age):
    #print value
    print(name,age)

#call fun.
demo("Ben",25)

# 2 create a function with variable len of args
def func1(*args):
    for i in args:
        print(i)
print("printing values:")
func1(20,40,60)
func1(80,100)

# 3 return multiple values from a function
   # [A] get result in tuple format
def calculation(a,b):
    add = a+b
    sub = a-b
     # return multiple values sepreted by comma
    return add, sub

res = calculation(40,10)
print(res)

   # [B] get result in unpack tuple

def calculation(a,b):
    return a+b, a-b
add, sub = calculation(50,10)
print(add,sub)


# 4 create a function with defalute args 
    # function with default argss
def show_employee(name,salary=9000):
    print("name:",name, "salary:",salary)

show_employee("Ben",1200)
show_employee("Jessa")


















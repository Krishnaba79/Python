#Online Order
order=[]
Total=[]
Milk=20
Soda=50
Choco=30

a=int(input("""
What would you like to order:
    
1) Milk........................20/-
2) Soda........................50/-
3) Choclates...................30/-
Your choice: """))

while a<=3:
    if a==1:
        print("You have ordered Milk. That would be 20 Rs")
        Quantity=int(input("Quantity: "))
        b=input("Would You like to add more to the cart(Y/N):")
        order.append("Milk")
        Total.append(Milk*Quantity)
        if b=="Y" or b=="y":
            c=input("2/3:")
            if c==2:
                print("Soda would be added to your cart")
                Quantity=int(input("Quantity: "))
                order.append("Soda")
                Total.append((Soda*Quantity))
            else:
                print("Chocolates would be added to your carts")
                Quantity=int(input("Quantity: "))
                order.append("Chocolates")
                Total.append(Choco*Quantity)
        else:
            pass
    elif a==2:
        print("You have ordered Soda. That would be 50 Rs")
        Quantity=int(input("Quantity: "))
        b=input("Would You like to add more to the cart(Y/N):")
        order.append("Soda")
        Total.append(Soda*Quantity)
        if b=="Y" or b=="y":
            c=input("1/3:")
            if c==1:
                print("Milk would be added to your cart")
                Quantity=int(input("Quantity: "))
                order.append("Milk")
                Total.append((Milk*Quantity))
            else:
                print("Chocolates would be added to your carts")
                Quantity=int(input("Quantity: "))
                order.append("Chocolates")
                Total.append(Choco*Quantity)
        else:
            pass
    elif a==3:
        print("You have ordered Choclates. That would be 30 Rs")
        Quantity=int(input("Quantity: "))
        b=input("Would You like to add more to the cart(Y/N):")
        order.append("Chocolates")
        Total.append(Choco*Quantity)
        if b=="Y" or b=="y":
            c=input("1/2:")
            if c==1:
                print("Soda would be added to your cart")
                Quantity=int(input("Quantity: "))
                Total.append((Milk*Quantity))
                order.append("Milk")
            else:
                print("Chocolates would be added to your carts")
                Quantity=int(input("Quantity: "))
                Total.append(Soda*Quantity)
                order.append("Soda")
        else:
            pass
    else:
        print("Invalid number")
    
    print("Order: ",order)
    print("Total: ",sum(Total))
    break


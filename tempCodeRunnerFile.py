count=1
for x in range(4):
    for y in range(3):
        print(count,end=" ")
        count+=1
        if count>=11:
            break
    print()

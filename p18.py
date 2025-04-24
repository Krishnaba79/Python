"""num=[123,456,789,101]
for i in num:
    print(str(i)[1])"""


nums = []
even = []
odd = []

for i in range(5):
    usr = int(input("Enter the no:"))
    nums.append(usr)
print(nums)

for x in nums:
    if x % 2 == 0:
        even.append(x)
        print(even)
    else:
        odd.append(x)
        print(odd)

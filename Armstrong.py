num = int(input("Enter the number :"))
sum = 0
cont = num
while cont > 0:
    dig = cont%10
    sum += dig ** 3
    cont //= 10
if num == sum:
    print("That is an Armstrong number")
else:
    print("That is not an Armstrong number")
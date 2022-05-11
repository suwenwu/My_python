num1 = int(input("请输入第一个数："))
num2 = int(input("请输入第二个数："))

while num1 % num2 != 0:
    c = num1 % num2
    num1 = num2
    num2 = c
else:
    print(num2)

import math

# 海伦公式
a = int(input("请输入第一个数"))
b = int(input("请输入第二个数"))
c = int(input("请输入第三个数"))
p = (a + b + c) / 2
s = math.sqrt(p * (p - a) * (p - b) * (p - c))
print("三角形的面积是：", s)

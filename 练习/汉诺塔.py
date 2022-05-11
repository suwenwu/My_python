# n:n个盘子，a表示起始杆，b表示过渡杆，c表示目标杆
def hanoi(n, a, b, c):
    if n == 1:
        print(a, "----->", c)
    else:
        # 第一步：将n-1个盘子从A搬到B，C为过渡杆
        hanoi(n - 1, a, c, b)
        # 第二步：将第n个盘子从A搬到C，
        hanoi(1, a, b, c)
        # 第三步：将n-1个盘子从B搬到C，A为过渡杆
        hanoi(n - 1, b, a, c)


# 先输入需要移动的盘子数量
n = int(input('请输入需要移动的盘子数量：'))

hanoi(n, "A", "B", "C")

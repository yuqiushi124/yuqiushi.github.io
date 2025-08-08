total = 0
for i in range(1,6):
    num = float(input(f'请输入第{i}个数字'))
    total+=num
average = total / 5

print(f'五个数字的平均值是:{average}')

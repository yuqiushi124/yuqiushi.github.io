age  = int(input('请输入你的年龄:'))

if  age<=0:
    print('年龄不能为复数')
elif age<=12:
    print('你是儿童')
elif age <=17:
    print('你是青少年')
else:
    print('你是成人')
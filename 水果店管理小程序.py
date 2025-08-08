fruits = ['苹果','香蕉','橙子']

while True:
    print('\n===水果店管理系统===')
    print('1.查看水果')
    print('2.添加水果')
    print('3.删除水果')
    print('4.修改水果')
    print('5.退出系统')

    choice = input('请选择功能（1-5）:')

    if choice =='1':
        print('\n当前水果列表:')
        for fruit in fruits:
            print(fruit)

    elif choice=='2':
        new_fruit = input('请输入要添加的水果:')
        fruits.append(new_fruit)
        print(f'{new_fruit}已添加')
    elif choice=='3':
        del_fruit=input('请输入要删除的水果：')
        if del_fruit in fruits:
            fruits.remove(del_fruit)
            print(f'{del_fruit}已删除')
        else:
            print('该水果不存在')
    elif choice=='4':
        old_fruit = input('请输入要修改的水果')
        if old_fruit in fruits:
            new_name = input('请输入要修改的水果名字：')
            index = fruits.index((old_fruit))
            fruits[index]= new_name
            print(f'{old_fruit}已修改为{new_name}')
        else:
            print('该水果不存在')
    elif choice=='5':
        print('退出系统，再见👋')
        break
    else:
        print('输入无效,请输入1-5之间的数字')
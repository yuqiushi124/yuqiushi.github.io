import os#判断文件是否存在
import random#实现随机推荐水果

FILENAME = "fruits.txt"#文件名

# 读取文件，加载水果列表
def load_fruits():
    if not os.path.exists(FILENAME):
        return ['苹果', '香蕉', '橙子']  # 如果没有文件，默认初始化列表
    with open(FILENAME, 'r', encoding='utf-8') as f:  #以只读模式（'r'）打开名为 FILENAME 的文件，使用 UTF-8 编码读取（避免中文乱码），with 语句是 Python 的上下文管理器，会自动帮你打开和关闭文件，保证用完后文件被正确关闭。
        lines = f.readlines()
    return [line.strip() for line in lines if line.strip()]  #列表推导式

# 保存水果列表到文件
def save_fruits(fruits):#定义一个函数叫save fruits，他有个参数fruits
    with open(FILENAME, 'w', encoding='utf-8') as f:  #以写入模式（'w'）打开名为 FILENAME 的文件，使用 UTF-8 编码读取（避免中文乱码）,'w'会覆盖原文件
        for fruit in fruits:
            f.write(fruit + '\n') #把当前的水果吗写入文件，后面加上换行符\n, 保证每个水果独占文件的一行 

# 主程序
def main():
    fruits = load_fruits()

    while True:
        print('\n===水果店管理系统===')
        print('1.查看水果')
        print('2.添加水果')
        print('3.删除水果')
        print('4.修改水果')
        print('5.随机推荐水果')
        print('6.退出系统')

        choice = input('请选择功能（1-6）:')

        if choice == '1':
            print('\n当前水果列表:')
            for fruit in fruits:
                print(fruit)

        elif choice == '2':
            new_fruit = input('请输入要添加的水果:').strip()
            fruits.append(new_fruit)
            print(f'{new_fruit}已添加')

        elif choice == '3':
            del_fruit = input('请输入要删除的水果：').strip()
            if del_fruit in fruits:
                fruits.remove(del_fruit)
                print(f'{del_fruit}已删除')
            else:
                print('该水果不存在')

        elif choice == '4':
            old_fruit = input('请输入要修改的水果:')
            if old_fruit in fruits:
                new_name = input('请输入要修改的水果名字：').strip()
                index = fruits.index(old_fruit)
                fruits[index] = new_name
                print(f'{old_fruit}已修改为{new_name}')
            else:
                print('该水果不存在')

        elif choice == '5':
            if not fruits:
                print('水果列表为空，无法推荐')
            else:
                recommend = random.choice(fruits)
                print(f'今天推荐你吃：{recommend}')

        elif choice == '6':
            save_fruits(fruits)
            print('退出系统，数据已保存，再见！')
            break

        else:
            print('输入无效，请输入1-6之间的数字')

if __name__ == "__main__":
    main()
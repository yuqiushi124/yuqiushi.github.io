import random

print("🎲 欢迎来到猜数字游戏！")
secret = random.randint(1, 100)  # 随机生成一个秘密数字
guess_count = 0

while True:
    guess = int(input("请输入你猜的数字（1~100）："))
    guess_count += 1

    if guess < secret:
        print("太小了！")
    elif guess > secret:
        print("太大了！")
    else:
        print(f"🎉 恭喜你猜对了！你用了 {guess_count} 次")
        break
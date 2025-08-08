import random
print('欢迎来到猜数字游戏！你最多有十次机会')

secret = random.randint(1,100)
guess_count = 0
guessed = False
low = 1
high = 100

while guess_count <10:
    guess = int(input(f'请输入你猜的数字(范围:{low}~{high}):'))
    guess_count += 1

    if guess < secret:
        print('太小了')
        low = max(low, guess +1 )

    elif guess > secret:
        print('太大了')
        high = min(high, guess-1)
    else:
        print(f'恭喜你答对了！你用了{guess_count}次')
        guessed = True
        break
if not guessed:
    print(f'很遗憾，你猜了十次没猜中。正确答案是{secret}')


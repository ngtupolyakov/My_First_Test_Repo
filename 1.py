import random
counter = 0
mid = 0
secret = random.randint(1, 100)
TL = 0
TM = 101
flag = False
mid += counter
counter = 0
while flag != True:
    counter += 1
    choice = random.choice([i for i in range(TL, TM)])
    int(input('Угадайте число \n'))
    if choice > secret:
        TM = choice
        print('Too much')
    elif choice < secret:
        TL = choice
        print('Too little')
    elif choice == secret:
        print('Congratulations', counter)
        flag = True

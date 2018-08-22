import random
num1 = int(input('請在1到10中選一個整數:'))
num2 = random.randint(1,10)
while num1 != num2:
    if num1 < 11:
        print('沒猜中喔')
    else:
        print('是1到10')
    num1 = int(input('請在1到10中選一個整數:'))
print('恭喜你猜中了')
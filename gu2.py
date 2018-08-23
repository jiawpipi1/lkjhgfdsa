import random
import easygui
num2 = random.randint(1,100)
num3 = 0
while True:
    num1 = int(easygui.enterbox('請從1到100選一個整數'))
    num3 += 1
    print('這是你猜的第',num3,'次')
    if num1 == num2:
        break
    elif num1 > num2:
        print('比答案大')
    else:
        print('比答案小')
print('恭喜你猜中了')
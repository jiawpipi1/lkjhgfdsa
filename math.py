num_1 = float(input('請輸入第一個數字'))
num_2 = float(input('請輸入第二個數字'))
num_1 = str(num_1)
num_2 = str(num_2)

if num_1 > num_2:
    print( num_1 + '大於' + num_2 )
elif num_1 == num_2:
    print( num_1 +'等於' + num_2 )
else:
    print( num_1 + '小於' + num_2 )
import easygui
while True: 
    f =easygui.choicebox('What do you want to eat?',choices = ['Italian:90',
        'waitress:20000','Max Chao:0'])
    num = int(easygui.integerbox('How many do you want',upperbound = 10,
        lowerbound = 1))
    p1 = f.split(':')
    e = easygui.choicebox('What do you want drink?', choices = ['cm:30',
        'stm:40',])
    p2 = e.split(':')
    num1 = int(easygui.integerbox('How many do you want',upperbound = 10,
        lowerbound = 1))
    pr1 = int(p1[1])
    pr2 = int(p2[1])
    pr3 = str(pr1*num + pr2*num1)
    num = str(num)
    num1 = str(num1)
    easygui.msgbox('you order '+num+'x'+ f +' '+num1+'x'+ e + '\n' +'\a'
                   + pr3 + '$','total','ok' )
    rep = easygui.ynbox('Do you still want to order?')
    if rep ==True:
        continue
    else:
        break
easygui.msgbox('You`re welcome!')



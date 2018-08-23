import progressbar
import time
data = []
cou = 0
bar = progressbar.ProgressBar(max_value=1000000)


with open('reviews.txt','r') as f:
    for line in f:
        data.append(line)
        cou += 1
        bar.update(cou)
print('讀完,共有',len(data),'筆留言')

word_dict = {}
for d in data:
    words = d.split(' ')
    for word in words:
        cou += 1
        if cou%10000000 == 0:
            print(cou)
            print(len(word_dict))
        if word in word_dict:
            word_dict[word] += 1
        else:
            word_dict[word] = 1

for word in wordict:
    if word_dict[word]>1000:
        print(word, word_dict[word])

print(len(word_dict))

while True:
    word = input('請問你要查詢哪個單字:')
    if word =='q':
        print('離開查詢')
        break
    if word in word_dict:
        print(word,'出現的次數:',word_dict[word])
    else:
        print('沒有出現這個字:',word)
print('程式結束')

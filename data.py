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
ol = 0
for d in data:
    ol += len(d)
print('均長:',ol/len(data))

data1 = []
for d in data:
    if len(d) < 150:
        data1.append(d)
print(data1[0])
print('小於150',len(data1))
saint=[]
for d in data:
    if 'saint' in d:
        saint.append(d)
print([0])
print('流言有saint的有:',len(saint),'筆')

Max=[]
for d in data:
    if 'Max' in d:
        Max.append(d)
print(Max[0])
print('流言有Max的有:',len(Max),'筆')

i= []


i = [d for d in data if'i' in d]
print(i[0])
print('流言有I的有:',len(i),'筆')
bang = []


bang = [d for d in data if'bang' in d]
print(bang[0])
print('流言有bang的有:',len(bang),'筆')
biang = ['趙華杉','趙華杉','趙華杉','趙華杉','趙華杉']
print('垃圾們:',biang)
index = int(input("請問第幾個人最廢 :"))-1
if -len(biang) <= index < len(biang):
   del biang[index]
   print('選得真好')
   print('其他垃圾;',biang)
else:
    print("看來你才是垃圾") 
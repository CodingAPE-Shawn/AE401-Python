#w 寫入模式
file = open('abc.txt','w')
file.write('AE401')
file.close()

#a 添加模式
file = open('abc.txt','a')
file.write('Python')
file.close()

#r 讀取模式
file = open('abc.txt','r')
a=file.read()
file.close()


import os.path
while True :
    print('====================')
    print('*  Word Counter    *')
    print('====================')
    print('(1). 輸入檔案')
    print('(2). 查詢檔案中單字次數')
    print('(3). 替換檔案中單字')
    print('(4). 離開系統')
    sel = input('選擇功能(1~4):')
    if sel=='1': # 輸入檔名，讀取內容
        fn = input('請輸入檔名(含副檔名): ')
        if os.path.isfile(fn):
            fo = open(fn, 'r')
            content = fo.read()
            print('檔案內容如下:\n', content)
        else:
            print('沒有這個檔案!!!')
        fo.close()
    elif sel=='2':#查詢單字出現次數(還要能輸入單字範圍)
    
    
    
    elif sel =='3': # 取代單字
        old = input('請輸入要被換掉的單字: ')
        new = input('請輸入取代的單字: ')
        content=content.replace(old, new)
        f=input('請輸入檔名(含副檔名):')
        file=open(f,'w')
        file.write(content)
        file.close()
    elif sel=='4': 
        break
    else:
        print('輸入錯誤，請重新輸入!')

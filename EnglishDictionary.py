d = {}

print('############################')
print('#歡迎進入阿茂的英文高手系統#')
print('############################')
print('*** 使用本系統，你將成為英文高手!!! ***')

while True:
    print('=>')
    print('1. 建立辭彙')
    print('2. 列出所有單字')
    print('3. 英翻中')
    print('4. 中翻英')
    print('5. 測驗學習成果')
    print('6. 離開系統')
    
    sel = input('請輸入欲執行選項: ')

    if sel=='1':
        while True:
            voc = input('輸入新單字(按0跳出): ')
            if voc == '0':
                break
            if voc not in d:
                m = input('輸入中文解釋: ')
                d[voc] = m
            else:
                print('單字已經存在')
    elif sel=='2':
        lk = sorted(d)
        for item in lk:
            print(item, '是', d[item])
    elif sel=='3': # 英翻中
        voc = input('輸入要查詢的英文單字(按0跳出): ')
        if voc == '0':
            break
        if voc in d: 
            print(d[voc])
        else:
            print('我的字典沒有這個單字')
    elif sel=='4': # 中翻英
        got=False
        ch = input('輸入要查詢的中文(按0跳出): ')
        if ch == '0':
            break
        for k,v in d.items():
            if ch==v:
                print(ch,'的英文是',k)
                got=True
        if not got:
            print('抱歉，查不到!')                                      
    elif sel=='5': # 測驗
        score=0
        print('The total score is', len(d), 'points')
        for k, v in d.items():
            print(v, ':')
            ans = input()
            if ans == k:
                score += 1
                print('correct! you got', score, 'points now')
            else:
                print('wrong! you got', score, 'points now')
    elif sel=='6':
        break
    else:
        print('輸入錯誤，請重新輸入!')


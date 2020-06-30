num=0
price=0
sell=0
sells=[]

print('########################')
print('#Python蘋果店進出貨系統#')
print('########################')

while True:
    
    print('功能=>')
    print('1. 設定')
    print('2. 進貨')
    print('3. 出貨')
    print('4. 營業額統計')
    print('5. 庫存顯示')
    print('6. 離開系統')
    
    sel = input('請輸入欲執行選項: ')

    if sel=='1': # 設定
        num = int(input('輸入蘋果數量: '))
        price = int(input('輸入蘋果單價: '))
        print('蘋果目前有', num, '顆')
        print('蘋果一顆', price, '元')
    elif sel=='2': # 進貨
        numin = int(input('輸入蘋果進貨數量: '))
        num = num + numin
        print('蘋果目前有', num, '顆')
    elif sel=='3': # 出貨
        numout = int(input('輸入出貨數量: '))
        print('應付', numout*price, '元')
        num = num - numout
        sell = sell + numout
        sells.append(numout)
        print('蘋果目前有', num, '顆')
    elif sel=='4': # 營業額與毛利
        for i in range(len(sells)):
            print(sells[i], '顆', sells[i]*price, '元')
        total = sell * price
        print('共賣了', sell, '顆')
        print('營業額', total, '元')
    elif sel=='5': # 庫存
        print('蘋果目前有', num, '顆')
    elif sel=='6':
        break
    else:
        print('wrong input')


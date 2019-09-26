a = input('請輸入身分證號:')

if len(a) != 10:
    print('錯誤')
    exit()

b = a[0]  #切出a的第1位
if not(b.isupper() or b.islower()):   #'A'<=b<='Z'
    print('第一位輸入錯誤')
    exit()



print('正確')
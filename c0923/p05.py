a = input('請輸入:')
b = a[0]
c = a[len(a)-1]

if b.isupper() and c.isupper():
    print('正確')
else:
    print('錯誤')


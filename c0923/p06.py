a = input('請輸入:')
b = a[0]
c = a[1:]

print(b)
print(c)

if b.isupper() and c.isdigit(): 
    print('正確')
else:
    print('錯誤')


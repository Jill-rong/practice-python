a = input('請輸入:')
b = a[0]
c = a[len(a)-1]
d = len(a)

if  not(b.isupper() or b.islower()):
    print('否')
    exit()
    
if not(c.isupper()  or c.islower()):
    print('否')
    exit()

if  d>=2:
    print('是')
else: 
    print('否')


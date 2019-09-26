import math

#------------
p = input('請輸入單價：')
a = input('請輸入數量：')

#------------
try:
    p = int(p)
    a = int(a)
except:
    print('請輸入數字')
    exit()

#------------
t = p * a

#------------
if t>1000:
    t=t*0.9

#------------
print('總金額=',round(t))


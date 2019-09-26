import math

#------------
a = input('請輸入本金：')
i = input('請輸入利率：')
p = input('請輸入期數：')

#------------
try:
    a = int(a)
    i = float(i)
    p = int(p)
except:
    print('請輸入數字')
    exit()

#------------
t = a*(1+i)**p

#------------
print('總金額=',round(t))


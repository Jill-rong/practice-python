import math

#------------
c = input('請輸入國文：')
e = input('請輸入英文：')
m = input('請輸入數學：')

#------------
try:
    c = int(c)
    e = int(e)
    m = int(m)
except:
    print('請輸入數字')
    exit()

#------------
if c>100 or c<0:
    print('國文成績錯誤')
    exit()

if e>100 or e<0:
    print('英文成績錯誤')
    exit()

if m>100 or m<0:
    print('數學成績錯誤')
    exit()

#------------
t = c + e + m
a = t / 3

#------------
print('總分=',t)
print('平均=',round(a,2))

#------------
if a>=60:
    print('及格')
else:
    print('不及格')
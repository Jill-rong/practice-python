import math

r = input('請輸入半徑：')

try:
    r = float(r)
except:
    print('請輸入數字')
    exit()

a = math.pi * r**2
print('面積:',a)
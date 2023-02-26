Python 3.7.3 (v3.7.3:ef4ec6ed12, Mar 25 2019, 22:22:05) [MSC v.1916 64 bit (AMD64)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> name = 'Uncle'
>>> print(name)
Uncle
>>> type(name)
<class 'str'>
>>> name.lower()
'uncle'
>>> name.upper()
'UNCLE'
>>> friend = 'บอย'
>>> print('สวัสดีบอย สบายดีไหม')
สวัสดีบอย สบายดีไหม
>>> print('สวัสดี' + friend + 'สบายดีไหม')
สวัสดีบอยสบายดีไหม
>>> money = 10
>>> print('บอยยืมเงิน 10 บาท')
บอยยืมเงิน 10 บาท
>>> print(friend + 'ยืมเงิน ' + str(money) + 'บาท)
      
SyntaxError: EOL while scanning string literal
>>> type(money)
<class 'int'>
>>> print(friend + 'ยืมเงิน ' + str(money) + 'บาท')
บอยยืมเงิน 10บาท
>>> print('{}ยืมเงิน {} บาท'.format(friend,money))
บอยยืมเงิน 10 บาท
>>> print(f'{friend}ยืมเงิน {money} บาท')
บอยยืมเงิน 10 บาท
>>> money = 1234567890
>>> print(f'{money:,}')
1,234,567,890
>>> print(f'{money:,.2f}')
1,234,567,890.00
>>>  print(f'{:,.2f}'.format(friend,money))
KeyboardInterrupt
>>> print(f'{:,.2f}'.format(money))
SyntaxError: f-string: empty expression not allowed
>>> print('{:,.2f}'.format(money))
1,234,567,890.00
>>> import math
>>> math.pi
3.141592653589793
>>> math.pi * (5 ** 2)
78.53981633974483
>>> from datetime import datetime
>>> datetime.now()
datetime.datetime(2023, 2, 19, 21, 30, 25, 769630)
>>> datetime.now().strftime('%y%m%d %H:%M:%S')
'230219 21:32:58'
>>> import random
>>> random.randint(1,7)
6
>>> store = ['ป้าส้ม','ป้าเล็ก','ลุงดำ']
>>> random.choice(store)
'ป้าส้ม'
>>> 

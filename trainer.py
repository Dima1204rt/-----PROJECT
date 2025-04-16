import random
from random import randint 

list_81=[1, 2, 3, 4, 5, 6, 7]
list_8=[0, 1, 2, 3, 4, 5, 6, 7]

x_list=[]

b=0
r=0

for i in range(10):
    bitx1=random.choice(list_81)
    bitx1=str(bitx1)
    dc=randint(1, 4)
    for i in range(dc):
        bitx=random.choice(list_8) 
        x_list.append(str(bitx))
    x=bitx1 + "".join(x_list)
    print('Восьмиричное число: ', x)
    for i in reversed(x):
        i=int(i)
        r=i*8**b+r #правильный ответ в десятичной СС
        b=b+1
    print('правильный ответ в десятичной СС: ', r)
    user_ans=input('Введите получившееся десятичное число: ')
    if user_ans == str(r):
        print('правильно!')
    else:
        print('неправильно!')
    x_list=[]
    b=0
    r=0
       



    
    

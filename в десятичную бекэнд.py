# перевод из любой в десятичную СС

import random
from random import randint 

list_21=[1]
list_2=[0, 1]
list_81=[1, 2, 3, 4, 5, 6, 7]
list_8=[0, 1, 2, 3, 4, 5, 6, 7]
list_161=[1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
list_16=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']

num_sys = input('Выберите систему счисления переводить ИЗ которой хотели бы потренироваться: ')

x_list=[]
b=0
ansi=0
ost_resh=10

for i in range(10):


    if num_sys == '2':

        bitx1=random.choice(list_21)
        bitx1=str(bitx1)
        dc=randint(1, 5)
        for i in range(dc):
            bitx=random.choice(list_2) 
            x_list.append(str(bitx))
        x=bitx1 + "".join(x_list)
        print('Двоичное число: ', x)
        for i in reversed(x):
            i=int(i)
            ansi=i*2**b+ansi #правильный ответ в десятичной СС
            b=b+1
        #print('правильный ответ в десятичной СС: ', ansi)

        user_ans=input('Введите получившееся десятичное число: ')
        if user_ans == str(ansi):
            print('ПРАВИЛЬНО!')
        else:
            print('НЕПРАВИЛЬНО!')

        ost_resh=ost_resh-1
        print('Осталось решить: ', ost_resh)
        x_list=[]
        b=0
        ansi=0


    if num_sys == '8':

        bitx1=random.choice(list_81)
        bitx1=str(bitx1)
        dc=randint(1, 4)
        for i in range(dc):
            bitx=random.choice(list_8) 
            x_list.append(str(bitx))
        x=bitx1 + "".join(x_list)
        print('Восьмеричное число: ', x)
        for i in reversed(x):
            i=int(i)
            ansi=i*8**b+ansi #правильный ответ в десятичной СС
            b=b+1
        #print('правильный ответ в десятичной СС: ', ansi)

        user_ans=input('Введите получившееся десятичное число: ')
        if user_ans == str(ansi):
            print('ПРАВИЛЬНО!')
        else:
            print('НЕПРАВИЛЬНО!')

        ost_resh=ost_resh-1
        print('Осталось решить: ', ost_resh)
        x_list=[]
        b=0
        ansi=0


    if num_sys == '16':
        
        bitx1=random.choice(list_161)
        bitx1=str(bitx1)
        dc=randint(1, 3)
        for i in range(dc):
            bitx=random.choice(list_16) 
            x_list.append(str(bitx))
        x=bitx1 + "".join(x_list)
        print('Шестнадцатеричное число: ', x)
        for i in reversed(x):

            if i == 'A': 
                i='10'
            if i == 'B':
                i='11'
            if i == 'C':
                i='12'
            if i == 'D':
                i='13'
            if i == 'E':
                i='14'
            if i == 'F':
                i='15'

            i=int(i)
            ansi=i*16**b+ansi #правильный ответ в десятичной СС
            b=b+1
        #print('правильный ответ в десятичной СС: ', ansi)
        user_ans=input('Введите получившееся десятичное число: ')

        if user_ans == str(ansi):
            print('ПРАВИЛЬНО!')
        else:
            print('НЕПРАВИЛЬНО!')

        ost_resh=ost_resh-1
        print('Осталось решить: ', ost_resh)
        x_list=[]
        b=0
        ansi=0

                

       


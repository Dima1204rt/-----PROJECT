# перевод из десятичной в любую другую СС

import random
from random import randint

list_101=[1, 2, 3, 4, 5, 6, 7, 8, 9]
list_10=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

num_sys = input('Выберите систему счисления переводить В которую хотели бы потренироваться: ')

x_list=[]
ost=0
c=1000
ans=[]
ost_resh=10


for i in range(10):

    bitx1=random.choice(list_101)
    bitx1=str(bitx1)
    if num_sys == '2':
        dc=randint(1, 2)
    if num_sys == '8':
        dc=randint(1, 2)
    if num_sys == '16':
         dc=randint(1, 2)     
    for i in range(dc):
        bitx=random.choice(list_10) 
        x_list.append(str(bitx))
    x=bitx1 + "".join(x_list)
    print('Десятичное число: ', x)
    x_list=[]


    if num_sys == '2':
        ost=0
        c=1000
        x=int(x)
        while c >= 2:
            c=x//2
            ost=x-c*2
            x=c
            ans.append(str(ost))
            
        ans.append(str(c))
        ans.reverse()

        ansi="".join(ans) #правильный ответ в двоичной СС
        #print('правильный ответ в двоичной СС: ', ansi)
        user_ans=input('Введите получившееся двоичное число: ')
        if user_ans == str(ansi):
            print('ПРАВИЛЬНО!')
        else:
            print('НЕПРАВИЛЬНО!')
        ost_resh=ost_resh-1
        print('Осталось решить: ', ost_resh)
        ans=[]


    if num_sys == '8':
        ost=0
        c=1000
        x=int(x)
        while c >= 8:
            c=x//8
            ost=x-c*8
            x=c
            ans.append(str(ost))
            
        ans.append(str(c))
        ans.reverse()

        ansi="".join(ans) #правильный ответ в восьмеричной СС
        #print('правильный ответ в восьмеричной СС: ', ansi)
        user_ans=input('Введите получившееся восьмеричное число: ')
        if user_ans == str(ansi):
            print('ПРАВИЛЬНО!')
        else:
            print('НЕПРАВИЛЬНО!')
        ost_resh=ost_resh-1
        print('Осталось решить: ', ost_resh)
        ans=[]


    if num_sys == '16':
        ost=0
        c=1000
        x=int(x)
        while c >= 16:
            c=x//16
            ost=x-c*16
            x=c
        
            if str(ost) == '10':
                ost='A'
                
            if str(ost) == '11':
                ost='B'

            if str(ost) == '12':
                ost='C'

            if str(ost) == '13':
                ost='D'

            if str(ost) == '14':
                ost='E'

            if str(ost) == '15':
                ost='F'
            ans.append(str(ost))

        if str(c) == '0':
                c=''

        if str(c) == '10':
                c='A'
                
        if str(c) == '11':
                c='B'

        if str(c) == '12':
                c='C'

        if str(c) == '13':
                c='D'

        if str(c) == '14':
                c='E'

        if str(c) == '15':
                c='F'

        ans.append(str(c))
        ans.reverse()

        ansi="".join(ans) #правильный ответ в шестнадцатеричной СС
        #print('правильный ответ в шестнадцатеричной СС: ', ansi)
        user_ans=input('Введите получившееся шестнадцатеричное число: ')
        if user_ans == str(ansi):
            print('ПРАВИЛЬНО!')
        else:
            print('НЕПРАВИЛЬНО!')
        ost_resh=ost_resh-1
        print('Осталось решить: ', ost_resh)
        ans=[]




        
       
        
    

         
        

        
        





'''         if str(ost) == '10':
                ost='A'
                
            if str(ost) == '11':
                ost='B'

            if str(ost) == '12':
                ost='C'

            if str(ost) == '13':
                ost='D'

            if str(ost) == '14':
                ost='E'

            if str(ost) == '15':
                ost='F'

            ans.append(str(ost))

        if str(c) == '10':
                c='A'
                
        if str(c) == '11':
                c='B'

        if str(c) == '12':
                c='C'

        if str(c) == '13':
                c='D'

        if str(c) == '14':
                c='E'

        if str(c) == '15':
                c='F'

        ans.append(str(c))

        ans.reverse()
        ansi="".join(ans)
        print(ansi)
'''

    
    
    
    

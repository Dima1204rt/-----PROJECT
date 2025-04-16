
from db import Database
import random
from random import randint


class App:

    db = Database()

    def __init__(self):

        self.num_sys=''
        self.direction=''
        self.x=0
        self.ansi=''
        self.n_pr=0 # количество примеров, для тренировки


    def generate (self, num_sys, direction):
        
        if direction == 'ИЗ десятичной':
            self.num_sys=num_sys
            ''''
            list_101=[1, 2, 3, 4, 5, 6, 7, 8, 9]
            list_10=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
            x_list=[]
            bitx1=random.choice(list_101)
            bitx1=str(bitx1)
            if self.num_sys == '2':
                dc=randint(1, 2)
            if self.num_sys == '8':
                dc=randint(1, 2)
            if self.num_sys == '16':
                dc=randint(1, 2)    
            for i in range(dc):
                bitx=random.choice(list_10) 
                x_list.append(str(bitx))
            self.x=bitx1 + "".join(x_list) #сгенерированное число
            self.x=int(self.x)
            '''
            self.x=randint(1, 150)
            return self.x
        
        if direction == 'В десятичную':
             self.num_sys=num_sys
             list_21=[1]
             list_2=[0, 1]
             list_81=[1, 2, 3, 4, 5, 6, 7]
             list_8=[0, 1, 2, 3, 4, 5, 6, 7]
             list_161=[1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
             list_16=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
             x_list=[]
             b=0
             self.ansi=0

             if self.num_sys == 'Двоичная':
                  bitx1=random.choice(list_21)
                  bitx1=str(bitx1)
                  dc=randint(4, 7) # выбор количества цифр в сгенерированном числе
                  for i in range(dc):
                      bitx=random.choice(list_2) 
                      x_list.append(str(bitx))
                  self.x=bitx1 + "".join(x_list)
                  return self.x
             
             if self.num_sys == 'Восьмеричная':
                  bitx1=random.choice(list_81)
                  bitx1=str(bitx1)
                  dc=randint(0, 2) # выбор количества цифр в сгенерированном числе
                  for i in range(dc):
                      bitx=random.choice(list_8) 
                      x_list.append(str(bitx))
                  self.x=bitx1 + "".join(x_list)
                  return self.x
             
             if self.num_sys == 'Шестнадцатеричная':
                  bitx1=random.choice(list_161)
                  bitx1=str(bitx1)
                  dc=randint(0, 1) # выбор количества цифр в сгенерированном числе
                  for i in range(dc):
                      bitx=random.choice(list_16) 
                      x_list.append(str(bitx))
                  self.x=bitx1 + "".join(x_list)
                  return self.x
                  
                  
             
    def convert(self, num_sys, direction):

        self.num_sys=num_sys
        self.direction=direction

        if self.direction == 'ИЗ десятичной':
            ost=0
            c=1000
            ans=[]
            
            if self.num_sys == 'Двоичная':
                while c >= 2:
                    c=self.x//2
                    ost=self.x-c*2
                    self.x=c
                    ans.append(str(ost))
                ans.append(str(c))
                ans.reverse()
                self.ansi="".join(ans) #правильный ответ в двоичной СС
                return self.ansi
            
            if self.num_sys == 'Восьмеричная':
                while c >= 8:
                    c=self.x//8
                    ost=self.x-c*8
                    self.x=c
                    ans.append(str(ost))
                ans.append(str(c))
                ans.reverse()
                self.ansi="".join(ans) #правильный ответ в восьмеричной СС
                return self.ansi
            
            if self.num_sys == 'Шестнадцатеричная':
                while c >= 16:
                    c=self.x//16
                    ost=self.x-c*16
                    self.x=c
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
                self.ansi="".join(ans) #правильный ответ в шестнадцатеричной СС
                return self.ansi
            
        if self.direction == 'В десятичную':
            b=0
            self.ansi=0

            if self.num_sys == 'Двоичная':
                for i in reversed(str(self.x)):
                    i=int(i)
                    self.ansi=i*2**b+self.ansi #правильный ответ в десятичной СС
                    b=b+1
                #return self.ansi
            
            if self.num_sys == 'Восьмеричная':
                for i in reversed(str(self.x)):
                    i=int(i)
                    self.ansi=i*8**b+self.ansi #правильный ответ в десятичной СС
                    b=b+1
                return self.ansi
            
            if self.num_sys == 'Шестнадцатеричная':
                for i in reversed(str(self.x)):
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
                    self.ansi=i*16**b+self.ansi #правильный ответ в десятичной СС
                    b=b+1
                return self.ansi


    def check(self, user_ans):
        self.ansi=str(self.ansi)
        user_ans=str(user_ans)
        print(self.ansi, user_ans)
        print(type(self.ansi), type(user_ans))
        if self.ansi == user_ans: 
            return '✅ПРАВИЛЬНО✅'
        else:
            return '❌НЕПРАВИЛЬНО❌' 
    


a=App()
print(a.generate('Двоичная', 'В десятичную'))
print(a.convert('Двоичная', 'В десятичную'))
print(a.check(345))


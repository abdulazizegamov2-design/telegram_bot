# a = int(input("a sonni yozing: "))
# b = int(input("b sonni kiritng: "))
# c = int(input("c sonni kiritng: "))

# count = 0

# if a>0:
#     count +=1
# else:
#     count +=0


# if b>0:
#     count +=1
# else:
#     count +=0



# if c>0:
#     count +=1
# else:
#     count +=0
# print(count)


# a = 17

# b = 20

# if a>b:
#     print(a,b)
# if a<b:
#     print(b,a)

# a = int(input("a ni kiriting: "))
# b = int(input("b ni kiriting: "))

# if a>b:
#     print(f"b = {a}\na = {b}")
# elif a==b:
#     b = b+a
#     print(f"b = {b}\na = {a}")

# else:
#     print(f"b = {a}\na = {a}")

# a =int(input("a sonini kiriting: "))
# b =int(input("b sonini kiriting: "))

# if a!=b:
#     a=a+b
#     b=a
#     print(a,b)
# else:
#     a,b=0,0
#     print(a,b)


# a =int(input("a sonini kiriting: "))
# b =int(input("b sonini kiriting: "))

# if a>b:
#     print(a)
# else:
#     print(b)

# a =int(input("a sonini kiriting: "))
# b =int(input("b sonini kiriting: "))
# c =int(input("c sonni kiriting: "))


# if c<b<a:
#     print(a)
# elif c<a<b:
#     print(b)
# elif a<b<c:
#     print(c)
# else:
#     print("hammasi teng")





# a=4000000
# b=int(input("nechi soat ishlagan"))
# d=a/100*25 +a
# s=a/100*10 +a
# soliq1=a-a/100*12
# if b>40 and b<60:
#     s=a/100*10 +a
#     print(s)
# elif b>60 and b<80:
#     d=a/100*25 +a
#     print(d)
# elif b>40 and b<60:
#     soliq=s-s/100*12
#     print(soliq)
# else:
#     print(soliq1)


# from math import*
# a=int(input())
# n=1
# s=0
# while n<=a:
#     s+=(-1)**(n-1)*sin(n**n)/(2**n)
#     n+=1
# print("%.2f" % s)

# from math import *
# a=int(input())
# n=1
# s=0
# while n<=a:
#     s+=(-1)**(n-1)*(1)/factorial((2*n-1))
#     n+=1
# print("%.4f" % s)
# from math import *
# def Yegindi(a:int, b:float) -> float:
#     """Bu funksiya a va b sonlarini yegindisini topadi"""
#     s = a + b
#     return s 

# def Raqamlar(a:int) -> int:
#     """Bu funksiya raqamlar yegindisini topadi"""
#     s = 0
#     while a != 0:
#         s += a % 10
#         a = a // 10
#     return s
  


# print(Yegindi(a=5, b=3))

# def Yegindi():
#     a, b = map(int, input().split())
#     s = a + b
#     print(s)
    
# Yegindi()
# Yegindi()
# Yegindi()
# Yegindi()











# def argsfunk(*son):
#     s=1                     
#     for i in son:
#         s*=i
#     return s
# print(argsfunk(5,6))



# def argsfunk(*son):
#     s=[]           
#     for i in son:
#        s.append(i**2)
        
#     return s
# print(argsfunk(5,6))



# def argsfunk(*son):
#     txt=son.split()
#     return max(txt,key=len)
# son="kiritilgan sonlar kvadratini hisoblash"
# print(argsfunk(son))

# def juftsonlar(lis):
#     def wrapper(li):
#         x=lis(li)
#         return[i for i in x if int(i)%2==0]
#     return wrapper
# @juftsonlar
# def sozlar(txt):
#     a=[]
#     for i in txt:
#         if i.isdigit():
#             a.append(i)
#     return a
# soz=input("soz kiriting")
# print(sozlar(soz))




# def misol(yuzga):
#     def wrapper (*args):
#         return yuzga(*args)+100
#     return wrapper
# @misol
# def add(a,b):
#     return(a+b)

# print(add(2,7))


# def misol(func):
#     def wrapper (*args):
#         return func(*args)*5
#     return wrapper
# @misol
# def add(a,b):
#     return(a+b)

# print(add(2,7))


# def misol(func):
#     def wrapper (*args):
#         return func(*args)**2
#     return wrapper
# @misol
# def add(a,b):
#     return(a+b)

# print(add(2,7))

# import wikipedia
# text = input("Qidiruv: ")
# wikipedia.set_lang('uz')
# qidiryabman = wikipedia.summary(f"{text}")

# print(qidiryabman)

# def juftsonlar(lis:list) -> int:
#     d=0
#     for i in lis:
#         if i%2==0:
#             d+=(i)
#     return d 
# print(juftsonlar([2,5,6,7,8]))




# def juftsonlar(lis:list) -> int:
#     d=[]
#     for i in lis:
#         if i>0:
#             d.append(i)
#     return d 
# print(juftsonlar([2,-2,-5]))
# def katta_kichik(sonlar)->int:
#     return min(sonlar), max(sonlar)
# print(katta_kichik([1,2,4,9,]))
# def toq(sonlar):
#     d=[]
#     for i in sonlar:
#         if i%2==1:
#             d.append(i)
#     return d
# print(toq([1,2,3,4 ]))

# def kvadrat(lis:list)-> int:
#     return [i**2 for i in lis]
# print(kvadrat([1,2,3,4]))

# a={"a":5,"b":12,"c":3}
# maxx=max(a,key=a.get)
# print(maxx)



# class ovqat











# #1-misol
# class PrimeNumber:
#     def is_prime(self, n):
#         if n < 2: return False
#         for i in range(2, int(n**0.5) + 1):
#             if n % i == 0: return False
#         return True

#     def check(self, n):
       
#         def find_neighbor(start, step):
#             curr = start + step
#             while curr > 1:
#                 if self.is_prime(curr): return curr
#                 curr += step
#             return None

#         smaller = find_neighbor(n, -1)
#         larger = find_neighbor(n, 1)

#         if self.is_prime(n):
#             return f"Natija: {n} - tub son. Yaqinlari: {smaller} va {larger}"
#         else:
#             return f"Natija: {n} - tub emas. Eng yaqin ikki tub son: {smaller} va {larger}"


# p = PrimeNumber()
# print("1-topshiriq natijasi:")
# print(p.check(13)) 
# print(p.check(10))









# #2-misol
# class CustomList:
#     def __init__(self, my_list):
#         self.my_list = my_list

#     def clean_and_sort(self):
#         result = list(set(self.my_list))
#         result.sort(reverse=True)
#         return result

# print("\n2-topshiriq natijasi:")
# cl = CustomList([1, 4, 2, 4, 1, 8, 3])
# print(f"yangi ro'yxat: {cl.clean_and_sort()}")










# #3-misol
# class Triangle:
#     def __init__(self, a, b, c):
#         self.a, self.b, self.c = a, b, c

#     def get_info(self):
#         a, b, c = self.a, self.b, self.c
#         if a + b > c and a + c > b and b + c > a:
#             if a == b == c:
#                 turi = "teng tomonli"
#             elif a == b or b == c or a == c:
#                 turi = "teng yonli"
#             else:
#                 turi = "turli tomonli"
#             return f"uchburchak yasash mumkin Turi: {turi}"
#         else:
#             return "uchburchak yasab bolmaydi"

# t = Triangle(5, 5, 8)
# print(t.get_info())









# #4-misol
# class NumberOperations:
#     def __init__(self, number):
      
#         self.number = number

#     def calculate(self):
#         s = str(self.number)
        
#         if len(s) > 2:
#             middle = s[1:-1].replace('0', '')
#             s = s[0] + middle + s[-1]
        
#         reversed_num = s[::-1]
        
#         digit_sum = sum(int(d) for d in str(self.number))
        
#         if digit_sum % 2 == 0:
#             math_result = digit_sum / 2
#         else:
#             math_result = digit_sum + 5
            
#         return f"Teskari (nolarsiz): {reversed_num}, Hisob natijasi: {math_result}"

# d = NumberOperations(106)
# print("Natija :", d.calculate())







# #5-misol
# class TupleAnalyzer:
#     def __init__(self, data_tuple):
#         self.data = data_tuple

#     def analyze(self):
#         numbers = [x for x in self.data if isinstance(x, (int, float))]
        
#         if not numbers:
#             return "sonlar yo'q"
        
#         total_sum = sum(numbers)
#         if total_sum % 2 == 0:
#             result = "Even"
#         else:
#             result = "Odd"
            
#         return f"topilgan sonlar: {numbers}, Yig'indi: {total_sum}, Natija: {result}"


# case1 = TupleAnalyzer(("olma", 10, "anor", 5, 3))
# print(" natijasi:", case1.analyze())

# c=[c*3 for c in "list " if c!=i]



# class variable:
#     count=0
#     def __init__(self,model,year):
#         self.__model=model
#         self.__year=year
#         variable.count+=1


#     def __str__(self):
#         return f"nomi:{self.__model}\nyil:{self.__year}"
#     @classmethod
#     def  get_total_cars(cls):
#         return variable.count

# mashina=variable("bmw",2016)
# mashina=variable("bmw",2014)
# mashina=variable("bmw",2015)
# mashina=variable("bmw",2017)
# print(variable.get_total_cars())
# print(mashina)



# class Bank:
#     def __init__(self, ism, balans):
#         self.ism = ism
#         self.__balans = balans
        
#     def depazit(self, summa):
#         self.__balans += summa
#         return self.__balans
    
#     def withdraw(self, withdrawal):
#         if self.__balans >= withdrawal:
#             self.__balans = self.__balans - withdrawal
#             return self.__balans
#         else:
#             print("sizning sho'tingizda mablag' yetarli emas")
    
#     def __str__(self):
#         return f"Ism: {self.ism}\nMablag': {self.__balans}"


# person1 = Bank("murodlox", 1500000)
# person1.depazit(500000)
# person1.withdraw(18000000)
# print(person1)




# class talab:
#     def __init__(self,title,price):
#         self.__title=title
#         self.__price=price

#     def __str__(self):
#         return f"nomi;{self.__title}\nnarxi:{self.__price}"































































# class Avto:
#     def __init__(self,name,narh):
#         self.narh = narh
#         self.name = name


#     @staticmethod
#     def son(x,y):
#         return x*y



# odj = Avto('Asilbek',100000)       
# print(odj.son(10,3))        


# a = int(input('sonni kiriting'))
# b = int(input('sonni kiriting'))
# def son(a,b):
        
#         return b**2
# print(son(a,b))

# a = str(input('ismingizni kiriting'))
# def oila():
#     return a
# append= [a]
# print(oila,a)

# def gol():
#     l = []
#     for i in range(1,100 ):
#         l.append(i**2)
#     return(l)
# print(gol())

# from typing import Any


# class Talaba:
#     def __init__(self,ism, familya,t_yil):
#         self.ism = ism
#         self.familya = familya
#         self.t_yil = t_yil


#     def get_info(self):
#         return f'{self.ism} {self.familya} {self.t_yil}'



#     def get_age(self,hozirgi_yil):
#         return hozirgi_yil - self.t_yil


# # talaba1 = Talaba('asilbek','Eshmuminov',2012)
# # print(talaba1.get_age(hozirgi_yil=2024))

# class Shaxs(Talaba):
#     def __init__(self, ism, familya, t_yil):
#         super().__init__(ism, familya, t_yil)
        



#    def get_info(self):
#         return super().get_info()    
          
# talaba = Shaxs('Asilbek','Eshmuminov',2012)
# print(talaba.get_info())



# class Talaba:
#     def __init__(self,ism,familya,t_yil):
#         self.ism = ism
#         self.familya = familya
#         self.t_yil = t_yil

#     def get_info(self):
#         return f'{self.ism} {self.familya} {self.t_yil}'
# #     def get_age(self,hozirgi_yil):
# #         return hozirgi_yil - int(self.t_yil)


# # talaba = Talaba('Asilbek','Eshmuminov','2012') 
# # print(talaba.get_info(), talaba.get_age(hozirgi_yil=2024))  

# class Shaxs(Talaba):
#     def __init__(self, ism, familya, t_yil):
#         super().__init__(ism, familya, t_yil)



#     def get_info(self):
#         return super().get_info()
    
# shaxs = Shaxs('Asilbek','Eshmuminov',2012) 
# print(shaxs.get_info())   








   
# d = {}     
# class Kurs:
#     @staticmethod
#     def get_addd():
#         while True:
#                 name = input('Kusr nomini kiritting:')
#                 price = input(10021)
#                 d[name] = price
#                 takror = input('Yana kurs qo\'shasizmi(ha/yoq)?:')
#                 if takror == 'yoq':
#                         break
#                 else:
#                         pass
#         return d
# obj = Kurs()
# print(obj.get_addd())
    
# l = []
# class Name():
#     @staticmethod
#     def add_name():
#         ishora = True
#         while ishora:
#             Name = input('ism kiriting:')
#             l.append(Name)
#             reply = input('Yana ism qoshasizmi(ha/yoq)')
#             if reply =='yoq':
#                 ishora = False
#             else:
#                 pass
#         return l
    
# name  = Name()
# print(name.add_name())    
l = []

class Range():
    @staticmethod
    def range(start,stop):
        while start < stop:
            l.append(start)
            start +=1
        return l 
    
a = Range()
print(a.range(1,100))
        












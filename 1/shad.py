# # class Shaxs:
# #     def __init__(self,ism,familya,t_yil,passport):
# #         self.ism = ism
# #         self.familya = familya
# #         self.t_yil = t_yil
# #         self.passport = passport


# #     def get_info(self):
# #         return f'{self.ism} {self.familya} {self.t_yil} {self.passport}'
    

# #     def get_age(self,hozirgi_yil):
# #         return hozirgi_yil - self.t_yil
    


# # talaba1 = Shaxs('Salohiddin','soliyev',2010,'Ad46698,')
# # # print(talaba1.get_age(hozirgi_yil = 2024))
# # # print(talaba1.get_info())




# # class Talaba(Shaxs):
# #     def __init__(self, ism, familya, t_yil, passport, id_raqam):
# #         super().__init__(ism, familya, t_yil, passport)
# #         self.id_raqam = id_raqam


# #     def get_id(self):
# #         return self.id_raqam
        
# # talaba = Talaba('Asilbek','Eshmuminov',2012,'AS457897', 234566871)
# # print(f'{talaba.get_info()}:id raqam -> {talaba.get_id()}')



# # class Afto:
# #     def __init__(self,madeli,rangi,yili,narxi,klametr=4):
# #         self.madeli = madeli
# #         self.rangi = rangi
# #         self.yili = yili
# #         self.narxi = narxi
# #         self.klametr =klametr



# #     def get_info(self):
# #         return f'{self.madeli} {self.rangi} {self.yili} {self.narxi} {self.klametr}'
    


# # avto = Afto('Mrs','qora',2020,10000)    
# # print(avto.get_info())

        
# # a = int(input('yoshingizni kiriting'))
# # class sonlar:
# #     def __init__(self,a):
# #         self.a = a
# #     def qa(self,hozirgi_yil):
# #         return hozirgi_yil - self.a

# # s = sonlar(a)
# # print(s.qa(hozirgi_yil=2024))
        
    
        


# class Mano:
    

#  def get_apper(self):
#         Talabalar = ['olim','hasan','husan'] 
#         baholar = {}
#         while Talabalar:
#             talaba = Talabalar.pop()
#             baho = int (input(f'{talaba} ni bahosini kiriting!'))
#             print(f'Talaba {talaba} baholandi')
#             baholar[talaba] = int(baho)
#         for k, v in baholar.items():
#             print(f'{k}ning bahosi {v}')

# mano = Mano()
# mano.get_apper()   





# from uuid import uuid4
# class Avto:
#     def __init__(self,madel,rang,yil,narh,km=1):
#         self.madel = madel
#         self.rang = rang
#         self.yil = yil
#         self.narh = narh
#         self.__km = km
#         self.__id = uuid4()


#     def get_info(self):
#         return f'{self.madel} {self.narh} {self.yil} {self.rang} {self.__km} {self.__id}'   



#     def __repr__(self):
#         return f'{self.madel} {self.rang}'
    
            
#     def __eq__(self, value: object):
#         return self.narh == value.narh



#     def __gt__(self,value: object):
#         return self.narh > value.narh




# avto1= Avto('gd','grh','4555',100)
# avto2= Avto('gd','grh','4555',100)
# print(avto1.get_info)   



























    




# talabalar = ['asilbek','salohiddin','abduvohid']
# def big_name():
#     """Ismi bosh harifini katta qilib beruvchi funcsiya"""
#     big_talaba_name = []
#     for talaba in talabalar:
#         big_talaba_name.append(talaba.title())
#     return big_talaba_name
# print(big_name())



# talabalar = ['asilbek','salohiddin','abduvohid','ali','vali']
# def bahola  (ismlar):
#     baholar = {}
#     for ism in ismlar:
#         baho = input(f'{ism.title()}ning baholarini kiriting!')
#         baholar[ism] = baho
#     return baholar
# x = bahola(talabalar)
# print(x)


# def avto_info(kompanya,madel,rangi,karobka,yili,narhi=None):
#     avto = {
#         'kampanya':kompanya,
#         'madel' : madel,
#         'rangi' : rangi,
#         'karobka': karobka,
#         'yili': yili,
#         'narh': narhi,

#     }


#     return avto


# avto1 = avto_info('GM','MALIBU','QORA','AVTOMAT',2024,23000)
# avto2 = avto_info('GM','Gentra','Qora','mahanika',2024)

# avto = [avto1,avto2]
# print(avto)
# print('onlene bozorda bor cars')
# for a in avto:
#     if a ['narh'] is not None:
#         narh = a['narh']
#     else:
#         narh = 'Nomalum'
#     print(f"{a['madel']} {a['rangi']} {narh}")
# a = int(input())


# funksalar

# def gth():
#     if a<100:
#         print('yuzdan kichik')
#     else:
#         print('yuzdan katta')
# gth()
# son = int(input())
# def kv():
#     print(son**2)

# kv()
# ismlar = ['ascsd', 'sdcsd', 'sdcsd']
# def big(ism):
#     x = []
#     for a in ism:
#         x.append(a.title())
#     return x
# s = big(ismlar)
# print(s)


# d = int(input('son kriting'))
# a = int(input('sonni kiriting'))
# if a>d:
#     print('a kotta')
# else:
#     print('d kichkina')



# h =int(input('yelingiz nechi'))
# d =(2024-h)
# print(d)


# # a = int(input('yoshingizni kiriting'))
# # b = (2024-a)
# # print(b)

# a =int(input('radiosi'))
# p =3.14
# x = p*a**2
# print(x)





# import random
# print(random.randint(0,100))





# import random

# def sontop(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f'1 dan {x} gacha son uyldimtopa olsizmi',end="")
#     taxminlar = 0
#     while True:
#         taxminlar +=1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("Xato. men o'ylagnson bundan kattaroq.Yana harakat qiling",end="")
#         elif taxmin>tasodifiy_son:
#             print("Xato men o'ylagan son bundan kichikroq.Yana harakat qiling",end="")
#         else:
#             break
#     print(f'Tabriklayman.{taxminlar} ta taxmin bilan tobdingiz!')
#     return taxminlar

# sontop()







# import random


# def sontap(x = 10):
#     tasodifiy_son = random.randint(1, x)
#     print(f'1 dan {x}gacha son oyladim topa olasizmi',end="")
#     taxminlar = 0
#     while True:
#         taxminlar +=1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("Xato. men o'ylagnson bundan kattaroq.Yana harakat qiling",end="")
#         elif taxmin>tasodifiy_son:
#             print("Xato.men o'ylagan son bundan kichikroq.yana harakat qiling",end="")
#         else:
#             break
#     print(f"Tabriklayman. {taxminlar} ta taxmin bilan tapdingiz!")
# #     return taxminlar
    
    
# # sontap()



# import random

# def sontop(x=10):
#     tasodifiy_son = random.randint(1,x)
#     print(f'1 dan {x} gacha son uyldimtopa olsizmi')
#     taxminlar = 0
#     while True:
#         taxminlar +=1
#         taxmin = int(input(">>>"))
#         if taxmin<tasodifiy_son:
#             print("Xato. men o'ylagnson bundan kattaroq.Yana harakat qiling",)
#         elif taxmin>tasodifiy_son:
#             print("Xato men o'ylagan son bundan kichikroq.Yana harakat qiling")
#         else:
#             break
#     print(f'Tabriklayman.{taxminlar} ta taxmin bilan tobdingiz!')
#     return taxminlar

# sontop()









# a = int(input('sonni kiriting'))
# b = int(input('sonni kiriting'))
# if a>b:
#     print('a kotta')
# else:
#     print('b kichik')


# for i in range(2,100, 2):
#     print(i)


# a = str(input('harif kiriting'))
# print(f'{a.upper()}')


# import random

# def sontop_pc(x = 10):
#     input(f'1 dan {x} gacha son uyladim  istalgan tugmani bosing.men topaman.')
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         if quyi != yuqori:
#             taxmin = random.randint(quyi,yuqori)
#         else:
#             taxmin = quyi
#         jovob = input(f"siz {taxmin} sonini o'yladingiz:to'g'ri(t)"
#                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)".lower())
#         if jovob =="-":
#             yuqori = taxmin - 1
#         elif jovob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f'men {taxminlar} tataxmin bilan topdim ')
#     return taxminlar
    
# sontop_pc()



# import random

# def sontop_pc(x = 10):
#     input(f'1 dan {x} gacha son uyladim  istalgan tugmani bosing.men topaman.')
#     quyi = 1
#     yuqori = x
#     taxminlar = 0
#     while True:
#         if quyi != yuqori:
#             taxmin = random.randint(quyi,yuqori)
#         else:
#             taxmin = quyi
#         jovob = input(f"siz {taxmin} sonini o'yladingiz:to'g'ri(t)"
#                      f"Men o'ylagan son bundan kattaroq (+), yoki kichikroq(-)".lower())
#         if jovob =="-":
#             yuqori = taxmin - 1
#         elif jovob == "+":
#             quyi = taxmin + 1
#         else:
#             break
#     print(f'men {taxminlar} tataxmin bilan topdim ')
#     return taxminlar
    
# sontop_pc()


# import datetime
# import time
# x = datetime.datetime.now()
# print(x.strftime("%d/%m/%Y,  %H:%M:%S"))
# print(x.year)
# print(x.monthbgt5)



# import requests
# url = 'https://dummyjson.com/users'
# responze  = requests.get(url)
# data = responze.json()
# users = data['users']
# for user in users:
#     print(user['username'])

# thislist= []

# for  i in range(1,100):

#     thislist.append(i**2)

# print(thislist)





# def kata_():
#     a=int(input('son kiriting'))
#     b=int(input('son kiriting'))
# if a>b:
#     print('a katta')
# else:


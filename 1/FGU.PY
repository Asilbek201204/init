# def home(ism):
#     print(f'{ism} Assalomu Aleykum')
# home(ism = 'Asilbek')

# def home(a,b):
#     print(a + b)
# home(a = 2, b = 5)    

# def home(x):
#     return x**2
# print(home(x=5))


# def home():
#     for i in range(1,100):
#         print(i)
# home()        

# def home():
#     for i in range(1,100):
#         return i
# print(home())

# a = int(input())
# b = int(input())
# def home(x,y):
#     return(x+y)**2
# print(home(10,20,))

# def home():
#     l=[]
#     for i in range(1,100):
#         l.append(i**2)
#     return l
# print(home())    



# def toliq_ism_yasa(ism,familya,otasini_ism):
#     if otasini_ism:
#         return f'{ism } {familya} otasining ismi{otasini_ism}'
#     else:
#         return f'{ism} {familya}'
# print(toliq_ism_yasa('olim','olimov',''))
# print(toliq_ism_yasa('olim','olimov','olim'))




# def did(a,b,d):
#     if a>b and a>d:
#         return f'kattasi a {a}'
#     elif b>a and b>d:
#         return f'kattasi b {b}'
#     else:
#         return f'kattasi d {d}'
# print(did(12,3,4))


# def juft():
#     for n in range(1,100):
#         if n % 2==0:
#             print(n)
# juft()
# l = []
# def juft():
#     for i in range(1,100):
#         if i % 2 ==1:
#             l.append(i**2)
#     return l
# print(juft())        


# file_name = 'datas.txt'
# ism = 'Asilbek'
# yosh = 12


# with open(file_name, 'w') as file:
#     file.write(f'{str(ism)}\n')
#     file.write(str(yosh)+'\n')



# with open(file_name,'a') as file:
#        file.write('salom' + '\n')
#        file.write(str(20) + '\n')



# import pickle
# talaba = {'ism':'olim','familya':'olimov','t_yil': 2012}
# talaba2 = {'ism':'olim','familya':'olimov','t_yil': 2012}   
# with open('info','wb') as file:
#      pickle.dump (talaba, file=file) 
#      pickle.dump(talaba, file=file)



# with open('info','rb') as file:
#      t = pickle.load(file=file )
# print(t)

file_name = 'data.txt'
ism ='asilbek'
yosh = 12
familya = 'Eshmuminov'



with open(file_name,'w') as file:
     file.write (f'{str(ism)}\n')
     file.write(str(yosh) + '\n')
     file.write(str(familya) +'\n')

with open(file_name) as file:
    f =  file.read()
print(f)




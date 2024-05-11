# # import  json

# # x = '{"name":"John","age":30,"city":"New york"}'


# # y = json.loads(x)

# # for i in y:
# #     print(i)



# import json  


# x = {
#     "name":"Json",
#     "age":30,

#     "city":"New York"

# }

# y = json .dumps(x)
# print(y)




# import json

# x = {
#   "name": "John",
#   "age": 30,
#   "married": True,
#   "divorced": False,
#   "children": ("Ann","Billy"),
#   "pets": None,
#   "cars": [
#     {"model": "BMW 230", "mpg": 27.5},
#     {"model": "Ford Edge", "mpg": 24.1}
#   ]
# }

# # print(json.dumps(X))

# usrs = json.dumps(x)
# user_dict = json. loads(usrs)
# cars = user_dict['cars']
# for car in  cars:
#     print(car['model'`])

# import requests
# url_name = 'https://dummyjson.com/users'
# response = requests.get(url=url_name)
# datas = response.json()
# users = datas['users']
# first_user = users[0]

# print(first_user['image'])


# import requests
# url_name = 'https://nbu.uz/uz/exchange-rates/json/'
# respons = requests.get(url=url_name)
# datas = respons.json()
# data = datas[-1]
# print(data['title'],data['cb_price'])


# import sqlite3

# class User():
#     @staticmethod
#     def curson(command,parameters=(), fetchone=False,fetchall=False,comment=False):
#         con = sqlite3.connect('db.sqlite3')
#         cursor = con.cursor ()
#         if fetchone:
#             return cursor.fetchone()
#         if fetchall:
#             return


# class User:
#     def __init__(self,ism,familya,t_yil):
#         self.ism = ism
#         self.familya = familya
#         self.t_yil = t_yil


#     def get_age(self,hozirgi_yil):
#         return hozirgi_yil - self.t_yil
           


#     def get_info(self):
#         return f'{self.ism} {self.familya} {self.t_yil}'
       
# user = User('Asilbek','Eshmuminov',2012)
# print(user.get_info(),user.get_age(2024)) 

d = {}
class User:
    @staticmethod
    def name ():
        while True:
            ism = input('ismingizni kiriting:')
            bahosi = input(f'{ism}ning bahosini kiriting')
            d[ism] = bahosi
            takror  = input('yana ism qoshasizmi(ha\yoq)')
            if takror =='yoq':
                break
            else:
                pass
        return d
obj = User()
print(obj.name())
            


    
    
    


        


        




















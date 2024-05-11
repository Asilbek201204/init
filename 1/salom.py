class Talaba:
    def __init__(self,ism, familya,t_yil):
        self.ism = ism
        self.familya = familya
        self.t_yil = t_yil


    def get_info(self):
        return f'{self.ism} {self.familya} {self.t_yil}'
    


    def get_age(self,hozirgi_yil):
        return hozirgi_yil - self.t_yil
    


talaba1 = Talaba ('Asilbek','Eshmuminov',2012)   
talaba2 = Talaba ('Salohiddin','soliyev',2010)
# print(talaba2.get_age(hozirgi_yil=2024))
# print(talaba1.get_info())



class Salom(Talaba):
    def __init__(self, ism, familya, t_yil):
        super().__init__(ism, familya, t_yil)

salom = Salom('Asilbek','Eshmuminov',2012)
print(salom.get_age(hozirgi_yil=2024))












        
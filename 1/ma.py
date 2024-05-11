class Talaba:
    def __init__(self,ism,familiya,t_yil):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil

    def tanishtir(self):
        return f'Men {self.ism} {self.familiya} {self.t_yil}'


    def get_age(self,new_year):
        return new_year - self.t_yil


talaba1 = Talaba('olim','olimov',2000)
talaba2 = Talaba('Hasan','Husanov',2004)
print(talaba2.tanishtir())
print(talaba1.get_age(new_year=2024))    




class Shaxs:
    def __init__(self,ism,familiya,t_yil,passport):
        self.ism = ism
        self.familiya = familiya
        self.t_yil = t_yil
        self.passport = passport


    def get_info(self):
        return f'{self.ism} {self.familiya} {self.t_yil} {self.passport}'
    

    def get_age(self,hozirgi_yil):
        return hozirgi_yil - self.t_yil
    

inson = Shaxs('Asilbek','Eshmuminov',2012,'AD123467')
inson1 = Shaxs('Asilbek','Olimov',2000,'ADdd23467')

print(inson.get_info())
print(inson1.get_age(2024))


class Talaba(Shaxs):
    def __init__(self, ism, familiya, t_yil, passport,id_raqam):
        super().__init__(ism, familiya, t_yil, passport)
        self.id_raqam = id_raqam


    def get_id(self):
        return self.id_raqam




talaba1= Talaba('Abduvohid','Abdujalilov',2004,'ad2769','24690647')    
print(f'{talaba1.get_info()}:id raqam -> {talaba1.get_id()}')
















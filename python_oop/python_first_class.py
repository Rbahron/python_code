class Student :
    def __init__(self,name,surname,lastname,age,sum,degree) -> None:
        self.name = name
        self.surname = surname
        self.lastname = lastname
        self.age = age
        self.degree = 1
        self.__sum = sum
        self.__degree = degree
    
    def introduction(self):
        print(self.name,self.surname,self.lastname,self.age)

    def get_name(self):
        return self.name
    
    def get_surname(self):
        return self.surname
    
    def get_lastname(self):
        return self.lastname
    
    def get_age(self,yil):
        return yil - self.age
    
    def set_bosqich(self,bosqich):
        self.degree = bosqich

    def update_degree(self):
        self.degree += 1
    
    @classmethod
    def get_degree(cls):
        cls.__degree +=1
    
    def get_sum (cls):
        cls.__sum +=1



talaba = Student('anvar','sobirov','og`abekovich',1992)

talaba.introduction()
print(talaba.degree)
talaba.degree = 2
print(talaba.degree)
talaba.set_bosqich(3)
print(talaba.degree)
talaba.update_degree()
print(talaba.degree)

class User :
    def __init__(self,name,surname,born_year,password) -> None:
        self.name = name
        self.surname = surname
        self.born_year = born_year
        self.password = password

    def get_info(self):
        print(f"Foydalanuvchi ismi:{self.name} familiyasi:{self.surname} tug`ilgan yili:{self.born_year} password:{self.password}")

    def get_name(self):
        return self.name
    
    def get_age(self,year):
        return year - self.born_year
    
user_1 = User('Omar','Xattob',932,'bangladesh')
user_1.get_info()
print(user_1.get_age(2023))
print(user_1.name)
print(user_1.surname)

student2 = Student('anvar','raximov','ibn',1887)


class Fan :
    def __init__(self,scienes_name) -> None:
        self.sceines_name = scienes_name
        self.count_students = 0
        self.students = []
    
    def add_students(self,student):
        self.students.append(student)
        self.count_students += 1
    
    def get_name(self):
        return self.sceines_name

    def get_student(self):
        return [student.introduction() for student in self.students]
    
    def get_student_numbers(self):
        return self.count_students

math_1 = Fan('math')


math_1.add_students(talaba)
math_1.add_students(student2)


print(math_1.sceines_name)
print(math_1.count_students)
stud = math_1.get_student()
print(stud)

def see_methods(class_object):
    return[method for  method in dir(class_object) if method.startswith('__') is False]

print(see_methods(Fan))
print(talaba.__dict__.keys)

class Avto :
    def __init__(self,model,color,type,price) -> None:
        self.model = model
        self.color = color
        self.type = type
        self.price = price
        self.km = 0

    def get_info(self):
        return f"Avto model:{self.model} color:{self.color} price:{self.price}"

    def update_km(self,km):
        self.km = km

class Avtosalon :
    def __init__(self,name,adress) -> None:
        self.name = name
        self.adress = adress
        self.count_cars = 0
        self.cars = []

    def add_cars(self,car):
        self.cars.append(car)
        self.count_cars += 1

    def get_info_about_cars(self):
        return [car1.get_info() for car1 in self.cars]

avto1 = Avto('malibu','black','ld',30000)
info = avto1.get_info()
print(info)
avto1.update_km(10000)
print(avto1.km)

avtosalon = Avtosalon('Buxara','Buxara')
avtosalon.add_cars(avto1)

info2 = avtosalon.get_info_about_cars()
print(info2)
print(see_methods(avto1))
print(avtosalon.__dict__)
print(avtosalon.__dict__.keys())

class Shaxs:
    def __init__(self,name,lastname,pasport,bornyear) -> None:
        self.name = name
        self.lastname = lastname
        self.pasport = pasport
        self.bornyear = bornyear

    def get_information(self):
        info = f"{self.name}  {self.lastname}"
        info += f"Pasport: {self.pasport},{self.bornyear} - yilda tug`ilgan"
        return info
    
    def get_age(self,yil):

        return yil - self.bornyear
    

person = Shaxs("Hassan",'Alimov',"FA4403444",1997)
print(f"{person.get_information()}, {person.get_age(2023)} yoshda")

class Talaba(Shaxs):
    def __init__(self, name, lastname, pasport, bornyear) -> None:
        super().__init__(name, lastname, pasport, bornyear)
        self.fanlar = []
    def fanga_yozil(self,fan):
        self.fanlar.appear(fan)
    
    def remove_fan(self,fan):
        if fan in self.fanlar:
            self.fanlar.remove(fan)
        else:
            print('siz bu fanga yozilmagansiz')

class Fan:
    pass

math_2 = Fan
cemistry = Fan
biology  = Fan

talaba_2 = Talaba
talaba_2.fanga_yozil(math_2)
talaba_2.fanga_yozil(cemistry)
talaba_2.fanga_yozil(biology)

class Proffesor(Shaxs):
    def __init__(self, name, lastname, pasport, bornyear,science) -> None:
        super().__init__(name, lastname, pasport, bornyear)
        self.ixtisosligi = science
        self.sciences = []
    
    def get_fan(self,specials):
        self.sciences.append(specials)
        

class Sotuvchi(Shaxs):
    def __init__(self, name, lastname, pasport, bornyear,experience) -> None:
        super().__init__(name, lastname, pasport, bornyear)
        self.experience = experience
        self.experience = []
    
    def ish_joylari(self,experience):
        self.experience.append(experience)

class Foydalanuvchi(Shaxs):
    def __init__(self, name, lastname, pasport, bornyear) -> None:
        super().__init__(name, lastname, pasport, bornyear)
        self.mahsulotlar = []

    def ilovalari(self,products):
        self.mahsulotlar.append(products)
        

class Mijoz(Shaxs):
    def __init__(self, name, lastname, pasport, bornyear) -> None:
        super().__init__(name, lastname, pasport, bornyear)
        self.ruxsatlar = []
    
    def malumotlar(self,allows):
        self.ruxsatlar.append(allows)
        
class Admin(Foydalanuvchi):
    def __init__(self, name, lastname, pasport, bornyear) -> None:
        super().__init__(name, lastname, pasport, bornyear)
    def ban_user():
        print('foydalanuvchi bloklandi')
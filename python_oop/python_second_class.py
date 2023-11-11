from uuid import uuid4
class Avto :
    __num_avto = 0
    def __init__(self,model,color,type,price,km) -> None:
        self.model = model
        self.color = color
        self.type = type
        self.price = price
        self.__km = km
        self.__id = uuid4()
        Avto.__num_avto += 1


    def get_info(self):
        return f"Avto model:{self.model} color:{self.color} price:{self.price}"

    def update_km(self):
        return self.__km
    def get_id(self):
        return self.__id
    def avto_add_km(self,km):
        if km >= 0:
            self.__km += km
        else:
            print('describing km of car is impossible')

    @classmethod
    def get_num_avto(cls):
        return cls.__num_avto

    
avto1 = Avto('malibu','black','turbo',20000,10000)
print(f"ID : {avto1.get_id()}")
print(f"km {avto1.update_km()}")
avto1.avto_add_km(1400)
print(avto1.update_km())
avto2 = Avto('matiz','black','best',15000,100000)
avto3 = Avto('lasetti','white','gentra',20000,12000)
print(Avto.get_num_avto())
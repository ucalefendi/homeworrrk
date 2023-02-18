# from typing import Literal
# ServiceTypes = Literal['call','sms','mb']


# class Credit:
#     servis_prices = {
#         'call':  10,
#         'sms' : 3,
#         'mb' : 5
#     }

#     def __init__(self,balance):
#         self.balance = balance

#     def decrease(self,service: ServiceTypes):
#         price = self.servis_prices.get(service)
#         if price > self.balance:
#             raise Exception('kifayet qeder balans yoxdur')
#         self.balance -= price


#     def increase(self,amount):
#         self.balance += amount


# class Phone:
#     def __init__(self,balance): 
#         self.credit = Credit(balance)
#         self.recieved_messages = []  
#         self.sent_messages = [] 


#     def send_message(self,message,target):

#         self.sent_messages.append(message)
#         target.recieved_messages.append(message) 
#         self.credit.decrease('sms')


# bphone = Phone(8)    
# cphone = Phone(10) 
# bphone.send_message('salam mellim',cphone)   
# # print(cphone.recieved_messages)
# bphone.sent_messages
# print(bphone.sent_messages)


          

# class Flash:
#     max_limit = 20 

#     def __init__(self):
#         self.__volt = 0

#     def get_volt_value(self):
#         return self.__volt


# class Phone:


#     def __init__(self):
#         self.flash = Flash()  


# phone = Phone()

# phone.flash.__volt = 100
# print(phone.flash.get_volt_value())
#********************************************************************************************************

# CameraSystem classinin each_camera_price adinda hidden bir propertysi olsun. Deyeri 50 verin


# Homework 27



#1. Nöqtələrin yerini dolduraraq proqramın işləməsini təmin edin.
    

    # CameraSystem classinin each_camera_price adinda hidden bir propertysi olsun. Deyeri 50 verin
# class CameraSystem:
#         __each_camera_price = 50
    
#         def get_camera_price(self):
#             return self.__each_camera_price * self.count
    
#         def set_camarea_count(self, count):
#            self.count = count
    
#     # MemorySystem classinin each_gb_price adinda hidden bir propertysi olsun. Deyeri 10 verin
# class MemorySystem:
#     __each_gb_price = 10
#     def set_memory_amount(self, amount):
#             self.memory_amount = amount
    
#     def get_memory_price(self):
#             return self.__each_gb_price * self.memory_amount
    
# class SmartDevice(CameraSystem,MemorySystem):
#     def __init__(self, camera_count, memory_amount):
#           self.set_memory_amount(memory_amount)
#           self.set_camarea_count(camera_count)
        
            
    
# class Phone(SmartDevice):
    
#         def get_total_price(self):
#             return self.get_camera_price() + self.get_memory_price() + 500
    
# class PremiumPhone(Phone):
#         def __init__(self, charger_price, camera_count, memory_amount):
#             self.charger_price = charger_price
#             super().__init__(camera_count,memory_amount)
    
#         def get_total_price(self):
#             return super().get_total_price() + self.charger_price
    
# class Laptop(SmartDevice):
#         def get_total_price(self):
#             return self.get_camera_price() + self.get_memory_price() + 2000
              

# class Tablet(SmartDevice):
#     def get_total_price(self):
#             return self.get_camera_price() + self.get_memory_price() + 1500
    
# samsung = Phone(4, 256)
# iphone = PremiumPhone(70, 3, 128)
# dell = Laptop(1, 512)
# huawei = Tablet(2, 256)


    
# def calculate_product_prices(*args):
#     prices = 0
#     for d in args:
#          prices += d.get_total_price()
#     return prices     
    
# print(calculate_product_prices(samsung, iphone, dell, huawei))


class Termostat:
    def __init__(self,celcius):
        self.celcius = celcius
    @property
    def kelvin(self):
        return self.celcius_to_kelvin(self.celcius)
    @property
    def faranheit(self):
        return self.celcius_to_faranheit(self.celcius)  
    @kelvin.setter
    def kelvin(self,value):
        self.celcius = self.kelvin_to_celcius(value)  
    @faranheit.setter
    def faranheit(self,value):
        self.celcius = self.faranheit_to_celcius(value)
    @staticmethod
    def celcius_to_kelvin(celcius):
        return celcius + 273
    @staticmethod
    def kelvin_to_celcius(kelvin):
        return kelvin - 273 
    @staticmethod
    def celcius_to_faranheit(celcius):
        return celcius * 1.8 + 32
    @staticmethod
    def faranheit_to_celcius(faranheit):
        return (faranheit -32) / 1.8
    @classmethod
    def get_termostat_by_kelvin(cls,kelvin):
        celcius = cls.kelvin_to_celcius(kelvin)
        return cls(celcius)


termostat = Termostat(25)   
# print(termostat.celcius_to_kelvin(10)) 
# print(Termostat.celcius_to_kelvin(10)) 
# print(Termostat.get_termostat_with_room_temperature())  
# print(Termostat.kelvin_to_celcius(275))     
# termostat = Termostat.get_termostat_by_kelvin(276)
# print(termostat.kelvin,termostat.faranheit,termostat.celcius)
termostat.faranheit = 70 
termostat.kelvin = 70
print(termostat.celcius,termostat.kelvin)


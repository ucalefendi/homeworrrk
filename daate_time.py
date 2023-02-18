#1)   koni hecmini hesablayan funksiya hazirlayin
# from math import pi as p
# def koni(r,h):
#     V = (1/3) * p * (r**2) *h
#     return V

# print(koni(12,4))   
# 
# 2)permutasiya ve kombinasiya hesablayan funksiya hazirlayin
# 

from math import factorial as f
#kombinasiya
# def  komb(n,r):
#     num_n = f(n)
#     num_r = f(r)
#     diff = f(n-r)
#     result = num_n/num_r * diff
#     return result
# print(komb(15,3))    


#permutasiya

# def per(n,r):
#     num_n = f(n)
#     num_r = f(r)
#     diff = f(n-r)
#     result = num_n/diff
#     return result
# print(per(10,5))  
# 

#3)
#  Giveaway programi duzeldin. Adamlar bitənə qədər hər enter basanda bir ad göstərsin.
# Input ⇒Adlari girin: Hesen, Arif, Elnur, Kamal

# Output⇒Kamal

# Output ⇒Arif

# Output ⇒Hesen  
# from random import shuffle
# names = input('adlari daxil edin:  ').split(', ')
# shuffle(names)
# for n in names:
#     input(n)




#4
# 4. Ədəd təxmin etmə oyunu hazırlayın. Müəyən bir araılq verin və program həmin aralıqda bir ədəd təyin etsin. 
# Daha sonra siz həmin ədədi tapana qədər oyun davam etsin. 
# Siz gizli ədədin aşağısında bir təxmin etdikdə program daha yuxarı, yuxarısında təxmin etdikdə isə daha aşağı desin.
#  Ən sonda ədədi neçə səfərə tapdığınızı qeyd etsin.
#  Əgər 10 üzərində təxmin etdikdən sonra tapıbsızsa məğlub sayılırsız, əks təqdirdə qalib.
# from random import randint

# start: int = int(input('ilk ededi girin: '))
# end: int = int(input('son ededi girin:  '))
# number: int = randint(start,end)
# attempt: int = 0
# while True:
#     attempt += 1
#     prediction: int = int(input('ededi girin:   '))
#     if prediction > number:
#         print('asaqi ededi qeyd edin')
#     elif prediction < number:
#         print('yuxari ededi qeyd edin')  
#     else:
#         print('dogrudur') 
#         if attempt > 10:
#             print('uduzdunuz') 
#         else:
#             print('qalib geldiniz')      
#         break  












# 5. Yer kürəsi ilə Pluton arasındakı məsfə 588 milyon kilometrdir. Saatda 90 km/saat sürətlə, 
# fasiləsiz hərəkət edən Niva maşını hansı tarixdə Yupiter planetinə nə zaman çatar?


# from datetime import datetime,timedelta

# def timeline(s,v):
#     time = s/v
#     return time
# print(timeline(588000000000,90)) 

# time(saat) = 6533333333.333333 = 272222223 gune beraberdir

# today = datetime.today()
# future = today + timedelta(days=272222223)
# print(future)

#6
# 6. “Saat 17:00, 04.06.2022 tarixində dərsə gəlin” cümləsindən istifadə edərək tarixi datetime formatına çevirin.


# data = 'Saat 17:00,04.06.2022 tarixində dərsə gəlin '
# pattern ='saat %H : %M, %Y.%m.%d tarixinde derse gelin'
# data_date = datetime.striptime(data,pattern)
# print(data_date)
# errroorr verirrrrr







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
# import random
# nam = input('adlari girin:  ')

# adlar = ['Hesen', 'Arif', 'Elnur', 'Kamal']

# for nam in adlar:
#     result = random.choice(adlar)
# print(result)    


#4
# 4. Ədəd təxmin etmə oyunu hazırlayın. Müəyən bir araılq verin və program həmin aralıqda bir ədəd təyin etsin. 
# Daha sonra siz həmin ədədi tapana qədər oyun davam etsin. 
# Siz gizli ədədin aşağısında bir təxmin etdikdə program daha yuxarı, yuxarısında təxmin etdikdə isə daha aşağı desin.
#  Ən sonda ədədi neçə səfərə tapdığınızı qeyd etsin.
#  Əgər 10 üzərində təxmin etdikdən sonra tapıbsızsa məğlub sayılırsız, əks təqdirdə qalib.

#BIRINCI USUL
# from random import randint
# count = 0
# correct_answer = 10
# correct_answer_attempt = 0
# for n in randint(1,20):
#     if randint(1,20) == n:
#         count += 1
#         if count > 10:
#             print('qalib gelmek ucun cehdlerin sayi 10 dan kicik olmalidir')
#     elif randint(1,20) < 10:
#         print('gizlin eded hazirki ededden yuksekdir')
#     elif randint(1,20) > 10:
#         print('gizlin eded  tapilan ededden kicikdir') 
#     else :
#         print('meglub oldunuz')       
       
#IKINCI USUL    
# if randint(1,20) == 10:
#     print('qalib')
# elif randint(1,20) < 10:
#     print('gizlin eded hazirki ededden yuksekdir')
# elif randint(1,20) > 10:
#     print('gizlin eded  tapilan ededden kicikdir') 
# else :
#     print('meglub oldunuz')       

# 5. Yer kürəsi ilə Pluton arasındakı məsfə 588 milyon kilometrdir. Saatda 90 km/saat sürətlə, 
# fasiləsiz hərəkət edən Niva maşını hansı tarixdə Yupiter planetinə nə zaman çatar?


from datetime import datetime,timedelta

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


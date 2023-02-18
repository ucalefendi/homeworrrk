# 1. 1000 ədəd random yığılmış floatdan ibarət list hazırlayın. Daha sonra girilən listin ən böyük elementini
#  tapan 2 funksiya hazırlayın. Birincisi parametrdəki listi sort edib, son elementi çıxarsın, digəri isə bu 
#  əməliyyat üçün seçilmiş alqoritm (infinity ilə başlayan ilk dəyərə sahib alqoritm) ilə işləsin. timeit ilə 
#  hazırladığınız iki funksiyanın 
# sürətlərini ölçün


import random
from timeit import timeit
from math import inf as infinity


# float_random_list = []
# for n in range(1,1001):
#     float_number = round(random.uniform(1,100),2)
#     float_random_list.append(float_number)


# def bignumbersort(a):
#     a.sort(key = lambda x: x ,reverse=True)
#     return a[0]


# def biggestnumber(numbers):
#     max_value = -infinity
#     for n in numbers:
#         if n > max_value:
#             max_value = n
#     return max_value

# # print(biggestnumber(float_random_list))            
 

# duration1 = timeit('bignumbersort(float_random_list)','from __main__ import float_random_list,bignumbersort')
# duration2 = timeit('biggestnumber(float_random_list)','from __main__ import float_random_list,biggestnumber')
# print(duration1,duration2)

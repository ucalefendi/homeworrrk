# # 2 input alacaqsiniz. Birinde reqemler ve digerinde reqemlerin uygun geleceyi nomre yazilisi olacaq. 
# # Hemin nomre yazilisi icerisindeki
# #  diesleri verilen reqemlerle evezlemelsiniz 


# number =input()
# pattern =input()

# print('+',pattern.replace('#', '{}').format(*number))


#homework11,tapsiriq 1
# 1. İstifadəçinin girdiyi mətn daxilindəki hərflərin ingilis əlifbasındakı sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin. Örnək:
# input: `Men Javascript oyrenirem`
# output: `13,5,14, 10,1,22,1,19,3,18,9,16,20, 15,25,18,5,14,9,18,5,13,`

# sentence = 'Men js oyrenirem'
# result = ''
# for char in sentence.lower():
#     if char.isalpha():
#         order = ord(char) - 96
#         result += str(order) + ','

# print(result)        

# #homework 11 tapsiriq 2
# Atadan 2 oğula bir ferma miras qalıb. 
# Ata vəsiyyətində deyir ki, fermanı ortadan 2-yə bölün, birinci yarısı böyük oğula, 
# 4ikinci yarısı isə kiçik oğula verilsin.
#  Ədalətsizliyi aradan qaldırmaq üçün qardaşlar razılaşır ki, 
#  gəl hərəmizə düşən fermadakı heyvanların qiymətlərini hesablayaq, 
#  əgər kimin ferması daha çox pul edirsə, o aradakı fərqi bağlamaq üçün cibindən çıxarıb, 
#  digərinə nəğd pul versin. Misal üçün əgər böyük qardaşın ferması 20000 manat, 
#  kiçik qardaşınkı 15000 manatdırsa, böyük qardaş öz cibindən çıxarıb kiçiyə 2500 manat versin,
#   beləliklə hər birinin sərvəti eyni olsun.
# Fermamız və qiymətlər aşağıdakı kimidir:
# ferma = ('at', 'inek', 'inek', 'keci', 'qoyun', 'qoyun', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'inek', 'keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}


# ferma1 = ferma[:len(ferma)//2]
# ferma2 = ferma[len(ferma)//2:]
# f1_price = 0
# f2_price = 0 
# for animal in ferma1:
#     f1_price += qiymetler[animal]

# for animal in ferma2:
#     f2_price += qiymetler[animal]   

# if f1_price > f2_price :
#     debt =(f1_price - f2_price) / 2
#     print('kicik qardas boyuk qardasa {} manat pul vermelidir. '.format(debt) )
# else: 
#     debt = (f2_price - f1_price)/2    
#     print('boyuk qardas kicik qardasa {} manat pu; vermelidir'.format(debt))



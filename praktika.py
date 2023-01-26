# Istifadəçinin girdiyi stringi binary şəklində göstərin. Örnək:
# input: 'Men Python 3 oyrenirem'
# input: 'Men Python 3 oyrenirem'
# output: '1001101 1100101 1101110 100000 
# 1010000 1111001 1110100 1101000 1101111 1101110 100000 110011 100000 
# 1101111 1111001 1110010 1100101 1101110 1101001 1110010 1100101 1101101'

#3 cu tapsiriq

# text = input('metni daxil edin:  ')
# for key in text :
#     print(bin(ord(key)))


# 1 ci tapsiriq
# İstifadəçinin girdiyi mətn daxilindəki hərflərin ingilis əlifbasındakı sırasına qarşılıq gələn ədədlərlə dəyişdirilmiş şəkildə göstərin. Örnək:
# input: Men Javascript oyrenirem
# output: 13,5,14, 10,1,22,1,19,3,18,9,16,20, 15,25,18,5,14,9,18,5,13,


# text = input('metni daxil edin:   ').lower()
# result=[]
# for key in text:
#     if key.isalnum():
#         result += str(ord(key) - 96)
# # comperehension =[ord(key) for key in result ] 
  
# print(result)  
     
#4cu tapsiriq
# Istifadəçi input olaraq color: rgb(127, 255, 12) şəklində CSS rəngi girəcək. 
# Siz istifadəçinin girdiyi rəngi 16-lıq sistemdəki qarşılığına çevirin. Örnək:
# input: color: rgb(244, 123, 12)
# output: color: f47b0c
# text = rgb(244, 123, 12) 


# Atadan 2 oğula bir ferma miras qalıb. Ata vəsiyyətində deyir ki,
#  fermanı ortadan 2-yə bölün, birinci yarısı böyük oğula, ikinci yarısı 
#  isə kiçik oğula verilsin. Ədalətsizliyi aradan qaldırmaq üçün qardaşlar razılaşır ki, 
#  gəl hərəmizə düşən fermadakı heyvanların qiymətlərini hesablayaq, əgər kimin ferması 
#  daha çox pul edirsə, o aradakı fərqi bağlamaq üçün cibindən çıxarıb, digərinə nəğd pul versin.
#   Misal üçün əgər böyük qardaşın ferması 20000 manat, kiçik qardaşınkı 15000 manatdırsa, 
#   böyük qardaş öz cibindən çıxarıb kiçiyə 2500 manat versin, beləliklə hər birinin sərvəti eyni olsun.
# Verilən məlumatlara əsasən hansı qardaş hansına nə qədər pul verməli olduğunu göstərən kod yazın
# Fermamız və qiymətlər aşağıdakı kimidir:

# ferma = ('at','inek','inek','keci','qoyun','qoyun','qoyun','inek','at','toyuq','inek','inek','keci', 'at', 'keci', 'qoyun', 'inek', 'at', 'toyuq', 'inek', 'keci', 'keci', 'inek', 'toyuq', 'inek', 'toyuq', 'keci', 'toyuq', 'at', 'keci', 'at', 'keci', 'inek', 'qoyun', 'keci', 'at', 'qoyun', 'inek', 'inek', 'toyuq', 'at', 'at', 'toyuq', 'at', 'inek', 'toyuq', 'inek', 'toyuq', 'toyuq', 'qoyun')
# qiymetler = {'at': 1200, 'inek': 900, 'toyuq': 50, 'keci': 300, 'qoyun': 150}

# price_at = ferma.count("at")*qiymetler.get('at')
# price_inek =ferma.count('inek')*qiymetler.get('inek')
# price_toyuq = ferma.count('toyuq')*qiymetler.get('toyuq')
# price_keci = ferma.count('keci')*qiymetler.get('keci')
# price_qoyun = ferma.count('qoyun')*qiymetler.get('qoyun')
# fermanin_deyeri = price_at+price_inek+price_keci+price_qoyun+price_toyuq

# at_number = ferma.count("at")
# inek_number =ferma.count('inek')
# toyuq_number = ferma.count('toyuq')
# keci_number = ferma.count('keci')
# qoyun_number = ferma.count('qoyun')













    




    



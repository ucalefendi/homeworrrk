baliqlar = {
    'qelseme teneffusu', '2 kamerali urek', 'uzgec', 'korteks yoxdur',
    'yumurtlama', 'dis yoxdur', '4 ayaq'
}

cuculer = {
    'toraks teneffusu', 'urek yoxdur', '6 ayaq',
    'korteks vardir', 'beyin yoxdur', 'yumurtlama', 'metamorfoz', 
    'dis yoxdur'
}

amfibialar = {
    'qelseme teneffusu', 'agciyer teneffusu', 'uzgec', '4 ayaq', 
    '2 kamerali urek', '3 kamerali urek', 'metamorfoz', 'kotex vardir',
    'yumurtlama', 'dis yoxdur'
}

surunenler = {
    'agciyer teneffusu', '3 kamerali urek', '4 ayaq', 'korteks vardir', 'yumurtlama',
    'dis var'
}

quslar = {
    'agciyer teneffusu', '4 kamerali urek', 'korteks vardir',
    'yumurtlama', 'dis yoxdur'
}

memeliler = {
    'agciyer teneffusu', '4 kamerali urek', '4 ayaq', 'korteks vardir',
    'dogma', 'dis vardir'
}

sinifler = {
    'baliqlar': baliqlar,
    'cuculer': cuculer,
    'amfibialar': amfibialar,
    'surunenler': surunenler,
    'quslar': quslar,
    'memeliler': memeliler,
}

# tapsiriqlar
# 1. Quşların xüsusiyyətlərinə `"2 ayaq"` əlavə edin.
# 2. Balıqların xüsusiyyətlərindən `"4 ayaq"` məlumatını çıxarın
# 3. Amfibialar ilə cücülərin ortaq cəhətlərini göstərən kod yazın
# 4. Balıqlar ilə amfibiaların fərqli cəhətlərini göstərən kod yazın
# 5. Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın
# 6. Quşlar ilə ən çox ortaq cəhətə sahib olan sinifi tapın
# 7. İstifadəçi input ilə sizə bəzi özəlliklər girəcək. Siz həmin özəlliklərə əsasən heyvanın hansı sinifə 
# aid ola biləcəyini təxmin edən kod yazın. 
# Örnək : input: dis yoxdur, agciyer teneffusu, korteks vardir 
#         output: Bu heyvan quslar sinifine aid ola biler

# #1
# quslar.add('2 ayaq')
# print(quslar)



#2
# baliqlar.remove('4 ayaq')
# print(baliqlar)


# #3
# accomplice =  amfibialar.intersection(cuculer)
# print(accomplice)

#4
# between_diff = baliqlar.difference(amfibialar)
# # print(between_diff)
# print(len(between_diff))

#5
# 5. Balıqlar ilə heç bir ortaq cəhətə sahib olmayan sinifi tapan kod yazın

# class_animal = [cuculer,amfibialar,surunenler,quslar,memeliler]
# print(class_animal)

# for el in class_animal:
#     if baliqlar.isdisjoint(el) == True:
#         print(el)
#     else:
#         print('her sinif ile ortaq ceheti var')


#6
# dif1 = len(quslar.intersection(baliqlar))
# dif2 = len(quslar.intersection(cuculer))
# dif3 = len(quslar.intersection(amfibialar))
# dif4 = len(quslar.intersection(surunenler))
# dif5 = len(quslar.intersection(memeliler))
# print(dif1,dif2,dif3,dif4,dif5)


# 7. İstifadəçi input ilə sizə bəzi özəlliklər girəcək. Siz həmin özəlliklərə əsasən heyvanın hansı sinifə 
# aid ola biləcəyini təxmin edən kod yazın. 
# Örnək : input: dis yoxdur, agciyer teneffusu, korteks vardir 
#         output: Bu heyvan quslar sinifine aid ola biler



text =input('ozellikleri daxil edin:  ')

def spes(text):
    return text
print(spes(text))    




    
    
       



        

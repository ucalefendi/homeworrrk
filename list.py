# yeni_list = [1,2,3,4,5,6,9,7,8,'ucal',type,False]

#chance list item
# yeni_list[2]=1994
# print(yeni_list)
# yeni_list[5:11]=[10,10]

# yeni_list.append(10000000000)
# print(yeni_list)

# yeni_list.extend(['ayten','arzu','eldar'])
# print(yeni_list)

# yeni_list.index(5)
# print(yeni_list)

# for element in yeni_list:
#     print('bu element listin icindedir',element)
##############################################################    

#ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci'] 
# 1. Fermada keçinin sırasını tapın
# 2. Fermadakı heyvanları ad sırasına görə sıralayın
# 3. Fermadan bir at çıxarıb, ən sağdan bir toyuq əlavə edin
# 4. Ən soldan bir keci əlavə edin
# 5. Fermanın yarısını dinamik bir şəkildə silin
# 6. Yeni gələn `['at', 'qoyun', 'inek', 'inek', 'qoyun']` heyvanları fermaya əlavə edin
# 7. Fermadakı heyvanları 3 qatına çıxarın
# 8. Fermadakı heyvanları tərsinə sıralayın
# 9. Fermadakı ineklerin sayının ümumi fermanın neçə faizi olduğunu tapın
# 10. Oxşar fermadan istəyən basqa bir fermerə fermamızın kopyasını verini
# 11. Fermada təmir işi getməlidi, heyvanları çölə çıxarmaq üçün fermanı təmizləyin
 
#a)index=ferma.index('keci')
#print(index)

# b)ferma.sort()
# print(ferma)

# C)ferma.remove('at')
# print(ferma)
# ferma.append('toyuq')
# print(ferma)

# D)ferma.insert(0, 'keci')
# print(ferma)


# f)m=['at', 'qoyun', 'inek', 'inek', 'qoyun']
# ferma.extend(m)
# print(ferma)

#g)
#print(ferma*3)

#h)
# ferma.reverse()
# print(ferma)

#i)
# ferma = ['at', 'qoyun', 'inek', 'at', 'inek', 'qoyun', 'at', 'at', 'keci'] 
# m=len(ferma)
# n=ferma.count('inek')
# print((n/m)*100)

#k)
# ferma.clear()
# print(ferma)
####################################

#2. Aşağıdakı `result` listinin 0-cı indexinə `numbers` listi daxilindəki müsbət ədədlərin cəmini,
 #1-ci indexə isə mənfi ədədlərin cəmini yerləşdirin.     -

# result = [0, 0]
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# menfi=0
# musbet=0

# for i in numbers:
#     if i > 0 :
#      musbet + i
#     elif i < 0 :
#         menfi += i

# result.clear()
# result.insert(0,musbet)
# result.insert(1,menfi)
# print(result)        


###################################################################################################3
#3)İstifadəçinin girdiyi ədədi tək ədədlərdən ibarət tərsinə çevirilmiş list şəklinə salın.
 #Listin bütün elementlərinin integer olmasına diqqət edin. Örnək:

# eded = list(input('ededi daxil edin'))
# eded.reverse()
# print(eded)

#4
#  `numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]` 
# list içərisindəki ən böyük və ən kiçik ədədi dinamik şəkildə tapın.
# numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
# min=min(numbers)
# max=max(numbers)
# print(min,max)
#####################################################################################
#5)Aşağıda tələbələrin semestr nəticələri qeyd edilmişdir. 
#Buna əsasən qeyd olunmuş statistik məlumatları eyni anda print edin.
# 1. Tələbə sayı
# 2. Ümumi ortalama.
# 3. Kəsilən tələbələrin ümumi faizi (51- qiymət alanlar)
# 4. Yüksək nəticə göstərən tələbələrin ümumu faizi (80+ qiytət alanlar)


r=[31, 38, 69, 83, 83, 56, 38, 41, 96, 48, 43, 60, 49, 47, 73, 60, 69, 96, 50, 74]
# 1)
telebe_sayi=len(r)
# print(telebe_sayi)

#2)
# cem=0
# for i in r:
#     cem += i
# print(cem)  
# 
#cem=1204  

#3)

#umumi_ortalama = cem/len(r)
#print(umumi_ortalama)

#4)
# kesilentelebe = 0
# for i in r:
#     if i < 51 :
#         kesilentelebe += i
# print((kesilentelebe/telebe_sayi)*100)

#5)
# kecentelebe = 0
# for i in r:
#     if i > 81 :
#         kesilentelebe += i
# print()        

    

  

    






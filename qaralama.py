# n = 10
# nresult = 1
# for i in range(1,n + 1): 
#     nresult *= i
    

# r = 15 
# rresult = 1
# for i in range(1, r + 1):
#     rresult *= i


# # diff = n - r
# # diffresult = 1
# # for i in range(1,diff + 1):
# #     diffresult *= i
# # print(diffresult)    

# def factorial(number):
#     result = 1
#     for i in range(1,number + 1):
#      result *= i
#     return result


# print(factorial(5)*154) 

# l ={'value1': factorial(4), 'value2' : factorial(7) }
# print(l)
    
# def get_site_name(site,pref,suf):
#     return site.removeprefix(pref).removesuffix(suf).capitalize()


# print(get_site_name('wwww.google.com','www.','.com'))   

# def get_site_name(site, pref, suf  ):
#     return site.removeprefix(pref).removesuffix(suf).capitalize()


# # # print(get_site_name('aws.amazon.or','aws.','.or'))

# # # site_info = {'site': 'www.amazon.com','pref':'www.','suf':'.com'}
# # # print(get_site_name(**site_info))
# # l =['www.azadliq.info','www.','.info']

# # print(get_site_name(*l))


# # def getmanat(*dollars):
# #     result = 0
# #     for d in dollars:
# #         result += d
# #     result = result * 1.7
# #     return round(result)

# # print(getmanat(71,78))  

# # def get_sum(numbers):
# #     result = 0
# #     for i in numbers:
# #         result += i
# #         return result


# # def getcurrency(*args,**kwargs):
# #     for key,value in kwargs.items() :
# #         print(f'{key.upper()} umumi qiymeti:{get_sum(args)* value}')

# # getcurrency(12, 53, 12, 54, azn=1.7, tl=20) 

# # 1. Girilen stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
# # `upunion('birlesmis', 'milletler', 'teskilati') => 'BMT'`

# # def get_reverse(*args):
# #     for char in args:
# #         return char[0].upper()

# # print(get_reverse('birlesmis', 'milletler', 'teskilati'))

# # def upunion(*govs):
# #      return ''.join([name[0].upper() for name in govs])

# # govs = [
# #     ['birlesmis', 'milletler', 'teskilati'],
# #     ['Azebaycan', 'respublikasi'],
# #     ['fovqalade', 'hallar', 'nazirliyi'],
# #     ['azerbaycan', 'avtomabil', 'yollari']
# # ]

# # print(upunion(*govs))

# # Girilen stringi qeyd edilen sekilde deyisen bir funksiya hazirlayin
# # chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') =>
# # 'Kitabi sehife-sehife oxumalisan ki,
# # oyrenesen'

# # def chstr(text,**kwargs):
# #      for key,value in kwargs.items():
# #         text = text.replace(key,value)
# #         return text   

# # print(chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren'))            


# # 3. Birinci argument ilk qiyməti, ikinci argument isə yeni qiyməti göstərir.
# #  Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.
# # `find_percent(200, 60) # output: qiymet 70% azalmisdir` 
# # `find_percent(100, 150) # output: qiymet 50% artmisdir`


# # def find_percent(first,second):
# #     diff = first - second
# #     persent = (abs(diff)/ first) * 100
# #     if first > second :
# #         print(f'qiymet {persent}% azalmisdir')
# #     elif first < second:
# #         print(f'qiymet {persent}% artmisdir')    
# #     else:
# #         print( 'qiymet deyismeyib' ) 

# # print(find_percent(45,154))           

# # Girilən listin ən böyük ədədindən ən kiçiyini çıxarıb, nəticə verən bir funksiya hazırlayın.
# # big_dif_sml([6, 3, 8, 9, 2]) => 7 # en  boyuk 9, en kicik 2

# # def diff(numbers):
# #     for n in numbers:
# #          return max(numbers) - min(numbers)

# # print(diff([6, 3, 8, 9, 2]))

# # 6. Verilmiş ədədləri tərsinə çevirib toplayan bir funksiya hazırlayın
    

# #     # print(getReversedSum(123, 567, 562, ...))
# #     # result: 1351

# # def get_reversed(num):
# #     num = str(num)[::-1]
# #     num = int(num)
# #     return num

# # def get_reversed_sum(*args):
# #     result = 0
# #     for i in args:
# #         result += get_reversed(i)
# #         return result

# # print(get_reversed_sum(458,6549))       

# # =====================================

# # def get_reversed(num):
# #     num = str(num)[::-1]
# #     num = int(num)
# #     return num

   

# # def get_reversed_sum(*args):
# #     result = 0
# #     for i in args:
# #         result += get_reversed(i)
# #     return result

# # print(get_reversed_sum(123, 567, 562))
# #######################################################

# # Aşağıdakı result listinin 0-cı indexinə numbers listi daxilindəki müsbət ədədlərin cəmini, 
# # -ci indexə isə mənfi ədədlərin cəmini yerləşdirin. 

# # result = [0, 0]
# # numbers = [10.2, -32, -5.45, 32, 7, 43, -24.06, -4, -6.33, 62]
 
# # for i in numbers:
# #     if i > 0:
# #         result[0] += i
# #     elif i < 0 :
# #         result[1] += i
# # print(result)        

# # a = [1,2]
# # b = a
# # b.append(3)
# # print(b)
# # print(a)

# ########################################
# # İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın. Örnək:
# # Input: This is an example! 
# # Output: sihT si na !elpmaxe


# # text = input('metni daxil edin:  ')
# # text = text.split()
# # text_reverse = [word[::-1] for word in text]
# # print((' '.join(text_reverse)))

# users = [

#     {'name': 'Ucal', 'username': 'ucl', 'password': '1234', 'blocked': False},
#     {'name': 'Akif', 'username': 'a456', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]
# # 1. istifadəçi username səhv girərsə belə bir istifadəçi yoxdur deyin
# # 2. şifrəni səhv girərsə şifrəniz yanlışdır deyin
# # 3. əgər blok olunubsa siz daxil ola bilməzsiniz deyin
# # 4. əgər hər şey qaydasındadırsa “filankes giriş etdiniz” deyin

# username = input('istifadeci adini daxil edin: ')
# current_user = None

# for info in users:
#     if info == info['username']:
#         current_user = info

# if current_user == None:
#     print('bele bir isdifadeci yoxdur')
#     exit() 

# password = input('sifreni daxil edin: ')  

# if current_user.get('password') != password :
#     print('sifreniz duzgun deyil')
#     exit()

# if current_user['blocked']:
#     print('daxil ola bilmezsiniz')
#     exit() 

# print('hormetli {} xos gelmisiniz'.format(current_user.get('name')))

#homework 3 . lesson 2
# 2. (Orta) İstifadəçidən nömrə istəyən bir program hazırlayın.
#  Nömrələr +994 ilə başlamalı və uzunluğu 13 ədəddən ibarət olmalıdı. 
# İlk characteri olan + çıxmaq şərtilə ancaq ədədlərdən ibarət olmalıdır

# number =input('nomreni daxil edin:  ')
# if len(number) ==14:
#     if number.startswith('+994'):
#         print('nomre dogrudur')
#     else:
#         print('basliqi duzgun deyil')
# else:
#     print('uzunluq duzgun deyil')
    
    # #lesson 3
# text = input('metni girin:  ')
# source = input('deyismek isdediyiniz sozu girin: ')
# target = input('neyi deyismek isdediyinizi girin: ')
# print('netice: \n '+ text.replace(source,target))


metn = """Salyut 1 kosmosa göndərilən ilk kosmik stansiya idi.
O, 1971-ci ilin aprelində Sovet İttifaqı tərəfindən orbitə buraxılıb və 1971-ci ilin oktyabr
ayına qədər kosmosda qaldı. Kosmosda olduğu müddətdə onu ekipajlarla birlikdə iki kosmik gəmi 
ziyarət etdi. Salyut 1-in məqsədi kosmik stansiyanın necə işlədiyini öyrənmək və sınaqdan keçirmək idi.
İkinci məqsəd kosmosda uzun müddət qalmağın 
insan orqanizminə necə təsir etdiyini öyrənmək idi. Onun bir sıra problemləri var idi,
lakin ondan gələcək stansiyalara kömək edən çox şey öyrənildi."""

# 1. Yuxarıdakı mətndə bu sözlərin hamısının işlənib-işənmədiyini yoxlayın - `kömək, həyat, sınaq`
# 2. Metnde işlənən ilk və son kosmos sözlərinin indeksini göstərin
# 3. Metinin `Salyut` ilə başlayıb `ildi.` ilə bitdiyini təstdiqləyən kod yazın

if 'kömək' in metn and 'həyat' in metn and 'sınaq' in metn :
    print('ok')
else:
    print('yoxdur')            






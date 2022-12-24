# luget= {'soyad': 'efendi',
#         'ad': 'ucal',
#         'tevellud' :'16-11-1994',
#         'work': 'soliton'
#         }


# # print(luget['soyad'])        
# # print(luget['work'])


# # luget['soyad']='efendiyev'
# # print(luget)

# luget2 = {
#     'universitet': 'texniki',
#     'tehsil': 'ali',
#     'fakulte': 'neqliyyat'

#         }      

# # user=luget.copy()
# # luget['ad'] = 'rustamov' 
# # user['work'] = 'bakuelectronics'
# # print(user)
# # luget.update(luget2)
# # print(luget)
# luget2.update(luget)
# print(luget2)
# # print(luget2.get('universitet'))
# # print(luget2.setdefault('korpus',5))
# # print(luget2.setdefault('kafedra','neqliyyatda dasinmalarC'))
# # emited = luget2.pop('soyad')
# # print(emited)
# # print(luget2)
# # print(list(luget2.items()))
# # print(list(luget2.values()))
# # print(list(luget2.keys()))
# movzular= ['cografiya','kimya','fizika','edebiyat']
# # print(str(movzular))
# #numbers = ['+994','95','95','95']
# full_numbers = '-'.join(numbers)
# # print(full_numbers)
# #numbers = full_numbers.split('-')
# #print(numbers)


# 1. Istifadəçi sizə `"5 salam"` şəklində solda ədəd, ortada, boşluq, 
# sağda isə bir input verəcək. Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər yazıb, 
# istifadəçiyə qatarın. Örnək yuxaridakı inputun outputu `salam salam salam salam salam`


# text =input('metni daxil edin: ')
# count,word = text.split(' ')
# # result = (word+ ' ') * int(count)
# # print(result)

# # 2. İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın. Örnək:
# # Input: `This is an example!` 
# # Output: `sihT si na !elpmaxe`

# # text=input('metni daxil edin: ')
# # words = text.split()
# # text_reverse = [word[::-1] for word in words]
# # print((' ').join(text_reverse))

# # ```python
# users = [
#     {'name': 'ucal', 'username': 'ucl', 'password': '1234', 'blocked': False},
#     {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
#     {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
# ]


# # 1. istifadəçi username səhv girərsə belə bir istifadəçi yoxdur deyin
# # 2. şifrəni səhv girərsə şifrəniz yanlışdır deyin
# # 3. əgər blok olunubsa siz daxil ola bilməzsiniz deyin
# # 4. əgər hər şey qaydasındadırsa “filankes giriş etdiniz” deyin



# username = input('adinizi daxil edin :  ')
# current_user = None

# for info in username :
#     if username == info['username']:
#         current_user = info

# if current_user == None:
#     print('bele isdifadeci yoxdur')  
#     exit

# password = input('sifreni daxil edin') 

# if current_user.get('pasword') != password:
#     print('sifreniz duzgun deyil')
#     exit

# if current_user.get('blocked'):
#     print('siz daxil ola bilmezsiniz') 
#     exit


# print('hormetli {} xosh gelmisiniz!'.format(current_user.get('name')))

# ##########################################################

# 1. İstifadəçinin boyunu artırın
# 2. Telefonun markasını dəyişərək Samsung edin
# 3. İstifadəçinin adını silin
# 4. İstifadəçinin ilk sifarişini silin
# 5. İstifadəçinin sifarişlərinin başına ball əlavə edin
# 6. Sonuna headphones əlavə edin

# user = {
#     'name': 'Elnur',
#     'height': 179,
#     'phone': {
#         'model': 'Iphone',
#     },
#     'orders': ['book', 'mouse', 'mousepad']
# }


# user['height'] += 1
# print(user)
# user['phone']['model'] = 'samsung'
# print(user)
# del user['name']
# print(user)
# del user['orders'][0]
# del user.get('orders')[0]
# print(user)

# orders = user.get('orders')
# orders.insert(0 , 'ball')
# orders.append('headphones')
# print(user)
############################################
# info = ["Resul", "Serifov", 35]
#     # 1. Yuxarıdakı arrayı dinamik olaraq `["Resul Serifov", 25]` vəziyyətinə gətirin
############################################
# 4. Aşağıdakı datada məhsulların ad və qiymətləri qeyd olunmuşdur.
    
shop = {
    "t-shirt" : 59.00,
    "jeans" : 75.00,
    "sweatshirt" : 60.00, 
    "shoe" : 124.99, 
    "jacket" : 154.90
}
    
# 5. Dictionary əsasən istifadəçi sizə məhsul adı girəcək. Bu məhsulun mağazada olan qiymətini
#  göstərən proqram hazırlayın. Girilən məhsul mağaza da olmadığı halda "None" qaytarın.
# 6. Mağazaya yeni məhsullar və qiymətlərini əlavə edin.
# 7. Mağazada nə qədər məhsul olduğunu göstərin
# 8. Məhsulların qiymətini 30% artırıb yeni qiymətləri mağazaya əlavə edin.

brend = input('mehsulu girin:   ')
for brend in shop :
    print(shop.get(value))


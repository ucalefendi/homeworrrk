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
# result = (word+ ' ') * int(count)
# print(result)

# 2. İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın. Örnək:
# Input: `This is an example!` 
# Output: `sihT si na !elpmaxe`

# text=input('metni daxil edin: ')
# words = text.split()
# text_reverse = [word[::-1] for word in words]
# print((' ').join(text_reverse))

# ```python
users = [
    {'name': 'ucal', 'username': 'ucl', 'password': '1234', 'blocked': False},
    {'name': 'Senan', 'username': 'sm_ov', 'password': '5423s', 'blocked': False},
    {'name': 'Kamal', 'username': 'km123', 'password': '34-kk-325', 'blocked': True}
]


# 1. istifadəçi username səhv girərsə belə bir istifadəçi yoxdur deyin
# 2. şifrəni səhv girərsə şifrəniz yanlışdır deyin
# 3. əgər blok olunubsa siz daxil ola bilməzsiniz deyin
# 4. əgər hər şey qaydasındadırsa “filankes giriş etdiniz” deyin



username = input('adinizi daxil edin :  ')
current_user = None

for info in username :
    if username == info['username']:
        current_user = info

if current_user == None:
    print('bele isdifadeci yoxdur')  
    exit

password = input('sifreni daxil edin') 

if current_user.get('pasword') != password:
    print('sifreniz duzgun deyil')
    exit

if current_user.get('blocked'):
    print('siz daxil ola bilmezsiniz') 
    exit


print('hormetli {} xosh gelmisiniz!'.format(current_user.get('name')))






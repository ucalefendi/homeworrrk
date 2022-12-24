# 1. Istifadəçi sizə `"5 salam"` şəklində solda ədəd, ortada, boşluq, sağda isə bir input verəcək. 
# Buna əsasən sağdakı yazını istifadəçinin qeyd etdiyi ədəd qədər yazıb, istifadəçiyə qatarın. 
# Örnək yuxaridakı inputun outputu `salam salam salam salam salam`


# text = input('metni daxil edin:   ')
# count, word = text.split(' ')
# result =(word+ ' ') * int(count)
# print(result)

# 2. İstifadəçinin girdiyi cümlədəki sözləri tərsinə çevirilmiş şəkildə istifadəçiyə qaytarın. Örnək:
# Input: `This is an example!` 
# Output: `sihT si na !elpmaxe`


# text = input('metni daxil edin:  ')
# words = text.split()
# result = [word[::-1] for word in words ]
# print((' ').join(result))

# user_info = {
#     'firstname': 'Elvin',
#     'lastname': 'Huseynov',
#     'username': 'elivin_h_ov',
#     'password': '12345',
#     'birthday': '19-08-1997'
# }
# Istifadəçi sizə bir input vasitəsilə bunun kimi bir məlumat girəcək:
# input: firstname Elcin, username elchina, birthday 18-08-2000
# Bu inputa əsasən yuxarıdakı dictionary-ni update edin ve istifadəçiye gosterin.
#  Misal yuxarıdakı inputa əsasən dictionary son halı aşağıdakı kimi olacaq.

#  user_info = {
#     'firstname': 'Elcin',
#     'lastname': 'Huseynov',
#     'username': 'elchina',
#     'password': '12345',
#     'birthday': '18-08-2000'
# }


#eded = 6

# if eded%2:
#     nov = 'tek'

ededler = [1, 53, 22, 5, 6, 1, 3, 4, 75]
# ['tek', 'tek', 'cut', 'tek', 'cut', 'tek', 'tek', 'cut', 'tek']

# novler = ['tek' if eded%2 else 'cut' for eded in ededler]
novler = {eded:'tek' if eded%2 else 'cut' for eded in ededler}
print(novler)
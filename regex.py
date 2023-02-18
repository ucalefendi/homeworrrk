import re 

# text = """Azərbaycanda Yeni il bayramı (1 və 2 yanvar), Beynəlxalq Qadınlar Günü (8 mart), Qələbə Günü (9 may), Müstəqillik Günü (28 may), Azərbaycan xalqının milli qurtuluş günü (15 iyun), Azərbaycan Respublikası Silahlı Qüvvələri günü (26 iyun), Müstəqilliyin Bərpası Günü (18 oktyabr), Zəfər Günü (8 noyabr), Azərbaycan Respublikasının Dövlət Bayrağı Günü (9 noyabr), Konstitusiya Günü (12 noyabr), Milli Dirçəliş Günü (17 noyabr), Dünya azərbaycanlılarının həmrəyliyi günü (31 dekabr), Novruz bayramı (beş gün), Qurban bayramı və Ramazan bayramı (iki gün) qeyd edilir. Müstəqillik günü, Milli Dirçəliş Günü və Konstitusiya Günü istisna olmaqla bayram günləri iş günü hesab edilmir. 2006-cı ildən bəri bayram günləri həftə sonuna düşəndə növbəti gün iş günü hesab edilmir."""

# value = re.findall('\d{2} [oktyabr | noyabr | dekabr]+', text)
# print(value)


# 1. Aşağıdakı listdə düzgün formada ad və soyad yazılmayan sözləri çıxarın:

# text ='Aygun Kazimova'
# value = re.search('[A-Z][a-z]+ [A-Z][a-z]+', text)
# # print(value)
# Nam = ['Aygun Kazimova', 'fermer Həsən', 'Namiq Qaracuxurlu', 'Rehim Rehimli', 'roya Ayxan', 'Eynulla']
# correct_name = []

# for n in Nam:
#     if re.search('[A-Z][a-z]+ [A-Z][a-z]+', n):
#         correct_name.append(n)

# print(correct_name)       


# 3. Aşağdakı mətindəki bütün saytları list şəklində çıxarın.
# text = """Dünyada bir çox saytlar mövcuddur. Bunların bir çoxu fərqli məqsədlərə xidmət edirlər. Müsal üçün http://www.google.com saytı axtarış üçün istifadə olunur. Digər yandan https://facebook.com və http://www.instagram.com saytları sosial şəbəkə kimi fəaliyyət göstərirlər"""
# val = re.search('^www\.\w+\.com$', text)
# val = re.findall('^www\.\w+\.com$',text)
# urls = re.findall("(?P<url>https?://[^\s]+)", text)  #cht gbt verdiyi


# 5)Aşağıdakı nömrələr arasında azercell nömrələri bir list daxilində toplayın:
Numbers = """051-235-642-12, 055-236-642-23, 077-623-234-26, 51-125-646-32, 50-125-542-12, 70-253-644-12, 050-135-346-64"""
azercell =re.findall('^051-\\d+ \\d+',Numbers)
print(azercell)

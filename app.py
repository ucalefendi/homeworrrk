# # def get_site_name(site,pref,suf):
# #     return site.removeprefix(pref).removesuffix(suf).upper()

# # print(get_site_name('www.google.com','www.','.com'))

# # def getmanat(*dollars):
# #     result = 0
# #     for d in dollars:
# #         result += d
# #     return result * 1.70
# # print(getmanat(78,45,89)) 



# def get_sum(numbers):
#     result = 0
#     for i in numbers:
#         result += i
#     return result        



# def getcurrency(*args,**kwargs):
#     result = 0
#     for key,value in kwargs.items():
#         print(f'{key.upper()} umumi qiymeti {get_sum(args) * value}') 
        

# print(getcurrency(45,21,36 ,azn = 1.7,Tl = 20))    

# 1. Girilen stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
# `upunion('birlesmis', 'milletler', 'teskilati') => 'BMT'`

# def upunion(*args):
#     return  ''.join([char[0].upper() for char in args])


# print(upunion('birlesmis', 'milletler', 'teskilati')) 

# govs = [['birlesmis', 'milletler', 'teskilati'],
#      ['dovlet','tehlukesizlik','xidmeti'],
#      ['qida','senayesi','teskilati']
#     ]



# result = [upunion(*gov) for gov in govs]
# print(result)


# Girilen stringi qeyd edilen sekilde deyisen bir funksiya hazirlayin
# chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren') => 
# 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'


# def chstr(text,**kwargs):
#     for key,value in kwargs.items():
#         text.replace(key,value)
#     return text
# print(chstr('Kitabi sehve-sehve oxumalisan ki, orgenesen', sehve='sehife', orgen='oyren')) 

# 3. Birinci argument ilk qiyməti, ikinci argument isə yeni qiyməti göstərir.
#  Yeni qiymətin ilkindən neçə faiz fərqləndiyini print edən funksiya düzəldin.
# `find_percent(200, 60) # output: qiymet 70% azalmisdir` 
# `find_percent(100, 150) # output: qiymet 50% artmisdir`   


# def find_percent(first,second):
#     diff = abs(first - second)
#     percent_count = (diff/first) * 100
#     if first > second:
#         print(f'qiymet {percent_count}% azalmisdir')
#     elif first < second :
#         print(f'qiymet {percent_count}% artmisdir')    
#     else:
#         print('qiymet beraberdir')   
# print(find_percent(100,250))         



# Verilmiş ədədləri tərsinə çevirib toplayan bir funksiya hazırlayın
# print(getReversedSum(123, 567, 562, ...))
# result: 1351
    
# def get_reversed_number(num):
#     num = str(num)[::-1]
#     num = int(num)
#     return num

# def get_multiple(*args):
#     result = 0
#     for i in args:
#         result += get_reversed_number(i)
#     return result    

# print(get_multiple(123,569))
    
get_reversed = lambda num: int(str(num)[::-1]) 
# get_reversed = lambda num: int(str(num))
# get_reversed = lambda num: int(str(num))


# print(get_reversed(123456789))


#call--back

# def change(l,callback):
#     return [callback(i) for i in l]

# numbers = [542987,4569874569,2356]    

# print(change(numbers,get_reversed))


# def changelist(num):
#     return num * 100

# def numberlist(numbers,callback):
#     return [callback(i) for i in numbers]


# print(numberlist(numbers,changelist))


# numbers = [542987,4569874569,2356] 
# numbers.sort() 
# numbers.append(154) 

# print(numbers)  
        
# pro = [{'top':10,'tapanca': 20,'supurge':30,'alma':75,'qrecqa':2}]

# products.sort()
# print(products)
# pro.sort(key =lambda product: product.get('top'))
# print(products)
    


# products = [
#     {'title': 'Honor', 'price': 1800},
#     {'title': 'Samsung Galaxy', 'price': 2700},
#     {'title': 'Huawei', 'price': 2000},
#     {'title': 'iPhone', 'price': 3000},
#     {'title': 'Nokia', 'price': 1200},
#     {'title': 'Oppo', 'price': 1900},
# ]


# products.sort(key =lambda product:product.get('price'),reverse =True)
# print(products)


# name = {'alma':'meyve','armud':'terevez','heyva':'qida','nar':'sefa'}
# # print(tuple(enumerate(name)))

# # for element,index in enumerate(name):
# #     print(index,element)

# print(dict(enumerate(name)))


# l = [1,2,3,4,5,6,7,8,9]

# val = min(l)
# var = sorted((1,5,3,2,9,11,15974,54),reverse = True)
# print(var)


# v= ('mahmud','elsen','ananas','heyva','alca','orxan')
# #print(sorted(('mahmud','elsen','ananas','heyva','alca','orxan'),key =len))
# products = [
#     {'title': 'Honor', 'price': 1800},
#     {'title': 'Samsung Galaxy', 'price': 2700},
#     {'title': 'Huawei', 'price': 2000},
#     {'title': 'iPhone', 'price': 3000},
#     {'title': 'Nokia', 'price': 1200},
    
# ]
  
# # val =tuple(zip(products,v))
# # print(val)
###################################################################################################################



a = {1,14,16,4,5,15,6}
b = {6,5,15,7,11,10,9,8}
c = {5,7,11,4,4,16,3,13,12,2}
d = {2,11,12}


# # adlar = {'ucal','camal','aydin','ismet','heyder'}
# # l= tuple(adlar)
# # betta = a.difference(b)
# alfa = a.intersection(b).intersection(c)
# betta = a.symmetric_difference(b)
# qamma = a.isdisjoint(b) #a b ile kesismenin olub olmadiqini yoxlayir ve geri donusu true ve ya falsedir
# teta = a.union(d)
# zeta = a.update(d)
# print(zeta)

        



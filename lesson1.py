#login=str(input('enter code'))        
#if login.isascii is true :
     #print('parol dogrudur!')     
#elif login.isalnum is true :
     #print('parol dogrudur') 
# login.islower or login.isupper:
     #print('bir kicik ve bir herf olmalidir!')  
#elif login.isalpha or login.isnumeric:
     #print('mutleq minimum bir herf ve minimum bir reqem olmalidir!')  
#else:
     





#x=str(input('siteni daxil edin'))
#print(x.removeprefix('http://').removesuffix('.com'))


#Verilen şəxsiyyət vəsiqəsinin düzgünlüyünü yoxlayan kod yazın. Şəxsiyyət vəsiqəsi:
#Şəxsiyyət vəsiqəsi 10 characterdən ibarət olmalıdır.
#Bunun ilk 3 hərfi hərhansı bir ölkənin qısaltması olmalıdır. Misal AZE, TUR, USA. 
#   Həmin qısaltmalar böyük hərflə yazılan ingilis şriftləridir.
#Daha sonrakı 7 character isə ancaq rəqəmlərdən ibarət olmalıdır


# AZE32089527
# id_number=input('seriani daxil edin')
# if len(id_number) != 10:
#      print('seria 10 xarakterden ibaret olmalidir!')
# elif not id_number[:3].isalpha() or not id_number[:3].isupper():
#      print('ilk 3 herf boyuk ve ingilis srifti olmalidir! ')
# elif not id_number[3:].isnumeric():  
#      print('3cu xarakterden sona qeder reqem olmalidir!') 
# else:
#      print('seriya duzgundur!')           




# (Orta) İstifadəçidən nömrə istəyən bir program hazırlayın. 
# Nömrələr +994 ilə başlamalı və uzunluğu 13 ədəddən ibarət olmalıdı.
# İlk characteri olan + çıxmaq şərtilə ancaq ədədlərdən ibarət olmalıdır   


# number=input('nomreni daxil edin')

# if len(number) == 14:
#      if number.startswith('+994'):
#          print('nomre dogrudur')
#      else:
#           print('basliqi duzgun deyil') 
# else:
#      print('uzunlugu duzgun deyil') 
           


# Metni girin: Sehvelerden en xosuma gelen sehve bu sehvedir 
# Deyismek istediyiniz sozu girin: sehve
# Neye deyismek istediyinizi girin: sehife
# Netice:
# sehifelerden en xosuma gelen sehife bu sehifedir


# text=input('metni girin: ')
# source=input('deyismek istediyiniz sozu girin: ')
# target=input('Neye deyismek istediyinizi girin: ')
# print('Netice:\n'+text.replace(source, target))  

# a=0
# while a<10:
#      print('leyla')

# i=0
# while i<=20:
#      if i%2==0:
#          print(i) 
#      i+=1   

# f=1  
# i=1
# while i<=15:
#      f=f*i
#      i=i+1
# print(f)

# c=0
# while c<5 :
#      print(c)
#      c+=1
# print(c)      


#1) 1-dən 100-ə kimi olan bütün ədədlərin toplamını tapın (1+2+3+...+99+100)
#2) 100000-dən aşağı doğru gedərək 9999-a bölünən ilk ədədi konsolda göstərin.


# a=99999

# while a<100000 :
#      a=a-1
#      a%9999
#      print(a)   



#3. `'Men her gun Python oyrenirem’` bu stringin saitlər çıxarılmış vəziyyətini konsolda göstərin.

# cumle = 'Men her gun Pyhton oyrenirem'
#print(len(cumle)-1)
#cumle=[27]

# num=1
# result=0
# while  num <= 100:
#      result += num
#      num += 1 
# print(result) 
# 
#  print(len(text))=28    

# text = 'Men her gun Pyhton oyrenirem'
# saitler='eiuao'
# counter=len(text)-1
# result= ''
# while counter >= 0:
#      char=text[counter]
#      if char not in saitler:
#           result += char
#      counter -= 1
# print(result) 
#############################################################################
#1. 1-dən 100-ə kimi olan bütün ədədlərin toplamını tapın (1+2+3+...+99+100)

# result=0
# for i in range(1, 101):
#      result=result+ i
# print(result)     

#2.100000-dən aşağı doğru gedərək 9999-a bölünən ilk ədədi konsolda göstərin.


# for i in range(1, 100000):
#     if i %9999 == 0:
#      print(i)
#      break     

#3. `'Men her gun Python oyrenirem’` bu stringin saitlər çıxarılmış vəziyyətini konsolda göstərin.


# text='Men her gun Python oyrenirem'
# text1=text[0:]
# saitler='aioue'
# result=''
# for char in text :
#      if char not in saitler :
#           result += char
# print(result)          

#4. (Orta) İstifadəçinin girdiyi cümlədə neçə heca olduğunu deyən program hazırlayın.
#Hecaların sayını tapmaq üçün saitlərdən istifadə edin.

# text=input()
# saitler='aioue'
# result=0
# for i in text:
#      if i in saitler:
#           result += 1
# print(result)                               
           

       
# text='Men her gun Python oyrenirem'
# saitler='aioue'
# textverse= text[0:]
# result = ''
# for char in text:
#      if char not in saitler:
#       result += char
# print(result)  
  


#verilen ededin reqemlerin cemini tapan kod hazirlayin

# eded = list(input('ededi daxil et  '))
# reqem = [0,1,2,3,4,5,6,7,8,9]
# while eded > 9:
#      if reqem in eded:
#           eded+=reqem
#           print(reqem)



     
# l=[True,'behram',3.2,1.5,[1,2,3 [1,2,3[1,2,3]]]]
# print(l[-1][1: -1]+ l[-1][-1][:-1][:: -1])





     
     
     







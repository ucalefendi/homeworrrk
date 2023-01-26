# 1. Girilen stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
# `upunion('birlesmis', 'milletler', 'teskilati') => 'BMT'`

# def upunion(*args):
#     return (''.join([name[0].upper() for name in args]))
# print(upunion('birlesmis', 'milletler', 'teskilati')) 

# 2. Girilen stringi qeyd edilen sekilde deyisen bir funksiya hazirlayin
# `chstr('Kitabi sehve-sehve oxumalisan ki,
#  orgenesen', sehve='sehife', orgen='oyren') => 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'`   

# def chstr(text,**kwargs):
#     for key,value in kwargs.items():
#         text.replace(key,value)
#     return text
# print(chstr('Kitabi sehve-sehve oxumalisan ki,  orgenesen', sehve='sehife', orgen='oyren'))        


# ########################
# #errorhandling
# bolunen = input('bolunen ededi daxil edin'   )
# bolen = input('boleni daxil edin'  )
# try: 
#   result = int(bolunen)/int(bolen)
# except ValueError as error_message:
#     print(f'ancaq eded girmek olar! xeta mesaji :{error_message}')  
# except ZeroDivisionError :
#     print('sifira bolmek olmaz,mexrec sifirdan ferqli olmalidir')  
# # except Exception as error_messsssage:
#     print(f'bilinmeyen bir xeta bas verdi! Xeta mesaji: {error_messsssage}')       


# print(result)

# animals = input('Heyvanlari girin: ').split(', ')
# prices = { 'inek': 500, 'toyuq': 50, 'qoyun': 120, 'at': 900, 'keci': 210 }
# # print('Umumi qiymet:', sum(map(lambda animal: prices[animal], animals)))
# print(lambda heyvan : prices[heyvan])

# 1. Bu kodda baş verə biləcək errorları araşdırıb, onları handle edin
# 2. Təxmin edə bilməyəcəyiniz errorlar üçün bir şərt qoşun
# 3. Əgər istifadəçi 10-dan artıq və ya 3-dən az heyvan giribsə internetdən 
# istədiyiniz bir erroru taparaq təyin edin.


# liste = [ 1,2,3,4,5,6,8,8,8,8,8,8]

# yeni_liste = map(lambda x: x * 2,liste)
# print(list(yeni_liste))


# def reverse_words(str):
#     return ' '.join(str.split(', ')[::-1])

# print(reverse_words("The greatest victory is that which requires no battle"))   
# # 
# result = ' '.join("The greatest victory is that which requires no battle".split(', ')[::-1]) 
# print(result)

def reverseWords(str):
    return ' '.join(reversed(str.split(' ')))

print(reverseWords("The greatest victory is that which requires no battle"))  
  
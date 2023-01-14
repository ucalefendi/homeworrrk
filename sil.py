# 1. Girilen stringlərin ilk hərfini böyüdüb, birləşdirən bir funksiya hazırlayın.
# `upunion('birlesmis', 'milletler', 'teskilati') => 'BMT'`

# def upunion(*args):
#     return (''.join([name[0].upper() for name in args]))
# print(upunion('birlesmis', 'milletler', 'teskilati')) 

# 2. Girilen stringi qeyd edilen sekilde deyisen bir funksiya hazirlayin
# `chstr('Kitabi sehve-sehve oxumalisan ki,
#  orgenesen', sehve='sehife', orgen='oyren') => 'Kitabi sehife-sehife oxumalisan ki, oyrenesen'`   

def chstr(text,**kwargs):
    for key,value in kwargs.items():
        text.replace(key,value)
    return text
print(chstr('Kitabi sehve-sehve oxumalisan ki,  orgenesen', sehve='sehife', orgen='oyren'))        
        

# n = 20
# nresult = 1
# for i in range(1,n+1):
#     nresult *= i
# print(nresult) 


# r = 15
# rresult = 1
# for i in range(1,r+1):
#     rresult *= i
# print(rresult)

# diff = n - r
# diffresult = 1
# for i in range(1,diff + 1):
#     diffresult *= i
# print(diffresult)    

# print(nresult/rresult*diffresult)

#faktorialin hesablanmasi

# def factorial(number):
#     result = 1
#     for i in range(1,number+1):
#         result *= i
#     return result  
# print(factorial(5)*2)     


# l = [factorial(9),factorial(8),factorial(7)]
# print(l)


def get_site_name(site,pref = 'www.',suff = '.com'):
    return site.removeprefix(pref).removesuffix(suff)

print(get_site_name('www.kayzen.com'))

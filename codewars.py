
#1
# def reverseWords(str):
#     return ' '.join(reversed(str.split(' ')))

# print(reverseWords("The greatest victory is that which requires no battle"))  

2
# "apple ban" --> ["apple 5", "ban 3"]
# "you will win" -->["you 3", "will 4", "win 3"]

# def add_length(str_):
#     answer = []
#     for word in str_.split():
#         answer.append(word + ' ' + str(len(word)))
#     return answer

# print(add_length("apple ban" ))  
# 
# 
# # def add_length(strr):
# 	return [i+' '+str(len(i)) for i in strr.split()] 


#3
#  16  -->  1 + 6 = 7
#    942  -->  9 + 4 + 2 = 15  -->  1 + 5 = 6
# 132189  -->  1 + 3 + 2 + 1 + 8 + 9 = 24  -->  2 + 4 = 6
# 493193  -->  4 + 9 + 3 + 1 + 9 + 3 = 29  -->  2 + 9 = 11  -->  1 + 1 = 2


#3cu calismanin helli .bu hell tam hell deyil.

from timeit import timeit
def get_digits_sum(number):
    digits = map(lambda x: int(x), str(number))
    
    return  sum(digits)
duration = timeit('get_digits_sum(942)')   
print(duration) 
      
   





# def get_digits_sum(number):
#     digits = map(lambda x: int(x), str(number))
#     return  sum(digits)

# #####################################
# 
 # [0, 4, 6, 8, 8, 8, 5, 5, 7] =>  [1, 1, 1, 3, 2, 1] => [3, 1, 1, 1] => [1, 3] => [1, 1] => [2]

# from timeit import timeit
# def get_count_list(numbers):
#     result = []
#     count = 1
#     before = None
#     for n in numbers:
#         if before != None and before == n:
#             count += 1
#         elif before != None and before != n:
#             result.append(count)   
#             count = 1
#         before = n
#     result.append(count)    
#     return result    
# print(get_count_list([0, 4, 6, 8, 8, 8, 5, 5, 7]))      


# def get_reducer(numbers):
#     if len(numbers) == 1:
#         return numbers[0]
#     return get_reducer(get_count_list(numbers)) 

# print(get_reducer(get_count_list([0, 4, 6, 8, 8, 8, 5, 5, 7])))

# duration1 = timeit('get_reducer(get_count_list(numbers))')
# print(duration1)







  

###teklif olunan helli.codewarsdan goturulen.
# def set_reducer(inp):
#     if len(inp) == 1:
#         return inp[0]
#     else:
#         reduced_array = []
#         counter = 1
#         current_number = inp[0]
#         for index in range(1, len(inp)):
#             if inp[index] == current_number:
#                 counter += 1
#             else:
#                 reduced_array.append(counter)
#                 current_number = inp[index]
#                 counter = 1
#         reduced_array.append(counter)
#         return set_reducer(reduced_array)  

# print(set_reducer(numbers))  
# 

# FIRST_NAME = {'A': 'Alpha', 'B': 'Beta', 'C': 'Cache'}
# SURNAME = {'A': 'Analogue', 'B': 'Bomb', 'C': 'Catalyst'}      


#5ci tapsiriq
# def alias_gen(f_name, l_name):
#     if (not f_name[0].isalpha() or not l_name[0].isalpha()):
#         return 'Your name must start with a letter from A - Z.'
#     return FIRST_NAME.get(f_name[0].upper()) + " " + SURNAME.get(l_name[0].upper())

# def alias(f_name,l_name):
#     if not f_name[0].isalpha() or not l_name[0].isalpha():
#         return 'your name must start with a letter from A -Z'
#     return FIRST_NAME.get(f_name[0].upper()) + " " + SURNAME.get(l_name[0].upper()) 
# print(alias('ucal','Beta'))      








# def alias_gen(f_name, l_name):
#     try:
#     	return FIRST_NAME[f_name.upper()[0]]+' '+SURNAME[l_name.upper()[0]]
#     except:
#     	return 'Your name must start with a letter from A - Z.'    

########################################################################
# def quarter_of(month):
#     year ={1: [1, 2, 3], 2: [4, 5, 6], 3: [7, 8, 9], 4: [10, 11, 12]}   
#     for k, v in year.items():
#         if month in v:
#             return k
## aylarin sirasini daxil ederek onun ilin hansi dorddebirine aid olduqunu tapan proqram

# def quarter_of(month):
#     year = {1:[1,2,3],2:[4,5,6],3:[7,8,9],4:[10,11,12]}
#     for key,value in year.items():
#         if month in value:
#             return key 










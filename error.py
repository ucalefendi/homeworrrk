
# # def count(num):    
# #     return num/(num -1)


# # print(count(10))


# bolunen = input()
# bolen = input()
# b = 15545

# try:
#      result = int(bolunen)/int(bolen)
# except ValueError :
#     print('yalniz eded daxil ola biler')
# except  ZeroDivisionError as xeta_mesaji: 
#     print(f'sifira bolmek olmaz daaaaaaaaaa xeta_mesaji : {xeta_mesaji}')
# except Exception : 
#     ('bilinmeyen bir xeta bas verdi' )   


from timeit import timeit


#              1
#           3     5
#        7     9    11
#    13    15    17    19
# 21    23    25    27    29
# Calculate the sum of the numbers in the nth row of this triangle (starting at index 1) e.g.: (Input --> Output)
def row_sum_odd_numbers(n):
    if type(n)==int and n>0:
        return n**3
    else:
        return "Input a positive integer"
duration = timeit('row_sum_odd_numbers(8)')  
print(duration)      

# print(row_sum_odd_numbers(3))        

# def row_sum_odd_numbers(n):
#     return sum(range(n*(n-1)+1, n*(n+1), 2))

# print(row_sum_odd_numbers(9999))    
# d = [160, 3, 1719, 19, 11, 13, -21]
# l = [2, 4, 0, 100, 4, 11, 2602, 36]
# def find_outlier(integers):
#     for el in integers:
#         if int(el)%2 == 0 and int(el) != 0:
#            if int(el)%2 !=0 and int(el) !=0 :
#             return el
        
                    

# print(find_outlier(l))
                          
    
# from timeit import timeit,repeat


# a = [1,2,3,4,5,6,7,8,9,10]

# comp = [i ** 2 for i in a]
# mapmet = map(lambda x: x**2,a)
# # print(comp,mapmet)

# zamanlama1 = timeit('[i ** 2 for i in a]','from __main__ import a',number = 100_000)
# zamanlama2 = timeit('map(lambda x: x**2,a)','from __main__ import a', number = 100_000)

# # print(zamanlama1,   zamanlama2)

# comp_result = repeat('[i ** 2 for i in a]','from __main__ import a',repeat= 5, number =10)
# print(comp_result)

# map_result = repeat('map(lambda x: x**2,a)','from __main__ import a',repeat=5,number = 100_0000000)
# print(map_result)

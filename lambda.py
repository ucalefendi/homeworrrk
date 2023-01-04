#HOMEWORK 15
#LESSON 1

#1)F = MA

# def get_force(m,a):
#     return m * a
# print(get_force(7,9))   

# get_force = lambda m,a : m * a
# print(get_force(7,8))

#2) a = v/t
# def acs(v,t):
#     return v/t
# print(acs(10,2))   

# acs = lambda v,t : v/t
# print(acs(10,2))

#4) s=at^2/2
# length = lambda a,t : (a * (t**2))/2
# print(length(2,2)) 

#5) E = m* g* h

# energy = lambda m,g,h : m * g * h
# print(energy(1,2,3))  

#6) v = s/t

# v = lambda s,t : s/t
# print(v(7,2))

#7) w = fs
# w = lambda f,s : f * s
# print(w(2,5))

# #8) T = 1/f
# T = lambda f : 1/f
# print(T(1))

#9)Ek = mv2/2

# e = lambda m,v : m * (v**2)/2
# # print(e(2,2))

# #10 p = f/s
# p =lambda f,s : f/s

# #11 v = s/t

# v = lambda s,t : s/t
 

physic = {
    'F': lambda m,a : m * a,
    'a': lambda v,t : v / t,
    'S': lambda a,t : (a*(t**2))/2,
    'E': lambda m,g,h : m * g * h,
    'v':lambda s,t : s/t,
    'w': lambda f,s : f * s,
    'T': lambda f   : 1/f,
    'Ek':lambda m,v : m * (v**2)/2,
    'P' :lambda F,S : F/S,
    'V' :lambda s,t : s/t 

}

print(physic.get('Ek')(0,0))
print(physic.get('a')(10,2))
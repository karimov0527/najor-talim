# def qanaqadir_funksiya(func,arg):
#     return func(arg)

# print(qanaqadir_funksiya(lambda a:a**2,5))



# numbers = [1,2,3,4,5,6]
# even_number = map(lambda x:x if x % 2 == 0 else 0, numbers)
# print((list(set(even_number))[1:]))
from functools import reduce
# # numbers = [1,2,3,4,5,6]
# # print(list(filter(lambda x : x%2 == 0, numbers)))
# # Maksimalni topish
# numbers = [1,2,3,4,5,6]
# # 1-uslub (Choynaklar uslubi)

# max = numbers[0]
# for i in numbers:
#     if max < i:
#         max = i

# # 2-pro lar uslubi

# print(reduce(lambda a,b: a if a> b else b, numbers))



# numbers = [1,6,6,4,3,7,7,6,10,9,5]
# def double(a,b):
    
#     if a == b :
#         print(a,'soni yonma yon turibdi ',numbers.index(a), 'va', numbers.index(b) + 1,'pzitsiyalarda')
#         return a
#     else:
#         return b
   
    



# reduce(double,numbers)




class Vektor:
    def __init__(self,x,y):
        self.x = x
        self.y = y

    def __str__(self):
        return f'({self.x},{self.y})'

    def __add__(self,other):
        x = self.x + other.x
        y = self.y + other.y
        return Vektor(x,y)
    def __sub__(self,other):
        x = self.x - other.x
        y = self.y - other.y
        return Vektor(x,y)
    def __mul__(self,other):
        x = self.x * other.x
        y = self.y * other.y
        return Vektor(x,y)
    # def __add__(self,other):
    #     x = self.x + other.x
    #     y = self.y + other.y
    #     return Vektor(x,y)
    
        
v1 = Vektor(10,8)
v2 = Vektor(5,3)
v3 = v1 + v2
v4 = v1 - v2
v5 = v1 * v2

print(v3)
print(v4)
print(v5)


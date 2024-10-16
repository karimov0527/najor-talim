# class Dasturchi:
#     job = "Google"
#     block = "A2"
#     floor = 3

# user1 = Dasturchi()
# user2 = Dasturchi()

# user1.name = "Alex"
# user1.age = 30

# user2.name = "Mary"
# user2.age = 27

# print(user1.name)

# -------------------------------------------------------------

# class Dasturchi:

#     def __init__(self,name,age):
#         self.job = "Google"
#         self.block = "A2"
#         self.floor = 3
#         self.name = name
#         self.age = age

# user1 = Dasturchi(name="Alex",age=27)
# user2 = Dasturchi(name="Mary",age=22)

# print(user1.__dict__)
# print(user2.__dict__)







# ----------------------------------

# class Dasturchi:

#     def __init__(self,name,age):
#         self.job = "Google"
#         self.block = "A2"
#         self.floor = 3
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return self.name
    

#     def code(self):
#         print(f"{self.name} kod yozmoqda ... va u {self.age} yoshda ... {self.job} kompaniyada ishlaydi")



# user1 = Dasturchi(name="Alex",age=27)
# user2 = Dasturchi(name="Mary",age=22)


# user1.code()
# user2.code()
    

# ----------------------------------




# class Dasturchi:

#     def __init__(self,name,age):
#         self.job = "Google"
#         self.block = "A2"
#         self.floor = 3
#         self.name = name
#         self.age = age

#     def __str__(self) -> str:
#         return self.name
    

#     def code(self):
#         print(f"{self.name} kod yozmoqda ... va u {self.age} yoshda ... {self.job} kompaniyada ishlaydi")
#     def code_with_friend(self,other : 'Dasturchi'):
#         print(f"{self.name} do'sti {other.name} bilan kod yozmoqda ...")



# user1 = Dasturchi(name="Alex",age=27)
# user2 = Dasturchi(name="Mary",age=22)


# user1.code()
# user2.code()
    
# user1.code_with_friend(other=user2)

# -----------------------------------------------------------------------------


class Dasturchi:

    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def is_older(self,other : 'Dasturchi') -> bool:

        if self.age > other.age:
            return True
        else:
            return False
    
user1 = Dasturchi(name="Shohrux",age=20)
user2 = Dasturchi(name="Bobur",age=19)
user3 = Dasturchi(name="Abbos",age=21)

print(user1.is_older(other=user2))
print(user1.is_older(other=user3))



    

# class Animal:
#     owner = "Shohrux"
#     def make_sound(self):
#         pass

# class Dog(Animal):
#     def make_sound(self):
#         print("Meauw")

# class Cat(Animal):
#     def make_sound(self):
#         print("Vov")
    


# c = Cat()
# d = Dog()

# c.make_sound()
# d.make_sound()


from multipledispatch import dispatch

@dispatch(int,int,int)
def add(x,y,z):
    return x + y + z


@dispatch(str,str)
def add(x,y):
    return x + " " + y

print(add(1,2,3))
print("Assalomu","alaykum")





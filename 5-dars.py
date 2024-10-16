# def devesion_by_zero(func):
#     def inner(*args):
#         if args[1] == 0 :
#             return "ERROR"
#         else:
#             return args[0]/args[1]
#     return inner
        
# @devesion_by_zero
# def div(a,b):
#     print(a/b)


# print(div(5,0))
# print(div(5,2))


def ism_familiyani_tekshirish(func):
    def inner(**kwargs):
        if kwargs["familiya"] == None :
            return kwargs["ism"]
        else:
            return kwargs
    return inner
        
@ism_familiyani_tekshirish
def toliq_ism_yasash(ism,familiya=None):
    ...

print(toliq_ism_yasash(ism="shohrux",familiya="karimov"))
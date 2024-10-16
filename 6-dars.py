
# def bir_marta_chaqir(func):
#     chaqir = True
#     def inner():
#         nonlocal chaqir
#         if chaqir:
#             func()
#             chaqir = False
            
#         else:
#             print("Bu func oldin chairilgan")
#     return inner

        
# @bir_marta_chaqir
# def salom_ber():
#     print("SAlom")

# salom_ber()
# salom_ber()
# salom_ber()
# salom_ber()
        

        
# from time import localtime

# def vaqtni_tekshirish(func):
#     hours = localtime().tm_hour
#     def inner(*args):
#         nonlocal hours
#         if hours in range(args[0],args[1]+1):
#             func(*args)
#         else:
#             print("salom bermiman")
#     return inner
        

# @vaqtni_tekshirish
# def salom_ber(start,finish):
#     print("Assalomu alaykum")

# salom_ber(10,12)
# def login_required(login_url): # bu yerda 3 qatlamlik funksiya ishlatildi
#     def wrapper(func):
#         def inner(request, *args, **kwargs):
#             if request['is_authenticated']:
#                 func(request, *args, **kwargs)
#             else:
#                 print(f"Siz {login_url} ga yo'latirildingiz")

#         return inner

#     return wrapper

# @login_required(login_url='users/login')
# def home_page(requst):
#     print("uy sahifasiga chizib berildi")

# # users login sahifasini yuboradi
# home_page({'usersname': 'admin', 'is_authenticated': True})




users = [
    {
        'id': 1,
        'name': 'Anvar',
        'notifications_on': False,
    },
    {
        'id': 2,
        'name': 'Sanjar',
        'notifications_on': True,
    },
    {
        'id': 3,
        'name': 'Setora',
        'notifications_on': True,
    },
    {
        'id': 4,
        'name': 'Malika',
        'notifications_on': False,
    },
]

def login_required(login_url): # bu yerda 3 qatlamlik funksiya ishlatildi
    def wrapper(func):
        def inner(request, *args):
            if request['is_authenticated']:
                func(request, *args)
            else:
                print(f"Siz {login_url} ga yo'latirildingiz")

        return inner

    return wrapper


def notify(force):
    def wrapper(func):
        def inner(request,users):
            for user in user:
                if user["notifications_on"] == True:
                    print("Reklama junatildi ")
                else:
                    print("Reklama baribir emailga junatdik😁")



        return inner

    
    return wrapper

    



@login_required(login_url='login')
@notify(force = True)
def notify_users(request,users):
    ...


notify_users(request={"is_authenticated":True},users=users)











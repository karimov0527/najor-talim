# class Mavjudod:
#     def __init__(self,ism,yosh,manzil):
#         self.ism = ism
#         self.yosh = yosh
#         self.manzil = manzil
    
#     def nafas_olish(self):
#         print("nafas olish")
    
#     def oziqlanish(self):
#         print("oziqlanish")

# class Xitoylik(Mavjudod):
#     def __init__(self, ism, yosh, manzil,status):
#         super().__init__(ism, yosh, manzil)
#         self.status = status

#     def korshapalak_yeyish(self):
#         ...
    
# xitoylik = Xitoylik(ism="Bao Hao",yosh=23,manzil="SHamghai",status="orta")
# print(xitoylik.ism)




class Parkovka:
    def __init__(self,filial_nomi,narxi,sigimi) :
        self.filial_nomi = filial_nomi
        self.narxi = narxi
        self.sigimi = sigimi
        self.tushum = 0
        self.mashinalar = []

    def kirish(self,mashina:dict,vaqt:float | int):
        self.tushum += vaqt * self.narxi
        self.mashinalar.append(mashina)
        print(mashina["mashina_nomi"],"parkovkaga qoyildi")
    
    def chiqish(self,mashina_raqami:str):
        for mashina in self.mashinalar:
            if mashina["mashina_raqami"] == mashina_raqami:
                self.mashinalar.remove(mashina)
                print(mashina["mashina_nomi"],"chiqib ketti")
                break
    
    def mashinalarni_korish(self):
        if len(self.mashinalar) == 0:
            print(f"{self.filial_nomi} fililaliga hali bironta ham mashina kirmadi")
        elif len(self.mashinalar) == 1:
            print(f"HOzirda {self.filial_nomi} da faqatgina {self.mashinalar[0]['mashina_nomi']} parkovka qilingan")
        else:
            mashinalar_nomlaari = []
            for mashinalar in self.mashinalar:
                mashinalar_nomlaari.append(mashinalar["mashina_nomi"])

                text = f'{", ".join(mashinalar_nomlaari[:-1])} va {mashinalar_nomlaari[-1]}'
                print(f"Hozirda {self.filial_nomi} da quidagi mashinalar mavjud: {text}")

filial1 = Parkovka(filial_nomi="Chilonzor",narxi=10_000,sigimi=20)
filial1.mashinalarni_korish()


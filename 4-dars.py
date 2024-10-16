class Tefal:
    def __init__(self,capasity:float) :
        self.capasity = capasity
    
    def start(self):
        print("Tefal yondi")
        self.__start_to_boil()
        self.__boiling()
        self.__finish()
    
    def __start_to_boil(self):
        print("Suv qaynashni boshladi")
    def __boiling(self):
        print("Suv qaynamoqda")
    def __finish(self):
        print("Suv qaynadi")
    

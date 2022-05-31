
class InformalAnimalInterface:

    def walk(self, steps: int):
        "Animal Walks in n steps"
        pass

    def mate(self, partner):
        "Animal mates with Partner"
        pass

class Dog(InformalAnimalInterface):

    def walk(self, steps):
        print("I walked")
    
    def mate(self, partner):
        print("I am mating")



print(issubclass(Dog, InformalAnimalInterface))
print(Dog.__mro__)
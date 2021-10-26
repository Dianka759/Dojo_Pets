class Ninja:

# implement __init__( first_name , last_name , pet , treats , pet_food )
    def __init__(self, first_name, last_name, pet, treats, pet_food): 
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.treats = treats
        self.pet_food = pet_food


# walk() - walks the ninja's pet invoking the pet play() method
    def walk(self):
        print(f"{self.first_name} is walking {self.pet.name}.")
        self.pet.play()
        return self

# feed() - feeds the ninja's pet invoking the pet eat() method
    def feed(self):
        print(f"{self.first_name} is feeding {self.pet.name}: {self.treats}.")
        self.pet.eat()
        return self
        
# bathe() - cleans the ninja's pet invoking the pet noise() method
    def bathe(self):
        print(f"{self.first_name} is bathing {self.pet.name}.")
        self.pet.noise()
        return self
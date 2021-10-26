class Pet:
# implement __init__( name , type , tricks ):
    def __init__(self, name, type, tricks):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = 0
        self.energy = 0

# implement the following methods:
# sleep() - increases the pets energy by 25
    def sleep(self):
        self.energy += 25
        print(f"{self.name} was bathed. Health: {self.health}, Energy: {self.energy}")
        return self

# eat() - increases the pet's energy by 5 & health by 10
    def eat(self):
        self.energy += 5
        self.health += 10
        print(f"{self.name} was fed. Health: {self.health}, Energy: {self.energy}")
        return self

# play() - increases the pet's health by 5
    def play(self):
        self.health += 5
        print(f"{self.name} was played with.  Health: {self.health}, Energy: {self.energy}")
        return self

# noise() - prints out the pet's sound
    def noise(self):
        if self.type == "green chicken":
            print("Meow Meow (yes, my parrot meows)")
        else: 
            print("...skrt skrt?")
        return self

    def pet_info(self):
        print(f"{self.name} is a {self.type}, that can {self.tricks}.")
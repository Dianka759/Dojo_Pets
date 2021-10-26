from Ninja import Ninja
from Pet import Pet

kiwi = Pet("Kiwi", "green chicken", "meow and whistle")
diana = Ninja("Diana", "Krawczyk", kiwi, "fruits & veggies", "Parrot Food")

diana.feed().walk().bathe()
kiwi.pet_info()

print()

szczurcia = Pet("Szczurcia", "rat", "parkour around the cage")
diana = Ninja("Diana", "Krawczyk", szczurcia, "candied sunflower seeds", "Rodent Food")

diana.feed().walk().bathe()
szczurcia.pet_info()

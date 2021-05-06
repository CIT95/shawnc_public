class Character():
    def __init__(self, name, HP):
        self.name = name
        self.HP = HP
        #self.attack = attack
        #self.defense = defense 

    def hitPoints(self):
        print(f"{self.name} has {self.HP} hit points")
  

class Human(Character): 
    def __init__(self, name, HP, charclass):
        super().__init__(name, HP)
        self.charclass = charclass

    def char(self):
        print(f"{self.name} is a {self.charclass} with {self.HP} hit points")

class Elf(Character):
    def __init__(self, name, HP, sp_attack):
        super().__init__(name, HP,)
        self.sp_attack = sp_attack
    
    def shoot(self):
        print(f"{self.name} is a stinky Elf with {self.HP} hit points")
        print(f"his special attack is {self.sp_attack}")


c = Character("Zoltar", 95)
c.hitPoints()
h = Human("tim", 77, "enchanter")
h.char()
h.hitPoints()
e = Elf("turdonius", 88, "fury of arrows")
e.shoot()
e.hitPoints()





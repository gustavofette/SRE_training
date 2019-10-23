class hero:
    def __init__(self, health, power):
        self.health = health
        self.power = power

    def attack(self, victim):
        victim.health -= self.power   

class goblin:
    def __init__(self, health, power):
        self.health = health
        self.power = power
        
    def attack(self, victim):
        victim.health -= self.power

hero1 = hero(10, 5)
goblin1 = goblin(6, 2)  
print (goblin1.health)
hero1.attack(goblin1)
print(goblin1.health)
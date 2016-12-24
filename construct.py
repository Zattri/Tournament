import math, random

class Fighter:

    def __init__(self, givenName, statPoints):
            self.name = str(givenName)
            self.hp = -1
            self.atk = 0
            self.str = 0
            self.defc = 0
            self.spd = 0
            self.agi = 0
            self.alive = True
            self.points = int(statPoints)

#==============================================================================
# Fetch Commands

    def getName(self):
        return str(self.name)

    def getHP(self):
        return int(self.hp)

    def getAtk(self):
        return int(self.atk)

    def getStr(self):
        return int(self.str)

    def getDef(self):
        return int(self.defc)

    def getSpd(self):
        return int(self.spd)

    def getAgi(self):
        return int(self.agi)

    def getAlive(self):
        return self.alive

#==============================================================================
# Set Commands

    def setAll(self, health, atk, strn, defc, spd, agi):
        self.health = health
        self.hp = health
        self.atk = atk
        self.str = strn
        self.defc = defc
        self.spd = spd
        self.agi = agi

    def setHealth(self, value):
        self.health = value

    def setHP(self, value):
        self.hp = value

    def setAtk(self, value):
        self.atk = value

    def setStr(self, value):
        self.str = value

    def setDef(self, value):
        self.defc = value

    def setSpd(self, value):
        self.spd = value

    def setAgi(self, value):
        self.agi = value

    def setAlive(self, value):
        if int(value) == 1:
            self.alive = True
        else:
            self.alive = False

#==============================================================================
#Print Commands

    def printStats(self):
        # Finish later
        print(self.name, "\nHP:", self.hp, "Def: ", self.defc, "\nAtk:", self.atk, "Str:", self.str, "Spd:", self.spd, "Agi:", self.agi)

    def printDodge(self):
        print(self.name, "dodged the attack!")

    def printDeath(self):
        print(self.name, "has fallen in battle!")

#==============================================================================
#Game Commands

    # Updates the living condition if the fighter is dead
    def updateAlive(self):
        if self.hp <= 0:
            self.alive = False
            self.printDeath()

    # Take HP damage from attack input and armour value
    def takeDamage(self, attack, armour):
        damage = int(attack) - int(armour)
        self.hp -= damage
        print(self.name, "took ", damage, "damage.")

    # Calculate the damage to be dealt
    def calcDamage(self):
        damage = self.getAtk() + self.getStr()
        return damage

    # Calculate the armour to use for resisting damage
    def calcArmour(self):
        armour = math.floor(self.defc / 2)
        return armour

    def calcInit(self):
        init = random.randint(0, 5) + self.spd
        return init

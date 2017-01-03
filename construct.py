import math, random

firstNames = ["Adam", "Geoffrey", "Gilbert", "Henry", "Hugh", "John", "Nicholas",
 "Peter", "Ralf", "Richard", "Robert", "Roger", "Simon", "Thomas", "Walter", "William"]
lastNames = ["Abbot", "Adams", "Barret", "Black", "Britton"]

class Fighter:

    def __init__(self, skillLevel, statPoints):
            self.name = str(firstNames[random.randint(0, len(firstNames) - 1)] + " "
            + lastNames[random.randint(0, len(lastNames) - 1)])
            self.health = 1
            self.hp = 1
            self.atk = 0
            self.str = 0
            self.defc = 0
            self.spd = 0
            self.agi = 0
            self.pos = None
            self.alive = True
            self.statPoints = int(statPoints)
            self.level = int(skillLevel)

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

    def getPos(self):
        return int(self.pos)

    def getAlive(self):
        return self.alive

#==============================================================================
# Set Commands

    def setAll(self, health, atk, strn, defc, spd, agi):
        self.health = health
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

    def setPos(self, value):
        self.pos = value

    def resetHP(self):
        self.hp = (self.health * 5)

#==============================================================================
#Print Commands

    def printStats(self):
        # Finish later
        print(self.name, "\nHP:", self.hp, "Def: ", self.defc, "\nAtk:",
         self.atk, "Str:", self.str, "Spd:", self.spd, "Agi:", self.agi, "\n")

    def printDodge(self):
        print(self.name, "dodged the attack!\n")

    def printDeath(self):
        print(self.name, "has fallen in battle!\n")

#==============================================================================
#Game Commands
#==============================================================================

    # Randomly generates stats based off of skill points and level
    def genStats(self):
        self.health =+ self.level
        self.atk =+ self.level
        self.str =+ self.level
        self.defc =+ self.level
        self.agi =+ self.level
        self.spd =+ self.level

        for i in range(0, self.statPoints):
            chosenStat = random.randint(0,5)

            if (chosenStat == 0):
                self.health += 1

            elif (chosenStat == 1):
                self.atk += 1

            elif (chosenStat == 2):
                self.str += 1

            elif (chosenStat == 3):
                self.defc += 1

            elif (chosenStat == 4):
                self.agi += 1

            elif (chosenStat == 5):
                self.spd += 1

        self.resetHP()

    # Updates the living condition if the fighter is dead
    def updateAlive(self):
        if self.hp <= 0:
            self.alive = False
            self.printDeath()

    # Take HP damage from attack input and armour value
    def takeDamage(self, attack, armour):
        damage = int(attack) - int(armour)
        self.hp -= damage
        print(self.name, "took", damage, "damage.\n")

    # Calculate the damage to be dealt
    def calcDamage(self):
        damage = self.getAtk() + random.randint(0, self.getStr())
        return damage

    # Calculate the armour to use for resisting damage
    def calcArmour(self):
        armour = math.floor(self.defc / 2)
        return armour

    def calcDodge(self):
        dodged = False
        targetInt = random.randint(0, 100)
        if targetInt < self.agi:
            dodged = True
            self.printDodge()
        return dodged

    def calcInit(self):
        init = random.randint(0, 5) + self.spd
        return init

    def joinArena(self, arena):
        arena.append(self)
        self.setPos(len(arena) - 1)

    def killFighter(self, arena):
        deadPos = self.getPos()
        arena.remove(self)
        for i in range(deadPos, len(arena)):
            fighter = arena[i]
            currPos = fighter.getPos()
            fighter.setPos(currPos - 1)

#==============================================================================
# Master commands

def takeHit(target, atker, arena):
    print(atker.getName(), "attacks", target.getName())
    if (target.calcDodge() == False):
        target.takeDamage(atker.calcDamage(), target.calcArmour())
        target.updateAlive()
        if target.getAlive() == False:
            target.killFighter(arena)

def findTarget(arena, pos):
    while True:
        target = random.randint(0, (len(arena) - 1))
        if target != pos:
            targetPos = target
            break
    return targetPos

#==============================================================================

class Fighter:

    def __init__(self, givenName, statPoints):
            self.name = str(givenName)
            self.hp = -1
            self.atk = 0
            self.defc = 0
            self.spd = 0
            self.agi = 0
            self.alive = True
            self.points = int(statPoints)

#==============================================================================
# Fetch Commands

    def getName():
        return self.name

    def getHP():
        return self.hp

    def getAtk():
        return self.atk

    def getDef():
        return self.defc

    def getSpd():
        return self.spd

    def getAgi():
        return self.agi

    def getAlive():
        return self.alive

#==============================================================================

#Print Commands
    def printStats():
        # Finish later
        print(self.name, "finish adding stats")

#==============================================================================

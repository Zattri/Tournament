import construct

dave = construct.Fighter("Dave", 10)
dave.genStats()
dave.resetStats()

bob = construct.Fighter("Bob", 10)
bob.genStats()
bob.resetStats()

phil = construct.Fighter("Phil", 10)
phil.genStats()
phil.resetStats()

# Gameloop
arena = []
dave.joinArena(arena)
bob.joinArena(arena)
phil.joinArena(arena)

battle = True
for fighter in arena:
    fighter.printStats()
print("Fight begins!\n")
while battle == True:
    if (len(arena) > 1):
        for fighter in arena:
            target = construct.findTarget(arena, fighter.getPos())
            # Target testing
            #print("Position", fighter.getPos())
            #print("Target:",target)
            construct.takeHit(arena[target], fighter, arena)
    else:
        break
print("A winner has been crowned -", arena[0].getName())

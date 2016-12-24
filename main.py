import construct

dave = construct.Fighter("Dave", 10)
dave.setAll(10, 3, 6, 5, 4, 5)

bob = construct.Fighter("Bob", 10)
bob.setAll(10, 4, 5, 3, 4, 5)

phil = construct.Fighter("Phil", 10)
phil.setAll(10, 5, 3, 4, 6, 5)

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

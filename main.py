import construct

dave = construct.Fighter("Dave", 10)
dave.setAll(10, 3, 6, 5, 4, 2)

bob = construct.Fighter("Bob", 10)
bob.setAll(10, 4, 5, 3, 4, 1)

# Gameloop
arena = []
arena.append(dave)
arena.append(bob)

battle = True
p1 = arena[0]
p2 = arena[-1]
# Fight loop
while battle == True:
    if p1.getAlive() == True and p2.getAlive() == True:
        p1.printStats()
        p2.printStats()
        if (p1.calcInit() >= p2.calcInit()):
            p2.takeDamage(p1.calcDamage(), p2.calcArmour())
            p2.updateAlive()
            if p2.getAlive() == False:
                p1.takeDamage(p2.calcDamage(), p1.calcArmour())
        else:
            p1.takeDamage(p2.calcDamage(), p1.calcArmour())
            if p1.getAlive() == False:
                p2.takeDamage(p1.calcDamage(), p2.calcArmour())
    else:
        break
print("A winner has been crowned")

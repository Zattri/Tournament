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
p1.printStats()
p2.printStats()
print("Fight begins!\n")
while battle == True:
    if p1.getAlive() == True and p2.getAlive() == True:
        if (p1.calcInit() >= p2.calcInit()):
            construct.takeHit(p2, p1)
            if p2.getAlive() == True:
                construct.takeHit(p1, p2)
        else:
            construct.takeHit(p1, p2)
            if p1.getAlive() == True:
                construct.takeHit(p2, p1)
    else:
        break
print("A winner has been crowned")

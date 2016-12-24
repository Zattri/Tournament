import construct

# Tournament AI game

# Construct Class -
# Make the AI Class
#   Name?
#   HP
#   Attack
#   Defence
#   Speed ?
#   Agility?
#   Crit?
#   Alive state
#   Winner?

# Functions -
#   Get Stats
#   Get Alive
#   Deal damage
#   Get turn order?

# Stats setup -
# Ability points given on generation
# Spend ability points randomly?
# Possibly base values then add / subtract some random values

# Tournament setup -
#   1v1 fights?
#   Multi-player fights?
#   Each attack hits a target
#   Target takes damage based off of attack - def etc etc

dave = construct.Fighter("Dave", 10)
dave.setAll(10, 3, 6, 5, 4, 2)
dave.printStats()

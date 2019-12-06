with open('day1inputs.txt', 'r') as file:
    masses = file.read().splitlines()
totalMass=0
# for mass in masses: totalMass += int(mass) // 3 - 2 #first one
for mass in masses:
    while int(mass) > 0:
        mass = int(mass) // 3 - 2
        if mass > 0: totalMass += mass
print(totalMass)
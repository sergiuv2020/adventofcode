with open('day1inputs.txt', 'r') as file:
    masses = file.read().splitlines()
totalMass=0
for mass in masses: totalMass += int(mass) // 3 - 2
print(totalMass)
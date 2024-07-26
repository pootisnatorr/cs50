mass = input('Enter the mass of the object (in kg): ')
light = 300000000


# Calculate the energy of the object in Joules
lightSquared = light * light
energy = int(mass) * lightSquared
print('Energy: ' + str(energy))
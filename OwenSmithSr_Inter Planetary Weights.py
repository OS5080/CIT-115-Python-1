# Inter Planetary Weights Project
# By: Owen Smith
#Planet Named Constants

nMercury = 0.38
nVenus = 0.91
nMoon = 0.165
nMars = 0.38
nJupiter = 2.34
nSaturn = 0.93
nUranus = 0.92
nNeptune = 1.12
nPluto = 0.066

#1. User Inputs

sName = input("What is your name: ")
sWeight = input("What is your weight: ")

#2. Float Convert:

fWeight = float(sWeight)

# 3. Covert Planet Weight

fMercury = fWeight * nMercury
fVenus = fWeight * nVenus
fMoon = fWeight * nMoon
fJupiter = fWeight * nJupiter
fSaturn = fWeight * nSaturn
fUranus = fWeight * nUranus
fNeptune = fWeight * nNeptune
fPluto = fWeight * nPluto

# 4. Print Outputs: Used string concatenations

print( "\n" + sName, "here are your weights on our Solar System's planets: ")
print('{:20}'.format("Weight on Mercury: ") + format(fMercury,'10.2f'))
print('{:20}'.format("Weight on Venus: ") + format(fVenus,'10.2f'))
print('{:20}'.format("Weight on Moon: ") + format(fMoon,'10.2f'))
print('{:20}'.format("Weight on Jupiter: ") + format(fJupiter,'10.2f'))
print('{:20}'.format("Weight on Saturn: ") + format(fSaturn,'10.2f'))
print('{:20}'.format("Weight on Uranus: ") + format(fUranus,'10.2f'))
print('{:20}'.format("Weight on Neptune: ") + format(fNeptune,'10.2f'))
print('{:20}'.format("Weight on Pluto: ") + format(fPluto,'10.2f'))

      

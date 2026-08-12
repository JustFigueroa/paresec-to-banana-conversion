import math

class Planet:
    PlanetName: str
    PlanetDistanceParsecs: float
    PlanetDistanceBanana: float

def format(num: float):
    numString = str(num)
    numList = list(numString)
    numOfCommas = math.ceil(len(numString) / 3)
    digits = len(numString)

    for i in range(numOfCommas):
        if (i == 0):
           continue
        else:
            numList.insert(len(numString) - (i*3), ",")
    for i in range(digits):
        newString = "".join(numList)
    return newString

parsecInches = 1214834000000000000
tempPlanet = Planet
tempPlanet.PlanetName = "Gooba"
tempPlanet.PlanetDistanceParsecs = 1
tempPlanet. PlanetDistanceBanana = parsecInches * tempPlanet.PlanetDistanceParsecs
format(parsecInches)
print(f"Distance to {tempPlanet.PlanetName} in Parsecs: {tempPlanet.PlanetDistanceParsecs}")
print(f"DIstance to {tempPlanet.PlanetName} in bananas: {format(tempPlanet.PlanetDistanceBanana)}")
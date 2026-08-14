import math
import QueryBuilder
import QuerySender
import Planet
import json


#This fucntion formats banana distance to create a readable banana distance. 
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

queryString = QueryBuilder.buildQuery()
data = QuerySender.sendRequest(queryString)
planets = [Planet.Planet(item["pl_name"], item ["hostname"], item ["sy_dist"] ) for item in data]
parsecInches = 1214834000000000000

for planet in planets:
    print(f"Planet Name: {planet.PlanetName}") 
    print(f"\tHost Star: {planet.HostStar}")
    if (planet.PlanetDistanceParsecs == None):
        print(f"\tDistance Parsecs: Unknown")
        print(f"\tDistance Banana: Unknown")
        print("")
    else: 
        print(f"\tDistance Parsecs: {planet.PlanetDistanceParsecs}")
        planet.PlanetDistanceBanana = "{:.0f}".format((parsecInches * planet.PlanetDistanceParsecs) / 7.0)
        print(f"\tDistance Banana: {planet.PlanetDistanceBanana}")
        print("")
#Testing the planet class and format fucntion
#tempPlanet = Planet
#tempPlanet.PlanetName = "Gooba"
#tempPlanet.PlanetDistanceParsecs = 1
#tempPlanet.PlanetDistanceBanana = "{:.0f}".format((parsecInches * tempPlanet.PlanetDistanceParsecs) / 7.0)
#format(parsecInches)
#print(f"Distance to {tempPlanet.PlanetName} in Parsecs: {tempPlanet.PlanetDistanceParsecs}")
#print(f"DIstance to {tempPlanet.PlanetName} in bananas: {format(tempPlanet.PlanetDistanceBanana)}")

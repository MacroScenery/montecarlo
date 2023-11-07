# monte carlo page 124
# 5.10 page 150
import random # use random.random()

class Computer:
  def __init__(self, virus=False, wasInfected=False):
    self.virus = virus
    self.wasInfected = wasInfected
  
  def __str__(self):
        return "{" + str(self.virus) + ", " + str(self.wasInfected) + "}"


def printNetwork(network, headerText=""):
    print(headerText)
    print("--------------")
    print("Index\t| Virus\t| Was Infected")
    print("--------------")
    for i in range(len(network)):
        print(str(i)+ "\t| " + str(network[i].virus) + "\t| " + str(network[i].wasInfected))

    print("--------------\n")
    return


def repairNetwork(network, numberOfRepairs):
 
    infectedComputers = [computer for computer in network if computer.virus]
    
    while (numberOfRepairs > 0  and len(infectedComputers) > 0):
        index = int(random.random() * len(infectedComputers))
        infectedComputers[index].virus = False
        infectedComputers.pop(index)
        numberOfRepairs -= 1

    return network

def nextStateVirus(network, p):
    infectedComputers = [computer for computer in network if computer.virus]
    noninfectedComputers = [computer for computer in network if not computer.virus]

    for virus in infectedComputers:
        for i in range(len(noninfectedComputers)):
            if random.random() < p:
                noninfectedComputers[i].virus = True
                if (noninfectedComputers[i].wasInfected == False):
                    noninfectedComputers[i].wasInfected = True




    newNetwork = infectedComputers + noninfectedComputers

    return newNetwork


# Runs through one state of network and returns new network
# Takes in a network array of booleans, proability of virus p
def nextState(network, p, numberOfRepairs):
    network = nextStateVirus(network, p)
    #printNetwork(network, headerText="Post-Virus")
    network = repairNetwork(network, numberOfRepairs)
    #printNetwork(network, headerText="Post-Repair")
    return network

def simulation(networkSize=20, p=0.1, numberOfRepairs=5):
    network = [Computer() for _ in range(networkSize)]
    network[ int(random.random() * networkSize) ] = Computer(True, True) # create network and make one random computer infected
    numberOfInfected = 1

    dayCounter = 0

    while (numberOfInfected > 0):
        #print("Day:" + str(dayCounter))
        numberOfInfected = 0
        network = nextState(network, p, numberOfRepairs)
        for computer in network:
            if computer.virus == True:
                numberOfInfected += 1
        
        dayCounter += 1
        

    return (network, dayCounter)

def monteCarlo(n, networkSize=20, p=0.1, numberOfRepairs=5):

    avgNumberOfDaysTillClean = 0.0
    probabilityInfectOnce = 0.0
    expectedComputersInfected = 0.0

    for i in range(n):
        print("Running simulation " + str(i+1))
        postNetwork, days = simulation(networkSize, p, numberOfRepairs)

        print("Calculating stats " + str(i+1))
        avgNumberOfDaysTillClean += days
        
        for computer in postNetwork:
            if computer.wasInfected == True:
                probabilityInfectOnce += 1

    
    avgNumberOfDaysTillClean /= float(n)

    probabilityInfectOnce /= float(networkSize * n)

    print(avgNumberOfDaysTillClean)
    print(probabilityInfectOnce)




def main():
    monteCarlo(1000)
    
    # network = [Computer() for _ in range(20)]
    # network[ int(random.random() * 20) ] = Computer(True, True) # create network and make one random computer infected
    # printNetwork(network, "Pre-Virus")
    # network = nextStateVirus(network, 0.5)
    # printNetwork(network, "Post-Virus")
    # n = 0
    # for computer in network:
    #     if computer.virus == True:
    #         n+=1
    # print(n)

    # network = repairNetwork(network, 5)
    # printNetwork(network, "Post-Repair")
    # n = 0
    # for computer in network:
    #     if computer.virus == True:
    #         n+=1
    # print(n)




if __name__ == "__main__":
    main()
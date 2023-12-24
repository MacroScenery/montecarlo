# monte carlo page 124
# 5.10 page 150
import random # use random.random()

# Computer Object
# Virus stores if computer has virus or not
# Was infected stroes if computer has been infected ever
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
 
    # split into infected computers
    infectedComputers = [computer for computer in network if computer.virus]

    while (numberOfRepairs > 0  and len(infectedComputers) > 0):
        index = int(random.random() * len(infectedComputers)) # choose an infected computer randomly
        infectedComputers[index].virus = False # make it noninfected
        infectedComputers.pop(index) # remove it from the list
        numberOfRepairs -= 1

    return network

def nextStateVirus(network, p):
    # Split computers in to noninfected and infected computers
    infectedComputers = [computer for computer in network if computer.virus]
    noninfectedComputers = [computer for computer in network if not computer.virus]

    # For each virus
    for virus in infectedComputers:
        # Each virus has a chance of spreading to any of the noninfected computers
        for i in range(len(noninfectedComputers)):
            if random.random() < p: # if the random chance occurs
                # Set virus to be true
                noninfectedComputers[i].virus = True
                if (noninfectedComputers[i].wasInfected == False): # if first infection
                    noninfectedComputers[i].wasInfected = True # set was infected




    newNetwork = infectedComputers + noninfectedComputers

    return newNetwork


# Runs through one state of network and returns new network
# Takes in a network array of booleans, proability of virus p
def nextState(network, p, numberOfRepairs):
    network = nextStateVirus(network, p) # Virus infections
    network = repairNetwork(network, numberOfRepairs) # Computer Repairs
    return network

def simulation(networkSize=20, p=0.1, numberOfRepairs=5):
    network = [Computer() for _ in range(networkSize)]
    network[ int(random.random() * networkSize) ] = Computer(True, True) # create network and make one random computer infected
    numberOfInfected = 1

    dayCounter = 0

    while (numberOfInfected > 0): # while there are still viruses
        #print("Day:" + str(dayCounter))
        numberOfInfected = 0
        network = nextState(network, p, numberOfRepairs) # run the states
        for computer in network:
            if computer.virus == True:
                numberOfInfected += 1 # check how many computers are infected
        
        dayCounter += 1
        

    return (network, dayCounter)

def monteCarlo(n, networkSize=20, p=0.1, numberOfRepairs=5):

    avgNumberOfDaysTillClean = 0.0 # Part A
    infectedAtLeastOnce = 0.0 # Part B
    meanInfect = 0.0 # Part C

    for i in range(n):
        print("Running simulation " + str(i+1))
        postNetwork, days = simulation(networkSize, p, numberOfRepairs) # run a simultaion, return network and number of days it takes
        print("Calculating stats " + str(i+1))
        avgNumberOfDaysTillClean += days

        counter = 0 # number of computers infected this simulation
        for computer in postNetwork:
            if computer.wasInfected == True:
                meanInfect += 1 # add to stat C
                
                counter += 1

        if (counter == networkSize): # if all computers have been infected
            infectedAtLeastOnce += 1


    
    avgNumberOfDaysTillClean /= float(n)
    infectedAtLeastOnce /= float(n)
    meanInfect /= float(n)

    # X = # of computers vistied by virus
    # Y = # of days to clean virus from network

    # Part A Average number of days till virus is gone
        # Part A -> E(Y)
    print("Mean number of days till virus is gone: " + str(avgNumberOfDaysTillClean))
    # Part B all computers must have been infected (at least one time)
        # Part B -> P{X=20}
    print("Proability of times each computer was infected at least once " + "{0:.4f}".format(infectedAtLeastOnce))
    # Part C is just number that get infected at least in general
        # Part C -> E(X)
    print("Mean number of computers infected " + str(meanInfect))




def main():
    while (True):
        print("Welcome to Monte Carlo Simulator")
        print("Opts:")
        print("1. Run Defualt Simulation (network = 20, p = 0.1, repairs = 5)")
        print("2. Run Custom Simulation")

        strInput = input()
        if (strInput=="1"):
            n = int(input("Number of trials: "))
            monteCarlo(n)
            break
        elif (strInput=="2"):
            networkSize = int(input("Number Of Computers: "))
            p = float(input("Proability of Virus spreading: "))
            repairs = int(input("Number of repairs made: "))
            n = int(input("Number of trials: "))
            monteCarlo(n=n, networkSize=networkSize, p=p, numberOfRepairs=repairs)
            break




if __name__ == "__main__":
    main()
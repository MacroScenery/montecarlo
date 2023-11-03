# monte carlo page 124
# 5.10 page 150
import random # use random.random()

class Computer:
  virus = False
  wasInfected = False
  
  def __init__(self, virus=False, wasInfected=False):
    self.virus = virus
    self.wasInfected = wasInfected
  
  def __str__(self):
        return "{" + str(self.virus) + ", " + str(self.wasInfected) + "}"


## TODO: Rewrite this function by getting indexs of infected pcs and choosing from that group
def repairNetwork(network, numberOfRepairs):
    if (len(network) <= numberOfRepairs):
        for computer in network:
            computer.virus = False
        return network
    
    numberOfInfected = 0
    for computer in network:
        if (computer.virus == True):
            numberOfInfected += 1
    
    while (numberOfRepairs > 0 and numberOfInfected > 0): # run repairs until number over or until no infected left
        choosen = int(random.random() * len(network)) # choose a random computer
        if (network[choosen].virus == True):
            network[choosen].virus = False
            numberOfInfected -= 1
            numberOfRepairs -= 1
    
    return network

def nextStateVirus(network, p):
    changeLog = [False] * len(network) # creates a lists of false values that is len(network)
    # false means value has not been changed this state
    # true means value has been changed

    # loop thorugh each computer
    for i in range(len(network)):
        # find an infected computer
        # check if the value was changed during this loop
        if ((network[i].virus == True) and (changeLog[i] != True)):
            
            for j in range(0, i):
                # move array backwards
                if (random.random() <= p): # if virus works
                    network[j].virus = True
                    if (network[j].wasInfected == False):
                        network[j].wasInfected = True
            
            for k in range(i+1, len(network)):
                # mov array forwards
                if (random.random() <= p): # if virus works
                    network[k].virus = True  
                    if (network[k].wasInfected == False):
                        network[k].wasInfected = True       

    return network

# Runs through one state of network and returns new network
# Takes in a network array of booleans, proability of virus p
def nextState(network, p, numberOfRepairs):
    network = nextStateVirus(network, p)
    network = repairNetwork(network, numberOfRepairs)
    return network

def simulation(networkSize=20, p=0.1, numberOfRepairs=5):
    network = [Computer()] * networkSize
    network[ int(random.random() * networkSize) ] = Computer(True, True) # create network and make one random computer infected
    numberOfInfected = 1

    while (numberOfInfected > 0):
        numberOfInfected = 0
        network = nextState(network, p, numberOfRepairs)
        for computer in network:
            print(computer)
            if computer.virus == True:
                numberOfInfected += 1
        




    return


def main():
    simulation(10)



if __name__ == "__main__":
    main()
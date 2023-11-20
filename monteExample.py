import random
import math

bdays = []

for i in range(4): 
    bdays.append(random.randint(1,365))

bdays.sort()

print(bdays)

diff = [
    min(bdays[1] - bdays[0], bdays[0] - bdays[1] + 365),
    min(bdays[2] - bdays[1], bdays[1] - bdays[2] + 365),
    min(bdays[3] - bdays[2], bdays[2] - bdays[3] + 365),
    min(bdays[0] - bdays[3], bdays[3] - bdays[0] + 365)
]   

minDiff = min(diff)

print(minDiff)

print(diff)


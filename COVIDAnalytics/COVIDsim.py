import matplotlib.pyplot as plt
from COVIDfunctions import *

#  Numbers of: Vulnerable + nonVulnerable = Number of population, Days before and after quarantine,
#  Interactions and their drop percentage during quarantine.
vul = 2000
nonV = 8000
NonQuarantineDays = 100
quarantineDays = 100
Interactions = 3000
InteractionsDropPrc = 0.7
#  Create population with Vulnerable and nonVulnerable instances.
pop = createPop(vul, nonV)
#  Before day 0, assign some people as patients for the spreading to commence.
startCOVID(pop, 20)
#  Start Simulation
d = beginSim(pop, NonQuarantineDays, Interactions, quarantineDays, InteractionsDropPrc)
print(d)
#  Create graph
plt.plot(d.keys(), d.values(), 'g')
plt.xlabel("Days passed since day 0")
plt.ylabel("Number of patients")
plt.title("Covid patients graph")
plt.text(NonQuarantineDays, d[NonQuarantineDays], "Quarantine starts")
plt.grid()
#  Insert a vertical line where quarantine starts.
plt.axvline(NonQuarantineDays)
#  Show Graph
plt.show()
#  ---End of Code---

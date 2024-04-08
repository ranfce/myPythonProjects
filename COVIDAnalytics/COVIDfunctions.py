from nonVulnerable import NonVulnerable
from Vulnerable import Vulnerable
import random as r


#  Takes the predetermined number of Vulnerable and nonVulnerable people and creates that many
#  instances of the Vulnerable and nonVulnerable classes. Then it randomly assigns
#  an appropriate age for each class and 1 kind of Disease or Address accordingly.
def createPop(vulN, nonVn):
    Humans = []
    sicknesses = ["High blood pressure", "Lung disease", "Diabetes"]

    for i in range(vulN):
        Humans.append(Vulnerable(r.randint(40, 110), sicknesses[r.randint(0, 2)]))

    for i in range(nonVn):
        Humans.append(NonVulnerable(r.randint(0, 110), "Addr" + str(r.randint(1, 200))))

    return Humans


#  Randomly "infects" a certain number of people, so that day 0 can commence.
def startCOVID(pop, startingPat):
    for i in range(startingPat):
        pop[r.randint(0, len(pop)-1)].isSick = True


#  2 people interacting have 20% chance of transmitting the virus.
def interact(h1, h2):
    if h1.isSick:
        if not h2.isSick:
            if r.randint(0, 100) < 20:
                h2.isSick = True
    if h2.isSick:
        if not h1.isSick:
            if r.randint(0, 100) < 20:
                h1.isSick = True


#  Each patient after 14 days is considered to be healthy again
#  but still possible to be once again infected.
def dayPassed(pop):
    for p in pop:
        if p.isSick:
            p.sickDay += 1
            if p.sickDay == 14:
                p.isSick = False
                p.sickDay = -1


#  Counts the number of patients in a day.
def getPatients(pop):
    cnt = 0
    for p in pop:
        if p.isSick:
            cnt += 1
    return cnt


#  Starts the whole simulation of spreading the virus between people for each day with specified interactions
#  per day. When days' number is reached, quarantine stats and the interactions are decreased.
#  In the end it returns a dictionary formatted as ***(int)Day's Number: (int)Patients***
def beginSim(pop, days, interPerDay, quarantine, InteractionsDropPrc):
    dictPatPerDay = {}
    for i in range(days):
        for j in range(interPerDay):
            num1 = r.randint(0, len(pop)-1)
            num2 = r.randint(0, len(pop)-1)
            while num1 == num2:
                num2 = r.randint(0, len(pop) - 1)
            interact(pop[num1], pop[num2])
        dayPassed(pop)
        NumP = getPatients(pop)
        dictPatPerDay[i] = NumP
        print("Day ", i, " ... number of patients:", NumP)

    print("Quarantine Begins")
    for i in range(quarantine):
        for j in range(int(interPerDay*InteractionsDropPrc)):
            num1 = r.randint(0, len(pop) - 1)
            num2 = r.randint(0, len(pop) - 1)
            while num1 == num2:
                num2 = r.randint(0, len(pop) - 1)
            interact(pop[num1], pop[num2])
        dayPassed(pop)
        NumP = getPatients(pop)
        dictPatPerDay[days + i] = NumP
        print("day ", days + i, " ... number of patients:", NumP)
    return dictPatPerDay


#  Debugging - Ignore
def printPop(p):
    for pop in p:
        pop.printInfo()
#  ---End of Code---

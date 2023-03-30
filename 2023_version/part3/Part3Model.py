from part2.Part2Model import getPassMarks, getDeferMarks, getFailMarks, getOutcomes


# Marks storing arrays ----------------------------------------------------
passMarks = getPassMarks()
deferMarks = getDeferMarks()
failMarks = getFailMarks()
outcome = getOutcomes()


# Sort marks -------------------------------------------------------------
def sortMarks():
    for i in range(len(outcome)):
        for x in range(len(outcome) - 1):
            if outcome[x] > outcome[x+1]:
                temp = outcome[x+1]
                outcome[x+1] = outcome[x]
                outcome[x] = temp

                temp = passMarks[x+1]
                passMarks[x+1] = passMarks[x]
                passMarks[x] = temp

                temp = deferMarks[x + 1]
                deferMarks[x + 1] = deferMarks[x]
                deferMarks[x] = temp

                temp = failMarks[x + 1]
                failMarks[x + 1] = failMarks[x]
                failMarks[x] = temp


# Print all outcomes into text file --------------------------------------
def printAllOutcomesToTextFile():
    sortMarks()
    dataFile = open("Part 3 text file.txt", "w")
    dataFile.write("Part 3: \n")
    count = 0

    for x in outcome:
        if x == 1:
            dataFile.write("\tProgress :- " + str(passMarks[count]) + ", " + str(deferMarks[count]) + ", " + str(failMarks[count]) + "\n")
        elif x == 2:
            dataFile.write("\tProgress (module trailer) :- " + str(passMarks[count]) + ", " + str(deferMarks[count]) + ", " + str(failMarks[count]) + "\n")
        elif x == 3:
            dataFile.write("\tModule retriever :- " + str(passMarks[count]) + ", " + str(deferMarks[count]) + ", " + str(failMarks[count]) + "\n")
        else:
            dataFile.write("\tExclude :- " + str(passMarks[count]) + ", " + str(deferMarks[count]) + ", " + str(failMarks[count]) + "\n")
        count += 1

    dataFile.close()
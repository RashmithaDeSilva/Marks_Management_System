from part1.MainModel import getPassMarks, getDeferMarks, getFailMarks, getOutcomes, spase


# Marks storing arrays ----------------------------------------------------
passMarks = getPassMarks()
deferMarks = getDeferMarks()
failMarks = getFailMarks()
outcome = getOutcomes()


# Print all outcomes with marks -------------------------------------------
def printAllOutcomes():
    print("Part 2 (List)")
    count = 0

    for x in outcome:
        if x == 1:
            print("\t%-26s :- " % "Progress", "%3d" % passMarks[count], ", %3d" % deferMarks[count], ", %3d" % failMarks[count])
        elif x == 2:
            print("\t%-26s :- " % "Progress (module trailer)", "%3d" % passMarks[count], ", %3d" % deferMarks[count], ", %3d" % failMarks[count])
        elif x == 3:
            print("\t%-26s :- " % "Module retriever", "%3d" % passMarks[count], ", %3d" % deferMarks[count], ", %3d" % failMarks[count])
        else:
            print("\t%-26s :- " % "Exclude", "%3d" % passMarks[count], ", %3d" % deferMarks[count], ", %3d" % failMarks[count])

        count += 1

    spase()
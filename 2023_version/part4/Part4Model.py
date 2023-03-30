from part1.MainModel import getUserInput, quitOrContinue, getOutcome, spase

# Get string ------------------------------------------------------------
def getString():
    return input()


# Get student number ----------------------------------------------------
def getStudentNumber():
    print("Enter student number :- ", end="")
    return getString()


# Data stor dictionary --------------------------------------------------
studentMarksDictionary = {}


# Main program ----------------------------------------------------------
def main():
    while True:
        loopBreak = True
        studentNumber = ""

        while loopBreak:
            studentNumber = getStudentNumber()
            for x in studentMarksDictionary.keys():
                if studentNumber.__eq__(x):
                    print("This student number already exist !\n")
                    loopBreak = True
                    break
                else:
                    loopBreak = False

            if len(studentMarksDictionary) == 0:
                loopBreak = False

        pMarks = getUserInput("Please enter your credits at pass: ")
        dMarks = getUserInput("Please enter your credits at defer: ")
        fMarks = getUserInput("Please enter your credits at fail: ")
        outcome = getOutcome(pMarks, fMarks)

        if outcome == 1:
            studentMarksDictionary.update({studentNumber : "Progress :- " + str(pMarks) + ", "+ str(dMarks) + ", " + str(fMarks)})
        elif outcome == 2:
            studentMarksDictionary.update({studentNumber: "Progress (module trailer) :- " + str(pMarks) + ", " + str(dMarks) + ", " + str(fMarks)})
        elif outcome == 2:
            studentMarksDictionary.update({studentNumber: "Do not Progress - module retriever :- " + str(pMarks) + ", " + str(dMarks) + ", " + str(fMarks)})
        else:
            studentMarksDictionary.update({studentNumber: "Exclude :- " + str(pMarks) + ", " + str(dMarks) + ", " + str(fMarks)})

        userAns = quitOrContinue()
        if userAns == -1:
            spase()
            print("\n", studentMarksDictionary)
            spase()
            break
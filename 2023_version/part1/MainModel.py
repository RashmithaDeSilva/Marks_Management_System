# Get integer value ------------------------------------------------------
def getIntegerInput():
    try:
        userInput = int(input())
        return userInput

    except ValueError:
        return -1


# Get inputs -------------------------------------------------------------
def getUserInput(inputName):
    while True:
        print(inputName, end="")
        userInput = getIntegerInput()

        if userInput == -1:
            print("Integer required !")
        elif userInput < 0 or userInput > 120:
            print("Out of range !")
        else:
            return userInput


# Get outcome ------------------------------------------------------------
def getOutcome(passMarks, failMarks):
    if passMarks == 120:
        print("Progress\n")
        return 1

    elif passMarks >= 100:
        print("Progress (module trailer)\n")
        return 2

    elif failMarks <= 79:
        print("Do not Progress - module retriever\n")
        return 3

    elif failMarks >= 80:
        print("Exclude\n")
        return 4


# Quit or Continue --------------------------------------------------------
def quitOrContinue():
    while True:
        print("Would you like to enter another set of data ?")
        userInput = input("Enter 'y' for yes or 'q' to quit and view results: ")
        if userInput.__eq__("Y") or userInput.__eq__("y"):
            return 0
        elif userInput.__eq__("Q") or userInput.__eq__("q"):
            return -1
        else:
            print("Invalid input !\n")


# Count outcome values ---------------------------------------------------
def countOutcomeValues(outCome, valueType):
    count = 0

    for x in outCome:
        if x == valueType:
            count += 1

    return count


# Print stars -------------------------------------------------------------
def printStars(outcomeName, starCount):
    print("\t%-10s %4d " % (outcomeName, starCount), end=" : ")
    for x in range(starCount):
        print("*", end=" ")
    print("")


# Spase -------------------------------------------------------------------
def spase():
    for x in range(100):
        print("-", end="")
    print("")


# Histogram ---------------------------------------------------------------
def histogram(outCome):
    progress = countOutcomeValues(outCome, 1)
    trailer = countOutcomeValues(outCome, 2)
    retriever = countOutcomeValues(outCome, 3)
    excluded = countOutcomeValues(outCome, 4)

    spase()
    print("\nHistogram")

    printStars("Progress", progress)
    printStars("Trailer", trailer)
    printStars("Retriever ", retriever)
    printStars("Excluded", excluded)

    print("\n", (progress + trailer + retriever + excluded), "outcomes in total")
    spase()


# Marks storing arrays ----------------------------------------------------
passMarks = []
deferMarks = []
failMarks = []
outCome = []


# Main program ------------------------------------------------------------
def main():
    while True:
        pMarks = getUserInput("Please enter your credits at pass: ")
        dMarks = getUserInput("Please enter your credits at defer: ")
        fMarks = getUserInput("Please enter your credits at fail: ")

        total = pMarks + dMarks + fMarks
        if total > 120 or total < 120:
            print("Total incorrect !\n")
        else:
            passMarks.append(pMarks)
            deferMarks.append(dMarks)
            failMarks.append(fMarks)
            outCome.append(getOutcome(pMarks, fMarks))

        if quitOrContinue() == -1:
            histogram(outCome)
            break


# Get marks --------------------------------------------------------------
def getPassMarks():
    return passMarks


def getDeferMarks():
    return deferMarks


def getFailMarks():
    return failMarks


def getOutcomes():
    return outCome
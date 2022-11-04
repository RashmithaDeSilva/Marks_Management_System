# 4COSC006C: Software Development I – Coursework specification (2021/22)
# Student ID: 20211546
# Date: 15/03/22

print("\tThe University Marks Program\n")
print("Enter 'USER NAME' To Your Name")
print("Enter 'Password' To '1234'" )

all_input_list = [[], [], [], [], [], [], [], []]
# ---------------[0],[1],[2],[3],[4],[5],[6],[7]-----------
#  0 = all pass,  1 = all defer,  2 = all fail,  3 = all program outputs,  4 = all progress,  5 = all module trailer
#  6 = all module retriever,  7 = all exclude

count = 1
wrong_count = 0
# count = To identify the inputs you entered separately
# wrong_count = To calculate the number of errors in the 'pass' you entered

# This is a program that The University requires, so this was built for to show the program interface pleasantly
while True:
        user_name = str(input("\nEnter Your USER NAME :- "))
        pw = int(input("Enter Your Password :- "))
        if pw == 1234:
                break
print("\nEnter 'Identification' To If You Are Student Type '1' Or You Are Staff Type '2'")
Id = int(input("Identification :- "))

#This is for student
if Id == 1:
        # Part 4
        # Finally, transfer your inputs into a text file as shown above
        text_file = open("Coursework.text", "w")
        text_file.write("\n\tAll Your Inputs\n\n")

        # The beginning of the program for students
        print("\n\n\tWelcom To Progression Table For Students !\n")
        while True:
                # Designed to retrieve your data and list it correctly
                try:
                        passs = int(input("Please enter your credits at pass :- "))
                        if wrong_count == 1:
                                print(passs, "Out Of Range\n")
                                print("The Program Stopped Because Your ANSWER Was OUT OF RANGE")
                                break
                        if 0 < passs < 20 or 20 < passs < 40 or 40 < passs < 60 or 60 < passs < 80 or 80 < passs < 100 or 100 < passs < 120:
                                print(passs, "Out Of Range\n")
                                print("If You Enter The Wrong Answer Again, The Program Will Stop")
                                wrong_count += 1
                                passs = int(input("Please enter your credits at pass :- "))
                        elif 120 < passs:
                                print(passs, "Out Of Range\n")
                                print("If You Enter The Wrong Answer Again, The Program Will Stop")
                                wrong_count += 1
                                passs = int(input("Please enter your credits at pass :- "))

                        defer = int(input("Please enter your credit at defer :- "))
                        fail = int(input("Please enter your credit at fail :- "))

                        count += 1
                        all = passs + defer + fail

                        if passs and defer and fail < 0:
                                print(all, "Total Incorrect\n")
                        elif all != 120:
                                print(all, "Total Incorrect\n")
                        elif passs == 120:
                                print("Progress\n")
                                text_file.write("Progress :- " + str(passs) + "," + str(defer) + "," + str(fail) + "\n")
                                all_input_list[4].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Progress")
                        elif passs == 100:
                                print("Progress (Module Trailer)\n")
                                text_file.write(
                                        "Progress (Module Trailer) :- " + str(passs) + "," + str(defer) + "," + str(
                                                fail) + "\n")
                                all_input_list[5].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Progress (Module Trailer)")
                        elif 0 <= fail <= 60:
                                print("Module Retriever\n")
                                text_file.write(
                                        "Module Retriever :- " + str(passs) + "," + str(defer) + "," + str(fail) + "\n")
                                all_input_list[6].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Module Retriever")
                        elif 61 <= fail:
                                print("Exclude\n")
                                text_file.write("Exclude :- " + str(passs) + "," + str(defer) + "," + str(fail) + "\n")
                                all_input_list[7].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Exclude")
                        break
                except ValueError:
                        print("Integer required\n")
                text_file.close()

#This is for staff
elif Id == 2:
        # Part 4
        # Finally, transfer your inputs into a text file as shown above
        text_file = open("Coursework.text", "w")
        text_file.write("\n\tAll Your Inputs\n\n")

        # The beginning of the program for staff
        print("\n\n\tWelcom To Progression Table For Staff !\n")
        while True:

                # Built to let you know if you need to go further after retrieving your data
                if 2 <= count:
                        print("\nWould You Like To Enter Another Set Of Data?")
                        forward = str(input("Enter 'y' for yes or 'q' to quit and view results : "))

                        if forward == "y":
                                print("\n""Rule", count)
                        elif forward == "q":
                                break
                        else:
                                print("The Program Stopped Because Your ANSWER Was Incorrect")
                                break

                # Designed to retrieve your data and list it correctly
                try:
                        passs = int(input("Please enter your credits at pass :- "))
                        if wrong_count == 1:
                                print(passs, "Out Of Range\n")
                                print("The Program Stopped Because Your ANSWER Was OUT OF RANGE")
                                break
                        if 0 < passs < 20 or 20 < passs < 40 or 40 < passs < 60 or 60 < passs < 80 or 80 < passs < 100 or 100 < passs < 120:
                                print(passs, "Out Of Range\n")
                                print("If You Enter The Wrong Answer Again, The Program Will Stop")
                                wrong_count += 1
                                passs = int(input("Please enter your credits at pass :- "))
                        elif 120 < passs:
                                print(passs, "Out Of Range\n")
                                print("If You Enter The Wrong Answer Again, The Program Will Stop")
                                wrong_count += 1
                                passs = int(input("Please enter your credits at pass :- "))

                        defer = int(input("Please enter your credit at defer :- "))
                        fail = int(input("Please enter your credit at fail :- "))

                        count += 1
                        all = passs + defer + fail

                        if passs and defer and fail < 0:
                                print(all, "Total Incorrect\n")
                        elif all != 120:
                                print(all, "Total Incorrect\n")
                        elif passs == 120:
                                print("Progress\n")
                                text_file.write("Progress :- " + str(passs) + "," + str(defer) + "," + str(fail) + "\n")
                                all_input_list[4].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Progress")
                        elif passs == 100:
                                print("Progress (Module Trailer)\n")
                                text_file.write(
                                        "Progress (Module Trailer) :- " + str(passs) + "," + str(defer) + "," + str(
                                                fail) + "\n")
                                all_input_list[5].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Progress (Module Trailer)")
                        elif 0 <= fail <= 60:
                                print("Module Retriever\n")
                                text_file.write(
                                        "Module Retriever :- " + str(passs) + "," + str(defer) + "," + str(fail) + "\n")
                                all_input_list[6].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Module Retriever")
                        elif 61 <= fail:
                                print("Exclude\n")
                                text_file.write("Exclude :- " + str(passs) + "," + str(defer) + "," + str(fail) + "\n")
                                all_input_list[7].append(1)
                                all_input_list[0].append(passs)
                                all_input_list[1].append(defer)
                                all_input_list[2].append(fail)
                                all_input_list[3].append("Exclude")

                except ValueError:
                        print("Integer required\n")

        print("\n\tHow Do You Want The Output\n")
        print("1. Horizontal Histogram")
        print("2. Vertical Histogram")
        print("3. List / Tuple / Directory Format")
        print("4. Text File")

        while True:
                try:
                        use_output_answer = int(input("\nEnter the number of the output you want :- "))

                        if use_output_answer == 1:
                                print("\n", "-" * 100, "\n")

                                # Part 1
                                # Creating a Horizontal Histogram from users data
                                progress = len(all_input_list[4])
                                module_trailer = len(all_input_list[5])
                                module_retriever = len(all_input_list[6])
                                exclude = len(all_input_list[7])
                                outcomes_in_total = progress + module_trailer + module_retriever + exclude

                                print("\tHorizontal Histogram\n")
                                print("Progress   ", progress, ":", progress * "*")
                                print("Trailer    ", module_trailer, ":", module_trailer * "*")
                                print("Retriever  ", module_retriever, ":", module_retriever * "*")
                                print("Excluded   ", exclude, ":", exclude * "*")
                                print("\n\t", outcomes_in_total, "Outcomes In Total\n")

                                print("-" * 100, "\n")
                                break

                        elif use_output_answer == 2:
                                print("\n", "-" * 100, "\n")

                                # Part 2
                                # Creating a Vertical Histogram from data obtained from users
                                progress = len(all_input_list[4])
                                module_trailer = len(all_input_list[5])
                                module_retriever = len(all_input_list[6])
                                exclude = len(all_input_list[7])
                                outcomes_in_total = progress + module_trailer + module_retriever + exclude

                                print("\tVertical Histogram\n")
                                print("progress     Trailing     Retriever     Excluded")

                                all_list = [[], [], [], []]

                                for x in range(progress):
                                        all_list[0].append("    *")
                                for x in range(module_trailer):
                                        all_list[1].append("    *")
                                for x in range(module_retriever):
                                        all_list[2].append("    *")
                                for x in range(exclude):
                                        all_list[3].append("    *")

                                Max = max(progress, module_trailer, module_retriever, exclude)

                                for i in range(Max):
                                        for x in all_list:
                                                try:
                                                        print(x[i], end="        ")
                                                except:
                                                        print("       ", end="     ")

                                        print()

                                print("-" * 100, "\n")
                                break

                        elif use_output_answer == 3:
                                print("\n", "-" * 100, "\n")

                                # part 3
                                # Retrieve user input data stored in List / Tuple / Directory format and return it to the user
                                print("\tOutput Uses Data From List, Tuple Or Dictionary\n")

                                pass_text = all_input_list[0]
                                defer_text = all_input_list[1]
                                fail_text = all_input_list[2]
                                program_outputs_text = all_input_list[3]
                                all_count = len(program_outputs_text)

                                for x in range(all_count):
                                        print(program_outputs_text[x], ":-", pass_text[x], ",", defer_text[x], ",",
                                              fail_text[x])

                                print("-" * 100, "\n")
                                break

                        elif use_output_answer == 4:
                                # Part 4
                                # Finally, transfer your inputs into a text file as shown above
                                text_file.close()
                                break

                        else:
                                print("Your Answer Is Incorrect !")

                except ValueError:
                        print("Integer required")
else:
        print("Your Answer Is Incorrect !")
        print("Program Is Stop..........!")
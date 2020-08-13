import re
def arithmetic_arranger(problems):
    for problem in problems:
        number_1_add = re.split("[ + ]|\s|[ - ]", problem)
        print(number_1_add)
        number_1_subtract = problem.replace(" ", "").split("-")[0]
        number_2_add = problem.replace(" ", "").split("+")[1]
        number_2_subtract = problem.replace(" ", "").split("-")[1]
        # user error...
        if len(problems) > 5:
            return "Error: Too many problems."
        elif "*" in problems or "/" in problems:
            return "Error: Operator must be '+' or '-'."
        elif "." in problems:
            return "Error: Numbers must only contain digits."
        elif len(number_1_add) > 4 or len(number_1_subtract) > 4 or len(number_2_add) > 4 or len(number_2_subtract) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            # no user error...
            def arranged_problems():
                # first number of length one, print number...
                if "+" in problem and len(number_1_add) == 1:
                    print(" " + " " + " " + number_1_add + "\n")
                elif "-" in problem and len(number_1_subtract) == 1:
                    print(" " + " " + " " + number_1_subtract + "\n")
                # first number of length two, print number...
                elif "+" in problem and len(number_1_add) == 2:
                    print(" " + " " + number_1_add + "\n")
                elif "-" in problem and len(number_1_subtract) == 2:
                    print(" " + " " + number_1_subtract + "\n")
                # first number of length three, print number...
                elif "+" in problem and len(number_1_add) == 3:
                    print(" " + number_1_add + "\n")
                elif "-" in problem and len(number_1_subtract) == 3:
                    print(" " + number_1_subtract + "\n")

                # second number of length one, print number...
                if "+" in problem and len(number_2_add) == 1:
                    print(" " + " " + " " + number_2_add + "\n")
                elif "-" in problem and len(number_2_subtract) == 1:
                    print(" " + " " + " " + number_2_subtract + "\n")
                # second number of length two, print number...
                elif "+" in problem and len(number_2_add) == 2:
                    print(" " + " " + number_2_add + "\n")
                elif "-" in problem and len(number_2_subtract) == 2:
                    print(" " + " " + number_2_subtract + "\n")
                # second number of length three, print number...
                elif "+" in problem and len(number_2_add) == 3:
                    print(" " + number_2_add + "\n")
                elif "-" in problem and len(number_2_subtract) == 3:
                    print(" " + number_2_subtract + "\n")


                # printing the line...
                if ("+" in problem and len(number_1_add) > 3) or ("-" in problem and len(number_1_subtract)) > 3 or ("+" in problem and len(number_2_add) > 3) or ("-" in problem and len(number_2_subtract) > 3):
                    print("\n------\n")
                elif len(number_1_add) > 2 or len(number_1_subtract) > 2 or len(number_2_add) > 2 or len(number_2_subtract) > 2:
                    print("\n-----\n")
                else:
                    print("\n----\n")

                if "+" in problem:
                    print(" " + " " + str(int(number_1_add) + int(number_2_add)))
                elif ("-" in problem) and (int(number_1_subtract) - int(number_2_subtract) > 0):
                    print(" " + " " + str(int(number_1_subtract) - int(number_2_subtract)))
                else:
                    print(" " + str(int(number_1_subtract) - int(number_2_subtract)))

                if problem != problems[-1]:
                    print(" " + " " + " " + " ")

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"])
import re # regular expressions
def arithmetic_arranger(problems):
    for problem in problems:
        number_1 = re.split("\+|\-", problem)[0].strip()
        number_2 = re.split("\+|\-", problem)[1].strip()
        # user error...
        if len(problems) > 5:
            return "Error: Too many problems."
        elif "*" in problems or "/" in problems:
            return "Error: Operator must be '+' or '-'."
        elif "." in problems:
            return "Error: Numbers must only contain digits."
        elif len(number_1) > 4 or len(number_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        else:
            # no user error...
            def arranged_problems():
                # FIRST number of length ONE, printing number...
                if len(number_1) == 1:
                    print(" " + " " + " " + number_1 + "\n")
                # FIRST number of length TWO, printing number...
                elif len(number_1) == 2:
                    print(" " + " " + number_1 + "\n")
                # FIRST number of length THREE, printing number...
                elif len(number_1) == 3:
                    print(" " + number_1 + "\n")
                # SECOND number of length ONE, printing number...
                if len(number_2) == 1:
                    print(" " + " " + " " + number_2 + "\n")
                # SECOND number of length TWO, printing number...
                elif len(number_2) == 2:
                    print(" " + " " + number_2 + "\n")
                # SECOND number of length THREE, printing number...
                elif len(number_2) == 3:
                    print(" " + number_2 + "\n")
                # printing the LINE...
                if len(number_1) > 3 or len(number_2) > 3:
                    print("\n------\n")
                elif len(number_1) > 3 or len(number_2) > 2:
                    print("\n-----\n")
                else:
                    print("\n----\n")

                # printing the SUM...
                if "+" in problem:
                    print("+" + " " + " " + str(int(number_1) + int(number_2)))
                elif ("-" in problem) and (int(number_1) - int(number_2) > 0):
                    print("-" + " " + " " + str(int(number_1) - int(number_2)))
                else:
                    print("-" + " " + str(int(number_1) - int(number_2)))
                # print FOUR SPACES...
                if problem != problems[-1]:
                    print(" " + " " + " " + " ")

print(arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]))
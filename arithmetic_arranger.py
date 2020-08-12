def arithmetic_arranger(problems):
    number_1_add = problem.replace(" ", "").split("+")[0]
    number_1_subtract = problem.replace(" ", "").split("-")[0]
    number_2_add = problem.replace(" ", "").split("+")[1]
    number_2_subtract = problem.replace(" ", "").split("-")[1]
    # if error...
    if len(problems) > 5:
        return "Error: Too many problems."
    elif "*" in problems or "/" in problems:
        return "Error: Operator must be '+' or '-'."
    elif "." in problems:
        return "Error: Numbers must only contain digits."
    elif len(number_1_add) > 4 or len(number_1_subtract) > 4 or len(number_2_add) > 4 or len(number_2_subtract) > 4:
        return "Error: Numbers cannot be more than four digits."
    else:
        # if no error...
        def arranged_problems():
            for problem in problems:
                # number of length one...
                if "+" in problem and len(number_1_add) == 1:
                    print(" " + " " + " " + number_1_add)
                elif "-" in problem and len(number_1_subtract) == 1:
                    print(" " + " " + " " + number_1_subtract)
                # number of length two...
                elif "+" in problem and len(number_1_add) == 2:
                    print(" " + " " + number_1_add)
                elif "-" in problem and len(number_1_subtract) == 2:
                    print(" " + " " + number_1_subtract)
                if len(number_1_add) > 2 or len(number_1_subtract) > 2 or len(number_2_add) > 2 or len(number_2_subtract) > 2:
                    print("-----")
                else:
                    print("----")

                if "+" in problem:
                    print(" " + " " + str(int(number_1_add + int(number_2_add)))
                else:
                    print(" " + " " + str(int(number_1_subtract - int(number_2_subtract)))

            return arranged_problems()
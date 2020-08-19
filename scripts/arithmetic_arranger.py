import re # regular expressions
def arithmetic_arranger(problems, results = False):
    
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = [[], [], [], []]

    for problem in problems:
        if "*" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."

        if re.search("[a-zA-Z]", problem) != None or "." in problem:
            return "Error: Numbers must only contain digits."
            
        if "+" in problem or "-" in problem:
            number_1 = re.split("\+|\-", problem)[0].strip()
            number_2 = re.split("\+|\-", problem)[1].strip()
            if len(number_1) > 4 or len(number_2) > 4:
                return "Error: Numbers cannot be more than four digits."

        # No user error...
        # Line 1...
        arranged_problems[0].append(number_1)
        # Line 2...
        arranged_problems[1].append(number_2)
        # Line 3
        if (max(len(number_1), len(number_2))) == 1:
            arranged_problems[2].append("---")
        elif (max(len(number_1), len(number_2))) == 2:
            arranged_problems[2].append("----")
        elif (max(len(number_1), len(number_2))) == 3:
            arranged_problems[2].append("-----")
        elif (max(len(number_1), len(number_2))) == 4:
            arranged_problems[2].append("------")
        # Line 4
        if results == True:
            if "+" in problem:
                arranged_problems[3].append(str(int(number_1) + int(number_2)))
            elif "-" in problem:
                arranged_problems[3].append(str(int(number_1) - int(number_2)))

    line_one = []
    line_two = []
    line_three = []
    line_four = []

    problem_width = []
    for element in line_three:
        problem_width.append(len(element))

    # Output formatting with tab and \n character...
    separator = "\t"

    for i in range(len(problems)):
        if arranged_problems[0][i] != arranged_problems[0][-1]:
            line_one.append(arranged_problems[0][i].rjust(problem_width[i]) + separator)
        else:
            line_one.append(arranged_problems[0][i].rjust(problem_width[i] + "\n"))

    for i in range(len(problems)):
        if "+" in problem:
            if arranged_problems[1][i] != arranged_problems[1][-1]:
                line_two.append("+" + arranged_problems[1][i].rjust(problem_width[i] - 1) + separator)
            else:
                line_two.append("+" + arranged_problems[1][i].rjust(problem_width[i] - 1) + "\n")
        elif "-" in problem:
            if arranged_problems[1][i] != arranged_problems[1][-1]:
                line_two.append("-" + arranged_problems[1][i].rjust(problem_width[i] - 1) + separator)
            else:
                line_two.append("-" + arranged_problems[1][i].rjust(problem_width[i] - 1) + "\n")

    if results == True:
        line_three.append(separator.join(arranged_problems[2]) + "\n")
    else:
        line_three.append(separator.join(arranged_problems[2]))

    if results == True:
        for i in range(len(problems)):
            if arranged_problems[3][i] != arranged_problems[3][-1]:
                line_four.append(arranged_problems[3][i].rjust(problem_width[i]) + separator)
            else:
                if problem[i] != problem[-1]:
                    line_four.append(arranged_problems[3][i].rjust(problem_width[i]) + "\n")
                else:
                    line_four.append(arranged_problems[3][i].rjust(problem_width[i]))
    
    return line_one + line_two + line_three + line_four
arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

    # for i in range(len(problems)):
    #     if arranged_problems[0][i] != arranged_problems[0][-1]:
    #         line_one.append(arranged_problems[0][i].rjust(problem_width[i])
    #     elif arranged_problems[0][i] == arranged_problems[0][-1]:
    #         line_one.append(arranged_problems[0][i].rjust(problem_width[i]))

    # for i in range(len(problems)):
    #     if "+" in problems[i]:
    #         if line_two[i] != line_two[-1]:
    #             print("+" + line_two[i].rjust(problem_width[i] - 1), end = separator)
    #         else:
    #             print("+" + line_two[i].rjust(problem_width[i] - 1), end = "\n")
    #     elif "-" in problems[i]:
    #         if line_two[i] != line_two[-1]:
    #             print("-" + line_two[i].rjust(problem_width[i] - 1), end = separator)
    #         else:
    #             print("-" + line_two[i].rjust(problem_width[i] - 1), end = "\n")
    # if with_results == True:
    #     print(separator.join(line_three), end = "\n")
    # else:
    #     print(separator.join(line_three))

    # if with_results == True:
    #     for i in range(len(problems)):
    #         if line_four[i] != line_four[-1]:
    #             print(line_four[i].rjust(problem_width[i]), end = separator)
    #         else:
    #             print(line_four[i].rjust(problem_width[i]), end = "\n")
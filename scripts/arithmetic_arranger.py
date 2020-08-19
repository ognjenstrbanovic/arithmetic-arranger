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
    for element in arranged_problems[2]:
        problem_width.append(len(element))

    # Output formatting with tab and \n character...
    separator = "    "

    for i in range(len(problems)):
        if arranged_problems[0][i] != arranged_problems[0][-1]:
            line_one.append(arranged_problems[0][i].rjust(problem_width[i]) + separator)
        else:
            line_one.append(arranged_problems[0][i].rjust(problem_width[i]) + "\n")

    for i in range(len(problems)):
        if "+" in problems[i]:
            if arranged_problems[1][i] != arranged_problems[1][-1]:
                line_two.append("+" + arranged_problems[1][i].rjust(problem_width[i] - 1) + separator)
            else:
                line_two.append("+" + arranged_problems[1][i].rjust(problem_width[i] - 1) + "\n")
        elif "-" in problems[i]:
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
                if problems[i] != problems[-1]:
                    line_four.append(arranged_problems[3][i].rjust(problem_width[i]) + "\n")
                else:
                    line_four.append(arranged_problems[3][i].rjust(problem_width[i]))

    string_1 = "".join(line_one)
    string_2 = "".join(line_two)
    string_3 = "".join(line_three)
    string_4 = "".join(line_four)
    arranged_strings = string_1 + string_2 + string_3 + string_4

    return arranged_strings

print(arithmetic_arranger(["3 + 855", "3801 - 2", "45 + 43", "123 + 49"]))
print("    3      3801      45      123\n+ 855    -    2    + 43    +  49\n-----    ------    ----    -----")
import re # regular expressions
def arithmetic_arranger(problems, with_results = False):
    
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
        if with_results == True:
            if "+" in problem:
                arranged_problems[3].append(str(int(number_1) + int(number_2)))
            elif "-" in problem:
                arranged_problems[3].append(str(int(number_1) - int(number_2)))

    line_one = arranged_problems[0]
    line_two = arranged_problems[1]
    line_three = arranged_problems[2]
    line_four = arranged_problems[3]

    problem_width = []
    for element in line_three:
        problem_width.append(len(element))

    # Output formatting with \n character...
    separator = "    "

    for i in range(len(problems)):
        if line_one[i] != line_one[-1]:
            print(line_one[i].rjust(problem_width[i]), end = separator)
        else:
            print(line_one[i].rjust(problem_width[i]), end = "\n")

    for i in range(len(problems)):
        if "+" in problems[i]:
            if line_two[i] != line_two[-1]:
                print("+" + line_two[i].rjust(problem_width[i] - 1), end = separator)
            else:
                print("+" + line_two[i].rjust(problem_width[i] - 1), end = "\n")
        elif "-" in problems[i]:
            if line_two[i] != line_two[-1]:
                print("-" + line_two[i].rjust(problem_width[i] - 1), end = separator)
            else:
                print("-" + line_two[i].rjust(problem_width[i] - 1), end = "\n")

    print(separator.join(line_three), end = "\n")

    if with_results == True:
        for i in range(len(problems)):
            if line_four[i] != line_four[-1]:
                print(line_four[i].rjust(problem_width[i]), end = separator)
            else:
                print(line_four[i].rjust(problem_width[i]), end = "\n")
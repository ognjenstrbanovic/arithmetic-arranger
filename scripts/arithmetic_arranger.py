import re # regular expressions
import string
def arithmetic_arranger(problems, true_or_false = False):
    arranged_problems = [[], [], [], []]
    for problem in problems:
        number_1 = re.split("\+|\-", problem)[0].strip()
        number_2 = re.split("\+|\-", problem)[1].strip()
        # User error...
        if len(problems) > 5:
            return "Error: Too many problems."
        elif "*" in problem or "/" in problem:
            return "Error: Operator must be '+' or '-'."
        elif any(character.isalpha() for character in problem) == True:
            return "Error: Numbers must only contain digits."
        elif len(number_1) > 4 or len(number_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # No user error...
        else:
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
            elif (max(len(number_1), len(number_2))) == 4 and (int(number_1) - int(number_2) < 0):
                arranged_problems[2].append("-------")
            elif (max(len(number_1), len(number_2))) == 4:
                arranged_problems[2].append("------")
            # Line 4
            if true_or_false == True:
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
    # Output formatting...
    for i in range(len(problems)):
        if line_one[i] != line_one[-1]:
            print(line_one[i].rjust(problem_width[i]), end = "    ")
        else:
            print(line_one[i].rjust(problem_width[i]))
    for i in range(len(problems)):
        if "+" in problem:
            if line_two[i] != line_two[-1]:
                print("+" + line_two[i].rjust(problem_width[i] - 1), end = "    ")
            else:
                print("+" + line_two[i].rjust(problem_width[i] - 1))
        if "-" in problem:
            if line_two[i] != line_two[-1]:
                print("-" + line_two[i].rjust(problem_width[i] - 1), end = "    ")
            else:
                print("-" + line_two[i].rjust(problem_width[i] - 1))
    print("    ".join(line_three))
    if true_or_false == True:
        for i in range(len(problems)):
            if line_four[i] != line_four[-1]:
                print(line_four[i].rjust(problem_width[i]), end = "    ")
            else:
                print(line_four[i].rjust(problem_width[i]))
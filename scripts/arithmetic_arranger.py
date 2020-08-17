import re # regular expressions
def arithmetic_arranger(problems, true_or_false = False):
    arranged_problems = [[], [], [], []]
    for problem in problems:
        number_1 = re.split("\+|\-", problem)[0].strip()
        number_2 = re.split("\+|\-", problem)[1].strip()
        # User error...
        if len(problems) > 5:
            return "Error: Too many problems."
        elif "*" in problems or "/" in problems:
            return "Error: Operator must be '+' or '-'."
        elif "." in problems:
            return "Error: Numbers must only contain digits."
        elif len(number_1) > 4 or len(number_2) > 4:
            return "Error: Numbers cannot be more than four digits."
        # No user error...
        else:
            # Line 1...
            arranged_problems[0].append(number_1)
            # Line 2...
            if "+" in problem:
                arranged_problems[1].append("+")
                arranged_problems[1].append(number_2)
            elif "-" in problem:
                arranged_problems[1].append("-")
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
                    if int(number_1) - int(number_2) > 0:
                        arranged_problems[3].append(str(int(number_1) - int(number_2)))
                    elif int(number_1) - int(number_2) < 0:
                        arranged_problems[3].append("-" + str(int(number_1) - int(number_2)))
    line_one = arranged_problems[0]
    line_two = arranged_problems[1]
    line_three = arranged_problems[2]
    line_four = arranged_problems[3]
    print(arranged_problems)
    # Output formatting...
    for element in line_one:
        if element != line_one[-1]:
            if len(number_1) > (len(number_2 + " " + " ")):
                print(element, end = "    ")
            else:
                print(element.rjust(len(number_2) - len(number_1)), end = "    ")
        else:
            print(element)
    for element in line_two:
        # if element != line_two[-1]:
            
        # else:

arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

#             if max(len(number_1), len(number_2)) < 5:
#                 line_two.append(number_2)
#     for string in arranged_problems:
#         if element != line_one[-1]:
#             print(element.rjust(2), end = "    ")
#         else:
#             print(element.rjust(2))
#     for element in line_two:
#         if element != line_two[-1]:
#             print("+".ljust(0), end = "")
#             print(element.rjust(2), end = "    ")
# arithmetic_arranger(["32 + 698", "3801 - 2", "45 + 43", "123 + 49"], True)

#             if "+" in problem:
#                 "+".ljust(1)
#                 if max(len(number_1), len(number_2)) < 2:
#                     line_two.append("{:=+d}".format(int(number_2)))
#             else:
#                 "-".ljust(1)
#                 line_two.append("{:= d}".format(int(number_2)))
#             # Line 3...
#             if len(problem) < 7:
#                 line_three.append('{:^16}'.format("---"))
#             elif len(problem) < 8:
#                 line_three.append("----")
#             elif len(problem) < 9:
#                 line_three.append("-----")
#             elif len(problem) < 11:
#                 line_three.append("------")
#             else:
#                 line_three.append("-------")
#             # Line 4...
#             if true_or_false == True:
#                 if "+" in problem:
#                     line_four.append(str(int(number_1) + int(number_2)))
#                 elif "-" in problem:
#                     if int(number_1) - int(number_2) > 0:
#                         line_four.append(str(int(number_1) - int(number_2)))
#                     elif int(number_1) - int(number_2) < 0:
#                         line_four.append(str(int(number_1) - int(number_2)))
#     for element in line_one:
#         if element != line_one[-1]:
#             print(f"{element:>5}", end = "    ")
#         else:
#             print(f"{element:>5}")
#     for element in line_two:
#         if element != line_two[-1]:
#             print(f"{element:>5}", end = "    ")
#         else:
#             print(f"{element:>5}")
#     for element in line_three:
#         if element != line_three[-1]:
#             print(f"{element:>5}", end = "    ")
#         elif element == line_three[-1]:
#             print(f"{element:>5}")
#     for element in line_four:
#         if element != line_four[-1]:
#             print(f"{element:>5}", end = "    ")
#         else:
#             print(f"{element:>5}")
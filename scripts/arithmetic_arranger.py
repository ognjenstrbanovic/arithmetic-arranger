import re # regular expressions
def arithmetic_arranger(problems, true_or_false = False):
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
        # no user error...
        else:
            line_one = []
            line_two = []
            line_three = []
            line_four = []
            my_separator = "    "
            if len(number_1) == 4 and len(number_2) == 4:
                line_one.append("  " + number_1)
                line_two.append("+" + " " + number_2)
                line_three.append("------")
                if true_or_false == True:
                    line_four.append(" " + " " + str(int(number_1) + int(number_2)))
            print(my_separator.join(line_one))
            print(my_separator.join(line_two))
            print(my_separator.join(line_three))
            print(my_separator.join(line_four))
arithmetic_arranger(["4444 + 1111", "5555 + 2222"], True)





            # for i in range(4):
            #     for problem in problems:
            #         if problem != problems[-1]:
            #             if i == 0:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print(" " + " " + number_1 + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         print(" " + " " + number_1 + "    ", end = "")
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print(" " + " " + number_1 + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         print(" " + " " + number_1 + "    ", end = "")
            #             elif i == 1:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("+" + " " + number_2 + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         print("+" + " " + " " + number_2 + "    ", end = "")
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("-" + " " + number_2 + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         print("-" + " " + " " + number_2 + "    ", end = "")
            #             elif i == 2:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("------" + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         print("------" + "    ", end = "")
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("------" + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         print("------" + "    ", end = "")
            #             elif i == 3 and true_or_false == True:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print(" " + " " + str(int(number_1) + int(number_2)) + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         print(" " + " " + str(int(number_1) + int(number_2)) + "    ", end = "")
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         if int(number_1) - int(number_2) > 0:
            #                             print(" " + " " + str(int(number_1) - int(number_2)) + "    ", end = "")
            #                         else:
            #                             print(" " + str(int(number_1) - int(number_2)) + "    ", end = "")
            #                     elif len(number_1) == 4 and len(number_2) == 3:
            #                         if int(number_1) - int(number_2) > 0:
            #                             print(" " + " " + str(int(number_1) - int(number_2)) + "    ", end = "")
            #                         else:
            #                             print(" " + str(int(number_1) - int(number_2)) + "    ", end = "")
            #         else:
            #             if i == 0:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print(" " + " " + number_1)
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print(" " + " " + number_1)
            #             elif i == 1:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("+" + " " + number_2)
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("+" + " " + number_2)
            #             elif i ==2:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("------")
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print("------")
            #             elif i == 3 and true_or_false == True:
            #                 if "+" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 4:
            #                         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
            #                 elif "-" in problem:
            #                     if len(number_1) == 4 and len(number_2) == 3:
            #                         if int(number_1) - int(number_2) > 0:
            #                             print(" " + " " + str(int(number_1) - int(number_2)))
            #                         else:
            #                             print(" " + str(int(number_1) - int(number_2)))

# elif len(number_1) == 4 and "+" in problem and len(number_2) == 2:
#     if i == 0:
#         print(" " + " " + number_1 + "    ", end = "")
#     elif i == 1:    
#         print("+" + " " + " " + " " + number_2 + "    ", end = "")
#     elif i == 2:
#         print("------" + "    ", end = "")
#     elif true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ", end = "")

# elif len(number_1) == 4 and "-" in problem and len(number_2) == 2:
#     if i == 0:    
#         print(" " + " " + number_1 + "    ", end = "")
#     elif i == 1:
#         print("-" + " " + " " + " " + number_2 + "    ", end = "")
#     elif i == 2:
#         print("------" + "    ", end = "")
#     elif true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ", end = "")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ", end = "")

# elif len(number_1) == 4 and "+" in problem and len(number_2) == 1:
#     if i == 0:
#         print(" " + " " + number_1 + "    ", end = "")
#     elif i == 1:
#         print("+" + " " + " " + " " + " " + number_2 + "    ", end = "")
#     elif i == 2:
#         print("------" + "    ", end = "")
#     elif true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ", end = "")

# elif len(number_1) == 4 and "-" in problem and len(number_2) == 1:
#     if i == 0:
#         print(" " + " " + number_1 + "    ", end = "")
#     elif i == 1:
#         print("-" + " " + " " + " " + " " + number_2 + "    ", end = "")
#     elif i == 2:
#         print("------" + "    ", end = "")
#     elif true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ", end = "")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ", end = "")

# elif len(number_1) == 3 and "+" in problem and len(number_2) == 4:
#     if i == 0:
#         print(" " + " " + " " + number_1 + "    ", end = "")
#     elif i == 1:
#         print("+" + " " + number_2 + "    ", end = "")
#     elif i == 2:
#         print("------" + "    ", end = "")
#     elif true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ", end = "")

# elif len(number_1) == 3 and "-" in problem and len(number_2) == 4:
#     if i == 0:
#         print(" " + " " + " " + number_1 + "    ", end = "")
#     elif i == 1:
#         print("-" + " " + number_2 + "    ", end = "")
#     elif i == 2:
#         print("------" + "    ", end = "")
#     elif true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ", end = "")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ", end = "")

# elif len(number_1) == 4 and "+" in problem and len(number_2) == 3:
#     if i == 0:
#         print(" " + " " + number_1)
#     elif i == 1:
#         print("+" + " " + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)))

# elif len(number_1) == 4 and "-" in problem and len(number_2) == 3:
#     if i == 0:
#         print(" " + " " + number_1)
#     elif i == 1:
#         print("-" + " " + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)))
#         else:
#             print(" " + str(int(number_1) - int(number_2)))

# elif len(number_1) == 4 and "+" in problem and len(number_2) == 2:
#     if i == 0:
#         print(" " + " " + number_1)
#     elif i == 1:    
#         print("+" + " " + " " + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)))

# elif len(number_1) == 4 and "-" in problem and len(number_2) == 2:
#     if i == 0:    
#         print(" " + " " + number_1)
#     elif i == 1:
#         print("-" + " " + " " + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)))
#         else:
#             print(" " + str(int(number_1) - int(number_2)))

# elif len(number_1) == 4 and "+" in problem and len(number_2) == 1:
#     if i == 0:
#         print(" " + " " + number_1)
#     elif i == 1:
#         print("+" + " " + " " + " " + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)))

# elif len(number_1) == 4 and "-" in problem and len(number_2) == 1:
#     if i == 0:
#         print(" " + " " + number_1)
#     elif i == 1:
#         print("-" + " " + " " + " " + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)))
#         else:
#             print(" " + str(int(number_1) - int(number_2)))

# elif len(number_1) == 3 and "+" in problem and len(number_2) == 4:
#     if i == 0:
#         print(" " + " " + " " + number_1)
#     elif i == 1:
#         print("+" + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)))

# elif len(number_1) == 3 and "-" in problem and len(number_2) == 4:
#     if i == 0:
#         print(" " + " " + " " + number_1)
#     elif i == 1:
#         print("-" + " " + number_2)
#     elif i == 2:
#         print("------")
#     elif true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)))
#         else:
#             print(" " + str(int(number_1) - int(number_2)))



# elif len(number_1) == 3 and "+" in problem and len(number_2) == 3:
#     print(" " + " " + number_1 + "    ")
#     print("+" + " " + " " + number_2 + "    ")
#     print("------" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 3 and "-" in problem and len(number_2) == 3:
#     print(" " + " " + " " + number_1 + "    ")
#     print("-" + " " + " " + number_2 + "    ")
#     print("------" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 2 and "+" in problem and len(number_2) == 4:
#     print(" " + " " + " " + " " + number_1 + "    ")
#     print("+" + " " + number_2 + "    ")
#     print("------" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 2 and "-" in problem and len(number_2) == 4:
#     print(" " + " " + " " + " " + number_1 + "    ")
#     print("-" + " " + number_2 + "    ")
#     print("------" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 1 and "+" in problem and len(number_2) == 4:
#     print(" " + " " + " " + " " + " " + number_1 + "    ")
#     print("+" + " " + number_2 + "    ")
#     print("------" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 1 and "-" in problem and len(number_2) == 4:
#     print(" " + " " + " " + " " + " " + number_1 + "    ")
#     print("-" + " " + number_2 + "    ")
#     print("------" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 3 and "+" in problem and len(number_2) == 3:
#     print(" " + " " + number_1 + "    ")
#     print("+" + " " + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 3 and "+" in problem and len(number_2) == 3:
#     print(" " + " " + number_1 + "    ")
#     print("-" + " " + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 3 and "+" in problem and len(number_2) == 2:
#     print(" " + " " + number_1 + "    ")
#     print("+" + " " + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 3 and "-" in problem and len(number_2) == 2:
#     print(" " + " " + number_1 + "    ")
#     print("-" + " " + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 3 and "+" in problem and len(number_2) == 1:
#     print(" " + " " + number_1 + "    ")
#     print("+" + " " + " " + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 3 and "-" in problem and len(number_2) == 1:
#     print(" " + " " + number_1 + "    ")
#     print("-" + " " + " " + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 2 and "+" in problem and len(number_2) == 3:
#     print(" " + " " + " " + number_1 + "    ")
#     print("+" + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 2 and "-" in problem and len(number_2) == 3:
#     print(" " + " " + " " + number_1 + "    ")
#     print("-" + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 1 and "+" in problem and len(number_2) == 3:
#     print(" " + " " + " " + " " + number_1 + "    ")
#     print("+" + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 1 and "-" in problem and len(number_2) == 3:
#     print(" " + " " + " " + " " + number_1 + "    ")
#     print("-" + " " + number_2 + "    ")
#     print("-----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 2 and "+" in problem and len(number_2) == 2:
#     print(" " + " " + number_1 + "    ")
#     print("+" + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 2 and "-" in problem and len(number_2) == 2:
#     print(" " + " " + number_1 + "    ")
#     print("-" + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 2 and "+" in problem and len(number_2) == 1:
#     print(" " + " " + number_1 + "    ")
#     print("+" + " " + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 2 and "-" in problem and len(number_2) == 1:
#     print(" " + " " + number_1 + "    ")
#     print("-" + " " + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 1 and "+" in problem and len(number_2) == 2:
#     print(" " + " " + " " + number_1 + "    ")
#     print("+" + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# elif len(number_1) == 1 and "-" in problem and len(number_2) == 2:
#     print(" " + " " + " " + number_1 + "    ")
#     print("-" + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")

# elif len(number_1) == 1 and "+" in problem and len(number_2) == 1:
#     print(" " + " " + " " + number_1 + "    ")
#     print("+" + " " + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         print(" " + " " + str(int(number_1) + int(number_2)) + "    ")
# else:
#     print(" " + " " + " " + number_1 + "    ")
#     print("-" + " " + " " + number_2 + "    ")
#     print("----" + "    ")
#     if true_or_false == True:
#         if int(number_1) - int(number_2) > 0:
#             print(" " + " " + str(int(number_1) - int(number_2)) + "    ")
#         else:
#             print(" " + str(int(number_1) - int(number_2)) + "    ")
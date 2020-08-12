def arithmetic_arranger(problems):
    if len(problems) > 5:
        return "Error: Too many problems."
    elif "*" in problems or "/" in problems:
        return "Error: Operator must be '+' or '-'."
    elif "." in problems:
        return "Error: Numbers must only contain digits."
    elif for problem in problems:
        if len(problem.replace(" ", "").split("+")[0]) > 4 or len(problem.replace(" ", "").split("-")[0]) > 4 or len(problem.replace(" ", "").split("+")[1]) > 4 or len(problem.replace(" ", "").split("-")[1]) > 4:
            return "Error: Numbers cannot be more than four digits."
    else:
        
        if len(problem.replace(" ", "").split("+")[0]) > 2 or len(problem.replace(" ", "").split("-")[0]) > 2 or len(problem.replace(" ", "").split("+")[1]) > 2 or len(problem.replace(" ", "").split("-")[1]) > 2:
            print("-----")
        else:
            print("----")
            return arranged_problems
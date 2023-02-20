import re

def arithmetic_arranger(problems, show_answer=False):

    if len(problems) > 5:
        return "Error: Too many problems."

    if len(problems) < 1:
        return "Error: No problems submitted."

    


    arranged_problems = ""

    return arranged_problems

def validate_problem(problem):

    stripped = problem.strip()

    if (re.search(regex_pattern, stripped)):
        return True
    else:
        return False

regex_pattern = "^\d{1,4}[\-\+]\d{1,4}$"

test_input = input("Enter test input: ")

print(validate_problem(test_input))


import re

# check args: must be 1-2
# check that first arg is list of strings
# check that each string:
#   is 1-4 digits followed by operator followed by 1-4 digits
#   if operator is * or /, error
#   if operand is not 1-4 digits, error

# output

INVALID_OPERATORS = "\/|\*"
VALID_OPERAND = "^\d{1,4}$"

 

def validate_input(list_of_problems, display_results=False):

    if (len(list_of_problems) < 2):
        return "Error: Too few problems."

    if (len(list_of_problems) > 5):
        return "Error: Too many problems."

    if type(display_results) != bool:
        return "Error: Results display flag must be True or False."

    if (validate_list(list_of_problems)):
        return True

    return False



def validate_list(my_list):

    for problem in my_list:

        split_list = problem.split()

        if not re.match(VALID_OPERAND, split_list[0]):
            print("digit error")
            return "Error: Numbers must only contain digits."

        if re.match(INVALID_OPERATORS, split_list[1]):
            print("operand error")
            return "Error: Operator must be '+' or '-'."

        if not re.match(VALID_OPERAND, split_list[2]):
            print("digit error")
            return "Error: Numbers must only contain digits."
    
    return True



def parse_problem(problem):

    operator1 = 0
    operator2 = 0
    split_problem = problem.split()
    parsed = []

    for i in split_problem:
        if i.isdigit():
            parsed.append(int(i))
        else:
            parsed.append(i)
    
    return parsed


def find_problems_lengths(my_list):

    max_lengths = []
    parsed = []
    
    for problem in my_list:
        parsed.append(parse_problem(problem))

    for prob in parsed:
        max_lengths.append(len(max(str(prob), key=len)))
    
    return max_lengths


def print_output(my_list):
    return



test_input = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

print(validate_input(test_input))

print(find_problems_lengths(test_input))
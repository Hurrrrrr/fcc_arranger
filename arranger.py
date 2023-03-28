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
MAX_LENGTH = 4

 

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
            parsed.append(i)
    
    return parsed


def find_problems_lengths(problems):

    max_lengths = []
    min_lengths = []
    differential_lengths = []

    for problem in problems:
        items = problem.split()
        max_problem_length = max(len(item) for item in items)
        max_lengths.append(max_problem_length)

    # more complicated than finding max length because we have to ignore operands
    for problem in problems:

        items = problem.split()
        min_problem_length = MAX_LENGTH

        for i in range(len(items)):
            if items[i].isdigit():
                if len(items[i]) < min_problem_length:
                    min_problem_length = len(items[i])

        min_lengths.append(min_problem_length)

    for i in range(len(max_lengths)):
        differential_lengths.append(max_lengths[i] - min_lengths[i])

    return differential_lengths

def calc_dash_count(problems):

    dash_count = []

    for problem in problems:
        max_digits = 0
        split_problem = problem.split()
        for item in split_problem:
            if (len(item)) > max_digits:
                max_digits = (len(item))
        dash_count.append(max_digits + 2)

    return dash_count


def print_output(problems):

    output_list = []
    lenghts = find_problems_lengths(problems)
    parsed = []
    dashes = calc_dash_count(problems)
    for problem in problems:
        parsed.append(parse_problem(problem))
    num_of_problems = len(parsed)

    # output for first line
    for i in range(num_of_problems):    
        output_list.append("  ")
        if len(parsed[i][0]) < len(parsed[i][2]):
            for j in range(lenghts[i]):
                output_list.append(" ")
        output_list.append(parsed[i][0])
        if (i + 1) < num_of_problems:
            output_list.append("    ")
        else:
            output_list.append("\n")
    
    #output for second line
    for k in range(num_of_problems):
        output_list.append(parsed[k][1])
        output_list.append(" ")
        if len(parsed[k][2]) < len(parsed[k][0]):
            for l in range(lenghts[k]):
                output_list.append(" ")
        output_list.append(parsed[k][2])
        if (k + 1) < num_of_problems:
            output_list.append("    ")
        else:
            output_list.append("\n")
    
    #output for third line
    for m in range(num_of_problems):
        for n in range(dashes[m]):
            output_list.append("-")
        if (m + 1) < num_of_problems:
            output_list.append("    ")
        else:
            output_list.append("\n")

    asdf = "".join(output_list)

    print(asdf)



test_input = ["32 + 698", "3801 - 2", "45 + 43", "123 + 49"]

print_output(test_input)
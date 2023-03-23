import re

# check args: must be 1-2
# check that first arg is list of strings
# check that each string:
#   is 1-4 digits followed by operator followed by 1-4 digits
#   if operator is * or /, error
#   if operand is not 1-4 digits, error

# output

def validate_input(list_of_problems, display_results=False):

    if (len(list_of_problems) < 2):
        return "Error: Too few problems."

    if (len(list_of_problems) > 5):
        return "Error: Too many problems."

    print(validate_list(list_of_problems))

def validate_list(my_list):

    for problem in my_list:

        split_list = my_list.split()

        if re.search(VALID_OPERAND, split_list[0]) == False:
            return "Error: Numbers must only contain digits."

        if re.search(INVALID_OPERATORS, split_list[1]) == True:
            return "Error: Operator must be '+' or '-'."

        if re.search(VALID_OPERAND, split_list[2]) == False:
            return "Error: Numbers must only contain digits."
    
    return True




INVALID_OPERATORS = "\/|\*"
VALID_OPERAND = "\d{1,4}"

test_input = input("Enter test input: ")

print(validate_problem(test_input))



# valid_regex_pattern = "^\d{1,4}[\-\+]\d{1,4}$"



# def validate_operand(operand):

#     if (re.search(valid_operand, replaced)) == False:
#         return "Error: Numbers must only contain digits."


# def arithmetic_arranger(problems, show_answer=False):

#     if len(problems) > 5:
#         return "Error: Too many problems."

#     if len(problems) < 1:
#         return "Error: Too many problems."
    


#     arranged_problems = ""

#     return arranged_problems

# def validate_problem(problem):

#     if (re.search(invalid_operators, problem)):
#         return "Error: Operator must be '+' or '-'."

#     replaced = problem.replace(" ", "")

#     if (re.search(valid_operand, replaced)) == False:
#         return "Error: Numbers must only contain digits."

    # if (re.search(valid_regex_pattern, replaced)):
    #     return True
    # else:
    #     return False
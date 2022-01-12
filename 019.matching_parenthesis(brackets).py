"""
Matching parenthesis(brackets)

Only 8 of parenthesis characters will be given as input.
The characters are: (, ), {, }, <, >, [, ]

Only when the parenthesis pairs are closed with its counterpart, the string is valid.

The correct order of characters is:
    (, or {, or <, or [ comes first, then ), or }, or >, or ] comes after.

Check if the string is closed in the correct order.

e.g.) ({()}): correct order, thus it is a valid string.
      []<>{}: correct order, thus it is a valid string.
      )( <] <(>): not correct order, thus it is an invalid string.

NOTE: consider how to check the given string is in order of 'open' first, 'close' last.
"""


def is_valid_parenthesis(string):
    """
    stack and dictionary will be used.
    """

    # Solution 1

    stack = []
    input_dict = {'(': ')', '[': ']', '<': '>', '{': '}'}  # dictionary
    open_parenthesis = {'(', '[', '<', '{'}  # set

    for character in string:
        if character in open_parenthesis:  # character is open parenthesis
            stack.append(character)
        else:  # character is close parenthesis
            if len(stack) == 0:
                return False
            else:
                if input_dict[stack.pop()] != character:
                    return False
    return True

    # # Solution 2
    #
    # stack = []
    # input_dict = {')': '(', ']': '[', '>': '<', '}': '{'}  # dictionary
    # open_parenthesis = {'(', '[', '<', '{'}  # set
    #
    # for character in string:
    #     if character in open_parenthesis:  # character is open parenthesis
    #         stack.append(character)
    #     else:  # character is close parenthesis
    #         if len(stack) == 0:  # stack is empty
    #             return False
    #         else:
    #             if input_dict[character] == stack[-1]:  # stack top is the same as input
    #                 stack.pop()
    #             else:
    #                 return False
    #
    # return True if len(stack) == 0 else False

    # # Solution 3
    #
    # stack = []
    # input_dict = {')': '(', ']': '[', '>': '<', '}': '{'}  # dictionary
    # open_parenthesis = {'(', '[', '<', '{'}  # set
    #
    # for character in string:
    #     if character in open_parenthesis:  # character is open parenthesis
    #         stack.append(character)
    #     else:  # character is close parenthesis
    #         if len(stack) != 0 and stack[-1] == input_dict[character]:
    #             stack.pop()
    #         else:
    #             return False
    # return False if len(stack) != 0 else True


def main():
    examples = ["({()})", "[]<>{}", ")(" "<]", "<(>)"]

    for example in examples:
        print(example, is_valid_parenthesis(example))


if __name__ == "__main__":
    main()

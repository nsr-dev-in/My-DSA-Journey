# function to check operator priority
def precedence(op):
    if op == '+' or op == '-':
        return 1
    elif op == '*' or op == '/':
        return 2
    elif op == '^':
        return 3
    return 0


# infix -> postfix conversion
def infix_to_postfix(exp):
    stack = []
    result = ""

    for ch in exp:

        # operand
        if ch.isalnum():
            result += ch

        # opening bracket
        elif ch == '(':
            stack.append(ch)

        # closing bracket
        elif ch == ')':
            while stack and stack[-1] != '(':
                result += stack.pop()
            stack.pop()

        # operator
        else:
            while (stack and precedence(stack[-1]) >= precedence(ch)):
                result += stack.pop()
            stack.append(ch)

    # pop remaining operators
    while stack:
        result += stack.pop()

    return result


# MAIN FUNCTION: infix -> prefix
def infix_to_prefix(expression):

    # 1. reverse expression
    expression = expression[::-1]

    # 2. swap brackets
    temp = ""
    for ch in expression:
        if ch == '(':
            temp += ')'
        elif ch == ')':
            temp += '('
        else:
            temp += ch

    # 3. infix -> postfix
    postfix = infix_to_postfix(temp)

    # 4. reverse postfix -> prefix
    prefix = postfix[::-1]

    return prefix


# Example
exp = "(A+B)*C"
print("Prefix:", infix_to_prefix(exp))

def postfix_to_infix(expression):
    stack = []

    for ch in expression:

        # if operand
        if ch.isalnum():
            stack.append(ch)

        # if operator
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new_exp = "(" + op1 + ch + op2 + ")"
            stack.append(new_exp)

    return stack[-1]


# Example
exp = "AB+C*"
print("Infix:", postfix_to_infix(exp))

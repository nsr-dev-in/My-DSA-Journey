def postfix_to_prefix(expression):
    stack = []

    for ch in expression:

        # operand
        if ch.isalnum():
            stack.append(ch)

        # operator
        else:
            op2 = stack.pop()
            op1 = stack.pop()

            new_exp = ch + op1 + op2
            stack.append(new_exp)

    return stack[-1]


# Example
exp = "AB+C*"
print("Prefix:", postfix_to_prefix(exp))

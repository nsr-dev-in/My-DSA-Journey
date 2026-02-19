def prefix_to_infix(expression):
    stack = []

    # traverse from right to left
    for ch in reversed(expression):

        # operand
        if ch.isalnum():
            stack.append(ch)

        # operator
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new_exp = "(" + op1 + ch + op2 + ")"
            stack.append(new_exp)

    return stack[-1]


# Example
exp = "*+ABC"
print("Infix:", prefix_to_infix(exp))

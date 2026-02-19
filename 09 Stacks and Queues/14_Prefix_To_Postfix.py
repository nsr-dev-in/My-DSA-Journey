# 14_Prefix_To_Postfix.py

def prefix_to_postfix(expression):
    stack = []

    # traverse from right to left
    for ch in reversed(expression):

        # if operand
        if ch.isalnum():
            stack.append(ch)

        # if operator
        else:
            op1 = stack.pop()
            op2 = stack.pop()

            new_exp = op1 + op2 + ch
            stack.append(new_exp)

    return stack[-1]


# Driver Code
if __name__ == "__main__":
    exp = input("Enter Prefix Expression: ")
    result = prefix_to_postfix(exp)

    print("Postfix Expression:", result)

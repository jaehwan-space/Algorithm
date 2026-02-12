while True:
    n = input()
    if n == ".":
        break
    stacks = []
    for i in n:
        if i == "(":
            stacks.append("(")
        elif i == "[":
            stacks.append("[")
        elif i == ")":
            if len(stacks) != 0 and stacks[-1] == "(":
                stacks.pop()
            else:
                stacks.append("-")
                break
        elif i == "]":
            if len(stacks) != 0 and stacks[-1] == "[":
                stacks.pop()
            else:
                stacks.append("-")
                break
    if len(stacks) == 0:
        print("yes")
    else:
        print("no")
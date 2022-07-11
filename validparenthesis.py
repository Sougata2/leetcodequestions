def valid_parenthesis(string):
    if not string or string == ' ':
        return False

    stack = []
    opening = ['[', '(', '{']
    closing = [']', ')', '}']
    for i in range(len(string)):
        if string[i] in opening:
            stack.append(string[i])
        else:
            if not stack:
                return False
            elif string[i] == closing[0] and stack[-1] != opening[0]:
                return False
            elif string[i] == closing[1] and stack[-1] != opening[1]:
                return False
            elif string[i] == closing[2] and stack[-1] != opening[2]:
                return False
            else:
                stack.pop()

    if not stack:
        return True
    else:
        return False


if __name__ == '__main__':
    print(valid_parenthesis('[[]](){]{}'))
    print(valid_parenthesis('{]'))
    print(valid_parenthesis(''))
    print(valid_parenthesis(' '))
    print(valid_parenthesis('()'))
    print(valid_parenthesis("([)]"))
    print(valid_parenthesis("{[]}"))
    print(valid_parenthesis("(("))

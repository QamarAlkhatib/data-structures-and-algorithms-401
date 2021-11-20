from stack_and_queue.stack import Stack

def validate_brackets(str):

    stack = Stack()
    for ch in str:
        if ch in ["(", "{", "["] :
            stack.push(ch)
        else:
            if not stack:
                return False
            current_char = stack.pop()
            if current_char == '(':
                if ch != ")":
                    return False
            if current_char == '{':
                if ch != "}":
                    return False
            if current_char == '[':
                if ch != "]":
                    return False
    # if stack:
    #     return False
    return True


if __name__ == "__main__":
    str = "()"
    #print(string.ascii_letters)
    print(validate_brackets(str))
    # letter = [string.ascii_letters]
    # print(letter)
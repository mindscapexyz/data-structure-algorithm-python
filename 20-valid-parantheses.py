def isValid(s: str) -> bool:
    index = 0
    buffer = []
    complement_parantheses = {
        ")": "(",
        "}": "{",
        "]": "[",
    }
    while index < len(s):
        current_char = s[index]
        if current_char in ["(", "{", "["]:
            buffer.append(s[index])
            index += 1
        elif current_char in [")", "}", "]"]:
            if index == 0:
                return False
            else:
                print(s[index])
                print(s[index - 1])
                if s[index - 1] == complement_parantheses.get(current_char):
                    buffer.pop()
                    index += 1
                else:
                    return False
        else:
            return False
    if buffer == []:
        return True
    else:
        return False


arg = "()[]{}"
result = isValid(arg)
print(result)

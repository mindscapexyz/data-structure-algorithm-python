class Solution:
    def romanToInt(self, s: str) -> int:
        num_value = []
        len_s = len(s)
        index = 0
        cur_index = 0
        while index < len_s:
            char = s[index]
            cur_index = s.index(char)
            if index+1 == len_s:
                next_char = 0
            else:
                next_char = s[index+1]
            match(char):
                case 'I':
                    if next_char == 'V':
                        num_value.append(4)
                        index += 2
                    elif next_char == 'X':
                        num_value.append(9)
                        index += 2
                    else:
                        num_value.append(1)
                        index += 1
                case 'V':
                    num_value.append(5)
                    index += 1
                case 'X':
                    if next_char == 'L':
                        num_value.append(40)
                        index += 2
                    elif next_char == 'C':
                        num_value.append(90)
                        index += 2
                    else:
                        num_value.append(10)
                        index += 1
                case 'L':
                    num_value.append(50)
                    index += 1
                case 'C':
                    
                    if next_char == 'D':
                        num_value.append(400)
                        index += 2
                    elif next_char == 'M':
                        num_value.append(900)
                        index += 2
                    else:
                        num_value.append(100)
                        index += 1
                case 'D':
                    num_value.append(500)
                    index += 1
                case 'M':
                    num_value.append(1000)
                    index += 1
                case _:
                    print("error")
        return sum(num_value)

        
import stack


def base_converter(dec_number, base):
    digits = "0123456789ABCDEF"

    rem_stack = stack.Stack()

    while dec_number > 0:
        rem = dec_number % base
        rem_stack.push(rem)
        dec_number = dec_number // base

    new_string = ""
    while not rem_stack.is_empty():
        new_string = new_string + digits[rem_stack.pop()]

    return new_string


print(base_converter(25, 2))  # Base 2
print(base_converter(29, 16))  # Base 16

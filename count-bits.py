def count_bits(x):
    num_bits = 0
    while x:
        num_bits += x & 1
        x >>= 1
    return num_bits


# 10 bits = 2 decimal
k = count_bits(111)
print(k)

# brute force O(n) solution - iterate through each bit in the input word
def parity_1(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1

    return result


def parity_2(x):
    result = 0
    while x:
        result ^= 1
        x &= x - 1  # Drops the lowest set bit of x
    return result

PRECOMPUTED_PARITY = [parity_1(i) for i in range(1 << 16)]
def parity_3(x):
    MASK_SIZE = 16
    BIT_MASK = 0xFFFF
    return (PRECOMPUTED_PARITY[x >> (3 * MASK_SIZE)] ^  # gets the first 16 bits in x
            PRECOMPUTED_PARITY[(x >> (2 * MASK_SIZE)) & BIT_MASK] ^  #
            PRECOMPUTED_PARITY[(x >> MASK_SIZE) & BIT_MASK] ^
            PRECOMPUTED_PARITY[x & BIT_MASK])

def parity_4(x):
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 1


input1 = 39
print("The parity for {} is {}".format(bin(input1), parity_1(input1)))

input2 = 103941
print("The parity for {} is {}".format(bin(input2), parity_2(input2)))

input3 = 42
print("The parity for {} is {}".format(bin(input3), parity_3(input3)))

input4 = 42
print("The parity for {} is {}".format(bin(input4), parity_4(input4)))
# brute force O(n) solution - iterate through each bit in the input word
def bf_parity(x):
    result = 0
    while x:
        result ^= x & 1
        x >>= 1

    return result

input1 = 39
print("The parity for {} is {}".format(bin(input1), bf_parity(input1)))
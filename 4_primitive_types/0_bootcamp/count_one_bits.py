# we consider a bit set if its value is 1
def count_set_bits(x):
    num_set_bits = 0
    while x:
        num_set_bits += x & 1
        x >>= 1

    return num_set_bits

input1 = 11
print("num_bits for {}: {}".format(bin(input1), count_set_bits(input1)))
input2 = 10
print("num_bits for {}: {}".format(bin(input2), count_set_bits(input2)))
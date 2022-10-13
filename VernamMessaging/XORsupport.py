#converts a string into a binary of 8 bits
def string_2_binary(string: str):
    """Takes a String as input.
    Returns a list of 8-bit binaries of the ASCII value for each letter in the string."""
    #returns a list of binaries of the ASCII value for each letter in the string
    #this also removes the first two elements of each letter which are just '0b', which indicates that it's a binary
    #the zfill method includes zeroes in excess to the length of the element to reach a final size
    #given that the output of bin()[2:] has 7 bits, we need one more to the left
    return [bin(ord(letter))[2:].zfill(8) for letter in str(string)]


#XOR binaries
def xor_binaries(binary1,binary2):
    """Takes two binaries of the same size as input.
    Returns their XOR-ed binary."""
    #XOR it with the key
    return [bin(int(binary1[bit],2)^int(binary2[bit],2))[2:].zfill(8) for bit in range(0,min(len(binary1),len(binary2)),1)];


#converts binaries to strings
def binary_2_string(binary) -> str:
    """Takes a binary as input. Returns its equivalent binary."""
    #the chr function transforms an int into its correspondent ASCII character
    #the int function transforms a number form a base into an int in base 10 (in the case of binaries, base 2)
    return ''.join(chr(int(bit,2)) for bit in binary);
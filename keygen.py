from os import urandom;
from hashlib import sha256;

#generates a pseudorandom key of length kLength
def keygen(kLength,BLOCKSIZE):
    """Generates a pseudorandom key of length kLength
    Uses a nonce to increase the output of the key to the required length
    -Assumes kLength is an integer>0
    Returns a key as a String"""
    #initializes the key
    key="";
    while len(key)<kLength:
        #generates a random key and hashes it
        #sha256 is a pseudorandom function that requires a string formated to utf-8 and outputs ???
        #encode is a method that allows encoding in specific formats, such as utf-8
        #hexdigest is a method that returns the data converted to hexadecimal (the first two characters returned are an indication of a hexadecimal number)
        #int converts the hexadecimal from base 16 to base 10
        key=str(sha256(str(urandom(BLOCKSIZE)).encode('utf-8')).hexdigest()[2:]);
    #truncate the key to have the desired length
    fkey=''.join(key[k] for k in range(kLength));
    return fkey;
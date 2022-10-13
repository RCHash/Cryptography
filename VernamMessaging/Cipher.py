from keygen import keygen;
from XORsupport import string_2_binary, xor_binaries, binary_2_string;

#defines a blocksize (in bytes) so that large files can be read safely
BLOCKSIZE=65536;

#Encrypts using the Vernam Cipher
def vernam_encrypt(plaintext: str) -> dict:
    """ Converts a plaintext to a ciphertext, adding a random key of the same size.
    -Takes a string as an input
    -Returns a dictionary with two keys: ciphertext and key"""
    #converts a string into a binary
    binplaintext=string_2_binary(plaintext);
    #get a rough key
    rough_binkey=string_2_binary(keygen(len(plaintext),BLOCKSIZE));
    #truncate the key to have the same length as the plaintext
    binkey=[];
    for i in range(0,len(binplaintext),1):
        binkey.append(rough_binkey[i]);
    #XOR it with the key
    binciphertext=xor_binaries(binkey,binplaintext);
    #convert the ciphertext back to a string
    ciphertext=binary_2_string(binciphertext);
    #convert the final key to string
    key=binary_2_string(binkey);
    #output ciphertext and key
    return {"ciphertext":ciphertext, "key":key};


#Encrypts using the Vernam Cipher
#FIX THIS
def vernam_decrypt(ciphertext: str, key: str, plaintext_file_output_name: str=None):
    """ Converts a ciphertext and its key into the original plainetxt.
    -Takes two strings of the same size as input
    -Returns a plaintext string"""
    #convert the ciphertext to binary
    bin_ciphertext=string_2_binary(ciphertext);
    #convert the key to binary
    binkey=string_2_binary(key);
    #XOR the ciphertext with the key
    binplaintext=xor_binaries(binkey,bin_ciphertext);
    #convert the result to string
    plaintext=binary_2_string(binplaintext);
    #return the plaintext
    return plaintext;
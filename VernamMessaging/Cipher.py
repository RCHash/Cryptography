from keygen import keygen;
from XORsupport import string2binary, xorbinaries, binary2string;

#defines a blocksize (in bytes) so that large files can be read safely
BLOCKSIZE=65536;

#Encrypts using the Vernam Cipher
def vernam_encrypt(plaintext):
    """ Converts a plaintext to a ciphertext, adding a random key of the same size.
    -Takes a string as an input
    -Returns a dictionary with two keys: ciphertext and key"""
    #converts a string into a binary
    binplaintext=string2binary(plaintext);
    #get a rough key
    roughbinkey=string2binary(keygen(len(plaintext),BLOCKSIZE));
    #truncate the key to have the same length as the plaintext
    binkey=[];
    for i in range(0,len(binplaintext),1):
        binkey.append(roughbinkey[i]);
    #XOR it with the key
    binciphertext=xorbinaries(binkey,binplaintext);
    #convert the ciphertext back to a string
    ciphertext=binary2string(binciphertext);
    #convert the final key to string
    key=binary2string(binkey);
    #output ciphertext and key
    return {"ciphertext":ciphertext, "key":key};

#Encrypts using the Vernam Cipher
#FIX THIS
def vernam_decrypt(ciphertext,key,plaintextfileoutputname=None):
    """ Converts a ciphertext and its key into the original plainetxt.
    -Takes two strings of the same size as input
    -Returns a plaintext string"""
    #convert the ciphertext to binary
    binciphertext=string2binary(ciphertext);
    #convert the key to binary
    binkey=string2binary(key);
    #XOR the ciphertext with the key
    binplaintext=xorbinaries(binkey,binciphertext);
    #convert the result to string
    plaintext=binary2string(binplaintext);
    #return the plaintext
    return plaintext;
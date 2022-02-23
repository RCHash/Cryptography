#Updates from the previous version:
#-allow users to input a string
#-investigate the hash function
#-changed the random function to a better one
#-allow input files - IMPLEMENTED IN THE ENCRYPTION BUT NOT DECRYPTION
#-allow output files - NOT YET IMPLEMENTED

from sys import argv;
from hashlib import sha256;
from os import urandom;

#defines a blocksize (in bytes) so that large files can be read safely
BLOCKSIZE=65536;

def vernam_encrypt(plaintext):
    #updated in version 1
    #convert the plaintext to binary
    binplaintext=string2binary(plaintext);
    #creates a key big enough to encompass the whole plaintext
    binkeytemp=[];
    while len(binkeytemp)<len(binplaintext):
        #generate a random key and hash it - FIX THIS
        #sha256 is a pseudorandom function that requires a string formated to utf-8 and outputs ???
        #encode is a method that allows encoding in specific formats, such as utf-8
        #hexdigest is a method that returns the data converted to hexadecimal
        #int converts the hexadecimal from base 16 to base 10
        key=int(sha256(str(urandom(BLOCKSIZE)).encode('utf-8')).hexdigest()[2:],16);
        #convert the key to binary
        for i in range(0,len(string2binary(key)),1):
            binkeytemp.append(string2binary(key)[i]);
    #truncate the key to have the same length as the plaintext
    binkey=[];
    for i in range(0,len(binplaintext),1):
        binkey.append(binkeytemp[i]);
    #XOR it with the key
    binciphertext=xorbinaries(binkey,binplaintext);
    print("vernam_encrypt: This is the binary ciphertext: "+str(binciphertext));
    #convert the ciphertext back to a string
    ciphertext=binary2string(binciphertext);
    print("vernam_encrypt: This is the ciphertext: "+ciphertext);
    #convert the final key to string
    key=binary2string(binkey);
    #output ciphertext and key
    return {"ciphertext":ciphertext, "key":key};

#FIX THIS
def vernam_decrypt(ciphertext,key):
    #updated in version 1
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

#converts a string into a binary of 8 bits
def string2binary(string):
    #returns a list of binaries of the ASCII value for each letter in the string
    #this also removes the first two elements of each letter which are just '0b', which indicates that it's a binary
    #the zfill method includes zeroes in excess to the length of the element to reach a final size
    #given that the output of bin()[2:] has 7 bits, we need one more to the left
    return [bin(ord(letter))[2:].zfill(8) for letter in str(string)]

#XOR binaries
def xorbinaries(binary1,binary2):
    #XOR it with the key
    return [bin(int(binary1[bit],2)^int(binary2[bit],2))[2:].zfill(8) for bit in range(0,min(len(binary1),len(binary2)),1)];

#converts binaries to strings
def binary2string(binary):
    #the chr function transforms an int into its correspondent ASCII character
    #the int function transforms a number form a base into an int in base 10 (in the case of binaries, base 2)
    return ''.join(chr(int(bit,2)) for bit in binary);

#main function
def main(basefile=None,keyfile=None):
    if basefile==None and keyfile==None:
        string=str(input("Please provide a string as an input: "));
        result=vernam_encrypt(string);
        print(result);
        print("This is the decrypted ciphertext: "+vernam_decrypt(result["ciphertext"],result["key"]));
    elif basefile==None or keyfile==None:
        #file input
        if keyfile==None:
            buf=getfileinfo(basefile);
        if basefile==None:
            buf=getfileinfo(keyfile);
        result=vernam_encrypt(buf);
        print(result);
        print("This is the decrypted ciphertext: "+vernam_decrypt(result["ciphertext"],result["key"]));
    else:
        buf=getfileinfo(basefile);
        #DEVELOP THIS TO DECRYPT THE FILES INSTEAD OF QUITTING
        quit();

def getfileinfo(file):
    with open(file, 'r') as afile:
        buf='';
        for block in afile:
            tempbuf=block;
            buf=buf+tempbuf;
    return buf;

#call main function
if __name__ == '__main__':
    if len(argv)==1:
        basefile=None;
        #TO BE IMPLEMENTED
        #vdecrypt=None;
        #vencrypt=None;
        main();
    elif len(argv)==2:
        basefile=argv[1];
        main(basefile);
    elif len(argv)==3:
        basefile=argv[1];
        keyfile=argv[2];
        main(basefile,keyfile);
    else:
        print("Use: either provide no arguments and enter a string after the prompt or provide a full path file argument for encryption.");
        quit();
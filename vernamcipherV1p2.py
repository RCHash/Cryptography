#Updates from the previous version:
#-allow users to input a string
#-investigate the hash function
#-changed the random function to a better one
#-allow input files - PENDING VERIFICATION (SINGLE FILE CHECKED OK)
#-allow output files - NOT YET IMPLEMENTED

from sys import argv;
from hashlib import sha256;
from os import urandom;
from os.path import exists;

#defines a blocksize (in bytes) so that large files can be read safely
BLOCKSIZE=65536;

def vernam_encrypt(plaintext,basefileoutputname=None,keyfileoutputname=None):
    """ Converts a plaintext to a ciphertext, adding a random key of the same size.
    -Takes a string as an input
    -Returns a dictionary with two keys: ciphertext and key"""
    #converts a string into a binary
    binplaintext=string2binary(plaintext);
    #creates a key big enough to encompass the whole plaintext
    binkeytemp=[];
    while len(binkeytemp)<len(binplaintext):
        #generate a random key and hash it
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
    #convert the ciphertext back to a string
    ciphertext=binary2string(binciphertext);
    #convert the final key to string
    key=binary2string(binkey);
    #output ciphertext and key
    return {"ciphertext":ciphertext, "key":key};

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

#converts a string into a binary of 8 bits
def string2binary(string):
    """Takes a String as input.
    Returns a list of 8-bit binaries of the ASCII value for each letter in the string."""
    #returns a list of binaries of the ASCII value for each letter in the string
    #this also removes the first two elements of each letter which are just '0b', which indicates that it's a binary
    #the zfill method includes zeroes in excess to the length of the element to reach a final size
    #given that the output of bin()[2:] has 7 bits, we need one more to the left
    return [bin(ord(letter))[2:].zfill(8) for letter in str(string)]

#XOR binaries
def xorbinaries(binary1,binary2):
    """Takes two binaries of the same size as input.
    Returns their XOR-ed binary."""
    #XOR it with the key
    return [bin(int(binary1[bit],2)^int(binary2[bit],2))[2:].zfill(8) for bit in range(0,min(len(binary1),len(binary2)),1)];

#converts binaries to strings
def binary2string(binary):
    """Takes a binary as input. Returns its equivalent binary."""
    #the chr function transforms an int into its correspondent ASCII character
    #the int function transforms a number form a base into an int in base 10 (in the case of binaries, base 2)
    return ''.join(chr(int(bit,2)) for bit in binary);

#returns the information from within the file
def getfileinfo(file):
    """Takes a file path as an input. Returns its content as a string."""
    #checks whether the file exists
    if not exists(file):
        print(file+" file does not exist.");
        quit();
    #opens the file
    try:
        with open(file, 'r') as afile:
            #sets the base string
            buf='';
            #for each block in the file, add the content to the string
            for block in afile:
                tempbuf=block;
                buf=buf+tempbuf;
    #if there is an IO Error (something wrong with the file)
    except IOError:
        print(f"Unable to open "+file+"\nProgram terminated.");
        quit();
    #if all is fine with the file
    else:
        #returns the content of the file
        return buf;

#writes on a new file - FIX THE WRITTING PART WITHIN THE "WITH"
def writeinfile(info,filename):
    """Creates a file with the information given in it. It assumes that there is no file with the same name in the same path.
    -Takes the information to be written as a string.
    -Takes the file path and name as a string
    -Returns True if successful and False otherwise."""
    try:
        with open(filename, 'w') as afile:
            #write the information within the file - TO DO
            print("TO DO");
    #if there is an IO Error (something wrong with the file)
    except IOError:
        #error message
        print("Unable to open "+filename);
        #returns failure
        return False;
    #if all is fine with the file
    else:
        #writes within the file
        afile.write(info);
        #returns success
        return True;

#writes information in a new file
def writefileinfo(info,originalfile,ftype):
    """Creates a new file with the information given in it. Makes sure not to overwrite a previously existing file.
    -Takes information to be written in a new file as a string.
    -Takes the original file path and name as a string.
    -Takes the type of file to be written ('p' for plaintext, 'c' for ciphertext and 'k' for key).
    -Returns True if successful.
    -Returns False otherwise."""
    #for valid file types
    if ftype=='c' or ftype=='p' or ftype=='k':
        #increments the original file name
        file=originalfile.join(ftype);
        #while there is a file with the incremented name, cycle through the possibilities
        i=1;
        while exists(file.join(i)):
            #increments i
            i+=1;
        #writes within the file
        if writeinfile(info,file):
            #returns success
            return True;
        else:
            #failure message
            print("Cannot write within "+file);
            #returns failure
            return False;
    #if the wrong file type argument is entered
    else:
        #notifies of wrong argument value
        print("Invalid file type argument for the writefileinfo function.");
        #returns failure
        return False;

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
        #encrypts the file's information
        result=vernam_encrypt(buf);
        print(result);
    else:
        #CHECK THIS
        buf1=getfileinfo(basefile);
        buf2=getfileinfo(basefile);
        #decrypts the files' information
        result=vernam_decrypt(buf1,buf2);
        print(result);

#call main function
if __name__ == '__main__':
    if len(argv)==1:
        basefile=None;
        main();
    elif len(argv)==2:
        basefile=argv[1];
        main(basefile);
    elif len(argv)==3:
        basefile=argv[1];
        keyfile=argv[2];
        main(basefile,keyfile);
    else:
        print("Use: either provide no arguments and enter a string after the prompt or provide a full path file argument for encryption. The user may provide either one or two files. In the first case, the file is considered the plaintext. In the second case, one file is considered the ciphertext and the second, the key.");
        quit();
#Updates from the previous version:
#-allow users to input a string
#-investigate the hash function
#-changed the random function to a better one
#-allow input files - PENDING VERIFICATION (SINGLE FILE CHECKED OK)
#-allow output files - PENDING VERIFICATION

from sys import argv;
from os.path import exists;
from XORsupport import string_2_binary, xor_binaries, binary_2_string
from filemanipulation import get_file_info, write_in_file, write_file_info
from Cipher import vernam_encrypt, vernam_decrypt

#main function
def main(basefile: str=None,keyfile: str=None):
    if basefile==None and keyfile==None:
        string=str(input("Please provide a string as an input: "));
        result=vernam_encrypt(string);
        print(result);
        print("This is the decrypted ciphertext: "+vernam_decrypt(result["ciphertext"],result["key"]));
    elif basefile==None or keyfile==None:
        #file input
        if keyfile==None:
            buf=get_file_info(basefile);
        if basefile==None:
            buf=get_file_info(keyfile);
        #encrypts the file's information
        result=vernam_encrypt(buf);
        print(result);
    else:
        #CHECK THIS
        buf1=get_file_info(basefile);
        buf2=get_file_info(basefile);
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
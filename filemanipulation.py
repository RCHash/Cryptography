from os.path import exists;

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

#writes on a new file
def writeinfile(info,filename):
    """Creates a file with the information given in it. It assumes that there is no file with the same name in the same path.
    -Takes the information to be written as a string.
    -Takes the file path and name as a string
    -Returns True if successful and False otherwise."""
    try:
        with open(filename, 'w') as afile:
            #write the information within the file - TO DO
            afile.write(info);
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
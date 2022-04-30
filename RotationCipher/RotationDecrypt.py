def RotDecrypt(ciphertext,wordListFileName):
    """
    Assumes the ciphertext is a string
    Breaks the cryptography if it is a simple rotation cipher
    Returns the best match for the plaintext
    """
    #loads words from the dictionary
    wordList=loadWords(wordListFileName);
    #cycle through the letters of the alphabet
    bestMatch=0;
    plaintext="";
    for i in range (26):
        #cycle through the ciphertext and create a shifted text
        shiftedText="";
        for element in ciphertext:
            raise NotImplementedError; #MISSING DIFFERENT CHARACTER HANDLER
            #move it to the right by i characters
            shiftedText.join(letterShifter(element,i));
        #separate it in words
        shiftedList=wordSeparator(shiftedText);
        #compare it to a dictionary for matches
        for word in shiftedList:
            if isValidWord(word):
                counter=counter+1;
        if counter>bestMatch:
            bestMatch=counter;
            plaintext=shiftedText;
    if bestMatch>0:
        return plaintext;
    else:
        return None;

def wordSeparator(text):
    """
    Assumes text is a string
    Separates the text into words
    Does not care whether the word is actually a word
    Returns a list of the words contained in text
    """
    #initializes the words list
    words=[];
    #cycles through the letters
    for letter in range(0,len(text),1):
        if (letter>0):
            raise NotImplementedError; #MISSING
        #SEEK A BETTER WAY TO COMPARE
        #if (text[letter]==" " or text[letter]==" ")

def loadWords(wordListFileName):
    """
    Assumes wordlist filename is a valid textfile with one word in each row
    Converts the words in the file into a list of words
    Returns the list of words
    Depending on the word list size, this may take a while to complete
    """
    print("Loading word list from file")
    # inFile: file
    inFile = open(wordListFileName, 'r');
    # wordList: list of strings
    wordList = [];
    for line in inFile:
        wordList.append(line.strip().lower());
    inFile.close();
    print("  ", len(wordList), "words loaded.");
    return wordList;

def isValidWord(word, wordList):
    """
    Assumes word is a string
    Assumes wordList is a list of strings
    Returns True if word is in the wordList; otherwise, returns False
    Does not mutate hand or wordList
    """
    #checks whether the word is in wordlist
    if word in wordList:
        #if not, return false
        return True;
    else:
        return False;

def letterShifter(letter,shift):
    """
    Assumes letter is a single alphabetic digit in unicode
    Assumes is an integer and 0<=shift<=26
    Shifts the letter by shift positions
    Returns the new letter
    """
    #figures whether the letter is upper or lower case
    if letter.upper()==letter:
        caps=True;
    else:
        caps=False;
    #returns the unicode number equivalent to the lower-cased letter
    order=ord(letter.lower());
    if (order+shift<=122):
        order=order+shift;
    else:
        order=96+shift-(122-order);
    #adjusts the case
    if caps:
        newLetter=chr(order).upper();
    else:
        newLetter=chr(order);
    return newLetter;
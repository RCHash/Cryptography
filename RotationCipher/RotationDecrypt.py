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
    bestMatchShift=0;
    for shift in range (26):
        #cycle through the ciphertext and create a shifted text
        shiftedText="";
        for element in ciphertext:
            #move it to the right by i characters
            if (ord(element)>=97 and ord(element<=122) or (ord(element)>=65 and ord(element)<=90)):
                shiftedText.join(letterShifter(element,shift));
            else:
                shiftedText.join(element);
        #separate it in words
        shiftedList=wordSeparator(shiftedText);
        #compare it to a dictionary for matches
        for word in shiftedList:
            if isValidWord(word):
                counter=counter+1;
        if counter>bestMatch:
            bestMatch=counter;
            plaintext=shiftedText;
            bestMatchShift=shift;
    if bestMatch>0:
        return (plaintext,bestMatchShift);
    else:
        return None;

def wordSeparator(text): #MISSING IMPLEMENTATION
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
    Assumes wordlist filename is a valid textfile with all words in the
     same row, each separated by a single space
    Converts the words in the file into a list of words
    Returns the list of words
    Depending on the word list size, this may take a while to complete
    """
    print("Loading word list from file...")
    # inFile: file
    inFile = open(wordListFileName, 'r');
    # wordList: list of strings
    wordList = [];
    # line: string
    line = inFile.readline();
    # wordlist: list of strings
    wordList = line.split();
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

wordListFileName="englishWords.txt";
testString="Glcr gur jbeq 'frphevgl' orybj sbe n serr cbvag."
loadWords(wordListFileName);
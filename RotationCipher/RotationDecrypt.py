def RotDecrypt(ciphertext: str,wordListFileName: str):
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
            if (ord(element)>=97 and ord(element)<=122) or (ord(element)>=65 and ord(element)<=90):
                shiftedText=shiftedText+letterShifter(element,shift);
            else:
                shiftedText=shiftedText+element;
        #separate it in words
        shiftedList=wordSeparator(shiftedText);
        #compare it to a dictionary for matches
        counter=0;
        for word in shiftedList:
            if isValidWord(word,wordList):
                counter=counter+1;
        if counter>bestMatch:
            bestMatch=counter;
            plaintext=shiftedText;
            bestMatchShift=shift;
    if bestMatch>0:
        return (plaintext,bestMatchShift);
    else:
        return None;

def wordSeparator(text: str): #MISSING IMPLEMENTATION
    """
    Assumes text is a string
    Separates the text into words
    Does not care whether the word is actually a word
    Returns a list of the words contained in text
    """
    #initializes the words list
    words=[];
    #initializes the list of alphabetical letters
    alphaLetters=[];
    for i in range(0,26,1):
        alphaLetters.append(chr(97+i));
        alphaLetters.append(chr(65+i));
    #cycles through the letters
    booleanDigitList=[];
    for letter in range(0,len(text),1):
        #mark them whether they're actual letters
        if (text[letter] in alphaLetters):
            booleanDigitList.append(True);
        else:
            booleanDigitList.append(False);
    #compose words with the boolean list
    word="";
    for i in range(0,len(text),1):
        if booleanDigitList[i]:
            word=word+text[i];
        elif booleanDigitList[i] and i==len(text)-1:
            if len(word)>0:
                words.append(word);
        else:
            if len(word)>0:
                words.append(word);
            word="";
    return words;

def loadWords(wordListFileName: str) -> list:
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

def isValidWord(word: str, wordList: list) -> bool:
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

def letterShifter(letter: str, shift: int) -> str:
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

#test code
wordListFileName="englishWords.txt";
testString="Frphevgl vf abg n fgebat srngher bs guvf zrffntr, vf vg?"
print(RotDecrypt(testString,wordListFileName));
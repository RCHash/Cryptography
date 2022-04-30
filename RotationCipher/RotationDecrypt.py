def RotDecrypt(ciphertext):
    """
    Assumes the ciphertext is a string
    Breaks the cryptography if it is a simple rotation cipher
    Returns the best match for the plaintext
    """
    #cycle through the letters of the alphabet
    bestMatch=0;
    plaintext="";
    for i in range (26):
        #cycle through the ciphertext
        for element in ciphertext:
            #move it to the right by i characters
            #MISSING
            #separate it in words
            #MISSING
            #compare it to a dictionary for matches
            #MISSING
            if curretMatches>bestMatch:
                bestMatch=currentMatch;
                plaintext=decryptedText;
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
        #SEEK A BETTER WAY TO COMPARE
        if (letter==" " or letter==" ")


#testcode
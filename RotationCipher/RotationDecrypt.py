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

    for element in text:


#testcode
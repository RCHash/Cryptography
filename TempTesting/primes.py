import random;

def gcd(a, b):
    """
    a, b: two positive integers
    Returns the greatest common divisor of a and b
    """
    if max(a,b)%min(a,b)==0:
        return min(a,b);
    else:
        return gcd(min(a,b),max(a,b)%min(a,b));

def genCoprime(phiN,rand=False):
    """
    assumes phiN is a positive integer
    returns the set of numbers k from 2 to phiN-1 such that k and phiN are coprimes
    """
    kl=[];
    for k in range(2,phiN,1):
        if (gcd(k,phiN)==1):
            kl.append(k);
    if rand and len(kl)>1:
        return random.choice(kl);
    else:
        return kl;

def isPrime(number):
    """
    assumes number is a positive integer
    returns whether a number is prime or not
    """
    prime=True;
    for n in range(2,int(number**0.5)+1,1):
        if number%n==0:
            prime=False;
            break;
    return prime;

def genRandomPrime(size):
    """
    returns a random prime of size number of digits
    """
    testNumber=random.randint(10**size,10**(size+1));
    while (not isPrime(testNumber)):
        testNumber=random.randint(10**size,10**(size+1));
    return testNumber;

def isPrimeDynProg(number,filePath):
    """
    assumes number is a positive integer
    assumes filePath is the file path to the database of primenumbers
     with each row containing one prime number
    returns whether a number is prime or not
    """
    #check for number's being prime
    prime=True;
    for num in primes:
        if number&num==0:
            prime=False;
    return prime;

def genPrimes(topNumber,filePath):
    """
    assumes topNumber is a positive integer
    assumes filePath is the file path to the database of primenumbers
     with each row containing one prime number
    updataes the primes file with primes up to topNumber
    returns the updated list of primes
    """
    #loads primes
    inFile=open(filePath,'r');
    #load a list of primes
    primes=[];
    for line in inFile:
        primes.append(int(line));
    inFile.close();
    #stores the number of primes
    numPrimes=len(primes);
    #generates primes, if necessary
    if primes[-1]<topNumber:
        for num in range(primes[-1]+1,topNumber+1,1):
            if isPrime(num):
                primes.append(num);
    #if there are new primes, update the primes database
    if numPrimes<len(primes):
        inFile=open(filePath,'w');
        for i in range(numPrimes,len(primes)+1,1):
            inFile.write(primes[i]);
        inFile.close();
    return primes;
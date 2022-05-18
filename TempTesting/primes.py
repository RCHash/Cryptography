import random;

FILEPATH="/home/user/Documents/Dev/TempTesting/primes.txt";

def gcd(a: int, b: int) -> int:
    """
    assumes a and b as two positive integers
    Returns the greatest common divisor of a and b
    """
    if max(a,b)%min(a,b)==0:
        return min(a,b);
    else:
        return gcd(min(a,b),max(a,b)%min(a,b));

def genCoprime(phiN: int,rand: bool=False) -> list:
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

def isPrime(number: int) -> bool:
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

def genRandomPrime(size: int) -> int:
    """
    assumes size is a positive integer
    returns a random prime of size number of digits
    """
    testNumber=random.randint(10**size,10**(size+1));
    while (not isPrime(testNumber)):
        testNumber=random.randint(10**size,10**(size+1));
    return testNumber;

def genRandomPrimeDynProg(size: int,filePath: str=FILEPATH) -> int:
    """
    assumes size is a positive integer
    assumes filePath is the file path to the database of primenumbers
     with each row containing one prime number
    returns a random prime of size number of digits using dynamic programming
    """
    raise NotImplemented('not yet implemented');
    #check whether the range is within the mapped primes
    #if not, check whether it is prime

def isPrimeDynProg(number:int,filePath: str=FILEPATH) -> bool:
    """
    assumes number is a positive integer
    assumes filePath is the file path to the database of primenumbers
     with each row containing one prime number
    returns whether a number is prime or not
    """
    #get the prime list
    primes=genPrimes(int(number**0.5),filePath=FILEPATH);
    #check for number's being prime
    prime=True;
    for num in primes:
        if number&num==0:
            prime=False;
    return prime;

def genPrimes(topNumber: int,filePath: str=FILEPATH) -> list:
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
    if numPrimes==0:
        for num in range(2,topNumber+1,1):
            if isPrime(num):
                primes.append(num);
    elif primes[-1]<topNumber+1:
        for num in range(primes[-1]+1,topNumber+1,1):
            if isPrime(num):
                primes.append(num);
    #if there are new primes, update the primes database
    if numPrimes<len(primes):
        inFile=open(filePath,'a');
        for i in range(numPrimes,len(primes),1):
            inFile.write(str(primes[i])+"\n");
        inFile.close();
    return primes;
 
if __name__=="__main__":
    # print(isPrimeDynProg(4000000000));
    pass;
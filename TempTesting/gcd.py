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

a=genCoprime(341,True);
print(a);
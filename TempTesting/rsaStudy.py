#Key-pair generation: generate a random private key and public key (the size is 1024-4096 bits).
#Encryption: It encrypts a secret message (integer in the range [0…key_length]) using the public key and decrypts it back using the secret key.
#Digital signatures: sign messages (using the private key) and verify message signature (using the public key).
#Key exchange: It securely transports a secret key used for encrypted communication.

#procedure for key generation
#1-Choose two different large random prime numbers p and q - OK
#2-Calculate n = p*q - OK
#3-n is the modulus for the public key and the private keys - OK
#4-Calculate  ϕ ( n ) = ( p − 1 )*( q − 1 ) - OK
#5-Choose an integer k such that 1 < k  < ϕ ( n ) and k is co-prime to ϕ ( n ) - OK
#6-k is released as the public key exponent - OK
#7-Compute d  to satisfy the  d*k ≡ 1 ( mod ϕ ( n ) )  i.e.: d*k = 1 + x * ϕ( n ) for some integer x
# that is, d = x * ϕ( n ) / k for the smallest x - OK
#8-d is kept as the private key exponent - OK

#INVESTIGATE ENCRYPTION AND DECRYPTION

import primes;

def dCalc(phiN: int, k: int) -> int:
    """
    calculates the secret key d
    """
    testVar=phiN+1;
    while (testVar%k!=0):
        testVar+=phiN;
    d=testVar;
    return d;

def rsaEncrypt(plaintext: str, e, n: int):
    """
    assumes m is a message integer
    assumes n is the product of p and q, two large prime numbers
    assumes e is
    """
    raise NotImplemented('not implemented');

def rsaDecrypt(ciphertext: str) -> str:
    """
    assumes ciphertext is encrypted with rsa
    """
    raise NotImplemented('not implemented');

message="secret message";

p=primes.genRandomPrime(2);
q=primes.genRandomPrime(2);
n=p*q; #n: modulus for the public key and the private keys
phiN=(p-1)*(q-1); #ϕ(n):
k=primes.genCoprime(phiN,True);
d=dCalc(phiN,k);
print("p=",str(p),"q=",str(q));
print("pk=",str(k),"sk=",str(d));

#algorithms to break RSA
#FERMAT
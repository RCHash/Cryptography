#Key-pair generation: generate a random private key and public key (the size is 1024-4096 bits).
#Encryption: It encrypts a secret message (integer in the range [0…key_length]) using the public key and decrypts it back using the secret key.
#Digital signatures: sign messages (using the private key) and verify message signature (using the public key).
#Key exchange: It securely transports a secret key used for encrypted communication.

#procedure for key generation
#1-Choose two different large random prime numbers p and q
#2-Calculate n = p*q
#3-n is the modulus for the public key and the private keys
#4-Calculate  ϕ ( n ) = ( p − 1 )*( q − 1 ) for the special case of prime numbers p and q
#5-Choose an integer k such that 1 < k < ϕ ( n ) and k is co-prime to ϕ ( n )
#6-k is released as the public key exponent and together with n becomes the public key
#7-Compute d to satisfy the  d*k mod ϕ ( n ) = 1  i.e.: d*k = 1 + x * ϕ( n ) for some integer x
# that is, d = x * ϕ( n ) / k for the smallest x
#8-d is kept as the private key exponent

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

#encryption takes place by:
#1- convert a plaintext message M to a number (usually with base64)
#2- add a padding to M by processing pad(num(M)), preferably OAEP,
# but PKCS#1 v1.5 should suffice for not very secure applciations
#3- calculate pad(num(M))^d mod n = C, where C is the ciphertext

#decryption takes place by:
#1- calculate C^k mod n = pad(num(M));
#2- remove the padding by unpadding unpad(pad(num(M))) = num(M);
#3- convert the number back into a message M

#algorithms to break RSA
#FERMAT
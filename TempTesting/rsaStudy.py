#Key-pair generation: generate a random private key and public key (the size is 1024-4096 bits).
#Encryption: It encrypts a secret message (integer in the range [0…key_length]) using the public key and decrypts it back using the secret key.
#Digital signatures: sign messages (using the private key) and verify message signature (using the public key).
#Key exchange: It securely transports a secret key used for encrypted communication.

import random;
import math;

message="secret message";
m="";
for character in message:
    m=m+str(ord(character));
m=int(m);
print(m);
p=random.randint(100,1000);
q=random.randint(100,1000);
e=random.randint(3,51);
n=p*q;
def rsaEncrypt(m,e,n):
    powerMessage=math.pow(m,e);
    ciphertext=powerMessage%n;
    return ciphertext;

def rsaDecrypt(ciphertext):
    pass;

print(rsaEncrypt(m,e,n));
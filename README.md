# Cryptography
Cryptographic applications meant to be useful
# Content
1. Vernam Cipher

The Vernam Cipher (AKA One-Time Pad) is a cipher in which the key is at least as long as the plaintext. If there is sufficient entropy in the key generation, the ciphertext is theoretically unbreakable.

There is a catch, however, associated with this cipher, which is usually the reason for not adopting it instead of other cryptographic algorithms.
The output of this cipher is twofold: the ciphertext itself and the key. The only way to actually decrypt it is to apply the algorithm 'backwards' with the key generated for that specific ciphertext (not even the person who encrypted would be able to decrypt it without the key - a detail that we'll address again latter).
Also, using the same key twice is extremely problematic, as it allows adversaries to apply attacks otherwise impossible against this cipher, such as the dictionary attack, by applying XOR to a pair of ciphertexts encrypted with the same key.
This means that communication with a Vernam Cipher demands both the ciphertext and its unique key to be delivered to the recipient. In this case, if an adversary gets them both, he is able to decrypt the message, making the encryption pointless against anyone with a minimum cryptographic knowledge.
On the other hand, if you have a secure enough communication channel through which you can send the key through without having to worry about adversaries, it also means that the encryption would be pointless for having this resource would allow you to send the plaintext message with the same level of security.

1.1. Secure Files with the Vernam Cipher

There is a potential application of the Vernam Cipher other than the fun and educational: when you are both the sender and the recipient.
In this case, you wouldn't need a communication channel with the recipient, as both are the same person.

"So what?", you could say. Well, if you want sensitive information of yours kept private even when an adversary gets his hands on your files, having them secured with this cipher and stored in different places would be a way to prevent the adversary from touching the sensitive information itself.

This means that applying this cipher for the indended purpose also requires a clever file storage architecture that will foil the adversary's attack on the senstive information. Not only that, it also requires your thinking about having a way to retrieve the sensitive information file-piece yourself once it's been stolen for, remember, not even you can break the cipher without the key (and having just the key is also pointless).

There are at least two side effects of this. One is that the cipher requires double the amount of space required to simply store the plaintext (for the key needs to be at least of the same size of the plaintext).
Two is that despite the real world application, it may be complex to use for this indended purpose if applied to a large amount of files (bear in mind that despite not being able to decrypt the ciphertext without the key, having two different ciphertexts with sufficiently similar keys still allows some attacks to partially succeed, i.e. revealing part of the plaintexts, and having many files encrypted increases the chance of resemblance between pairs of files).
Although qualitatively speaking, these two side effects entail that this kind of application should be reserved for a small quantity of files with a small enough size.

1.2. Secure Communication with the Vernam Cipher

Another way to use the Vernam Cipher is to use it for secure communications. This may seem contradictory with the above information, but it isn't. It works relying not on a secure communication channel, but on a single secure message. If a single secure message can be transfered between two parties, all further communication can be made relatively secure with the Vernam Cipher, still making it impossible for an adversary to decrypt the messages, but introducing other kinds of vulnerabilities.

More info later on.

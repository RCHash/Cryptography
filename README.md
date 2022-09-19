<style>
    br
    {
        line-height:10px;
    }
    h1, h2, h3, h4
    {
        font-weight:bold;
    }
</style>
<h1>Cryptography</h1>
Cryptographic applications meant to be useful
<h2>Content</h2>
<h3>1. Vernam Cipher:</h3>
    <p>The Vernam Cipher (AKA One-Time Pad) is a cipher in which the key is at least as long as the plaintext. If there is sufficient entropy in the key generation, the ciphertext is theoretically unbreakable.</p>
    <p>There is a catch, however, associated with this cipher, which is usually the reason for not adopting it instead of other cryptographic algorithms.</p>
    <p>The output of this cipher is twofold: the ciphertext itself and the key. The only way to actually decrypt it is to apply the algorithm 'backwards' with the key generated for that specific ciphertext (not even the person who encrypted would be able to decrypt it without the key - a detail that we'll address again latter).</p>
    <p>Also, using the same key twice is extremely problematic, as it allows adversaries to apply attacks otherwise impossible against this cipher, such as the dictionary attack, by applying XOR to a pair of ciphertexts encrypted with the same key.</p>
    <p>This means that communication with a Vernam Cipher demands both the ciphertext and its unique key to be delivered to the recipient. In this case, if an adversary gets them both, he is able to decrypt the message, making the encryption pointless against anyone with a minimum cryptographic knowledge.</p>
    <p>On the other hand, if you have a secure enough communication channel through which you can send the key through without having to worry about adversaries, it also means that the encryption would be pointless for having this resource would allow you to send the plaintext message with the same level of security.</p>

<h4>1.1. Secure Files with the Vernam Cipher</h4>
    <p>There is a potential application of the Vernam Cipher other than the fun and educational: when you are both the sender and the recipient.</p>
    <p>In this case, you wouldn't need a communication channel with the recipient, as both are the same person.</p>
    <p>"So what?", you could say. Well, if you want sensitive information of yours kept private even when an adversary gets his hands on your files, having them secured with this cipher and stored in different places would be a way to prevent the adversary from touching the sensitive information itself.</p>
    <p>This means that applying this cipher for the indended purpose also requires a clever file storage architecture that will foil the adversary's attack on the senstive information. Not only that, it also requires your thinking about having a way to retrieve the sensitive information file-piece yourself once it's been stolen for, remember, not even you can break the cipher without the key (and having just the key is also pointless).</p>
    <p>There are at least two side effects of this. One is that the cipher requires double the amount of space required to simply store the plaintext (for the key needs to be at least of the same size of the plaintext).</p>
    <p>Two is that despite the real world application, it may be complex to use for this indended purpose if applied to a large amount of files (bear in mind that despite not being able to decrypt the ciphertext without the key, having two different ciphertexts with sufficiently similar keys still allows some attacks to partially succeed, i.e. revealing part of the plaintexts, and having many files encrypted increases the chance of resemblance between pairs of files).</p>
    <p>Although qualitatively speaking, these two side effects entail that this kind of application should be reserved for a small quantity of files with a small enough size.</p>
    <p>The code provided here is intended to allow this very application. Although it should work fine on a terminal, maybe I'll work on a GUI version of it in the future. Anyone is welcome to contribute.</p>

<h4>1.2. Secure Communication with the Vernam Cipher:</h4>
    <p>Another way to use the Vernam Cipher is to use it for secure communications. This may seem contradictory with the above information, but it isn't. It works relying not on a secure communication channel, but on a single secure message. If a single secure message can be transfered between two parties, all further communication can be made relatively secure with the Vernam Cipher, still making it impossible for an adversary to decrypt the messages directly, but introducing other kinds of vulnerabilities.</p>
    <p>It works as follows. A single message is securely delivered to a recipient other than the sender. This takes the communication channel, whichever it is, to be secure for the purpose of sending that particular message (it may be unreliable for all other messages without a problem, though). The content of the message either has the method to derive all further keys related to future messages or simply the method associated with the key for the next message (of course there can be variations such as having a message contain the method for deriving keys for a limited amount of future messages). This entails not having to send the key to the recipient for all messages after the first, making whatever communication channel useful for sending encrypted messages without fear of their being decrypted directly (even by brute force attacks).</p>
    <p>As a clarification, the method to derive all further keys, above, should be understood as the combination of key-generating algorithms and key seeds.</p>

<h4>1.3. Challenges:</h4>
    <p>It goes without saying that this application of the Vernam Cipher comes with its challenges and also requires careful thinking and design. Despite being possible to use the code already provided here to apply this approach, it is rather laborious to do so as it is. Maybe in the future I'll work on a communication app that uses this approach. Anyone is welcome to contribute as well.</p>
    <p>However, there are two issues with the proposed idea. First and foremost, the first secure message itself, which has to be securely delivered. If an adversary can intercept it, he will also be able to decrypt other messages as well. The second is the method selected for deriving further keys; if it is changed at every message, there is a lot more work associated with it, but adversaries with the first message who aren't able to intercept one message after that won't be able to read messages beyond the one they missed; if it is one method for deriving all future keys, communication tends to flow much faster at the cost of an adversary with the first message being able to decrypt all future messages, regardless of having missed one or more.</p>
    <p>An adversary with knowledge of this method's being in use could also try to use a specific key generating method to brute-force the key. In order to prevent that, two countermeasures are suggested.</p>
    <p>First, a design measure is that this communication method should not, <i>a priori</i>, rely on a single key-generating algorithm (SHA256 is used as a key generating algorithm here just to prove the method works). This would increase the difficulty of brute-forcing the key.</p>
    <p>Second, the key seed should not be something trivial or easily obtainable through the use of a dictionary. Brute-force adversaries often employ dictionary attacks before attempting to brute-force, as this would more often succeed in breaking encryption, relying on the fact that the seed is somehow weak. For generating strong seeds, one could think of many good ways, such as those for generating strong passwords.</p>
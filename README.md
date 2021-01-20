# Elgamal-Algorithm
Elgamal Encryption 

The ElGamal encryption system is a public key encryption algorithm by Taher Elgamal  in 1985 that is based on the Diffie-Hellman key exchange. We assume that the message 
m
 that Alice encrypts and sends to Bob is an integer. We describe the three components of ElGamal encryption, namely key generation, encryption, and decryption.
 
 ### Bob: Key Generation
 To generate his private key and his public key Bob does the following.
 
 1. Bob choose a prime ***p*** and a generator    ![](https://latex.codecogs.com/svg.latex?g%5Cin%20%5Cmathbb%7BZ%7D%5E%7B%5Cbigotimes%20%7D_%7B%5Cmathit%7Bp%7D%7D).
 2. Bob chooses a random ![](https://latex.codecogs.com/svg.latex?%5Cmathit%7Bb%7D%5Cin%20%5Cmathbb%7BN%7D).
 3. Bob computes ![](https://latex.codecogs.com/svg.latex?%5Cmathbf%7B%5Cmathit%7BB%7D%7D%3D%5Cmathit%7Bg%5E%7B%5Cmathit%7Bb%7D%5Cbigotimes%7D%20%7D) in ![](https://latex.codecogs.com/svg.latex?%28%5Cmathbb%7BZ%7D%5E%7B%5Cbigotimes%20%7D_%7B%5Cmathit%7Bp%7D%7D%2C%20%5Cbigotimes%20%29).
 4. Bob publieshed his public key ***p*** , ***g***, ***B*** in the key directory.
 
 
### Alice: Encryption
To encrypt a message ![](https://latex.codecogs.com/svg.latex?m%5Cin%20%5Cmathbb%7BZ%7D_%7Bp%7D%5E%7B%5Cbigotimes%20%7D) Alice does the following.

1. Alice gets Bob's public key ***p***, ***g***, ***B*** from the key directory.
2. Alice chooses a random ![](https://latex.codecogs.com/svg.latex?a%5Cin%20%5Cmathbb%7BN%7D).
3. Alice computes the shared secret ![](https://latex.codecogs.com/svg.latex?s%3DB%5E%7Ba%5Cbigotimes%20%7D).
4. Alice computes ![](https://latex.codecogs.com/svg.latex?A%3Dg%5E%7Ba%5Cbigotimes%20%7D).
5. Alice encrypts ***m*** by computing ![](https://latex.codecogs.com/svg.latex?%5Cmathit%7BX%7D%3Dm%5Cbigotimes%20s).
6. Alice sends (***A, X***) to Bob.


### Bob: Decryption
The information available to Bob to decrypt a message are his private key ***b*** and his public key consisting of the prime ***p***, the generator ***g***, and ![](https://latex.codecogs.com/svg.latex?%5Cmathit%7B%5Ctextit%7B%7D%5Cmathit%7BB%7D%3Dg%5E%7Bb%7D%7D). To decrypt a message ***(A,X)*** Bos does the following. 

1. Bob receives (***A, X***) from Alice.
2. Bob computes the shared secret ![](https://latex.codecogs.com/svg.latex?s%3DA%5E%7Bb%5Cbigotimes%20%7D).
3. Bob computes the inverse ![](https://latex.codecogs.com/svg.latex?s%5E%7B-1%5Cbigotimes%20%7D) of ***s*** in ![](https://latex.codecogs.com/svg.latex?%28%5Cmathbb%7BZ%7D%5E%7B%5Cbigotimes%20%7D_%7Bp%7D%2C%20%5Cbigotimes%20%29).
4. Bob decrypts the message by computing ![](https://latex.codecogs.com/svg.latex?%5Cmathbf%7B%5Cmathit%7BM%7D%7D%3D%5Cmathbf%7B%5Cmathit%7BX%7D%7D%5Cbigotimes%20s%5E%7B-1%5Cbigotimes%20%7D).


We now show that the message ***M*** received by Bob is equal to Alice's plain text message ***M***. We have ![](https://latex.codecogs.com/svg.latex?%5Cinline%20%5Cmathbf%7B%5Cmathit%7BM%7D%7D%3D%5Cmathbf%7B%5Cmathit%7BX%7D%7D%5Cbigotimes%20s%5E%7B-1%5Cbigotimes%20%7D%3D%28m%5Cbigotimes%20s%29%5Cbigotimes%20s%5E%7B-1%5Cbigotimes%20%7D%3Dm%5Cbigotimes%20%28s%5Cbigotimes%20s%5E%7B-1%5Cbigotimes%20%7D%29%3Dm%5Cbigotimes%201%20%3D%20m).

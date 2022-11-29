# cryptosystem
A cryptosystem is a structure or scheme consisting of a set of algorithms that converts plaintext to ciphertext to encode or decode messages securely. it ensures Confidentiality,Integrity,Authenticity between the sender and recipient  and can verify each other’s identities and the destination of the message.

## About the project 
This project deals with encryption and decryption,the former means to change a plain text to a cipher text whereas the latter is the reverse of encryption.The main goal of encryption is for security and prevention of unauthorized access to the information,so in this project we presented the 3 types of cryptosystems namely affine,transposition and RSA.


### Affine cryptosystem
This is a type of monoalphabetic substitution cipher,where each letter in an alphabet is mapped to its numeric equivalent, encrypted using a simple mathematical function, and converted back to a letter.
#### How does it work:
1,The user inputs 2 keys and the input check function(in this function we used the sys module) will check if both keys are greater than zero,one of the keys is less than the length of the alphabet list and also one of the keys and the length of our alphabet list has a gcd of 1

2,Then after checking the keys,the user will enter those valid keys along with the data to be encrypted into the encryption function

3,The encryption function first calls the input check function and checks the keys validity then it performs 2 main tasks,the first is it searches for each letter in our data inside the alphabet list and returns the index each letter is found on.Second,it substitutes the keys and the index of the letters in ax+b mod len(alphabet list) equation and the solution will be the index of each of the letters of the resulting encrypted text(the letters for the encrypted text are taken from the alphabet list)

4,For decryption the user will still call the input check function but additionally it will input the length of the alphabet list and that one key the input check function checked for us then the inverse fuction will perform the modular inverse of the key and the decryption function will takes the 2 keys, the modular inverse of the other key and the data to be decrypted and it will substitute it in a^-1(x-b) mod len(alphabet list)equation and the solution will be the index of each of the letters of the resulting decrypted text(the letters for the decrypted text are taken from the alphabet list)  

5,The main function-in this function the user inputs the data to be encrypted or decrypted,the encryption keys and chooses the mode,which means the user gets to choose if he or she wants the data to be encrypted or decrypted and based on the user's preference the encryption or decryption function will be called and the output will be displayed to the user at the end of the execution.

#### How does it works
1 the program accepts input from the user such as 

a. data- which can be plaintext or ciphertext to be encrypted or decrypted using the function within the class

b. key - which is int represents the number of columns when input data is put row by row

c. mode - which is string which allows us to choose between which function gets called (Encryption or Decryption ) within the main function using conditional statement.

2  Encryption function - after input data is put out in a grid using iteration where the number of columns is equal to key this function starts to read down the columns in order and returns the encrypted(cipher) text.

3  Decryption function - this function work out the column lengths by dividing the length of the input data by the key using iteration and then write the input data out in columns again, then re-order the columns by reforming the key word.

4 main function - when this function gets called it performs the code within the encryption or decryption function as they gets called based on the mode we choose


### RSA 
The RSA algorithm is an asymmetric cryptography algorithm; this means that it uses a public
key and a private key (i.e two different, mathematically linked keys). As their names suggest,
a public key is shared publicly, while a private key is secret and must not be shared with
anyone.
The RSA algorithm is named after those who invented it in 1978: Ron Rivest, Adi Shamir,
and Leonard Adleman.
How it works
The RSA algorithm ensures that the keys are as secure as possible. The following steps highlight how it works:
1. Generating the keys

● Select two large prime numbers, let's call them x and y.The prime numbers need to
be large so that they will be difficult for someone to figure out.
Then calculate n = x.y

● Calculate the phi function of which is the number of numbers in the range 1 to n that
are coprime with n.It can easily be calculated as: ϕ(n)=(x−1)(y−1)

● Select an integer e, such that e is co-prime to ϕ(n) and 1<e<ϕ(n).The pair of numbers
(n,e) makes up the public key.

● Calculate d such that e.d = 1 mod ϕ(n)
d can be found using the extended euclidean algorithm. The pair (n,d) makes up the
private key.

2. Encryption
Given a plaintext P, represented as a number, the ciphertext C is calculated as:
C = P^e mod n

3. Decryption
Using the private key (n,d), the plaintext can be found using:
P = C^d mod n
Theorems used include:
euclidian algorithm which is used to calculate the gcd of numbers recursively 
extended euclidian algorithm which is used in the calculation of d.
inverse modulo to calculate the private key which is used in decryption.


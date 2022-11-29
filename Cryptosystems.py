import math, sys

mylist='ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
lenlist=len(mylist)
class affine(object):

    def inputcheck(a,b):   #takes 2 keys as an input and checks if they are valid encryption keys
        
        #we got to makes sure that the gcd of the first key and the length of mylist is 1
        if a < 0 or b < 0 or b > lenlist - 1:
            sys.exit(' invalid keys choosen, a must be greater than 0 and b must be between 0 and %s.' % (lenlist - 1))
        if math.gcd(a, lenlist) != 1:
            sys.exit('invalid keys choosen, a = %s and the size or length of mylist = %s are not relatively prime. Choose a different key.' % (a,lenlist))
        else:
            print("you have choosen valid keys ")

    
    def encryption(a,b,data): #takes the previous a,b and the data to be encrypted
        affine.inputcheck(a,b) # we call it here to check the input keys
        encrypted=' '
        for letter in data:
            if letter in mylist:  #letter is an iterator in the data 
                letterindex=mylist.find(letter)#letterindex is the index in which we found letter from data in mylist
                encrypted+=mylist[((letterindex*a+b)%lenlist)]# this is simply the formula ax+b mod len(list) in our case x=letterindex
            
            else:
                data
        return encrypted
    def inverse(a,lenlist):  #finds the inverse of a
        for i in range(1,lenlist+1):
            result = ((i * a) % lenlist) #this and the lines below are simply showing that if i*a%lenlist=1 then i is the inverse of a
            if result== 1:
                 break
            else:
                a
        return i
    def decryption(a,b,data,i):#i refers to the inverse of a which we get from the inverse function
        affine.inputcheck(a,b) # we call it here to check the input keys
        decrypted=' '
        i = affine.inverse(a,lenlist)
        for letter in data:
            if letter in mylist:
                letterindex=mylist.find(letter)
                decrypted+=mylist[((letterindex  - b) * i % lenlist)]#it is the same as the formula a^-1(x-b)%lenlist in our case x=letterindex
            else:
                decrypted += letter
        return decrypted

def main():
    data = input("Enter here plaintext or encrypted text : ")
    a = int(input("Enter the first key: "))
    b = int(input("Enter the second key: "))
    mode = input("Wanna Encrypt or Decrypt? : ")
    message=' '
    if mode.lower().startswith("e"): # if there is spelling incorrectness here it only requires the first speling of the input in mode variable when in the lowercase to be "e"
        message= affine.encryption(a,b,data)
    elif mode.lower().startswith("d"): # if there is spelling incorrectness here it only requires the first speling of the input in mode variable when in the lowercase to be "d"
            i = affine.inverse(a,lenlist)
            message= affine.decryption(a,b,data,i)
    print("out put: ",message)
main() 



class Transposition:
    
    def Encryption(plaintext,key):
        plaintext = plaintext.replace(" ","") # to remove white places between stringsin the input data
        encryptedtext = '' #empty string to collect encryptedtext
        textlen=len(plaintext)
        
        while textlen%key>0: 
            plaintext=plaintext+' ' 
        textlen=len(plaintext)
        columns = textlen//key
        for i in range(key): # iterating through range of keys
            for j in range(columns): # iterating through range of columns
                encryptedtext=encryptedtext+plaintext[i+j*key] # collecting ecrypted message reading through columns one by one
        return encryptedtext
        

    def Decryption(encryptedtext,key):   
        textlen=len(encryptedtext)
        key=textlen//key 
        plaintext='' # empty string to collect plaintext
        columns = textlen//key # 
        for i in range(key):
            for j in range(columns):
                plaintext=plaintext+encryptedtext[i+j*key]
        return  plaintext
    
def main():
    data = input("Enter here plaintext or cipher(encrypted)text : ")
    key = int(input("Enter key: "))
    mode = input("Wanna Encryption/Decryption? : ")
    if mode.lower().startswith("e"): # if there is spelling incorrectness here it only requires the first speling of the input in mode variable when in the lowercase to be "e"
           
        text = Transposition.Encryption(data,key)  # parameters accept the input data and key as a value  when gets called
        
    elif mode.lower().startswith("d"): # if there is spelling incorrectness here it only requires the first speling of the input in mode variable when in the lowercase to be "d"
            
        text = Transposition.Decryption(data,key) # parameters accept the input data and key as a value  when gets called 
    print("Output: ",text )
    
main()




from math import gcd, sqrt
import random
import sys

sys.setrecursionlimit(5000)

class RSA:
  def isprime(num):
    for i in range(2, int(sqrt(num))):
      if num % i == 0:
        return False
    return True
      
  def generateprimes():        
    while True:
      number=random.randint(1,1000000)
      if RSA.isprime(number):
          return number
          
  def calculate_gcd(self,num1, num2):
      if num2 == 0:
          return num1
      else:
          return RSA.calculate_gcd(num2, num1 % num2)

  def inverse(a, m):  #finds the inverse of a
    if gcd(a, m) != 1:
       return None # no mod inverse exists if a & m aren't relatively prime
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
      q = u3 // v3 # // is the integer division operator
      v1, v2, v3, u1, u2, u3 = (u1 - q * v1), (u2 - q * v2), (u3 - q * v3), v1, v2, v3
    return u1 % m
        
  def generatekey():    
     
    p=RSA.generateprimes()
    
    q=RSA.generateprimes()

    n= p*q
    
    e = random.randrange(2, (p - 1) * (q - 1))
    while gcd(e, (p - 1) * (q - 1)) != 1:
      e = random.randrange(2, (p - 1) * (q - 1))
    

    return n, e, RSA.inverse(e, (p-1)*(q-1))

  def pad(char):
    return "%03d" % char


  def padblock(block):
    block = str(block)
    while len(block) % 3 != 0:
      block = "0" + block
    return block
  
  def encrypt(message, n, e):    
    blocksize = 1
    size = "127"
    while int(size + "127") < n:
      size += str(127)
      blocksize += 1
      
      
    encryptedblocks = []
    while len(message) % blocksize != 0:
      message += " "
      
    msg = list(message.encode("ascii"))    
    for i in range(0, len(msg), blocksize):
      block = msg[i: min(blocksize + i, len(msg))]      
      block = map(RSA.pad, block)
      blockint = int("".join(block))      
      encryptedblocks.append(str(pow(blockint, e, n)))
      
    return ",".join(encryptedblocks)

  def decrypt(message, n , d):
    blocksize = 1
    size = "127"
    while int(size + "127") < n:
      size += str(127)
      blocksize += 1
      
      
    decrypted = []
    msg = message.split(",")
    for blockint in msg:
      decryptedblock = pow(int(blockint), d, n)      
      decryptedblock = RSA.padblock(decryptedblock)

      for i in range(0, len(decryptedblock), 3):
        decrypted.append(chr(int(decryptedblock[i:i+3])))
      
    return "".join(decrypted)
def main( ):
    
          print("Rsa!")        
        
          numb,pub, pri =RSA.generatekey()
          message=input("enter ur message: ")
          mode = input("Do you want Encryption/Decryption? : ")
          if mode.lower().startswith("e"):
              enc = RSA.encrypt(message,numb, pub)
              print(enc)
          elif mode.lower().startswith("d"):
             dec = RSA.decrypt(enc,numb, pri)
             print(dec)
main( )
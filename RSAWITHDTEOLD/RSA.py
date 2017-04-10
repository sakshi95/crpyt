'''RSA Encryption
'''

import random
import os
from createcsv import searchMapvalueElement
from createcsv import searchElement
from createcsv import returnDiifMapValue
global keyp,np,cipher
'''
Euclid's algorithm for determining the greatest common divisor
Use iteration to make it faster for larger integers
'''


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


'''
Euclid's extended algorithm for finding the multiplicative inverse of two numbers
'''
'''  d=1
temp=(d*e)%phi
while temp!=1:
temp=(d*e)%phi
return d'''


def private_Key_Gen(e, phi):
    d = 2
    temp = (d * e) % phi
    while temp != 1:
        d += 1
        if (d != e):
            temp = (d * e) % phi

            # print(temp)
    return d


'''
Tests to see if a number is prime.
'''


def is_prime(num):
    if num == 2:
        return True
    if num < 2 or num % 2 == 0:
        return False
    for n in range(3, int(num ** 0.5) + 2, 2):
        # print("n={}"+str(n))
        if num % n == 0:
            return False
    return True


def generate_keypair(p, q):
    if not (is_prime(p) and is_prime(q)):
        raise ValueError('Both numbers must be prime.')
    elif p == q:
        raise ValueError('p and q cannot be equal')
    # n = pq
    n = p * q

    # Phi is the totient of n
    phi = (p - 1) * (q - 1)

    # Choose an integer e such that e and phi(n) are coprime
    e = random.randrange(1, phi)

    # Use Euclid's Algorithm to verify that e and phi(n) are comprime
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(1, phi)
        g = gcd(e, phi)

    print("e=", e)
    print("phi=", phi)
    # Use Extended Euclid's Algorithm to generate the private key
    d = private_Key_Gen(e, phi)

    # Return public and private keypair
    # Public key is (e, n) and private key is (d, n)

    return ((e, n), (d, n))


def encrypt(message):

    global  keyp,np,cipher
    plaintext=searchElement(message)
    print message+' ='+plaintext

    # Unpack the key into it's components
    print ("RSA Encrypter/ Decrypter")
    #p = int(input("Enter a prime number (17, 19, 23, etc): "))
    #q = int(input("Enter another prime number (Not one you entered above): "))
    public, private = generate_keypair(17, 19)
    print ("Your public key is ", public, " and your private key is ", private)
    key, n = public
    keyp, np=private

    # Convert each letter in the plaintext to numbers based on the characterusing a^b mod m
    cipher = [(ord(char) ** key) % n for char in plaintext]

    #print (''.join(map(lambda x: str(x), cipher)))
    # print(ord(plaintext))
    # Return the array of bytes

    return (''.join(map(lambda x: str(x), cipher)))


def decrypt(ciphertext,privatekey):
    global cipher
    key=int(float(privatekey))
    # Unpack the key into its components
    #keyp, np = private
    # Generate the plaintext based on the ciphertext and key using a^b mod m
    for char in cipher:
        value=((char ** key) % np)
        if value>127:
           return str(returnDiifMapValue(key))

    plain = [chr((char ** key) % np) for char in cipher]
    # Return the array of bytes as a string
    value="".join(plain)
    #print "mapvalue:",value
    getvalue=searchMapvalueElement(value,key)

    return str(getvalue)





if __name__ == '__main__':
    '''
    Detect if the script is being run directly by the user
    '''
    os.system('cls')
    print ("RSA Encrypter/ Decrypter")
    p = int(input("Enter a prime number (17, 19, 23, etc): "))
    q = int(input("Enter another prime number (Not one you entered above): "))
    print ("Generating your public/private keypairs now . . .")
    public, private = generate_keypair(p, q)
    print ("Your public key is ", public, " and your private key is ", private)
    message = input("Enter a message to encrypt with your private key: ")

    encrypted_msg = encrypt(public, message)
    print (''.join(map(lambda x: str(x), encrypted_msg)))
    print ("Decrypting message with private key ", private, " . . .")
    print ("Your message is:")
    print (decrypt(private, encrypted_msg))
    print ("Your decrypted message can be seen in decptfile.txtfile ")

    decrypt(private, encrypted_msg)








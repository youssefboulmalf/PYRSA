from random import randint
import math
from art import *


#global values used for storing state of pub_key and priv_key
public_key=[]
private_key=[]

def random_prime_in_range(x, y):
    #checking for all posible prime numbers inbetween semi random range
    prime_number_list = []
    for n in range(x, y):
        isPrime = True

        for num in range(2, n):
            if n % num == 0:
                isPrime = False

        if isPrime:
            prime_number_list.append(n)


    return prime_number_list


def calculate_e(n,φ):
    print("Calculating possible e values...")
    r = list(range(2, φ))
    
    #caluculating estimated time.
    #TODO  calculate estimate with one timed loop for better accuracy
    print(f"Estimated time: {math.floor((6.499999999062311e-07 * (0.5 * φ * (φ + 1)))/60)+1} minutes")
    possibilities = []

    #checking for values that dont have common divisors with n or φ
    for value in r:
        divisors = []
        for i in range(2, min(n, value)+1):
            if n %i == value%i == 0:
                divisors.append(i)
        for i in range(2, min(φ, value)+1):
            if φ %i == value%i == 0:
                divisors.append(i)
        if not len(divisors)  > 0:
            possibilities.append(value)
    return possibilities[randint(0,len(possibilities)-1)]


def calculate_d(e,φ):
    l = []
    b=1
    while not len(l) >= 1:
        
        #checking for values that fit e*d(modφ)=1
        for i in range(1, b*1000):
            d = e * i
            if d % φ == 1:
                l.append(i)
        b+=1
    if len(l) > 1:
        r = randint(0, len(l)-1)
        return l[r]
    if len(l) == 1:
        return l[0]
    

def encrypt_message():
    global public_key

    if len(public_key) == 0:
        print("No public key loaded!")
        menu()
    value = list(input("Type the message you would like to encrpyt:\n"))
    print(f"Encrpyting...")
    stage = []
    for i in value:
        stage.append(ord(i))
    encrypted_message_list = []
    for index, i in enumerate(stage):
        # first int can't start with a "-"
        if index == 0:
            encrypted_message_list.append(f"{str((pow(i,public_key[0]))%public_key[1])}")
        else:
            encrypted_message_list.append(f"-{str((pow(i,public_key[0]))%public_key[1])}")
    
    message = "".join(encrypted_message_list)
    print(f"Encrypted message:\n{message}")
    menu()

def decrypt_message():
    global private_key
    if len(private_key) == 0:
        print("No private key loaded!")
        menu()
    crypt = input("Type the message you would like to decrpyt:\n")
    value = crypt.split("-")
    print(f"Decrypting....")
    stage = []
    for i in value:
            stage.append(int(i))
    decrypted_message_list = []
    for i in stage:
        decrypted_message_list.append(chr((pow(i,private_key[0]))%private_key[1]))
    message = "".join(decrypted_message_list)
    print(f"Decrypted message:\n{message}")
    menu()




def create_key():
    global public_key
    global private_key
    public_key=[]
    private_key=[]
    print("Generating key pair......")
    #TODO Make range setting that can be changed depending on the difficulty of encryption
    range = [1,randint(200, 300)]
    prime_numbers = random_prime_in_range(range[0],range[1])
    p = prime_numbers[randint(0,len(prime_numbers)-1)]
    q = prime_numbers[randint(0,len(prime_numbers)-1)]
    n = p*q
    φ = (p-1)*(q-1)
    e = calculate_e(n,φ)
    public_key.append(e)
    public_key.append(n)
    d = calculate_d(e,φ)
    private_key.append(d)
    private_key.append(n)
    print(f"Your public key is: {public_key}")
    print(f"Your private key is: {private_key}")
    menu()
    

def load_public_key():
    x = input("first number:")
    if not isinstance(x, int):
        print("no valid number was supplied")
        menu()
    y = input("second number:")
    if not isinstance(y, int):
        print("no valid number was supplied")
        menu()
    global public_key
    public_key = [x,y]
    menu()


def load_private_key():
    x = input("first number:")
    if not isinstance(x, int):
        print("no valid number was supplied")
        menu()
    y = input("second number:")
    if not isinstance(y, int):
        print("no valid number was supplied")
        menu()
    global private_key
    private_key= [x,y]
    menu()


def view_key_pair():
    global public_key
    global private_key
    if not len(public_key) == 0:
        print(f"Public key : {public_key}")
    else:
        print("Public key not loaded")
    if not len(private_key) == 0:
        print(f"Private key : {private_key}")
    else:
        print("Private key not loaded")
    menu()
    

def menu():
    print(f"Options:\n1. Generate key pair\n2. Load public key\n3. Load public key\n4. Encrypt message\n5. Decrypt message\n6. View key pair\n" )
    choise = input("Choose an option:")
    if not choise.isdigit():
        print("No valid option was selected")
        menu()
    if choise == "1":
        create_key()
    if choise == "2":
        load_public_key()
    if choise == "3":
        load_private_key()
    if choise == "4":
        encrypt_message()
    if choise == "5":
        decrypt_message()
    if choise == "6":
        view_key_pair()
        

def main():
    tprint("PYRSA",font="swwampland",chr_ignore=True)
    print(f"RSA encryption tool made by Youssef Boulmalf\n\n")
    menu()

if __name__ == "__main__":
    main()

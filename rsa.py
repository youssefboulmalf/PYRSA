from random import randint
import math


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
    print(f"Estimated time: {math.floor((6.499999999062311e-07 * (0.5 * φ * (φ + 1)))/60)} minutes")
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


def calculate_d(i,e,φ):
    l = []

    #checking for values that fit e*d(modφ)=1
    for i in range(1, i*1000):
        d = e * i
        if d % φ == 1:
            l.append(i)
    if len(l) == 0:
        #if no value = 1, repeat with more possibilities
        #TODO Make calculation continue from last number of loop for optimalisation
        calculate_d((i+1),e,φ)
    if len(l) > 1:
        print('e')        
        r = randint(0, len(l)-1)
        print(r)
        return l[r]
    if len(l) == 1:
        print('s')
        return l[0]
    

def encrypt_message():
    global public_key

    if len(public_key) == 0:
        print("No public key loaded!")
        menu()
    value = int(input("Type the message you would like to encrpyt:\n"))
    print(f"Encrpyting...")
    encrypted_message =  (pow(value,public_key[0]))%public_key[1]
    print(f"Encrypted message:\n{encrypted_message}")
    menu()

def decrypt_message():
    global private_key
    if len(private_key) == 0:
        print("No private key loaded!")
        menu()
    value = int(input("Type the message you would like to decrpyt:\n"))
    print(f"Decrypting....")
    decrypted_message = (pow(value,private_key[0]))%private_key[1]
    print(f"Decrypted message:\n{decrypted_message}")
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
    d = calculate_d(1,e,φ)
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
    print(f"RSA encryption tool made by Youssef Boulmalf\n\n")
    menu()

if __name__ == "__main__":
    main()

class RSAEncryption:
    """
    RSA Encryption class.
    Start by generating some keys with generate_keys
    """
    # Parameters to print private & public
    # Ex. RSAEncryption.private_key
    import random
    private_key = ""
    public_key = ""

    def __init__(self):
        pass

    # This is not really optimized and uses a loop to test prime-numbers. So don't do anything crazy.
    def generate_keys(self, low_prime_num, high_prime_num):
        """
        Method for key generation
        :param low_prime_num: lowest price number range (int)
        :param high_prime_num: highest prime number range (int)
        :return: Prints privatekey, publickey and modulus.
        """

        # D value in blog post.
        self.private_key = ""
        self.public_key = ""
        avail_prime = []
        e_avail_prime = []

        # Generating some prime numbers.
        for num in range(low_prime_num, high_prime_num + 1):
           # all prime numbers are greater than 1
            if num > 1:
                for i in range(2, num):
                    if (num % i) == 0:
                        break
                else:
                    avail_prime.append(num)  
                    
        # Selecting an index for avail prime. Can't select the last number.
        low_prime_rand = self.random.randrange(0, len(avail_prime) - 1)
        # Make it so the higher prime is higher then low prime.
        high_prime_rand = self.random.randrange(low_prime_rand, len(avail_prime))

        p = avail_prime[low_prime_rand]
        q = avail_prime[high_prime_rand]
        print("P = ", p)
        print("Q = ", q)
        
        modulus = p*q
        f_mod = (p-1)*(q-1)
        print("Mod= ",modulus)
        print("f_Mod= ",f_mod)
        
        # Now the public key is done, and for RSA its usally 65537.
        #The public keys is the same in most cases its the modulus thats the diffrence.
        self.public_key = 181
        print("E = 181")

        # We no have to find the D value and we use Modular multiplicative inverse toS do so.
        for i in range(0, 1000):
            x = E*i
            if x % F == 1:
                self.private_key = i
        print("D = ", self.private_key)

        # Return priv/pubkey and mod
        print("Publickey: {}\nPrivatekey: {}\nModulus: {}".format(self.public_key, self.private_key, modulus))
    
    @staticmethod
    def encrypt(pubkey, message, modulus):
        """
        Method for encryption
        :param pubkey:  public-key (int)
        :param message: The message you want to encrypt (string)
        :param modulus: What modulus you want to use for the encryption
        :return: Message (string)
        """
        # Lets first deal with the message
        # Split the message
        split_message = [char for char in message]
        #convert the message into ascii decmial
        converted_message = [ord(x) for x in split_message]
        
        # Creating a new list with the encrypted message.
        encrypted_message = []
        for i in converted_message:
            p = int(i)**int(pubkey) % modulus
            encrypted_message.append(p)

        # Return the message.
        return encrypted_message

    @staticmethod
    def decrypt(privkey, message, modulus):
        """
        Method for decryption
        :param privkey:  private-key (int)
        :param message: The message you want to decrypt (int, split the numbers with , ex: 73, 45, 59
        :param modulus: What modulus you want to use for the decryption (int)
        :return: Message (string)
        """
        # First we have to create a list with the message.
        split_encrypted_message = message.split(",") 
        # Decrypting
        decrypted_ascii_message = []
        for j in split_encrypted_message:
            p =int(j)**int(privkey) % modulus
            decrypted_ascii_message.append(p)

        # Converting into string
        print(decrypted_ascii_message)
        #decrypted_message = [chr(int(x, 16)) for x in encrypted_ascii_message]

        # Return string
        #return "".join(decrypted_message)


def main():
    #a = RSAEncryption()
    #a.generate_keys(1, 20)
    #print(a.encrypt(181, "times when i cant really answer any message because there are times like these", 221))
    #b = input("What would you like encrypted or decrypted?(Separate numbers with ',' for decryption):")
    #print(a.decrypt(925, b, 221))
    


if __name__ == "__main__":
    main()

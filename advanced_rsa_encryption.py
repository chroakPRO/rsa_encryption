from _typeshed import Self
from typing import Tuple, List, Dict


class RSAEncryption:
    """
    RSA Encryption class.
    Start by generating some keys with generate_keys
    """
    # Parameters to print private & public
    # Ex. RSAEncryption.private_key
    import random
    from typing import Dict, Set, List, Tuple
    privat_key: str = ""
    public_key: str = ""
    def __init__(self):
        pass

    def is_prime(self, num: int) -> bool:

        if num == 2:
            return True
        if num < 2 or num % 2 == 0:
            return False
        for n in range(3, int(num ** 0.5) + 2, 2):
            if num % n == 0:
                return False
        return True

    def generate_random_prime(self, max_prime_length: int) -> int:
        while 1:
            ran_prime = self.random.randint(0, max_prime_length)
            if self.is_prime(ran_prime):
                return ran_prime

    def gcd(self, a: int, b: int) -> int:
        while b != 0:
            a, b = b, a % b
        return a

    def egcd(self, a: int, b: int) -> int:
        if a == 0:
            return(b, 0, 1)
        else:
            g, y, x = self.egcd(b % a, a)
            return (g, x - (b // a) * y, y)

    def generate_keys(self) -> Tuple[Tuple[int, int], Tuple[int, int]]:
        """
        Method for key generation
        :return: publickey, and privatekey with modulus (tuple)
        """
        # D value in blog post.

        self.private_key: int = ""
        self.public_key: int = ""

        p: int = self.generate_random_prime(10000000000)
        q: int = self.generate_random_prime(10000000000)

        modulus = p * q
        print("Modulus ", modulus)
        f_mod = (p - 1) * (q - 1)
        print("F_mod ", f_mod)

        # Next is to find co-prime to modulus
        self.public_key = self.random.randint(1, f_mod)
        g = self.gcd(self.public_key, f_mod)
        while g != 1:
            self.public_key = self.random.randint(1, f_mod)
            g = self.gcd(self.public_key, f_mod)

        print("public_key=", self.public_key, " ", "modulus=", modulus)
        # Next we have to find the private key.
        # For that we use multiplication inverse.
        self.private_key = self.egcd(self.public_key, f_mod)[1]

        # Check that d is positiv.
        self.private_key = self.private_key % f_mod
        if self.private_key < 0:
            self.privat_key += f_mod

        return (self.private_key, modulus), (self.public_key, modulus)

    @staticmethod
    def encrypt(text, public_key: Tuple[int, int]) -> str:
        """
        Method for encryption
        :param public_key:  Publickey and modulus (tuple, int)
        :param message: The message you want to encrypt (string)
        :return: Message (string)
        """
        # Converts the char to ascii decimal and then performs encryption.
        key, n = public_key
        ctext = [pow(ord(char), key, n) for char in text]
        return ctext

    @staticmethod
    def decrypt(ctext, private_key: Tuple[int, int]) -> str:
        """
        Method for decryption
        :param private_key:  Privatekey and modulus (tuple, int)
        :param emessage: The message you want to decrypt (list, int)
        :return: Message (string)
        """
        # Creates a list with all the characters in the text and performs the decryption
        try:
            key, n = private_key
            text = [chr(pow(char, key, n)) for char in ctext]
            return "".join(text)
        except TypeError as e:
            print(e)


if __name__ == '__main__':
    a: object = RSAEncryption()
    public_key, private_key = a.generate_keys() # gen_keys . return Tuple[int, int]
    print("Public: ", public_key)
    print("Private: ", private_key)
    message: str = RSAEncryption.encrypt("This is the time we are going to have sex so lets have ti and lets not stop and saying ",
                    public_key)
    print("encrypted  =", message)
    plaintext: str = RSAEncryption.decrypt(message, private_key)
    print("decrypted =", plaintext)

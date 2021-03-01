#Simple version of RSA
import sys

p = 3
q = 11
n = p*q
f = (p-1) * (q-1)
#Has to follow the rule 1 < e < f
e = 7
#Coe for finding the d value is in the blog 
#Christopherek.dev/blog-posts/encryption-post.html)
d = 3
message = 13

#This will encrypt the message.
#Which in this case can only be between 1-99 (Check out more advanced version.)

def encrypt(message, public_key, n):
    encrypted_message = message**public_key % n 
    return encrypted_message
    
def decrypt(message, private_key, n):
    decrypted_message = message**private_key % n
    return decrypted_message
    

if __name__ == "__main__":
    a = encrypt(message, e, n)
    b = decrypt(a, d, n)

    print(a)
    print(b)
    
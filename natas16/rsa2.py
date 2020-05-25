'''  RSA encryption
     inspired on: https://www.youtube.com/watch?v=M7kEpw1tn50
     and http://jcla1.com/blog/rsa-public-private-key-encryption-explained

     some conditions:
        - prime numbers must be > 1 and not equal
        - prime factor must sufficiently large to accommodate the ascii numbers, let's say > 150
        - so for example (2, 191) will do as well as (11, 17)
'''

class RSA():
    ''' methods for calculating keys, encrypt and decrypt ascii messages
    '''
    @staticmethod
    def gcd(a, b):
        while b:
            a, b = b, a % b
        return a

    @classmethod
    def encrypt(cls, message):
        message_letters = [ord(letter) for letter in message]
        message_encrypted = ''.join([chr(letter**cls.public_key % cls.prime_factor) for letter in message_letters])
        return message_encrypted

    @classmethod
    def decrypt(cls, message_encrypted):
        message_encrypted_letters = [ord(letter) for letter in message_encrypted]
        message = ''.join([chr(letter**cls.private_key % cls.prime_factor) for letter in message_encrypted_letters])
        return message

    @classmethod
    def calc_keys(cls, prime_1, prime_2):
        cls.prime_factor = prime_1 * prime_2
        totient = (prime_1 - 1) * (prime_2 - 1)

        # calculate the possible public keys where gcd(public_key, totient) == 1, then select the 5th one (this is abritary, any
        # of the public_keys could have been selected
        # (Note above link has an error that the gcd of public_key and totient must be 1, not public_key
        #  and the prime_factor as suggested in the article)
        public_keys = []
        for i in range(totient):
            if cls.gcd(i, totient) == 1:
                public_keys.append(i)
        cls.public_key = public_keys[4]

        # calculate the private key based on public key and totient when (public_key * private_key - 1) % totient == 0
        cls.private_key = 0
        x = -1
        while x != 0:
            cls.private_key += 1
            x = (cls.public_key * cls.private_key - 1) % totient

        return (cls.prime_factor, cls.public_key, cls.private_key)


def main():
    rsa = RSA()
    print(rsa.calc_keys(7493025776465062819629921475535241674460826792785520881387158343265274170009282504884941039852933109163193651830303308312565580445669284847225535166520307, 7020854527787566735458858381555452648322845008266612906844847937070333480373963284146649074252278753696897245898433245929775591091774274652021374143174079))

    message = 'hello this is my encrypted message'
    encrypted_message = rsa.encrypt(message)
    decrypted_message = rsa.decrypt(encrypted_message)

    if message == decrypted_message:
        print('Hurray!!')
        print(f'message: {message}\nencrypted message: {encrypted_message}'
              f'\ndecrypted message: {decrypted_message}')
    else:
        print('Ough, someting wrong here  ... !')


if __name__=="__main__":
    main()
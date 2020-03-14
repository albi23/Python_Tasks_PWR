import os
import pickle
import sys

import rsa
from rsa import common


def gen_keys(key_length: int):
    public_key, private_key = rsa.newkeys(key_length)

    key_pub_file = open("key.pub", "w")
    key_prv_file = open("key.prv", "w")

    key_pub_file.write(str(public_key))
    key_prv_file.write(str(private_key))

    key_prv_file.close()
    key_pub_file.close()
    # --->  PrivateKey(10067138627844967993, 65537, 9891408770195711813, 16318216531, 616926403)
    # cipher = rsa.encrypt(b'Hello', public_key)
    # print(cipher)
    # print(len(cipher))
    # output_file = open("zaszyfrowane.txt", "w")
    # output_file.write(str(private_key))
    # output_file.close()
    # decrypt = rsa.decrypt(cipher, private_key)

    # print(decrypt)
    # base64Text = base64.b64encode(cipher).decode()

    # print(base64Text)

    # text = rsa.decrypt(base64.b64decode(base64Text.encode()), private_key)
    # print(text.decode())


def encrypt(message: str):
    if not os.path.isfile('key.pub'):
        print("Error: File \"key.pub\" does not appear to exist. Generate it first.")
        exit(0)

    with open('key.pub', 'rb') as config_dictionary_file:
        # Step 3
        key_pub = pickle.load(config_dictionary_file)

        # After config_dictionary is read from file
        print(key_pub)

    # key_pub_file = open("key.pub", "r")
    # key_pub = key_pub_file.readline()
    # key_pub_file.close()

    common.byte_size(key_pub.n)
    cipher = rsa.encrypt(b'Hello', key_pub)
    print(cipher)



def decrypt(param):
    if not os.path.isfile('key.prv'):
        print("Error: File \"key.prv\" does not appear to exist. Generate it first.")
        exit(0)

    key_prv_file = open("key.prv", "r")
    key_prv = key_prv_file.readline()
    key_prv_file.close()
    print(key_prv)
    pass


def print_usage():
    print("Usage : python RSA.py --gen-keys number_length")
    print("      : python RSA.py --encrypt message")
    print("      : python RSA.py --decrypt encrypt_message")
    exit(1)
    pass


if __name__ == '__main__':

    if len(sys.argv) != 3:
        print_usage()

    if sys.argv[1] == '--gen-keys':
        gen_keys(int(sys.argv[2]))
    elif sys.argv[1] == '--encrypt':
        encrypt(sys.argv[2])
    elif sys.argv[1] == '--decrypt':
        decrypt(sys.argv[2])
    else:
        print_usage()

    # random_generator = Random.new().read
    # key = RSA.generate(1024, random_generator)  # generate pub and priv key
    #
    # publickey = key.publickey()  # pub key export for exchange

    # encrypted = publickey.encrypt('encrypt this message', 32)
    # encrypted = publickey.encrypt('encrypt this message',(32).to_bytes(2, byteorder='big'))
    # message to encrypt is in the above line 'encrypt this message'

    # print('encrypted message:', encrypted)  # ciphertext
    # f = open('encryption.txt', 'w')
    # f.write(str(encrypted))  # write ciphertext to file
    # f.close()

    # decrypted code below

    # f = open('encryption.txt', 'r')
    # message = f.read()
    #
    # decrypted = key.decrypt(ast.literal_eval(str(encrypted)))
    #
    # print('decrypted', decrypted)
    #
    # f = open('encryption.txt', 'w')
    # f.write(str(message))
    # f.write(str(decrypted))
    # f.close()

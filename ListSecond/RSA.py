import os
import pickle
import sys

import rsa
from Crypto.Util.number import _rabinMillerTest
from numpy import long
from rsa import common
from rsa.transform import int2bytes


def gen_keys(key_length: int):

    if key_length < 100:
        print("Minimum key length should be greater than 100")
        exit(1)

    public_key, private_key = rsa.newkeys(key_length)

    if _rabinMillerTest(private_key.p, 10_000) == 0:
        raise Exception('Number p ', private_key.p, " is not prime")
    elif _rabinMillerTest(private_key.q, 10_000) == 0:
        raise Exception('Number q ', private_key.q, " is not prime")

    with open('key.pub', 'wb') as key_pub_file:
        pickle.dump(public_key, key_pub_file)

    with open('key.prv', 'wb') as key_prv_file:
        pickle.dump(private_key, key_prv_file)
    print('Keys generated successfully.')


def encrypt(message: str):
    if not os.path.isfile('key.pub'):
        print("Error: File \"key.pub\" does not appear to exist. Generate it first.")
        exit(0)

    with open('key.pub', 'rb') as key_pub_file:
        key_pub = pickle.load(key_pub_file)

    max_block_size = common.byte_size(key_pub.n) - 11
    for i in range(0, len(message), max_block_size):
        cipher = rsa.encrypt(message[i: max_block_size + i].encode(), key_pub)
        int_form = int.from_bytes(cipher, byteorder='big')
        print(int_form)


def decrypt(param: str):
    if not os.path.isfile('key.prv'):
        print("Error: File \"key.prv\" does not appear to exist. Generate it first.")
        exit(0)

    with open('key.prv', 'rb') as key_prv_file:
        private_key = pickle.load(key_prv_file)

    decrypted = rsa.decrypt(int2bytes(long(param)), private_key)
    print(decrypted)


def print_usage():
    print("Usage : python RSA.py --gen-keys number_length")
    print("      : python RSA.py --encrypt message")
    print("      : python RSA.py --decrypt encrypt_message")
    exit(1)


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

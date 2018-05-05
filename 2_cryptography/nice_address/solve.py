# -*- coding: utf-8 -*-

''' УСЛОВИЕ ЗАДАЧИ:
    На вход подаются две строки - публичный ключ в шестнадцатеричном формате
    и четыре шестнадцатеричных знака, с которых должен начинаться красивый адрес.
    Найти дополнительный приватный ключ в шестнадцатеричном формате для получения красивого адреса. '''

# P - public key, K - private key
# P = G * K
# addr = right(keccak256(P), 20)
# P(nice) = G * (K + K(nice)) = G * K + G * K(nice) = P + G * K(nice)

import sys
from my_secp256k1 import *
from sha3 import keccak_256

SIZE = 64
CUT_SIZE = 24

# Get string from stdin
def readline():
    return sys.stdin.readline().rstrip()

# Convert int to hex
def to_hex(int_value):
    return hex(int_value)[2:].zfill(SIZE)

# Get public key for a nice address
# P(nice) = P + G * K(nice)
def get_new_pubkey(old_pubkey, nice_privkey):
    return add(old_pubkey, multiply(G, int(nice_privkey, 16)))

# Get Ethereum address from the public key
def get_address(public_key):
    x, y = public_key
    return keccak_256(bytes.fromhex(to_hex(x) + to_hex(y))).hexdigest()[CUT_SIZE:]

# Check if the Ethereum address starts with a given value
def check_address(pubkey, start_value):
    return get_address(pubkey)[:len(start_value)] == start_value

str_pubkey, start_value = readline(), readline()
public_key = (int(str_pubkey[:64], 16), int(str_pubkey[64:], 16))

nice_privkey = 0
while True:
    hex_nice_privkey = to_hex(nice_privkey)
    new_pubkey = get_new_pubkey(public_key, hex_nice_privkey)
    if check_address(new_pubkey, start_value):
        print(hex_nice_privkey)
        break
    nice_privkey += 1

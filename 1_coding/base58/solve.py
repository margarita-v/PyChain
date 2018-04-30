# -*- coding: utf-8 -*-

''' УСЛОВИЕ ЗАДАЧИ:
    На вход подаются Bitcoin-адреса в двоичном виде, длина каждого адреса равна 176 символов.
    Определить символ алфавита, который используется чаще всего в Base58-представлениях данных адресов.
    Если самый частый символ - единица, то указать следующий по частоте символ. '''

import sys, hashlib
from bitcoin import base58

def to_bytes(hex_string):
    return bytes.fromhex(hex_string)

def sha256(string):
    return hashlib.sha256(to_bytes(string))

BYTE_LEN = 8
BASE58 = '123456789ABCDEFGHJKLMNPQRSTUVWXYZabcdefghijkmnopqrstuvwxyz'

if __name__ == '__main__':
    counter = dict()
    for char in BASE58:
        counter[char] = 0
    
    for line in sys.stdin.readlines():
        line = line.rstrip()
        address = ''
        while line != '':
            num = line[:BYTE_LEN]
            value = hex(int(num, 2))[2:]
            value = value.zfill(2)
            address += value
            line = line[BYTE_LEN:]

        # Remove two leading zeros
        address = address[2:]

        # Perform a double hashing
        first = sha256(address)
        checksum = sha256(first.hexdigest())

        # Checksum is the first 8 digits from the double hashed result
        # Add checksum to Bitcoin address
        result = address + checksum.hexdigest()[:BYTE_LEN]

        # Encode address to Base58
        enc_result = base58.encode(to_bytes(result))
        for char in enc_result:
            counter[char] += 1

    # We don't need to calculate a count of '1'
    counter['1'] = 0
    print(max(counter, key=counter.get))

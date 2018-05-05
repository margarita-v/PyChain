# -*- coding: utf-8 -*-

''' УСЛОВИЕ ЗАДАЧИ:
    На вход подается приватный ключ в шестнадцатеричном формате.
    Требуется напечатать две строки:
    Ethereum-адрес по данному ключу и последовательность чисел, разделенных пробелом, - 
    позиции в шестнадцатеричной записи адреса, в которых строчная буква должна быть заменена на заглавную. '''

# Формула получения адреса: addr=right(keccak256(pubkey), 20)

import sys
from eth_utils import to_checksum_address
from sha3 import keccak_256
from py_ecc.secp256k1 import privtopub

SIZE = 64
CUT_SIZE = 24

def to_hex(int_value):
    return hex(int_value)[2:].zfill(SIZE)

def get_address(string):
    x, y = privtopub(bytes.fromhex(string.rstrip()))
    public_key = to_hex(x) + to_hex(y)
    return keccak_256(bytes.fromhex(public_key)).hexdigest()[CUT_SIZE:]

for line in sys.stdin.readlines():
    public_key = get_address(line)
    print(public_key)
    checksum_address = to_checksum_address(public_key)[2:]
    result = []
    i = 0
    while i < len(checksum_address):
        if public_key[i] != checksum_address[i]:
            result.append(str(i))
        i += 1
    print(' '.join(result))

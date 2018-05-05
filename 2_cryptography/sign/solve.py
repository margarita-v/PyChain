# -*- coding: utf-8 -*-

''' УСЛОВИЕ ЗАДАЧИ:
    На вход подаются пары строк - приватный ключ в шестнадцатеричном формате
    и набор символов длиной не более 255 символов.
    Вывести три компонента цифровой подписи в шестнадцатеричном формате. '''

import sys
from sha3 import keccak_256
from py_ecc.secp256k1 import ecdsa_raw_sign

SIZE = 64
lines = sys.stdin.readlines()

def get_line(index):
    return lines[index].rstrip()

def to_hex(int_value):
    return hex(int_value)[2:]

def to_filled_hex(int_value):
    return to_hex(int_value).zfill(SIZE)

i = 0
while i < len(lines):
    privkey, message = get_line(i), get_line(i + 1)
    i += 2
    message_hash = keccak_256(message.encode()).hexdigest()
    v, r, s = ecdsa_raw_sign(bytes.fromhex(message_hash), bytes.fromhex(privkey))
    print('{0}\n{1}\n{2}'.format(to_hex(v), to_filled_hex(r), to_filled_hex(s)))

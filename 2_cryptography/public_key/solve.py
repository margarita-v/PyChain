# -*- coding: utf-8 -*- 

''' УСЛОВИЕ ЗАДАЧИ:
    На вход подается приватный ключ в шестнадцатеричном формате. Длина строки равна 64 символа.
    Требуется получить публичный ключ.
    В ответе необходимо выравнять координаты публичного ключа до 32-байтных слов и сконкатенировать. '''

import sys
from py_ecc.secp256k1 import privtopub

SIZE = 64

def to_hex(int_value):
    return hex(int_value)[2:].zfill(SIZE)

for line in sys.stdin.readlines():
    x, y = privtopub(bytes.fromhex(line.rstrip()))
    print(to_hex(x) + to_hex(y))

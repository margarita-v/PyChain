import sys, hashlib, codecs
from bitcoin import base58

data = sys.stdin.buffer.readline()
data_enc = codecs.encode(data, 'hex')

def ripemd160(data):
    return hashlib.new('ripemd160', data).digest()

def sha256(data):
    return hashlib.sha256(data).digest()

def print_b58(data):
    print(base58.encode(data))

def print_res(name, func = None):
    print(name)
    if func is not None:
        print_b58(func(data))
        print_b58(func(data_enc))
    else:
        print_b58(data)
        print_b58(data_enc)
    print()

print_res('ripemd160', ripemd160)
print_res('sha256', sha256)
print_res('clear input')

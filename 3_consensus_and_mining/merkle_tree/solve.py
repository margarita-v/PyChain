import sys, binascii
from hashlib import sha256

def reverse_hash(hex_string):
    return binascii.unhexlify(hex_string)[::-1]

def bitcoin_hash(value):
    return sha256(sha256(value).digest())

def get_merkle_node(first, second):
    # Reverse inputs before and after hashing
    result = bitcoin_hash(reverse_hash(first) + reverse_hash(second)).digest()[::-1]
    return binascii.hexlify(result).decode()

def get_merkle_root(hashList):
    length = len(hashList)
    if length == 1:
        return hashList[0]
    newHashList = []
    # Process pairs. For odd length, the last is skipped
    for i in range(0, length - 1, 2):
        newHashList.append(get_merkle_node(hashList[i], hashList[i + 1]))
    if length % 2 == 1: # odd, hash last item twice
        newHashList.append(get_merkle_node(hashList[-1], hashList[-1]))
    return get_merkle_root(newHashList)

if __name__ == '__main__':
    hashList = [line.rstrip() for line in sys.stdin.readlines()[1:]]
    print(get_merkle_root(hashList))

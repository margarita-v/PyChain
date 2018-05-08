# http://pythonfiddle.com/merkle-root-bitcoin/
import hashlib
 
# Hash pairs of items recursively until a single value is obtained
def merkle(hashList):
    length = len(hashList)
    if length == 1:
        return hashList[0]
    newHashList = []
    # Process pairs. For odd length, the last is skipped
    for i in range(0, length - 1, 2):
        newHashList.append(hash2(hashList[i], hashList[i+1]))
    if length % 2 == 1: # odd, hash last item twice
        newHashList.append(hash2(hashList[-1], hashList[-1]))
    return merkle(newHashList)
 
def hash2(a, b):
    # Reverse inputs before and after hashing
    # due to big-endian / little-endian nonsense
    a1 = a.decode('hex')
    a11 = a1[::-1]
    # print a11.encode('hex')
    b1 = b.decode('hex')[::-1]
    #print b1.encode('hex')
    concat = a11+b1
    #print concat.encode('hex')
    concat2 = hashlib.sha256(concat).digest()
    print "hash1:" + concat2.encode('hex')
    h = hashlib.sha256(concat2).digest()
    print "hash2:" + h[::-1].encode('hex')
    print ''
    return h[::-1].encode('hex')
 
# https://blockexplorer.com/rawblock/000000000000030de89e7729d5785c4730839b6e16ea9fb686a54818d3860a8d
txHashes = [
        '5eab9fc7bda0017450f05232e8e219df936a4dd787b8e8706622074d5bee9222',
        'fd7cbc5db77bd282ea281a02d05b6b3dd0ae9f21659ba23d362aa2b774cdfef1',
        '3a0d89d8e0ccc13bfc11af67fe8297b37903415ff9d194e594fb91b985adec13',
        '8aa115ab1511601a86a627e3ddd0f2dba53f068d97d098be53f656c9d6495dd6'
]  	
 
print merkle(txHashes)

import sys, binascii

def readline():
    return sys.stdin.readline().rstrip()

def to_bytes(string):
    return binascii.hexlify(string.encode())

def func(string):
    result = ''
    for char in string:
        result += hex(ord(char))
    print(result)
    print('!!!')
    return bytes(result.encode())
    #return bytes.fromhex(result)

checksum, first = readline(), func(readline())
print(checksum, first)

checksum_bytes = to_bytes(checksum)
print(checksum_bytes)

second = bytes.fromhex('10fb1498')
#second = binascii.hexlify(bytes.fromhex('10fb1498'))
print(second)

test = first + second
print(test)
print(len(test))
print('next')

test_str = test.decode()
print(test_str)

print(len(test))
print(len(test) // 8)
#res = 0
#for byte in test:
 #   res ^= ord(byte)
#print(res)

hell = b'\x31\x32\x33\x34\x64\x69\x47\x69\x10\xfb\x14\x98'
print(len(hell))

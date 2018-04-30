import sys

def readline():
    return sys.stdin.readline().rstrip()

checksum = bytes.fromhex(readline())
first = readline().encode()

print(checksum)
print(first)

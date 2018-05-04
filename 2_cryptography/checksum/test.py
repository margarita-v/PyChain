import sys

BLOCK_SIZE = 4

def readline():
    return sys.stdin.readline().rstrip()

def get_hex(value):
    return hex(value)[2:]

checksum, first = readline(), readline()
bytes_array = [get_hex(byte) for byte in bytes.fromhex(checksum)]

# Convert first to bytes
for char in first:
    bytes_array.append(get_hex(ord(char)))

#for byte in bytes.fromhex('9fb03375'):
 #   bytes_array.append(get_hex(byte))
print(bytes_array)

blocks = []
i, result, length = 0, 0, len(bytes_array)
while i < length:
    current = ''
    j = 0
    while j < BLOCK_SIZE and i < length:
        current += bytes_array[i]
        i += 1
        j += 1
    current = int(current, 16)
    result ^= current
    blocks.append(current)

print(get_hex(result))

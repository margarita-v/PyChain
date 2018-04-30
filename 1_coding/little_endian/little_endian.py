BYTE_LEN = 7
RESULT_LEN = 28
BYTE_COUNT = RESULT_LEN // BYTE_LEN
BINARY_FORMAT = '0{}b'.format(RESULT_LEN)

if __name__ == '__main__':
    number = int(input())
    binary = format(number, BINARY_FORMAT)

    result = ''
    length = 0
    while length < BYTE_COUNT:
        result = binary[:BYTE_LEN] + result
        binary = binary[BYTE_LEN:]
        length += 1
    print(result)

def rlp_decode(inp):
    if inp is None or len(inp) == 0:
        return ''
    output = ''
    (offset, dataLen, dataType) = decode_length(inp)
    if dataType is str:
        #output = substr(input, offset, dataLen)
        output = inp[offset:dataLen]
    elif dataType is list:
        #output = [substr(input, offset, dataLen)]
        output = [inp[offset:dataLen]]
    print(dataType)
    print(output)
    
    #return output + rlp_decode(substr(input, offset + dataLen))
    #print(output)
    output += rlp_decode(inp[(offset + dataLen):])
    return output

def decode_length(input):
    length = len(input)
    if length == 0:
        raise Exception("input is null")
    prefix = ord(input[0])
    if prefix <= 0x7f:
        return (0, 1, str)
    elif prefix <= 0xb7 and length > prefix - 0x80:
        strLen = prefix - 0x80
        return (1, strLen, str)
    elif prefix <= 0xbf and length > prefix - 0xb7 and length > prefix - 0xb7 + to_integer(substr(input, 1, prefix - 0xb7)):
        lenOfStrLen = prefix - 0xb7
        strLen = to_integer(substr(input, 1, lenOfStrLen))
        return (1 + lenOfStrLen, strLen, str)
    elif prefix <= 0xf7 and length > prefix - 0xc0:
        listLen = prefix - 0xc0;
        return (1, listLen, list)
    elif prefix <= 0xff and length > prefix - 0xf7 and length > prefix - 0xf7 + to_integer(substr(input, 1, prefix - 0xf7)):
        lenOfListLen = prefix - 0xf7
        listLen = to_integer(substr(input, 1, lenOfListLen))
        return (1 + lenOfListLen, listLen, list)
    else:
        raise Exception("input don't conform RLP encoding form")

def to_integer(b):
    length = len(b)
    if length == 0:
        raise Exception("input is null")
    elif length == 1:
        return ord(b[0])
    else:
        return ord(substr(b, -1)) + to_integer(substr(b, 0, -1)) * 256

import sys

if __name__ == '__main__':
    for line in sys.stdin.readlines():
        line = line.rstrip()
        input = bytes.fromhex(line)
        print(line)
        print(input)
        print()
        #for byte in input:
         #   print(type(byte))
          #  print(chr(byte))
        #print('END')
        
        #print(rlp_decode(input))

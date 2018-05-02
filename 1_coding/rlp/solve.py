import sys

for line in sys.stdin.readlines():
    line = line.rstrip()

    str_prefix = line[:2]
    prefix = bytes.fromhex(str_prefix)
    line = line[2:]

    if prefix >= b'\x80' and prefix <= b'\xb7':
        # String
        #length = prefix - b'\x80'
        result = str_prefix
        while len(line) > 0:
            result += line[-2:]
            line = line[:-2]
        print(result)
    else:
        # List
        answer = str_prefix
        str_list = []
        while len(line) > 0:
            str_prefix = line[:2]
            prefix = bytes.fromhex(str_prefix)
            line = line[2:]

            # Check prefix for range
            length = 2
            if prefix >= b'\x80' and prefix <= b'\xb7':
                length = int(str_prefix[1]) * 2
            #parsed_string = line[:length]
            result = str_prefix + line[:length]
            line = line[length:]
            str_list.insert(0, result)
        print(answer + ''.join(str_list))

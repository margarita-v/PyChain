import sys, json, my_transactions

class MyTransaction:
    def __init__(self, data):
	    self.__dict__ = json.loads(data)

for line in sys.stdin.readlines():
    tx = MyTransaction(line.replace('\'', '"'))
    print(tx.blockHash)

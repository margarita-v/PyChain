# -*- coding: utf-8 -*-

''' УСЛОВИЕ ЗАДАЧИ:
    На вход дается год рождения школьника и результат хэш-функции SHA-3.
    Параметр хэш-функции - дата рождения школьника в формате UTC.
    Определить день и месяц рождения школьника. '''

import sys
from sha3 import keccak_256
from datetime import datetime, timedelta

# Хэш-функция принимает на вход набор байт.
# В Ethereum целые числа конвертируются как 256-битный код с порядком байт big-endian.
SIZE = 256 // 8

def date_to_bytes(date):
    utc = date.strftime('%s')
    return (int(utc)).to_bytes(SIZE, byteorder='big')

def readline():
    return sys.stdin.readline().rstrip()

if __name__=='__main__':
    year, sha = int(readline()), readline()

    # Generate days for a given year
    days = dict()
    start_date = datetime(year, 1, 1)
    end_date = datetime(year, 12, 31)
    d = start_date
    days[start_date] = date_to_bytes(start_date)
    while d < end_date:
        d += timedelta(days=1)
        days[d] = date_to_bytes(d)
    for date, byte in days.items():
        if keccak_256(byte).hexdigest() == sha:
            print(date.strftime('%d.%m'))
            break

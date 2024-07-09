#flag{b1n42y_s3r2ch_f7w}

from pwn import *
import pandas as pd

def custom_sort_key(word):
    return [ord(char) for char in str(word)]  

file_path = 'wordlist.txt'
df = pd.read_csv(file_path, header=None, names=["Names"])

sorted_df = df.sort_values(by="Names", key=lambda col: col.map(custom_sort_key)).reset_index(drop=True)

first = 0
last = len(df.index) - 1

while first <= last:
    io = process('./bruteforcer')
    io.recvuntil(":")
    mid = (first + last) // 2 
    print(first, last)
    password_maybe = sorted_df.iloc[mid]['Names']
    
    io.sendline(password_maybe.encode())
    out = io.recvline().split()[-1]
    print(out)
    if out == b'low':
        first = mid + 1
    elif out == b'high':
        last = mid - 1
    else:
        print(f"Password found: {password_maybe}")
        break
    io.close()


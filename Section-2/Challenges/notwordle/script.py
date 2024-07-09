
from pwn import *

for x in "_qwertyuioplkjhgfdsazxcvbnm":
    io = process("./notwordle")
    maybe = ""
    for i in range(30):
        maybe += x
    io.recvuntil(":")
    io.send(f"{maybe}\n".encode())
    out = io.recvline()
    print(out)
    io.close()
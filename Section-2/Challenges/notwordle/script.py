
#pr377y_5u23_7h15_15_n07_w0rd13
#flag{pr377y_5u23_7h15_15_n07_w0rd13}
from pwn import *


found = ""
while len(found) <30:
    for x in "_qwertyuioplkjhgfdsazxcvbnm0123456789":
        maybe = found + x * (30-len(found))  
        
        io = process("./notwordle")
        
        io.recvuntil(":")  
        io.sendline(maybe.encode()) 
        
        
        out = io.recvline().split()[0]
        print(out)
        if(int(out.decode()) > len(found)):
            found += x
        
        io.close()

import  socket
import sys
print("Hi I am clinet")

c=socket.socket()
host_name=socket.gethostname()
c.connect(('mayank-Vostro-3558',9999))
print(c.recv(1024).decode())

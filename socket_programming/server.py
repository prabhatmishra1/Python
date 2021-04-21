# import  socket
# print("Hi I am Server")
#
# s=socket.socket()
# print("socket is created")
# host_name=socket.gethostname()
# s.bind((host_name,9999))
# s.listen(3)
# print('Wating for connection........')
# while True:
#     c,add=s.accept()
#     print('connected with',add)
#     c.send(bytes('Hi how are you client' ,'utf-8'))
#     c.close()


#SERVER
import socket

def Main():
    host = "0.0.0.0"
    port = 7001

    print(socket.gethostname())

    mySocket = socket.socket()
    mySocket.bind((host,port))

    mySocket.listen(1)
    conn, addr = mySocket.accept()
    print ("Connection from: " + str(addr))
    while True:
            data = conn.recv(1024).decode()
            if not data:
                    break
            print ("from connected  user: " + str(data))

            data = str(data).upper()
            print ("sending: " + str(data))
            conn.send(data.encode())

    conn.close()

if __name__ == '__main__':
    Main()

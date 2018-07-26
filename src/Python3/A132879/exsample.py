import socket

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind(("localhost", 9999))
sock.listen(1)
conn, addr = sock.accept()
print(addr)
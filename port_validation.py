import socket
host, port = "127.0.0.1", 5432
s=socket.socket(); s.settimeout(2)
print("open" if s.connect_ex((host,port))==0 else "closed")
s.close()

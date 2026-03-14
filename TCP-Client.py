import socket

target_host = "www.google.com"
target_port = 80

# AF_INET is the address family constant used in socket programming
# for IPv4 (Internet Protocol version 4) communication
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((target_host, target_port))

client.send(b"GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")

response = client.recv(4096)

print(response.decode())
client.close()
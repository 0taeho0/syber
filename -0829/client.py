import socket


def echo_client(msg, host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.connect((host, port))
        s.sendall(msg.encode())
        data = s.recv(1024)
        print(f"Received: {data.decode()}")


echo_client("hello world :D", '127.0.0.1', 65432)

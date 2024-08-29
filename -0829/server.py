import socket

def echo_server(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.bind((host, port))
        s.listen()
        print(f"Server listening on {host}:{port}")
        conn, addr = s.accept()
        with conn:
            print(f"Connected by {addr}")
            while(True):
                data = conn.recv(1024)
                if not data:
                    break
                conn.sendall(data)


echo_server('127.0.0.1', 65432)

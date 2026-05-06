import socket
import time

HOST = '127.0.0.1'
PORT = 65432

def client_node(offset):
    local_time = time.time() + offset
    print(f"[Client Offset {offset}] Local time: {local_time:.2f}")

    # Step 1: Create socket and bind to random port
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.bind((HOST, 0))
    client_port = s.getsockname()[1]

    # Step 2: Send time + port
    s.connect((HOST, PORT))
    s.send(f"{local_time},{client_port}".encode())
    s.close()

    # Step 3: Listen for adjustment
    listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    listener.bind((HOST, client_port))
    listener.listen(1)

    conn, _ = listener.accept()
    adjustment = float(conn.recv(1024).decode())

    adjusted_time = local_time + adjustment

    print(f"[Client Offset {offset}] Adjustment received: {adjustment:.2f}")
    print(f"[Client Offset {offset}] Adjusted time: {adjusted_time:.2f}\n")

    conn.close()
    listener.close()


if __name__ == "__main__":
    offset = float(input("Enter clock offset (e.g. 2.5): "))
    client_node(offset)
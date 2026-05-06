import socket
import threading
import time

HOST = '127.0.0.1'
PORT = 65432
NUM_CLIENTS = 3

client_times = {}  # {(ip, port): time}
lock = threading.Lock()

def handle_client(conn, addr):
    try:
        data = conn.recv(1024).decode()
        print("Raw data:", data)

        # Expect: time,port
        if "," not in data:
            print("Invalid data from client:", data)
            return

        client_time, client_port = data.split(",")
        client_time = float(client_time)
        client_port = int(client_port)

        print(f"Received time {client_time:.2f} from {addr[0]}:{client_port}")

        with lock:
            client_times[(addr[0], client_port)] = client_time

    except Exception as e:
        print("Error handling client:", e)

    finally:
        conn.close()


def send_adjustments():
    all_times = list(client_times.values())
    coordinator_time = time.time()
    all_times.append(coordinator_time)

    avg_time = sum(all_times) / len(all_times)
    print(f"\nAverage time: {avg_time:.2f}\n")

    for (ip, port), client_time in client_times.items():
        adjustment = avg_time - client_time
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            s.connect((ip, port))
            s.send(str(adjustment).encode())
            s.close()

            print(f"Sent adjustment {adjustment:.2f} to {ip}:{port}")

        except Exception as e:
            print(f"Error sending to {ip}:{port} →", e)


def main():
    print("Coordinator started. Waiting for client times...\n")

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind((HOST, PORT))
    server.listen(NUM_CLIENTS)

    threads = []

    for _ in range(NUM_CLIENTS):
        conn, addr = server.accept()
        t = threading.Thread(target=handle_client, args=(conn, addr))
        t.start()
        threads.append(t)

    for t in threads:
        t.join()

    print("\nAll clients responded. Sending adjustments...\n")

    send_adjustments()
    server.close()


if __name__ == "__main__":
    main()
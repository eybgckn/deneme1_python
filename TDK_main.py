
#!/usr/bin/env python3
import socket

IP, PORT = "10.11.12.190", 8003

while True:
    cmd = input("> ").strip()
    if cmd.lower() in {"quit", "exit"}:
        break
    with socket.create_connection((IP, PORT), 3) as s:
        s.sendall((cmd + "\n").encode())
        if cmd.endswith("?"):
            print(s.recv(1024).decode().strip())


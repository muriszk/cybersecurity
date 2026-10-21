import socket 

alvo = input("Type the IP of your domain: ")

for port in range(5000,6000):
    cilent = socket.socket()

    cilent.settimeout(1)

    result = cilent.connect_ex((alvo, port))

    if result == 0:
        print(f"Port {port} open")
    else:
        print(f"Port {port} closed")

    cilent.close()

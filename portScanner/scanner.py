import socket 

alvo = input("Type the IP of your domain: ")
savePath = './cybersecurity/portScanner/log.txt'

with open(savePath, 'a') as file:

    for port in range(5000,6000):
        client = socket.socket()

        client.settimeout(1)

        result = client.connect_ex((alvo, port))

        if result == 0:
            print(f"Port {port} open", file = file)

        client.close()

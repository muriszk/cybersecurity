import socket 

alvo = input("Digite o IP ou domínio: ")

for porta in range(1,101):
    cliente = socket.socket()

    cliente.settimeout(1)

    resultado = cliente.connect_ex((alvo, porta))

    if resultado == 0:
        print(f"Porta {porta} aberta")
    else:
        print(f"Porta {porta} fechada")

    cliente.close()

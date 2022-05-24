import socket

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

ip = input("Inserire l'indirizzo del server: ")
port = input("Inserire la porta per la comunicazione: ")

while True:
    m = input("Inserire il numero del motore da muovere: ")
    if int(m) == 0:
        res = s.sendto(m.encode(), (f"{ip}", int(port)))
        print("Chiusura comunicazione in corso...")
        s.close()
        break
    elif int(m) > 5 or int(m) < 0:
        res = s.sendto(m.encode(), (f"{ip}", int(port)))
        print("Motore non valido...")
    else:
        m2 = input("Inserisci il valore di quanto muovere il motore: ")
        m = m + ',' + m2
    res = s.sendto(m.encode(), (f"{ip}", int(port)))

    if res:
        print("\nMessaggio inviato...")
    else:
        print("Errore... riprovare")
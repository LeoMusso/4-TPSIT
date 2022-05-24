from threading import Thread, local
import socket
import csv
import os

class send(Thread):
    def __init__(self, nome, s, port):
        Thread.__init__(self)
        self.nome = nome

    def run(self):
        name = input("Inserire il nome utente: ")
        ip = "192.168.0.104"
        #ip = "127.0.0.1"
        while True:
            m = str(input(""))
            m2 = m.upper()
            if m2 == 'EXIT':
                s.close()
            else:
                m = '>>' + name + ': ' + m
                res = s.sendto(m.encode(), (f"{ip}", int(port)))

class receive(Thread):
    def __init__(self, nome, s):
        Thread.__init__(self)
        self.nome = nome

    def run(self):
        while True:
            mess = s.recvfrom(1024)
            mess = mess[0].decode()
            if len(mess) < 0:
                s.close()
            else:
                print(mess)

########################MAIN#####################
#####################FILE_MANAGER################
fileName = r"C:\\Users\\leomu\\Documents\\scuola\\tpsiti\\4btob\\Python\\chat\\rubrica\\rub.csv"
ceck = os.path.isfile(fileName)
if ceck:
    print("Il file esiste...")
else:
    print("il file non esiste...")
    question = str(input("Vuoi creare il file? [Y/N] "))
    question = question.upper()

    if question == 'Y' or question == "YES":
        with open(fileName, 'w', newline='')as filecsv:
            filecsv.close()

##################CONNESSIONE####################
port = 888
'''
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.connect(("8.8.8.8", 80))
loc = str(s.getsockname()[0])
s.close()'''
loc = "127.0.0.1"
s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
if s.bind((loc, port)):
    print("server in ascolto...")
else:
    print("Connessione fallita...")
        ###############THREAD##############
s1 = send("send", s, port)
s2 = receive("receive", s)
s2.start()
s1.start()
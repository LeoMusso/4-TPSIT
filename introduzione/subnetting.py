#####################  LIBERIE  ################################

##################### DIZIONARI ##############################
sub = {30:'255.255.255.252', 29:'255.255.255.248', 28:'255.255.255.240', 27:'255.255.255.227', 26:'255.255.255.192', 25:'255.255.255.128', 24:'255.255.255.0'}

##################### FUNZIONI  ###############################
def ipchecker():
    while True:
        ip = input('Inserisci un indirizzo Ip: ')
        a = ip.split('.')
        try:
            if ((len(a) == 4) and (1 <= int(a[0]) <= 223) and (int(a[0]) != 127) and (int(a[0]) != 169 or int(a[1]) != 254) and (0 <= int(a[1]) <= 255) and (0 <= int(a[2]) <= 255) and (0 <= int(a[3]) <= 255)):
                break
        except ValueError:
            print('please enter an integer')
        else:
            if (int(a[0]) == 127):
                answer = input(
                    'this is a loopback ip address do you wish to continue')
                if answer == 'yes' or answer == 'y':
                    continue
                else:
                    break
            print('Ip non valido\n')
            continue
    return ip

def divisione(ip):
    IpSplit = ip.split(".")
    return IpSplit


def dec_bin(n):
    b =''
    temp = n
    if n == 0:
        b = '00000000'

    while n > 0:
        if n % 2 == 0:
            b ='0'+ b
        else:
            b ='1'+ b
        n = int(n/2)
    
    if 0 < temp < 1:
        b = "0000000" + b
    elif 1 < temp <= 3:
        b = '000000' + b
    elif 4 <= temp <= 7:
        b = '00000' + b 
    elif 8 <= temp <= 16:
        b = '0000' + b
    
    return b

def conversione():
    Ip = ipchecker()
    #print(Ip)
    
    ipchech = bin(int(Ip.split('.')[0])).split('b')
    ipcut = str(ipchech[:3])

    if ipcut == '110':
        ipsplit = Ip.split('.')
        realip = str(ipsplit[0] + '.' + ipsplit[1] + ipsplit[2] + '.')
        lastoct = int(Ip.split('.')[3])

        lastsub = 0
        ipblocks = [2, 4, 16, 32, 64, 128, 254]
        ipblockerselector = 0
        
        selector = int(input('Inserire il numero di utenti: '))
        
        for i in ipblocks:
            if i >= selector:
                ipblockerselector = i
                break        
        if ipblockerselector == 2:
            lastsub = 252
        elif ipblockerselector == 4:
            lastsub = 248
        elif ipblockerselector == 16:
            lastsub = 240
        elif ipblockerselector == 32:
            lastsub = 224
        elif ipblockerselector == 64:
            lastsub = 192
        elif ipblockerselector == 128:
            lastsub = 128
        elif ipblockerselector == 254:
            lastsub = 0

        subnet = '255.255.255.'+ str(lastsub)
        subnetsplit = subnet.split('.')

        binsubnet = []

        for i in subnetsplit:
            binsubnet.append(bin(int(i)).split('b')[1])
        binsubjoin = ''.join(binsubnet)
        cidr = binsubjoin('1')

        print('you needed a network that can accommodate  ' + str(selector) +
             '  nodes in a network\n\nyou would probably use this subnet mask:\n' + subnet + ' = /' + str(cidr))

        while True:
            option = input('Vuoi andare avanti e calcolare gli indirizzi? (y/n):\t')
            if option == 'y' or option == 'Y':
                subSplit = subnet.split('.')

                print(subSplit[1])

###################### CODICE #########################
conversione()
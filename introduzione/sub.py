def ipchecker():
    while True:
        ip=input('enter a valid ip address:\n')
        a=ip.split('.')
        try:
            if ( (len(a)==4) and ( 1<=int(a[0])<=223) and (int(a[0])!=127) and (int(a[0])!=169 or int (a[1])!=254) and (0<= int(a[1])<=255) and (0<=int(a[2]) <=255) and (0<=int(a[3])<=255)):
                print('correct ip address')
                break
        except ValueError:
            print('please enter an integer')
        else:
            if (int(a[0])==127):
                answer=input('this is a loopback ip address do you wish to continue')
                if answer=='yes' or answer=='y':
                    continue
                else:
                    break
            print('bad ip')
            continue
    return ip


def Subnetor():

    while True:
        # collecting valid ip address from users
        ip = ipchecker()
        # checks
        ipchecks = bin(int(ip.split('.')[0])).split('b')[1]
        ipcut = str(ipchecks[:3])
        if ipcut == '110':
            #cutting out the last octet
            ipsplit = ip.split('.')
            realip = str(ipsplit[0]+'.'+ipsplit[1]+'.'+ipsplit[2]+'.')
            #cutting out the last octet for operations on class c ip addresses
            lastoct = int(ip.split('.')[3])

            #getting the last octet for class c subnets mainly
            lastsub = 0
            ipblocks = [2, 4, 16, 32, 64, 128, 254]
            ipblockselector = 0
            selector = int(input('enter number of users per network:\n'))
            for i in ipblocks:
                if i >= selector:
                    ipblockselector = i
                    break
            if ipblockselector == 2:
                lastsub = 252
            elif ipblockselector == 4:
                lastsub = 248
            elif ipblockselector == 16:
                lastsub = 240
            elif ipblockselector == 32:
                lastsub = 224
            elif ipblockselector == 64:
                lastsub = 192
            elif ipblockselector == 128:
                lastsub = 128
            elif ipblockselector == 254:
                lastsub = 0

            subnet = '255.255.255.'+str(lastsub)
            subnetsplit = subnet.split('.')

            binsubnet = []
            for i in subnetsplit:
                binsubnet.append(bin(int(i)).split('b')[1])
            binsubjoin = ''.join(binsubnet)
            cidr = binsubjoin.count('1')

            print('you needed a network that can accommodate  ' + str(selector) +
                  '  nodes in a network\n\nyou would probably use this subnet mask:\n' + subnet + ' = /' + str(cidr))
            while True:
                option = input(
                    'wanna go ahead and print the ip address (y/n)?:\t')
                if option == 'y':
                    subSplit = subnet.split('.')

                    if (0 <= int(subSplit[1]) < 255):
                        print('subnetting in the second octet')
                        binoctet = bin(int(subSplit[1])).split('b')[1]
                        print(binoctet)
                        increament = 256-int(subSplit[1])
                        print(increament)
                        #count.counts(increament)

                    elif (0 <= int(subSplit[2]) < 255):
                        print('subnetting in the third octet')
                        binoctet = bin(int(subSplit[2])).split('b')[1]
                        #print(binoctet)
                        increament = 256 - int(subSplit[2])
                        #print(increament)
                        #count.counts(increament)

                    elif (0 <= int(subSplit[3]) < 255):
                        print('subnetting in the last octet')
                        binoctet = bin(int(subSplit[3])).split('b')[1]
                        #print(binoctet)
                        increament = 256 - int(subSplit[3])
                        #print(increament)
                        #iplist = count.counts(increament)

                        file1 = open("text3.txt", "w")
                        filewriteoption = input(
                            '\n wanna push the ip addresses to a file? (y/n):')
                        for ip in iplist:
                            if int(ip) > lastoct:
                                print(realip+str(ip))
                                str1 = realip+str(ip)
                                if filewriteoption == 'y':
                                    file1.writelines(str1)
                        file1.close()
                        if filewriteoption == 'y':
                            print('\n file writing done! check text3.txt your pc\n')

                else:
                    print('thank you for using my application bye\n')
                    import time
                    time.sleep(2)
                    print('exiting.......')
                    exit()
        elif ipcut != '110':
            print('...But enter a class C ip address')


Subnetor()
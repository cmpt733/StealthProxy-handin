import argparse as Argp
import asyncio as Aio
import sys
from support import config as Fig
from support import connect as Connect
from support.password import (invalidPass, savePass,inputPass, genRanPass)
from support.serverhandle import Serverhandle as Sh


def ser_server(Setting):
    #Setting belongs to class Fig.Config
    lop = Aio.get_event_loop()
    if lop is not None:
        pass
    else:
        print ("No current event loop, try again")
        lop = Aio.get_event_loop()
    # get server side address and port, and password
    sevAdr=Setting.serverAddr
    sevPot=Setting.serverPort
    pwd=Setting.password
    ldr = Connect.Address(sevAdr, sevPot)
    sev = Sh(loop=lop, password=pwd, addr_listen=ldr)
    print('listening port is '+ str(sevPot))
    print('sample command to set up client, replace ip 127.0.0.1 with actual hostname if connected from internet\n\n')
    # print the password use in client side
    print('python3 client.py -l "http://127.0.0.1'  +":"+ str(sevPot)+"/#"+ savePass(Setting.password)+'"')
    def Listening(address):
        print("\n\nlistening")
    #keep listening
    Aio.ensure_future(sev.listen(Listening))
    lop.run_forever()


def main():
    # use argparse to command-line interfaces
    struct = Argp.ArgumentParser(description='shadowsocks implements. Server side.')

    argues=struct.add_argument_group('argues')

    argues2=argues.add_argument('-lp',metavar='ListenPort',type=int,help='the port serverlisten to,set to 8388 in default')
    argues3=argues.add_argument('-c', metavar='ConnectKey', help='connect key for valification and encryption between server and client')
    argues4=argues.add_argument('-r',action='store_true',default=False,help='initialize with a random password')

    args = struct.parse_args()
    

    #GetServerAddr=args.la
    GetServerPort=args.lp
    GetPassword=args.c
    GetRando=args.r
    NoRando=not GetRando


    Setting = Fig.Config(None, None, None, None, None)
    # test the available of server

    if GetServerPort:
        Setting = Setting._replace(serverPort=GetServerPort)
    if GetPassword:
        try:
            pwd= inputPass(GetPassword)
            Setting = Setting._replace(password=pwd)
        except invalidPass:
            struct.print_usage()
            print('password error')
            sys.exit(1)
    sdr=Setting.serverAddr
    sdrEmpty=sdr is None
    if  sdrEmpty:
        Setting = Setting._replace(serverAddr='0.0.0.0')
    spt=Setting.serverPort
    sptEmpty=spt is None 
    if sptEmpty:
        Setting = Setting._replace(serverPort=8388)
    pwdEmpty=Setting.password is None
    if pwdEmpty:
        if NoRando:
            struct.print_usage()
            print('please incluse a password, -c can be use to connect with an existing password or -r can generate a random password')
            sys.exit(1)

    if GetRando:
        print('randomly initial with a password')
        Setting = Setting._replace(password=genRanPass())

    ser_server(Setting)


if __name__ == '__main__':
    main()

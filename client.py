import argparse as Argp
import asyncio as Aio
import sys
from threading import local
from support import config as Fig
from support import connect as Connect
from support.password import invalidPass, inputPass
from support.clienthandle import Localhandle as Lh


def client_server(argues: Fig.Config):
    lop = Aio.get_event_loop() #get event loop
    if lop is not None:
        pass
    else:
        print ("No current event loop, try again")
        lop = Aio.get_event_loop()
    # get client and server side address and port, and password
    locAdr=argues.localAddr
    locPort=argues.localPort
    servAddr=argues.serverAddr
    servPort=argues.serverPort
    passwd=argues.password

    ldr = Connect.Address(locAdr, locPort)
    rdr = Connect.Address(servAddr,servPort)
    # connect to the client side
    sev = Lh(loop=lop,password=passwd,addr_listen=ldr,remoteAddr=rdr)
    if ldr:
        if locPort:
            print('Listen to %s:%d\n' % (locAdr,locPort))
    def Listening(address):
        print("listening")
    # continue listening until end
    Aio.ensure_future(sev.listen(Listening))
    lop.run_forever()


def main():
    # use argparse to command-line interfaces
    structconfig = Argp.ArgumentParser(description='shadowsocks implements client')

    argues = structconfig.add_argument_group('argues')

    argues1=argues.add_argument('-l',metavar='Link',help='use link contains server address, port and password to connect')
    argues2=argues.add_argument('-sa', metavar='ServerAddress', help='server address')
    argues3=argues.add_argument('-sp',metavar='ServerPort',type=int,help='server port, default: 8388')
    argues4=argues.add_argument('-c', metavar='ConnectKey', help='connect key for valification and encryption between server and client')

    args = structconfig.parse_args()
    GetUrl=args.l
    GetServerAddr=args.sa
    GetServerPort=args.sp
    GetPassword=args.c


    Setting = Fig.Config(None, None, None, None, None)


    if GetUrl:
        try:
            url_setting = Fig.loadURL(GetUrl)
        except:
            structconfig.print_usage()
            if Fig.InvalidURLError:
                print(f'invalid url {GetUrl!r}')
                sys.exit(1)

        Setting = Setting._replace(**url_setting._asdict())
    # test the available of client and server
    if GetServerAddr:
        Setting = Setting._replace(serverAddr=GetServerAddr)

    if GetServerPort:
        Setting = Setting._replace(serverPort=GetServerPort)

    if GetPassword:
        try:
            pwd = inputPass(GetPassword)
            Setting = Setting._replace(password=pwd)
        except invalidPass:
            structconfig.print_usage()
            print('invalid password')
            sys.exit(1)
    no_ldr=Setting.localAddr is None
    no_lpo=Setting.localPort is None
    no_pwd=Setting.password is None
    no_sdr=Setting.serverAddr is None
    no_spo=Setting.serverPort is None
    
    Setting = Setting._replace(localAddr='127.0.0.1')
    Setting = Setting._replace(localPort=1080)

    if no_spo:
        Setting = Setting._replace(serverPort=8388)

    if no_pwd:
        structconfig.print_usage()
        print('need ConnectKey, use -c to add connect key')
        sys.exit(1)

    if no_sdr:
        structconfig.print_usage()
        print('\n need ServerAddress, use -sa to add server address, default to 127.0.0.1 \n')

    client_server(Setting)


if __name__ == '__main__':
    main()

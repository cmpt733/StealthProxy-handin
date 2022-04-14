import logging
import typing
import socket as Sc
import asyncio
import sys

from . import connect as Con
from .encryption import enc_pass as encrypt
from .securesocket import SecureSocket as Ses


#we need to make a socket connection and logger.
#Then we can do the listening.
Connection = Sc.socket
logger = logging.getLogger(__name__)


class Serverhandle(Ses):
    # create a server
    def __init__(self,loop,password,addr_listen):
        #loop=asyncio.AbstractEventLoop loop
        #password: bytearray
        #addr_listen: Con.Address
        super().__init__(loop=loop, pin=encrypt.codec(password))
        lisaddr = addr_listen
        self.addr_listen = lisaddr
    
    async def listen(self, didListen):
        #didListen: typing.Callable=None
        try:
            # start to listen from client
            with Sc.socket(Sc.AF_INET, Sc.SOCK_STREAM) as listener:
                socket_option=listener.setsockopt(Sc.SOL_SOCKET, Sc.SO_REUSEADDR, 1)
                set_block=listener.setblocking(False)
                bind_addr=listener.bind(self.addr_listen)
                max_connect=listener.listen(Sc.SOMAXCONN)

                logger.info('Listen to %s:%d' % self.addr_listen)
                if not didListen:
                    print ("it is not listening.")
                else:
                    GetName=listener.getsockname()
                    didListen(GetName)

                while 1:
                    connection, address = await self.loop.sock_accept(listener)
                    logger.info('Receive %s:%d', *address)
                    asyncio.ensure_future(self.handleConnection(connection))
                else:
                    print("connection fail")
        except:
            sys.exit

    # keep connection from the local client side
    async def handleConnection(self, connection):
        # connection: Connection
        buf = await self.denc_input(connection)
        # if not socks
        if not buf:
            connection.close()
            return
        
        b0 = 0x00
        b1 = 0x01
        b3 = 0x03
        b4 = 0x04
        b5 = 0x05
        # because socks5 is 0x05, so if not 0x05
        if buf[0] != b5:
            connection.close()
            return

        await self.denc_output(connection, bytearray((b5, b0)))

        buf = await self.denc_input(connection)
        if len(buf) < 7 or buf[1] != b1:
            connection.close()
            return

        dstIP = None
        dstPort = buf[-2:]
        dstPort = int(dstPort.hex(), 16)
        dstFamily = None
        desport = buf[3]
        flag1=buf[3] == b1
        flag2=buf[3] == b3
        flag3=buf[3] == b4
        if flag1:
            # ipv4
            ipAddress_bin = buf[4:8]
            ipAddress_str = Sc.inet_ntop(Sc.AF_INET, ipAddress_bin)
            # check whether it works, if not go again
            if ipAddress_str is str:
                pass
            else: 
                ipAddress_str = Sc.inet_ntop(Sc.AF_INET, ipAddress_bin)
            dstAddr = Con.Address(ip=ipAddress_str, port=dstPort)
            dstFamily = Sc.AF_INET
        elif flag2:
            # domain
            dstip = buf[5:-2]
            dstIP = dstip.decode()
            dstAddr = Con.Address(ip=dstIP, port=dstPort)
        elif flag3:
            # ipv6
            ipAddress_bin = buf[4:20]
            ipAddress_str = Sc.inet_ntop(Sc.AF_INET6, ipAddress_bin)
            # same issue
            if ipAddress_str is str:
                pass
            else:
                ipAddress_str = Sc.inet_ntop(Sc.AF_INET, ipAddress_bin)
            dstAddr = (dstIP, dstPort, 0, 0)
            dstFamily = Sc.AF_INET6
        else:
            connection.close()
            return

        dstServer = None
        
        if not dstFamily:
            host = dstAddr[0]
            port = dstAddr[1]
            for response in await self.loop.getaddrinfo(host, port):
                dstFamily = response[0]
                socktype = response[1]
                proto = response[2]
                dstAddr = response[4]
                try:
                    dstser = Sc.socket(dstFamily, socktype, proto)
                    dstServer = dstser
                    dstServer.setblocking(False)
                    await self.loop.sock_connect(dstServer, dstAddr)
                    break
                except OSError:
                    if dstServer is None:
                        pass
                    else:
                        dstServer.close()
                        dstServer = None
        else:
            try:
                dstser = Sc.socket(family=dstFamily, type=Sc.SOCK_STREAM)
                if dstser is None:
                    dstser = Sc.socket(family=dstFamily, type=Sc.SOCK_STREAM)
                else:
                    dstServer = dstser
                    dstServer.setblocking(False)
                    await self.loop.sock_connect(dstServer, dstAddr)
            except OSError:
                if dstServer is None:
                    pass
                else:
                    dstServer.close()
                    dstServer = None

        if dstFamily is not None:
            pass
        else:
            return

        await self.denc_output(connection,bytearray((b5, b0, b0, b1, b0, b0, b0, b0, b0, b0)))
        def cleanUp(task):
            if succuess == 1:
                dstServer.close()
                connection.close()

        conn = asyncio.ensure_future(self.dencrypt_input(dstServer, connection))
        conn2dst = conn
        dstconn = asyncio.ensure_future(self.enc_input(connection, dstServer))
        dst2conn = dstconn
        task = asyncio.ensure_future(asyncio.gather(conn2dst, dst2conn, loop=self.loop, return_exceptions=True))
        #task.add_done_callback(cleanup.cleanUp)
        # condition
        succuess=1
        task.add_done_callback(cleanUp)
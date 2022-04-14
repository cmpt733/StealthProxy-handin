import typing
import socket as Sc
import asyncio
import sys
import logging

from . import connect as Con
from .encryption import enc_pass as encrypt
from .securesocket import SecureSocket as Ses

'''
    First we need to make a socket connection and logger.
    Then we can do the listening.
'''
Connection = Sc.socket
logger = logging.getLogger(__name__)


class Localhandle(Ses):
    # create a local side
    def __init__(self, loop, password, addr_listen, remoteAddr):
        # loop : asyncio.AbstractEventLoop
        # password : bytearray
        # addr_listen : net.Address
        # remoteAddr : net.Address
        super().__init__(loop=loop, pin=encrypt.codec(password))
        lisaddr = addr_listen
        self.addr_listen = lisaddr
        readdr = remoteAddr
        self.remoteAddr = readdr

    # The local side starts listening and receives the connection from 
    # the browser
    async def listen(self, didListen):
        # didListen: typing.Callable=None
        try:
            with Sc.socket(Sc.AF_INET, Sc.SOCK_STREAM) as listener:
                # local client listening
                socket_option = listener.setsockopt(Sc.SOL_SOCKET, Sc.SO_REUSEADDR, 1)
                set_block = listener.setblocking(False)
                bind_addr = listener.bind(self.addr_listen)
                max_connect = listener.listen(Sc.SOMAXCONN)
                

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
            sys.exit()

    #listen.listen(self, didListen)

    # headle the connection
    async def handleConnection(self, connection):
        # connection: Connection
        remoteServer = await self.dialRemote()
        def cleanUp(task):
            # if the condition fit, it will exit
            if success == 1:
                remoteServer.close()
                connection.close()

        # read the data from local user and send to server 
        ltore = asyncio.ensure_future(self.dencrypt_input(connection, remoteServer))
        localToremote = ltore
        # send data from local user to proxy
        retol = asyncio.ensure_future(self.enc_input(remoteServer, connection))
        remoteTolocal = retol
        task = asyncio.ensure_future(asyncio.gather(localToremote, remoteTolocal, loop=self.loop, return_exceptions=True))
        # check the data is whether send successful, if works well, success is 1 otherwise is 0
        success=1
        task.add_done_callback(cleanUp)

    # make the socket connect our server
    async def dialRemote(self):
        try:
            reconn = Sc.socket(Sc.AF_INET, Sc.SOCK_STREAM)
            remote_connection = reconn
            remote_connection.setblocking(False)
            # check the socket is working or not.
            if remote_connection.setblocking(False):
                # set some condition to check
                pass
            else:
                sys.exit
            await self.loop.sock_connect(remote_connection, self.remoteAddr)
        except Exception as err:
            # give the error message when it face the exception
            rec=remote_connection
            adr=self.remoteAddr
            err_str=str(err)
            error_msg = "Connection fail"+err_str
            raise ConnectionError(error_msg)
        return remote_connection

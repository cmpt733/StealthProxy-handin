from logging import *
import socket
from asyncio import *

from .encryption import enc_pass


flag=True
Log1 = getLogger(__name__)


class SecureSocket:
    
    #SecureSocket is the socket connection we define to both decode and encode data on server adn client side
    # create a encrypt TCP socket
    def __init__(self,loop,pin):
        #
        #loop type:asyncio.AbytearrtractEventloop
        #pin type:enc_pass
        # check if the loop is empty or not
        if loop:
            self.loop=loop
        else:
            self.loop=get_event_loop() 
        self.pin = pin

    # decrypt the data from input data flow
    async def denc_input(self,connection):
        # connection type:socket.socket
        input_flow = await self.loop.sock_recv(connection, 1024)
        Log1.debug('%s:%d codeblock1 %r', *connection.getsockname(), input_flow)
        bytearr = bytearray(input_flow)
        self.pin.denc_data(bytearr)
        return bytearr

    # After getting the origin data from input data flow, encrypt them and write to output
    async def denc_output(self, connection, bytearr):
        #connection: socket.socket
        #bytearr: bytearray
        bytearr_byte=bytes(bytearr)
        Log1.debug('%s:%d codeblock11 %s', *connection.getsockname(), bytearr_byte)

        #bytearr = bytearr.copy()

        self.pin.enc_data(bytearr)
        await self.loop.sock_sendall(connection, bytearr)

    # encrypt the input data from source and send to the destination, when there is no data, break
    async def enc_input(self, destination, source):
        #destination: socket.socket
        #source: socket.socket
        
        #encrypt data flow
        
        Log1.debug('codeblock2 %s:%d => %s:%d', *source.getsockname(), *destination.getsockname())

        while flag:
            if flag:
                input_flow = await self.loop.sock_recv(source, 1024)
            if input_flow:
                pass
            else:
                break

            await self.denc_output(destination, bytearray(input_flow))

    # dencrypt the input data from source and send to the destination
    # The source and destination is different from enc_input
    async def dencrypt_input(self, destination, source):
        #destination: socket.socket
        #source: socket.socket
        #decode dataflow
        Log1.debug('codeblock22 %s:%d => %s:%d', *source.getsockname(), *destination.getsockname())

        while flag:
            if flag:
                bytearr = await self.denc_input(source)
            if bytearr:
                pass
            else:
                break

            await self.loop.sock_sendall(destination, bytearr)
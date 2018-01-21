import socketserver, time
from constants import HOST, PORT, GATE_1
from gpio_actions import *


class ClientHandler(socketserver.BaseRequestHandler):
    def handle(self):
        while True:
            msg_data = self.request.recv(1024)
            
            if not msg_data: break

            response = msg_data

            self.request.send(response)
        print('close')
        self.request.close()
 

address = (HOST, PORT)
server = socketserver.ThreadingTCPServer(address, ClientHandler)
server.serve_forever()
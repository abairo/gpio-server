from socket import *
import threading
 
class Client(threading.Thread):
    
    def __init__(self, client, server, port, *message):
  
        self.client = client
 
        self.server = server
  
        self.port = port
         
        self.msgs = message
 
        threading.Thread.__init__(self)
 
    def run(self):
 
        sockobj = socket(AF_INET, SOCK_STREAM)
        sockobj.connect((self.server, self.port))
         
        for msg in self.msgs:
            sockobj.send(msg)
 
            import json
            data = sockobj.recv(1024)
            msg = json.loads(data)
            print('Cliente', self.client, 'recebeu:', msg['value'])
 
        print('close')
        sockobj.close()


serverHost = 'localhost'
serverPort = 8100
import json

message = [(json.dumps(dict(value=1)).encode())]

for client in range(1):
    Client(client, serverHost, serverPort, *message).start()

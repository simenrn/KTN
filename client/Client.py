# -*- coding: utf-8 -*-
import socket
from MessageReceiver import MessageReceiver
from MessageParser import MessageParser

class Client:
    """
    This is the chat client class
    """

    def __init__(self, host, server_port):
        """
        This method is run when creating a new Client object
        """

        # Set up the socket connection to the server
        self.connection = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        receiveThread = MessageReceiver(client,self.connection)# lager instans av MessageReceiver
        receiveThread.start() # kjører run() i MessageReceiver i en ny tråd
        messageParser = MessageParser() #lager instans av MessageParser
    
        self.run()

    def run(self):
        # Initiate the connection to the server
        self.connection.connect((self.host, self.server_port))
        
        
    def disconnect(self):
        self.connection.close() # lukker socketen mellom klient og server
        receiveThread.join()    # slår sammen messageReceive tråden med main tråden(lukker)
        pass

    def receive_message(self, message):
        messageParser.parse(message)
        # Kaller på messageparser med message fra messagereceiver med
        # udekodet json melding
        pass

    def send_payload(self, data):
        self.connection.send(data)
        pass
        
    # More methods may be needed!


if __name__ == '__main__':
    """
    This is the main method and is executed when you type "python Client.py"
    in your terminal.

    No alterations are necessary
    """
    client = Client('localhost', 9998)

    print "Clients receive thread: ", receiveThread.name

        print "Write login to start chatting, or help to get info: "
        while True:
            data = raw_input("Enter request: ")
            data_list = data.split(" ",1)
            if (data_list[0] == "logout"):
                send_payload(messageParser.parse_send(data_list[0], None))
                self.disconnect()
                break
            if (0 < len(data_list) < 3 ):
                if len(data_list) == 1:
                    send_payload(messageParser.parse_send(data_list[0], None))
                else:
                    send_payload(messageParser.parse_send(data_list[0],data_list[1]))
            else:
                print "Invalid input.."

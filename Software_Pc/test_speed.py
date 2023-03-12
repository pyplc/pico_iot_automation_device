
import socket
import sys
import json
import time

var = {'Q1':'off', 'Q2':'off', 'Q3':'off', 'Q4':'off'}

# Create a TCP/IP socket
sock = socket.create_connection(('10.0.0.100', 10000))  # 'espressif' oder 'localhost'


def send_data():
        # Create a TCP/IP socket
        #self.sock = socket.create_connection(('10.0.0.100', 10000))  # 'espressif' oder 'localhost'
        try:
            # Send data
            #global var
            #var['Q1'] = 'on'
            str_json = json.dumps(var)
            #message = b'R1_on'
            message = bytes(str_json, 'utf-8')
            print('sending {!r}'.format(message))
            sock.sendall(message)
            # Anzeige was gestepelt wurde löschen
            amount_received = 0
            amount_expected = len(message)

            while amount_received < amount_expected:
                data = sock.recv(100)
                amount_received += len(data)
                print('received {!r}'.format(data))

        finally:
            print('socket open')
            #self.sock.close()

a = 0

while True:
        if a <= 20:
                var['Q1'] = 'on'
        else:
                var['Q1'] = 'off'

        if a >= 25:
                var['Q2'] = 'on'
        else:
                var['Q2'] = 'off'
        print(a)
        a += 1
        var['Q4'] = str(a)
        send_data()
        #time.sleep(0.1)
        if a >= 40:
                a = 0

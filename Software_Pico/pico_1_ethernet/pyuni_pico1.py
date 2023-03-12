import network
import time
from usocket import socket
from machine import Pin, SPI, UART, WDT
import rp2

# wotchdog objekt
#wdt = WDT(timeout=20000)  # enable it with a timeout of 2s

#intern led
led = Pin(25, Pin.OUT)
led.value(1)

#var
temp = 0.0
var = {'Q1':'off', 'Q2':'off', 'Q3':'off', 'Q4':'off', 'temp':'0.0'}

#serial objekt
uart1 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

# Setup your network configuration below
IP_ADDRESS = '10.0.0.100'
SUBNET_MASK = '255.255.255.0'
GATEWAY_ADDRESS = '10.0.0.138'
DNS_SERVER = '0.0.0.0'

def init():
    spi=SPI(1,2_000_000, mosi=Pin(11),miso=Pin(12),sck=Pin(10), polarity=0, phase=0, bits=8)
    nic = network.WIZNET5K(spi,Pin(13),Pin(15)) #spi,cs,reset pin
    nic.ifconfig((IP_ADDRESS, SUBNET_MASK, GATEWAY_ADDRESS, DNS_SERVER))
    while not nic.isconnected():
        time.sleep(1)
        print(nic.regs())     

def server_loop(): 
    s = socket()
    s.bind(('10.0.0.8', 10000)) #Source IP Address
    s.listen(5)
    led.value(0)
    
    while True:
        conn, addr = s.accept() # programm bleibt stehen bis etwas empfangen wird
        print('conn', conn)
        print("Connect to:", conn, "address:", addr) 
        print("Loopback server Open!")
        while True:
            try:
                data = conn.recv(2048)
                led.value(1)
            except:
                conn.close()
                print('Close Connection')
                led.value(0)
                break
            print(data.decode('utf-8'))
            if data != 'NULL':
                #print('erste')
                uart1.write('2')
                #if uart1.any():
                    #rxd = 1
                # zeit warten bis antwort von pico 2 kommt
                time.sleep(0.06)
                rxd = uart1.read()
                #print('Zweite')
                global var, wdt
                #b = bytearray(rxd, encoding="utf-8")
                str1 = rxd.decode('UTF-8')
                var['Q3'] = str1
                try:
                    conn.send(bytes(str(var),'UTF-8'))
                except:
                    conn.close()
                    print('Abort Connection')
                    led.value(0)
                    break
                # watchdog reset
                #wdt.feed()
                
                led.value(0)

def client_loop():
    s = socket()
    s.connect(('10.0.0.8', 10000)) #Destination IP Address
    
    print("Loopback client Connect!")
    while True:
        data = s.recv(2048)
        print(data.decode('utf-8'))
        if data != 'NULL' :
            s.send(data)
            
def main():
    init()
    server_loop() #Loopback Server Mode
    #client_loop() #Loopback client Mode

#if __name__ == "__main__":
main()
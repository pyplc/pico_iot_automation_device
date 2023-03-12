
from machine import I2C, Pin, UART
from sh1106 import SH1106_I2C
import framebuf
import time
from onewire import OneWire
from ds18x20 import DS18X20
from utime import sleep, sleep_ms

# Initialisierung GPIO, OneWire und DS18B20
one_wire_bus = Pin(6)
sensor_ds = DS18X20(OneWire(one_wire_bus))

# One-Wire-Geräte ermitteln
devices = sensor_ds.scan()
#print(devices)
print('init fertig')
print(devices)

#intern led
led = Pin(25, Pin.OUT)

WIDTH  = 128                                            # oled display width
HEIGHT = 64                                          # oled display height

i2c = I2C(0, scl=Pin(5), sda=Pin(4))                                           # Init I2C using I2C0 defaults, SCL=Pin(GP9), SDA=Pin(GP8), freq=400000
print("I2C Address      : "+hex(i2c.scan()[0]).upper()) # Display device address
print("I2C Configuration: "+str(i2c))                   # Display I2C config

#serial objekt
uart1 = UART(0, baudrate=9600, tx=Pin(0), rx=Pin(1))

oled = SH1106_I2C(WIDTH, HEIGHT, i2c)                  # Init oled display

# Raspberry Pi logo as 32x32 bytearray
buffer = bytearray(b"\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00|?\x00\x01\x86@\x80\x01\x01\x80\x80\x01\x11\x88\x80\x01\x05\xa0\x80\x00\x83\xc1\x00\x00C\xe3\x00\x00~\xfc\x00\x00L'\x00\x00\x9c\x11\x00\x00\xbf\xfd\x00\x00\xe1\x87\x00\x01\xc1\x83\x80\x02A\x82@\x02A\x82@\x02\xc1\xc2@\x02\xf6>\xc0\x01\xfc=\x80\x01\x18\x18\x80\x01\x88\x10\x80\x00\x8c!\x00\x00\x87\xf1\x00\x00\x7f\xf6\x00\x008\x1c\x00\x00\x0c \x00\x00\x03\xc0\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00")

# Load the raspberry pi logo into the framebuffer (the image is 32x32)
fb = framebuf.FrameBuffer(buffer, 32, 32, framebuf.MONO_HLSB)

# Clear the oled display in case it has junk on it.
oled.fill(0)

# Blit the image from the framebuffer to the oled display
oled.blit(fb, 96, 0)

# Add some text
oled.text("Raspberry Pi",5,5)
oled.text("Pico",5,15)

# Finally update the oled display so the image & text is displayed
oled.show()

tempTimer = False
tempStart = False
tempOn = 0
tempOff = 0
temp = 'keine Messung'

def temp():
    global tempTimer, tempOn, tempOff, sensor_ds, device, tempStart, temperatur
    
    if tempTimer == True:
        # Temperatur messen
        #print('step_1')
        if not tempStart:
            sensor_ds.convert_temp()
            tempStart = True
            #print('step_2')
        if tempOn < time.ticks_ms():
            #print('step_3')  
            if tempOff < time.ticks_ms():
                for device in devices:
                    print('Sensor:', device)
                    temperatur = str(sensor_ds.read_temp(device))
                    #temp = str(temp_float)
                    print('Temperatur:', temperatur, '°C')               
                tempTimer = False
                if not devices:
                    print('fehler messung temp')
    
    if tempTimer == False:
        tempOn = time.ticks_ms()
        tempOn += 750
        tempOff = tempOn + 2000
        tempTimer = True
        tempStart = False


ledTimer = False
deadlineOn = 0
deadlineOff = 0

def main():
    global ledTimer, deadlineOn, deadlineOff
    if ledTimer == True:     
        if deadlineOn < time.ticks_ms():          
            led.value(0)
            if deadlineOff < time.ticks_ms():
                ledTimer = False

    if ledTimer == False:
        deadlineOn = time.ticks_ms()
        deadlineOn += 1000
        deadlineOff = deadlineOn + 1000
        ledTimer = True
        led.value(1)
     
x = 0

while True:
    main()
    temp()
    oled.fill(0)
    oled.text(str(x),5,25)
    oled.show()
    #x += 1
    value = uart1.read()
    #if uart1.any():
        #x += 1
        #uart1.write(str(x))
    if value:
        x += 1
        #uart1.write(str(x))
        uart1.write(temperatur)
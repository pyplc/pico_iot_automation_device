**Pico IOT Automation Device** 

Here 2 pico are used, pico 1 is for communication and pico 2 is for arithmetic and output. In theory, all common protocols are supported, such as MQTT, Modbus, TEXT. Only TEXT (json) was tested here.

* 5V for Pico 1+2
* 24V for IO card (i2c)
* IO card protected against polarity reversal and overvoltage
* Both cards protected against polarity reversal
* Pico 2 is monitored with hardware wotchdog ic

Here the example was drawn with Kicad5.

![KICAD_Blid](https://github.com/pyplc/pico_iot_automation_device/blob/main/doc/pyplc.png)

![PCB](https://github.com/pyplc/pico_iot_automation_device/blob/main/doc/image.jpg)

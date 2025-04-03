import onewire
import machine
import ds18x20
import time

#initialize pin connected to the ds sensor. 
ds_pin = machine.Pin(12)
#create a object from onewire lib initialize with the pin.
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

#scan for the device on the bus.
roms = ds_sensor.scan()

while True :
    ds_sensor.convert_temp()
    time.sleep(1)
    for rom in roms:
        print(round(ds_sensor.read_temp(rom)), end= '\n')



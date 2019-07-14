import time
from energenie import Messages, OpenThings, radio, encoder, Devices

OpenThings.init(Devices.CRYPT_PID)

PURPLE_ID = 0x68B # captured from a real device using Monitor.py
m = OpenThings.alterMessage(
    Messages.SWITCH,
    header_sensorid=PURPLE_ID,
    recs_0_value=1)
purple_on = OpenThings.encode(m)

m = OpenThings.alterMessage(
    Messages.SWITCH,
    header_sensorid=PURPLE_ID,
    recs_0_value=0)
purple_off = OpenThings.encode(m)

GREEN_ON  = encoder.build_switch_msg(True, device_address=1)
GREEN_OFF = encoder.build_switch_msg(False, device_address=1)

def light_on(time1):
    if __name__ == "__main__":
        radio.init()
        try:
            radio.modulation(ook=True)
            radio.transmit(GREEN_ON)
            time.sleep(time1)
        finally:
            radio.finished()

def light_off(time1):
    if __name__ == "__main__":
        radio.init()
        try:
            radio.modulation(ook=True)
            radio.transmit(GREEN_OFF)
            time.sleep(time1)
        finally:
            radio.finished()
while True:
    light_off(0.5)
    light_on(0.5)
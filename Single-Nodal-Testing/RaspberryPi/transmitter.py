import time
import spidev
from pyrf24 import *
import RPi.GPIO as GPIO

# Setup SPI
spi = spidev.SpiDev()
spi.open(0, 0)
spi.max_speed_hz = 8000000

# Setup NRF24L01
radio = RF24(22, 0)
radio.begin()
radio.setPALevel(RF24_PA_LOW)  # Set power level
radio.enableDynamicPayloads()
#radio.setDataRate(RF24_2MBPS)

# Set the network address and channel
network_address = b"00001"
channel = 0
radio.openWritingPipe(network_address)
radio.setChannel(channel)

# Main loop
i = 0
while True:
    message = f"{i}:\tHello from Raspberry Pi!123456789-123456789-"
    radio.write(message.encode('utf-8'))
    print("Sent: ", message)
    i = i+1

# Cleanup
radio.powerDown()
spi.close()

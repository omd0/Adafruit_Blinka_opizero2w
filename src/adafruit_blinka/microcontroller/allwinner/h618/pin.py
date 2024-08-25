# SPDX-FileCopyrightText: 2024 Emad-Fussi for Adafruit Industries
# This code was written with assistance from Claude, an AI assistant created by Anthropic, PBC
# SPDX-License-Identifier: MIT
"""Allwinner H618 Pin Names"""
from adafruit_blinka.microcontroller.generic_linux.libgpiod_pin import Pin

# First, determine the chip number
__chip_num = 1
with open("/sys/class/gpio/gpiochip0/label", "r") as f:
    label = f.read().strip()
    if label == "1f02c00.pinctrl":  # You may need to verify this for Orange Pi Zero 2W
        __chip_num = 0

# Define pin mappings
PH0 = Pin((__chip_num, 224))
PH1 = Pin((__chip_num, 225))
PH2 = Pin((__chip_num, 226))
PH3 = Pin((__chip_num, 227))
PH4 = Pin((__chip_num, 228))
PH5 = Pin((__chip_num, 229))
PH6 = Pin((__chip_num, 230))
PH7 = Pin((__chip_num, 231))
PH8 = Pin((__chip_num, 232))
PH9 = Pin((__chip_num, 233))

PI6 = Pin((__chip_num, 262))
PI5 = Pin((__chip_num, 261))
PI4 = Pin((__chip_num, 260))
PI3 = Pin((__chip_num, 259))
PI2 = Pin((__chip_num, 258))
PI1 = Pin((__chip_num, 257))
PI0 = Pin((__chip_num, 256))
PI10 = Pin((__chip_num, 266))
PI12 = Pin((__chip_num, 268))
PI13 = Pin((__chip_num, 269))
PI16 = Pin((__chip_num, 272))

# Define special function pins
I2C1_SDA = PI6
I2C1_SCL = PI5
I2C0_SDA = PH0
I2C0_SCL = PH1

SPI1_MOSI = PH6
SPI1_MISO = PH7
SPI1_SCLK = PH8
SPI1_CS0 = PH5
SPI1_CS1 = PH9

UART0_TX = PH0
UART0_RX = PH1
UART2_TX = PI5
UART2_RX = PI6
UART3_TX = PI4
UART3_RX = PI5
UART4_TX = PH2
UART4_RX = PH3
UART5_TX = PH2
UART5_RX = PH3

PWM1 = PI12
PWM2 = PI13
PWM3 = PH2
PWM4 = PH3

# Define port mappings
i2cPorts = (
    (0, I2C0_SCL, I2C0_SDA),
    (1, I2C1_SCL, I2C1_SDA),
)
# ordered as spiId, sckId, mosiId, misoId
spiPorts = (
    (1, SPI1_SCLK, SPI1_MOSI, SPI1_MISO),
)
# ordered as uartId, txId, rxId
uartPorts = (
    (0, UART0_TX, UART0_RX),
    (2, UART2_TX, UART2_RX),
    (3, UART3_TX, UART3_RX),
    (4, UART4_TX, UART4_RX),
    (5, UART5_TX, UART5_RX),
)
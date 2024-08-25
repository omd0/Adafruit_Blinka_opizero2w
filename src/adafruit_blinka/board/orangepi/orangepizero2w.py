# SPDX-FileCopyrightText: 2024 Emad-Fussi for Adafruit Industries
# This code was written with assistance from Claude, an AI assistant created by Anthropic, PBC
# SPDX-License-Identifier: MIT
"""Pin definitions for the Orange Pi Zero 2W."""

from adafruit_blinka.microcontroller.allwinner.h618 import pin

PH0 = pin.PH0
UART0_TX = pin.PH0
I2C0_SDA = pin.PH0

PH1 = pin.PH1
UART0_RX = pin.PH1
I2C0_SCL = pin.PH1

PH2 = pin.PH2
UART5_TX = pin.PH2
PWM3 = pin.PH2

PH3 = pin.PH3
UART5_RX = pin.PH3
PWM4 = pin.PH3

PH4 = pin.PH4
PH5 = pin.PH5
SPI1_CS0 = pin.PH5

PH6 = pin.PH6
SPI1_CLK = pin.PH6
SPI1_SCLK = pin.PH6

PH7 = pin.PH7
SPI1_MOSI = pin.PH7

PH8 = pin.PH8
SPI1_MISO = pin.PH8

PH9 = pin.PH9
SPI1_CS1 = pin.PH9

PI0 = pin.PI0
PI1 = pin.PI1
PI2 = pin.PI2
PI3 = pin.PI3

PI4 = pin.PI4
UART3_TX = pin.PI4

PI5 = pin.PI5
UART2_TX = pin.PI5
I2C1_SCL = pin.PI5

PI6 = pin.PI6
UART2_RX = pin.PI6
I2C1_SDA = pin.PI6

PI12 = pin.PI12
PWM1 = pin.PI12

PI13 = pin.PI13
PWM2 = pin.PI13

PI16 = pin.PI16

# SPI
SCLK = pin.PH6
MOSI = pin.PH7
MISO = pin.PH8

# I2C
SDA = pin.PI6
SCL = pin.PI5
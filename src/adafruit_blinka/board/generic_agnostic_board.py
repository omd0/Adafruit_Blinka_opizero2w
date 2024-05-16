# SPDX-FileCopyrightText: 2024 Brent Rubell for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""Pin definitions for a generic, os-agnostic, board."""
from adafruit_blinka.microcontroller.generic_agnostic_board import pin

# Digital pins
Dx_INPUT_TRUE = pin.D0
Dx_INPUT_FALSE = pin.D1
Dx_INPUT_TRUE_PULL_UP = pin.D2
Dx_INPUT_TRUE_PULL_DOWN = pin.D3
Dx_OUTPUT_TRUE = pin.D4
Dx_OUTPUT_FALSE = pin.D5

# Analog pins
Ax_INPUT_RAND_INT = pin.A0
Ax_INPUT_FIXED_INT = pin.A1
Ax_OUTPUT_WAVE_SINE = pin.A2
Ax_OUTPUT_WAVE_SAWTOOTH = pin.A3

# I2C pins
SDA = pin.SDA
SCL = pin.SCL

# SPI pins
SCLK = pin.SCLK
SCK = pin.SCK
MOSI = pin.MOSI
MISO = pin.MISO
CS = pin.D6

# UART pins
UART_TX = pin.UART_TX
UART_RX = pin.UART_RX

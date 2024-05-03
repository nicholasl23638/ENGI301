"""
--------------------------------------------------------------------------
Drive
--------------------------------------------------------------------------
License:   
Copyright 2021-2024 - Nicholas Leibert

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, this 
list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE 
DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE 
FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL 
DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR 
SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER 
CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, 
OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE 
OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Drive
  Responsible for controlling left & right drive motors, monitoring limit switch to detect wall collisions.

Software API:

    send_to_motor()
        - converts left & right desired power into signals sent to motor GPIO pins
        
    update()
        - called periodically in timer.py
        - determines what direction the roomba is supposed to drive

    stop()
        - stop motors

"""
import button
import RPi.GPIO as gpio
import time

limit_sw_id = 'P2_3'
left_motor_in1 = 'P2_1'
left_motor_in2 = 'P2_19'

right_motor_in1 = 'P2_18'
right_motor_in2 = 'P1_36'

limit_sw = button.Button(limit_sw_id)

gpio.setup(left_motor_in1, gpio.OUT)
gpio.setup(left_motor_in2, gpio.OUT)
gpio.setup(right_motor_in1, gpio.OUT)
gpio.setup(right_motor_in2, gpio.OUT)

gpio.output(left_motor_in1, gpio.LOW)
gpio.output(left_motor_in2, gpio.LOW)
gpio.output(right_motor_in1, gpio.LOW)
gpio.output(right_motor_in2, gpio.LOW)


def send_to_motor(left_pwr, right_pwr):
    if left_pwr < 0:
        gpio.output(left_motor_in1, gpio.LOW)
        gpio.output(left_motor_in2, gpio.HIGH)
    elif left_pwr > 0: 
        gpio.output(left_motor_in1, gpio.HIGH)
        gpio.output(left_motor_in2, gpio.LOW)
    else:
        gpio.output(left_motor_in1, gpio.LOW)
        gpio.output(left_motor_in2, gpio.LOW)

    if right_pwr < 0:
        gpio.output(right_motor_in1, gpio.LOW)
        gpio.output(right_motor_in2, gpio.HIGH)
    elif right_pwr > 0: 
        gpio.output(right_motor_in1, gpio.HIGH)
        gpio.output(right_motor_in2, gpio.LOW)
    else:
        gpio.output(right_motor_in1, gpio.LOW)
        gpio.output(right_motor_in2, gpio.LOW)


def update():
    hit_wall = limit_sw.is_pressed()

    if hit_wall:
        # back up, then turn, then continue driving forwards
        send_to_motor(-0.5, -0.5)
        time.sleep(3)
        send_to_motor(0.5, -0.5)
        time.sleep(1)
    else:
        send_to_motor(0.5, 0.5)

def stop():
    send_to_motor(0, 0)

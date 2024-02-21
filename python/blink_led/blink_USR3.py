# -*- coding: utf-8 -*-
"""
--------------------------------------------------------------------------
Blink USR3 led
--------------------------------------------------------------------------
License:   
Copyright 2024 - <NAME>

Redistribution and use in source and binary forms, with or without 
modification, are permitted provided that the following conditions are met:

1. Redistributions of source code must retain the above copyright notice, 
this list of conditions and the following disclaimer.

2. Redistributions in binary form must reproduce the above copyright notice, 
this list of conditions and the following disclaimer in the documentation 
and/or other materials provided with the distribution.

3. Neither the name of the copyright holder nor the names of its contributors 
may be used to endorse or promote products derived from this software without 
specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" 
AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE 
IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE 
ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE 
LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR 
CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF 
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS 
INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN 
CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) 
ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF 
THE POSSIBILITY OF SUCH DAMAGE.
--------------------------------------------------------------------------

Simple script that will:
Use the Adafruit BBIO library to blink the USR3 LED at 5 Hz

--------------------------------------------------------------------------
"""
import Adafruit_BBIO.GPIO as GPIO
import time

if __name__ == "__main__":
    
    # 1/10 of a second -- two loops
    sleep_time = 0.1
    # led state toggle
    is_high = False
    # set up led GPIO
    GPIO.setup("USR%d" % 3, GPIO.OUT)

    while True:
        # toggle logic
        if(is_high):
            GPIO.output("USR%d" % 3, GPIO.LOW)
        else:
            GPIO.output("USR%d" % 3, GPIO.HIGH)
        
        is_high = not is_high
        time.sleep(sleep_time)
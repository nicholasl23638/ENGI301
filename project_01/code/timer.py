"""
--------------------------------------------------------------------------
Timer
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

Timer
  Runs on bootup, manages setting & updating run time, updates drive.py

Software API:

    main()
        - initializes UI allowing user to select their desired run time in minutes
        - upon user selection, runs roomba drive for selected run time

"""

import ht16k33 as hex_display
import button
import drive
import time

# Pins
inc_button_id = 'P2_2'
# P2_9 – SCL, P2_11 – SDA
hex_bus = "i2c_1"

inc_button = button.Button(inc_button_id)
hex_timer = hex_display.HT16K33(hex_bus)

hex_display_time = 30
start_time = -1 # seconds
run_time = 1800 # seconds

def main():
    # set time w/ inc button
    last_not_press_time = time.time()
    last_button = False
    while(time.time() - last_not_press_time < 2): # if button pressed for 2 seconds exit loop
        hex_timer.update(hex_display_time)

        if not inc_button:
            last_not_press_time = time.time()
        
        if inc_button != last_button and not inc_button: # if button released, increment time by 5 mins
            if (hex_display_time == 60):
                hex_display_time = 0
                run_time = 0
            
            hex_display_time += 5
            run_time += 5 * 60
        
        last_button = inc_button


    # run timer for run_time seconds
    start_time = time.time()

    while(time.time() - start_time < run_time):
        hex_timer.update(int(run_time - (time.time() - start_time)))

        start_time = time.time()
        drive.update()
    
    drive.stop()

if __name__ == "__main__":
    main()
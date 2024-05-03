<h1>Homemade Roomba</h1>

<h2>Running on robot bootup</h2>

1. Add the file /etc/rc.local and make it executable

touch /etc/rc.local
chmod a+x /etc/rc.local

2. Add code to run your code to /etc/rc.local

#!/bin/bash

cd /home/ENGI301/project_01/code
bash -c 'python3 timer.py' &

exit 0

<h2>Dependencies</h2>
RPi.GPIO (pip install RPi.GPIO)
time
contents of 'python' folder

<h2>Pins & Communication Protocols</h2>
Digital IO:
- P2_2 –> UI Button
- P2_3 –> Limit switch
- P2_1 –> Left motor power
- P2_19 –> Left motor polarity
- P2_18 –> Right motor power
- P1_36 –> Right motor polarity

I2C:
- P2_9 –> Hex Display SCL
- P2_11 –> Hex Display SDA

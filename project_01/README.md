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

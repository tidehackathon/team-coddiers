# team-Coddiers

![alt text](/img/coddiers_logo.jpg)

* 2nd Lt. **Dominik DAWIDZIAK** / 🇵🇱 / Regional IT Center Bydgoszcz
* 2nd Lt. **Paweł ŻURAWSKI** / 🇵🇱 / Regional It Center Bydgoszcz
* 2nd Lt. **Patryk BARCZAK** / 🇵🇱 / Military University of Technology Warsaw
* 2nd Lt. **Norbert WASZKOWIAK** / 🇵🇱 / Military University of Technology Warsaw
---
# Installation
### Requirements:
- [Mission Planer](https://ardupilot.org/planner/docs/mission-planner-installation.html) / We suggest disabling Altitude Angel login during installation
- Virtual Machine with [ArduPilot](https://ardupilot.org/dev/docs/building-setup-linux.html?fbclid=IwAR03JKKK8-jABCSgNqTpenUjjdYro7u2j_tUFHjnqu7RoCnN3Oc8vvZVVgc#building-setup-linux) installed and the drone's starting location configured
- The following program code ;)
- Wi-Fi network to connect all the above components together. (We can run everything on one computer, the important thing is to have a connection to some network for ArduPilot to connect to it and then copy the IP address of the virtual machine on which we are running ArduPilot)

### List of steps
1. Fully run ArduPilot
2. Launch and set up the Mission Planner, but do not launch the mission
3. Run the operation of our code
4. Run the mission

## ArduPilot Component
### How to add a drone's starting location in ArduPilot:
1. Open the file:
   * _ardupilot/Tools/autotest/locations.txt_
2. At the end of the file we add:
    * ```ukr_2=48.5471376,35.1047295,296,249```

### How to run ArduPilot with the required location:
1. Open a terminal and type the following command:
    * ```sim_vehicle.py -v ArduPlane -L ukr_2 --console```
2. Open a second terminal and type:
   * ```ifconfig```
3. Copy the IP address (you will need it later)

## Mission Planer Component
1. Open Mission PLaner
2. Change connection type to TCP (Top right corner)
3. Press the "Connect" button:
   * Enter the previously copied ip address
   * Enter port: `5762`
4. Go to the "Plan" tab
   * click the `load WP file` button and select the `planned_S2.waypoints` file.
   * (accept the information from the box if it pops up).
   * click 'Save WP' button.
5. Go to the "Data" tab
   * if you see "DISARMED" in red on the panel then in the actions select "Arm/Disarm".

### In order to start / restart the mission
1. Press the "Mission restart" button
2. Press the "Auto" button
3. Change the speed to 14.0 and accept it with the "Change Speed" button
4. **!!! Make sure the speed has changed !!!**
5. **!!! Make sure the aircraft is in "Armed" mode !!!**

## Our program Component
If you are using an IDE, such as PyCharm:
1. In the main.py file on the line:
   * `vehicle = dronekit.connect('tcp:172.20.10.7:5763', baud=115200)` type the previously copied IP address of the ArduPilot
2. Run the main.py action

If you use the command line:
1. Edit the main.py file, on the line:
   * `vehicle = dronekit.connect('tcp:172.20.10.7:5763', baud=115200)` type the previously copied IP address of the ArduPilot
2. Run the main.py action with the command: `python main.py`

### To control the route graph window:
- Hold down the left mouse button and move it to **rotate** the image
- Hold the right mouse button and move it to **flip** the image
- Hold the mouse wheel and move it to **move** the image
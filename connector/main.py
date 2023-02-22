import dronekit

# git clone https://github.com/dronekit/dronekit-python <- to install dronekit fior pyhton3
# cd dronekit-python
# sudo python setup.py install
# pyenv shell 3.10.0     <- to chyba trzeba
# cd ..
# python main.py


def getDroneData():
    vehicle = dronekit.connect('tcp:51.145.133.68:5763', baud=115200)
    print("Vehicle's Latitude = ",
          vehicle.location.global_relative_frame.lat)
    print("Vehicle's Longitude = ",
          vehicle.location.global_relative_frame.lon)
    print("Vehicle's Altitude = ",
          vehicle.location.global_relative_frame.alt)
    print(" Global Location (relative altitude): %s" %
          vehicle.location.global_relative_frame)
    print(" GPS: %s" % vehicle.gps_0)
    print(" Heading: %s" % vehicle.heading)

    return

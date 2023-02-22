from videoReader import video_reader
import dronekit

drone_height = 0
compas_angle = 0
vehicle = dronekit.connect('tcp:51.145.133.68:5763', baud=115200)

video_reader(vehicle)

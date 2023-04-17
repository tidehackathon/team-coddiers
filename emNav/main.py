from videoReader import video_reader
import dronekit

drone_height = 0
compas_angle = 0
vehicle = dronekit.connect('tcp:172.20.10.7:5763', baud=115200)

video_reader(vehicle)

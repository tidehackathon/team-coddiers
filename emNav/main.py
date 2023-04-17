from videoReader import video_reader
import dronekit

drone_height = 0
compas_angle = 0
vehicle = dronekit.connect('tcp:10.8.235.136:5763', baud=115200)

video_reader(vehicle)

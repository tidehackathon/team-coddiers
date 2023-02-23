from videoReader import video_reader
import dronekit

drone_height = 0
compas_angle = 0
vehicle = dronekit.connect('tcp:51.145.133.68:5763', baud=115200)


# Tu poniżej jest sczytywanie czy znajdzie waypoint 3, jak znajdzie co potrzebuje to go przerwij i odpal film

def handle_message(self, name, message):
    print(message)
    if str(message).find('Reached waypoint #3'):
        print('Barczak rób ze mną co chcesz :) Najlepiej odpalaj filma"')
        return True


vehicle.add_message_listener('STATUSTEXT', handle_message)

while True:
    pass

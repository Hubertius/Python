from random import randint


class Rocket:
    def __init__(self, speed):
        self.altitude = 0
        self.speed = speed

    def moveUP(self):
        self.altitude += 1
        self.speed **= 2


rockets = []
for i in range(5):
    speed = randint(1, 10)
    rockets.append(Rocket(speed))
for i in range(5):
    random_value_of_altitude = randint(0, 4)
    rockets[random_value_of_altitude].moveUP()
rockets_altitude = [r.altitude for r in rockets]
rockets_speed = [r.speed for r in rockets]
print("Rockets altitude: ", rockets_altitude)
print("Rockets speed:\t  ", rockets_speed)
exit(0)

class Road:

    def __init__(self, length, width):
        self._length = length
        self._width = width

    def mass_asphalt(self, weight=25, thickness=5):
        return f'Масса асфальта: {(self._length * self._width * weight * thickness)}'


road = Road(20, 5000)
print(road.mass_asphalt())




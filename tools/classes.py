'''
/ this code contains the classes used in the algorithms
'''


class Battery:
    number = 0

    def __init__(self, pos_x, pos_y, capacity):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        Battery.number += 1

    def match_with_house(self, house):
        if house.output < self.capacity:
            return True
        else:
            return False


class Battery_type:
    number = 0

    def __init__(self, pos_x, pos_y, capacity, type):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.capacity = capacity
        self.type = type
        Battery.number += 1

    def match_with_house(self, house):
        if house.output < self.capacity:
            return True
        else:
            return False


class House:
    number = 0

    def __init__(self, pos_x, pos_y, output):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.output = output
        House.number += 1


class Cable:
    def __init__(self, pos_x, pos_y, battery_nr):
        self.pos_x = pos_x
        self.pos_y = pos_y
        self.battery_nr = battery_nr

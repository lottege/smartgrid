'''
 / Makes a cable between a house and a battery using Manhattan distance
 / Works following the order in the list of houses from the file
'''
from tools import helpers


def cable_list():
    connected = 0
    cable_list = []
    cl = []
    batteries = helpers.readtxt("tools/wijk1_batterijen.txt")
    houses = helpers.readcsv("tools/wijk1_huizen.csv")

    for i in range(len(houses)):
        for j in range(len(batteries)):
            if helpers.match_with_house(houses[i], batteries[j]) and houses[i].output > 0:
                cable = helpers.Cable(houses[i].pos_x, houses[i].pos_y, i)
                cable_list.append(cable)
                cl = helpers.connect_to_battery(i, j, cable_list, batteries, houses)
                connected += 1
                break

    return len(cl), houses, batteries, cl



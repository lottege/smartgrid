'''
 / Makes a cable between a house and a battery using Manhattan distance
 / Starting from the first house in the list, the house connects to its closest battery
'''
from tools import helpers


def cable_list_sneller():
    cable_list = []
    cl = []
    connected = 0

    batteries = helpers.readtxt("tools/wijk1_batterijen.txt")
    houses = helpers.readcsv("tools/wijk1_huizen.csv")

    distance = helpers.distance_sort(batteries, houses)

    for i in range(len(houses)):
        for key in distance[i]:
            if helpers.match_with_house(houses[i], batteries[key[0]]) and houses[i].output > 0:
                cable = helpers.Cable(houses[i].pos_x, houses[i].pos_y, i)
                cable_list.append(cable)
                cl = helpers.connect_to_battery(i, key[0], cable_list, batteries, houses)
                connected += 1
                break

    return len(cl), houses, batteries, cl


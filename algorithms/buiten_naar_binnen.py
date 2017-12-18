'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''
from tools import helpers


def buiten_naar_binnen():
    cable_list = []
    cl = []
    connected = 0

    batteries = helpers.readtxt("tools/wijk1_batterijen.txt")
    houses = helpers.readcsv("tools/wijk1_huizen.csv")

    distance = helpers.distance_sort(batteries, houses)
    sorted_houses = helpers.sort_houses(houses)

    for house in sorted_houses:
        for key in distance[house[0]]:
            if helpers.match_with_house(houses[house[0]], batteries[key[0]]) and houses[house[0]].output > 0:
                cable = helpers.Cable(houses[house[0]].pos_x, houses[house[0]].pos_y, key[0])
                cable_list.append(cable)
                cl = helpers.connect_to_battery(house[0], key[0], cable_list, batteries, houses)
                connected += 1
                break

    return len(cl), houses, batteries, cl

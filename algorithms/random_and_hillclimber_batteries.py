'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''

from random import randint
from tools import helpers


def random_and_hillclimber_batteries():
    print("amount of random restarts?")
    random_restarts = input()

    battery_locations = []
    winner = []

    batteries = helpers.readtxt("tools/wijk1_batterijen.txt")
    houses = helpers.readcsv("tools/wijk1_huizen.csv")

    previous = 20000

    for a in range(int(random_restarts)):
        helpers.reset_batteries(batteries)
        for bat in batteries:
            bat.pos_x = randint(0, 50)
            bat.pos_y = randint(0, 50)

        distance = helpers.distance_sort(batteries, houses)
        sorted_houses = helpers.sort_houses(houses)
        score, connected = helpers.connection_score(sorted_houses, distance, batteries, houses)

        if score < previous:
            helpers.reset_batteries(batteries)
            cl = helpers.connection(sorted_houses, distance, batteries, houses)
            previous = score
            battery_locations = []
            for bat in batteries:
                battery = helpers.Battery(bat.pos_x, bat.pos_y, bat.capacity)
                battery_locations.append(battery)
            winner = cl

    final_batteries = battery_locations
    print("amount of hillclimber moves?")
    moves = input()

    for b in range(int(moves)):
        for i in range(len(battery_locations)):
            battery_locations[i].pos_x = final_batteries[i].pos_x
            battery_locations[i].pos_y = final_batteries[i].pos_y
        helpers.reset_batteries(battery_locations)
        helpers.swap(battery_locations[randint(0, 4)], battery_locations)

        distance = helpers.distance_sort(battery_locations, houses)
        sorted_houses = helpers.sort_houses(houses)
        score, connected = helpers.connection_score(sorted_houses, distance, battery_locations, houses)

        if score < previous:
            previous = score
            helpers.reset_batteries(battery_locations)
            hill = helpers.connection(sorted_houses, distance, battery_locations, houses)
            final_batteries = []
            for bat in battery_locations:
                battery = helpers.Battery(bat.pos_x, bat.pos_y, bat.capacity)
                final_batteries.append(battery)
            winner = hill

    return len(winner), houses, final_batteries, winner





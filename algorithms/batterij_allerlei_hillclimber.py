'''
 / connects houses to the closest battery if it has enough capacity, starting with the furthest houses from the centre
'''

from random import randint
from tools import helpers


def batterij_allerlei_hillclimber():
    print("amount of random restarts?")
    random_restarts = input()
    houses = helpers.readcsv("tools/wijk1_huizen.csv")
    winner = []
    batteries = []
    final_batteries = []
    battery_locations = []

    capacities = [450, 900, 1800]
    connected = 0
    price = 0

    previous = 100000
    score = 8000
    for a in range(int(random_restarts)):
        batteries = []
        while connected < 149:
            battery_type = randint(0, 2)
            bat = helpers.Battery_type(randint(0, 50), randint(0, 50), capacities[battery_type], battery_type)
            batteries.append(bat)
            price = helpers.price_calc(batteries, score)
            distance = helpers.distance_sort(batteries, houses)
            sorted_houses = helpers.sort_houses(houses)
            score, connected = helpers.connection_score(sorted_houses, distance, batteries, houses)

            helpers.reset_batteries_type(batteries)

        if price < previous:
            cl = helpers.connection(sorted_houses, distance, batteries, houses)
            previous = price
            battery_locations = []
            for bat in batteries:
                battery = helpers.Battery_type(bat.pos_x, bat.pos_y, bat.capacity, bat.type)
                battery_locations.append(battery)
            winner = cl

    print("amount of hillclimber moves?")
    moves = input()

    for b in range(int(moves)):
        amount_batts = len(battery_locations) - 1
        helpers.swap(battery_locations[randint(0, amount_batts)], battery_locations)
        helpers.reset_batteries_type(battery_locations)

        distance = helpers.distance_sort(battery_locations, houses)
        sorted_houses = helpers.sort_houses(houses)
        score, connected = helpers.connection_score(sorted_houses, distance, battery_locations, houses)
        price = helpers.price_calc(battery_locations, score)

        if price < previous:
            helpers.reset_batteries_type(battery_locations)
            previous = price
            hill = helpers.connection(sorted_houses, distance, battery_locations, houses)

            final_batteries = []
            for bat in battery_locations:
                battery = helpers.Battery_type(bat.pos_x, bat.pos_y, bat.capacity, bat.type)
                final_batteries.append(battery)
            winner = hill

    return len(winner), houses, final_batteries, winner







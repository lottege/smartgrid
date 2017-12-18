'''
/ this code contains the functions used in the algorithms
'''

import csv
import operator
from tools import classes
from random import randint

Cable = classes.Cable
House = classes.House
Battery = classes.Battery
Battery_type = classes.Battery_type


# reads txt files and makes battery objects from the input
def readtxt(txtfile):
    with open(txtfile, newline='') as batterijen1:
        readCSV = csv.reader(batterijen1, delimiter=']')
        next(readCSV, None)

        battery_list = []
        for row in readCSV:
            parts = row[0].split(',')
            battery = Battery(int(parts[0].strip()[1:]), int(parts[1].strip()), float(row[1].strip()))
            battery_list.append(battery)

        return battery_list


# reads csv files and makes house objects from the input
def readcsv(csvfile):
    with open(csvfile) as wijk1:
        readCSV = csv.reader(wijk1, delimiter=',')
        next(readCSV)

        house_list = []
        for row in readCSV:
            house = House(int(row[0]), int(row[1]), float(row[2]))
            house_list.append(house)

        return house_list


# check if the battery capacity still fits the house
def match_with_house(house, battery):
    if house.output < battery.capacity:
        return True
    else:
        return False


# connection is made between house and battery
def connect_to_battery(house, battery, cable_list, batteries, houses):
    # cable loops through x
    connected = 0
    while cable_list[-1].pos_x != batteries[battery].pos_x:
        if cable_list[-1].pos_x < batteries[battery].pos_x:
            cable = Cable(cable_list[-1].pos_x + 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_x > batteries[battery].pos_x:
            cable = Cable(cable_list[-1].pos_x - 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

    # cable loops through y
    while cable_list[-1].pos_y != batteries[battery].pos_y:
        if cable_list[-1].pos_y < batteries[battery].pos_y:
            cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y + 1, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_y > batteries[battery].pos_y:
            cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y - 1, battery)
            cable_list.append(cable)

    if cable_list[-1].pos_y == batteries[battery].pos_y and cable_list[-1].pos_x == batteries[battery].pos_x:
        connected += 1
        batteries[battery].capacity -= houses[house].output

    houses[house].battery = battery
    return cable_list


# the houses are being sorted on their distance to the batteries
def distance_sort(batteries, houses):
    distances = []
    for j in range(len(houses)):
        distance = {}
        for i in range(len(batteries)):
            dis = (abs(houses[j].pos_x - batteries[i].pos_x) + abs(houses[j].pos_y - batteries[i].pos_y))
            distance[i] = dis
        sorted_distance = sorted(distance.items(), key=operator.itemgetter(1))
        distances.append(sorted_distance)

    return distances


# the houses are being sorted on their distance to the centre
def sort_houses(houses):
    distance = {}
    for i in range(len(houses)):
        dis = (abs(houses[i].pos_x - 25) + abs(houses[i].pos_y - 25))
        distance[i] = dis

    sorted_distance = sorted(distance.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_distance


# the houses are being sorted (reversed) on their distance to batteries
def sort_on_battery_distance(batteries, houses):
    distances = []
    for j in range(len(houses)):
        distance = []
        for i in range(len(batteries)):
            dis = (abs(houses[j].pos_x - batteries[i].pos_x) + abs(houses[j].pos_y - batteries[i].pos_y))
            triple = [dis, i, j]
            distance.append(triple)
        sorted_distance = sorted(distance, key=operator.itemgetter(0))
        distances.append(sorted_distance)

    end_sort = sorted(distances, key=lambda x: x[0][0], reverse=True)
    return end_sort


# all houses will be connected to the battery from the list
def connection(sorted_houses, distance, batteries, houses):
    cable_list = []
    cl = []
    connected = 0
    for house in sorted_houses:
        for key in distance[house[0]]:
            if match_with_house(houses[house[0]], batteries[key[0]]) and houses[house[0]].output > 0:
                cable = Cable(houses[house[0]].pos_x, houses[house[0]].pos_y, key[0])
                cable_list.append(cable)
                cl = connect_to_battery(house[0], key[0], cable_list, batteries, houses)
                connected += 1
                break
    return cl


# the score of the connection will be calculated without actually making the connections
def connection_score(sorted_houses, distance, batteries, houses):
    score = 150
    connected = 0
    for house in sorted_houses:
        for key in distance[house[0]]:
            if match_with_house(houses[house[0]], batteries[key[0]]) and houses[house[0]].output > 0:
                score += update_score(houses[house[0]], batteries[key[0]])
                houses[house[0]].battery = key[0]
                connected += 1
                break
    return score, connected


# sets the capacity of the batteries back to it's starting value
def reset_batteries(batteries):
    for bat in batteries:
        bat.capacity = 1507.0


# the battery moves 1 random step per swap
def swap(battery, batteries):
    amount = 1
    direction = randint(1, len(batteries)-1)
    if direction == 1:
        battery.pos_x += amount
    elif direction == 2:
        battery.pos_x -= amount
    elif direction == 3:
        battery.pos_y += amount
    elif direction == 4:
        battery.pos_y -= amount


# calculates the score
def update_score(house, battery):
    x = abs(house.pos_x - battery.pos_x) + abs(house.pos_y - battery.pos_y)
    battery.capacity -= house.output
    return x


# batteries of different types get their starting capacity
def reset_batteries_type(batteries):
    for bat in batteries:
        if bat.type == 0:
            bat.capacity = 450
        elif bat.type == 1:
            bat.capacity = 900
        else:
            bat.capacity = 1800


# price of the batteries will be calculated
def price_calc(final_batteries, score):
    price = 0
    for bat in final_batteries:
        if bat.type == 0:
            price += 900
        elif bat.type == 1:
            price += 1350
        else:
            price += 1800
    price += score

    return price


# makes a connection to a known battery
def connection_end(batteries, houses):
    cable_list = []
    cl = []
    connected = 0
    for house in houses:
        cable = Cable(house.pos_x, house.pos_y, house.battery)
        cable_list.append(cable)
        cl = connect_to_battery_end(house, house.battery, cable_list, batteries, houses)
        connected += 1
    return cl


# calculats the score of the connections to a known battery
def connection_score_end(batteries, houses):
    score = 150
    connected = 0
    for house in houses:
        score += update_score(house, batteries[house.battery])
        connected += 1
    return score


# checks if batteries have enough capacity for the switch
def check_switch(house, second_house, battery, second_battery):
    if (battery.capacity + house.output - second_house.output) > 0 and (second_battery.capacity + second_house.output - house.output) > 0:
        # checks if total number of cables goes down if switched
        current_score_house_1 = check_score(house, battery)
        current_score_house_2 = check_score(second_house, second_battery)
        new_score_house_1 = check_score(house, second_battery)
        new_score_house_2 = check_score(second_house, battery)
        if current_score_house_1 + current_score_house_2 > new_score_house_1 + new_score_house_2:
            return True

    return False


# switches two houses to new batteries
def switch_score(house, second_house, battery, second_battery, score):
    refill_capacity(house, battery)
    refill_capacity(second_house, second_battery)
    score -= (abs(update_score(house, battery)) + abs(update_score(second_house, second_battery)))
    drain_capacity(house, second_battery)
    drain_capacity(second_house, battery)
    score += abs(update_score(house, second_battery)) + abs(update_score(second_house, battery))
    house.battery = second_battery.number
    second_house.battery = battery.number

    return score


# connects to battery
def connect_to_battery_end(house, battery, cable_list, batteries, houses):
    # cable loops through x
    while cable_list[-1].pos_x != batteries[battery].pos_x:
        if cable_list[-1].pos_x < batteries[battery].pos_x:
            cable = Cable(cable_list[-1].pos_x + 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_x > batteries[battery].pos_x:
            cable = Cable(cable_list[-1].pos_x - 1, cable_list[-1].pos_y, battery)
            cable_list.append(cable)

    # cable loops through y
    while cable_list[-1].pos_y != batteries[battery].pos_y:
        if cable_list[-1].pos_y < batteries[battery].pos_y:
            cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y + 1, battery)
            cable_list.append(cable)

        elif cable_list[-1].pos_y > batteries[battery].pos_y:
            cable = Cable(cable_list[-1].pos_x, cable_list[-1].pos_y - 1, battery)
            cable_list.append(cable)

    if cable_list[-1].pos_y == batteries[battery].pos_y and cable_list[-1].pos_x == batteries[battery].pos_x:
        batteries[battery].capacity -= house.output

    house.battery = battery
    return cable_list


def check_score(house, battery):
    return abs(house.pos_x - battery.pos_x) + abs(house.pos_y - battery.pos_y)


def drain_capacity(house, battery):
    if battery.capacity - house.output > 0:
        battery.capacity -= house.output
        return True
    else:
        return False


def refill_capacity(house, battery):
    battery.capacity += house.output

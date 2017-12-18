'''
/ Makes a cable between a house and a battery in 2 ways:
 / 1: making new cables all alongside each other
 / 2: connecting cables all together
 / plot met mat plot lib
'''

import classes
import helpers
import random


cable_list = []
new_cable_list = []
connected = 0
tries = 5000
i = 0
q = 0
score = 150

old_cost = 6000 * 9
new_cost = old_cost

batteries = helpers.readtxt("wijk1_batterijen.txt")
houses = helpers.readcsv("wijk1_huizen.csv")

# Option 1: places cables alongside others (longer dict, no dict checks)
for battery in range(len(batteries)):
    batteries[battery].number = battery
    for house in range(len(houses)):
        if helpers.match_with_house(houses[house], batteries[battery]) and houses[house].output > 0:
            helpers.drain_capacity(houses[house], batteries[battery])
            houses[house].output -= houses[house].output
            score += helpers.update_score(houses[house], batteries[battery])
            connected += 1

print(score)

for z in range(tries):
    l = 50
    q += 1


    houses2 = helpers.readcsv("wijk1_huizen.csv")
    for house in range(len(houses2)):
        houses[house].output = houses2[house].output

    for k in range(l):
        a = random.choice(houses)
        b = random.choice(houses)

        while batteries[a.battery] is batteries[b.battery]:
            a = random.choice(houses)
            b = random.choice(houses)

        for m in range(20):
            if helpers.check_switch(a, b, batteries[a.battery], batteries[b.battery]):
                score = helpers.switch_score(a, b, batteries[a.battery], batteries[b.battery], score)               
                i += 1

        if new_cost < old_cost:
            i += 1
            connected_new = connected
            old_cost = new_cost
            new_cable_list = cable_list
       
for battery in range(len(batteries)):
    print(batteries[battery].capacity)
for house in range(len(houses)):
    cable = classes.Cable(houses[house].pos_x, houses[house].pos_y, battery)
    cable_list.append(cable)
    helpers.connect_to_battery(houses[house], batteries[houses[house].battery], cable_list)
    connected += 1

return len(cable_list), houses, batteries, cable_list

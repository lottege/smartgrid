from tools import helpers


def brute_force_batterijen():
    batteries = helpers.readtxt("tools/wijk1_batterijen.txt")
    houses = helpers.readcsv("tools/wijk1_huizen.csv")
    winner = []
    previous = 10000

    for i0 in range(50):
        for j0 in range(50):
            helpers.reset_batteries(batteries)
            batteries[0].pos_x = i0
            batteries[0].pos_y = j0

            distance = helpers.distance_sort(batteries, houses)
            sorted_houses = helpers.sort_houses(houses)
            score, connected = helpers.connection_score(sorted_houses, distance, batteries, houses)

            if score < previous:
                previous = score
                helpers.reset_batteries(batteries)
                cl = helpers.connection(sorted_houses, distance, batteries, houses)
                battery_locations = []
                for baty in batteries:
                    battery = helpers.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                    battery_locations.append(battery)
                winner = cl

            for i1 in range(50):
                for j1 in range(50):
                    helpers.reset_batteries(batteries)
                    batteries[1].pos_x = i1
                    batteries[1].pos_y = j1

                    distance = helpers.distance_sort(batteries, houses)
                    sorted_houses = helpers.sort_houses(houses)
                    score, connected = helpers.connection_score(sorted_houses, distance, batteries, houses)

                    if score < previous:
                        previous = score
                        helpers.reset_batteries(batteries)
                        cl = helpers.connection(sorted_houses, distance, batteries, houses)
                        battery_locations = []
                        for baty in batteries:
                            battery = helpers.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                            battery_locations.append(battery)
                        winner = cl

                for i2 in range(50):
                    for j2 in range(50):
                        helpers.reset_batteries(batteries)
                        batteries[2].pos_x = i2
                        batteries[2].pos_y = j2

                        distance = helpers.distance_sort(batteries, houses)
                        sorted_houses = helpers.sort_houses(houses)
                        score, connected = helpers.connection_score(sorted_houses, distance, batteries, houses)

                        if score < previous:
                            previous = score
                            helpers.reset_batteries(batteries)
                            cl = helpers.connection(sorted_houses, distance, batteries, houses)
                            battery_locations = []
                            for baty in batteries:
                                battery = helpers.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                                battery_locations.append(battery)
                            winner = cl

                    for i3 in range(50):
                        for j3 in range(50):
                            helpers.reset_batteries(batteries)
                            batteries[3].pos_x = i3
                            batteries[3].pos_y = j3

                            distance = helpers.distance_sort(batteries, houses)
                            sorted_houses = helpers.sort_houses(houses)
                            score, connected = helpers.connection_score(sorted_houses, distance, batteries, houses)

                            if score < previous:
                                previous = score
                                helpers.reset_batteries(batteries)
                                cl = helpers.connection(sorted_houses, distance, batteries, houses)
                                battery_locations = []
                                for baty in batteries:
                                    battery = helpers.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                                    battery_locations.append(battery)
                                winner = cl

                        for i4 in range(50):
                            for j4 in range(50):
                                helpers.reset_batteries(batteries)
                                batteries[4].pos_x = i4
                                batteries[4].pos_y = j4

                                distance = helpers.distance_sort(batteries, houses)
                                sorted_houses = helpers.sort_houses(houses)
                                score, connected = helpers.connection_score(sorted_houses, distance, batteries, houses)

                                if score < previous:
                                    previous = score
                                    helpers.reset_batteries(batteries)
                                    cl = helpers.connection(sorted_houses, distance, batteries, houses)
                                    battery_locations = []
                                    for baty in batteries:
                                        battery = helpers.Battery(baty.pos_x, baty.pos_y, baty.capacity)
                                        battery_locations.append(battery)
                                    winner = cl

    return len(winner), houses, battery_locations, winner

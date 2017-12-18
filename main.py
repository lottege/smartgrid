from algorithms import random_and_hillclimber_batteries, cable_list, cable_list_sneller, verre_huizen_eerst, \
    buiten_naar_binnen, brute_force_batterijen, batterij_allerlei_hillclimber

# import visualisatie as vis


print("how would you like to place the batteries? "
      "\nto use: "
      "\n - cable_list press 0"
      "\n - cable_list_sneller press 1 "
      "\n - verre_huizen_eerst press 2"
      "\n - buiten_naar_binnen press 3"
      "\n - random_and_hillclimber_batteries press 4"
      "\n - brute_force_batterijen press 5"
      "\n - batterij_allerlei_hillclimber press 6")
algorithm = input()
print("thanks")

if algorithm == "0":
    segments, vis_houses, vis_batteries, vis_cables = cable_list.cable_list()

elif algorithm == "1":
    segments, vis_houses, vis_batteries, vis_cables = cable_list_sneller.cable_list_sneller()

elif algorithm == "2":
    segments, vis_houses, vis_batteries, vis_cables = verre_huizen_eerst.verre_huizen_eerst()

elif algorithm == "3":
    segments, vis_houses, vis_batteries, vis_cables = buiten_naar_binnen.buiten_naar_binnen()

elif algorithm == "4":
    segments, vis_houses, vis_batteries, vis_cables = random_and_hillclimber_batteries.random_and_hillclimber_batteries()

elif algorithm == "5":
    segments, vis_houses, vis_batteries, vis_cables = brute_force_batterijen.brute_force_batterijen()

elif algorithm == "6":
    segments, vis_houses, vis_batteries, vis_cables = batterij_allerlei_hillclimber.batterij_allerlei_hillclimber()

print("amount of needed cable segments: ", segments)
# vis.visualisation(vis_houses, vis_batteries, vis_cables)

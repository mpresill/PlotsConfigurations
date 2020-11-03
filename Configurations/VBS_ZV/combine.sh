#! /bin/bash
cut=Resolved_SR
variable=DNNoutput


#combine -M Significance /afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_03Nov2020/${cut}/${variable}/datacard.txt  -t -1 --expectSignal=1

#combine cards
#combineCards.py  boosted_sr=/afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_03Nov2020/Boosted_SR/${variable}/datacard.txt resolved_sr=/afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_03Nov2020/Resolved_SR/${variable}/datacard.txt > /afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_03Nov2020/combined_card.txt


combine -M Significance /afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_03Nov2020/combined_card.txt -t -1 --expectSignal=1

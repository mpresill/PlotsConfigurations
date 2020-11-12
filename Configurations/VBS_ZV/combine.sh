#! /bin/bash
cut=Boosted_SR
variable=DNNoutput
Date=11Nov2020

#combine -M Significance /afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_11Nov2020/${cut}/${variable}/datacard.txt  -t -1 --expectSignal=1

#combine cards
#combineCards.py  boosted_sr=/afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_${Date}/Boosted_SR/${variable}/datacard.txt resolved_sr=/afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_${Date}/Resolved_SR/${variable}/datacard.txt > /afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_${Date}/combined_card_SR.txt


combine -M Significance /afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_${Date}/combined_card_SR.txt -t -1 --expectSignal=1

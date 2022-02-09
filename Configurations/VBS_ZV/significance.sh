#! /bin/bash
cut=Boosted_SR
variable=DNNoutput_All_years
Date=21Feb2021_2018SR_Allyears
version=2018_SR

#combine -M Significance /afs/cern.ch/user/a/ahakimi/ZV_analysis/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/2018_v7/Datacards_${Date}/${cut}/${variable}/datacard.txt  -t -1 --expectSignal=1

#combine cards
#only SR
#combineCards.py  boosted_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_SR/${variable}/datacard.txt resolved_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_SR/${variable}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_SR.txt

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_SR.txt -t -1 --expectSignal=1

#SR + CR both cats
#combineCards.py  boosted_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_SR/${variable}/datacard.txt resolved_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_SR/${variable}/datacard.txt resolved_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_DYcr/${variable}/datacard.txt resolved_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${variable}/datacard.txt boosted_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_DYcr/${variable}/datacard.txt boosted_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${variable}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all.txt

# Boosted SR +CR 
#combineCards.py  boosted_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_SR/${variable}/datacard.txt boosted_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_DYcr/${variable}/datacard.txt boosted_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${variable}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_boosted.txt

#combineCards.py resolved_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_SR/${variable}/datacard.txt resolved_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_DYcr/${variable}/datacard.txt resolved_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${variable}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved.txt

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all.txt -t -1 --expectSignal=1

combine -M Significance /afs/cern.ch/work/m/mpresill/public/Alex/Datacards2016/combined_card_boosted.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved.txt -t -1 --expectSignal=1
#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_SR.txt -t -1 --expectSignal=1

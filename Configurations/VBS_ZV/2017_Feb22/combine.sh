#! /bin/bash
CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted
SR_var=DNNoutput_pruned_bReq_morebins #try other binnings
cutDY=DYcr_bTag
cutSR=SR_bTag
Date=01Mar2022_2017
version=2017_Feb22

#Boosted SR +CR 

combineCards.py  boosted_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR}/${SR_var}/datacard.txt boosted_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY}/${CR_var_boost}/datacard.txt  > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_boosted_${SR_var}.txt
#boosted_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR_var}/datacard.txt

combineCards.py resolved_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR}/${SR_var}/datacard.txt resolved_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY}/${CR_var_res}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_${SR_var}.txt
#boosted_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR_var}/datacard.txt
combineCards.py boosted_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR}/${SR_var}/datacard.txt boosted_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY}/${CR_var_boost}/datacard.txt resolved_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR}/${SR_var}/datacard.txt resolved_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY}/${CR_var_res}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all_${SR_var}.txt

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all.txt -t -1 --expectSignal=1

combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_boosted_${SR_var}.txt -t -1 --expectSignal=1

combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_${SR_var}.txt -t -1 --expectSignal=1

combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all_${SR_var}.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_SR.txt -t -1 --expectSignal=1

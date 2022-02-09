#! /bin/bash
CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted
SR_var=DNNoutput_full_morebins #try other binnings
Date=24Nov2021_2018
version=doublebin

#Boosted SR +CR 

#combineCards.py  boosted_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_SR_bVeto/${SR_var}/datacard.txt boosted_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_DYcr_bVeto/${CR_var_boost}/datacard.txt boosted_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR_var}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_boosted_${SR_var}.txt

combineCards.py resolved_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_SR_bVeto/${SR_var}/datacard.txt resolved_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_DYcr_bVeto/${CR_var_res}/datacard.txt resolved_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR_var}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_${SR_var}.txt


text2workspace.py /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_${SR_var}.txt --channel-masks


combine /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_${SR_var}.root -M FitDiagnostics --saveShapes --saveWithUncertainties --setParameters mask_resolved_sr=1

#combineCards.py boosted_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_SR_bVeto/${SR_var}/datacard.txt boosted_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_DYcr_bVeto/${CR_var_boost}/datacard.txt boosted_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR_var}/datacard.txt resolved_sr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_SR_bVeto/${SR_var}/datacard.txt resolved_DYcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_DYcr_bVeto/${CR_var_res}/datacard.txt resolved_topcr=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR_var}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all_${SR_var}.txt

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_boosted_${SR_var}.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_${SR_var}.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all_${SR_var}.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_SR.txt -t -1 --expectSignal=1

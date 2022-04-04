#! /bin/bash
CR_var_res=DYfit_Z_bin
CR_var_boost=DYfit_Z_bin
SR1_var=DNNoutput_pruned_bVeto #try other binnings
SR2_var=DNNoutput_pruned_bReq
cutDY1=DYcr_bVeto
cutSR1=SR_bVeto
cutDY2=DYcr_bTag
cutSR2=SR_bTag
Date=24Mar2022_2016
version=2016_Feb22

#Boosted SR +CR 

combineCards.py  boosted_sr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR1}/${SR1_var}/datacard.txt boosted_DYcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt boosted_topcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR1_var}/datacard.txt boosted_sr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR2}/${SR2_var}/datacard.txt boosted_DYcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt boosted_topcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR2_var}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_boosted_comb.txt

combineCards.py resolved_sr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR1}/${SR1_var}/datacard.txt resolved_DYcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt resolved_topcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR1_var}/datacard.txt resolved_DYcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  resolved_sr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_comb.txt
#resolved_topcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR2_var}/datacard.txt> /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_comb.txt

combineCards.py boosted_sr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR1}/${SR1_var}/datacard.txt boosted_DYcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt boosted_topcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR1_var}/datacard.txt boosted_sr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR2}/${SR2_var}/datacard.txt boosted_DYcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt boosted_topcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR2_var}/datacard.txt resolved_sr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR1}/${SR1_var}/datacard.txt resolved_DYcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt resolved_topcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR1_var}/datacard.txt resolved_sr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR2}/${SR2_var}/datacard.txt resolved_DYcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt resolved_topcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR2_var}/datacard.txt> /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all_comb.txt

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_boosted_comb.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_resolved_comb.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all_comb.txt -t -1 --expectSignal=1

#combine -M Significance /afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_SR.txt -t -1 --expectSignal=1

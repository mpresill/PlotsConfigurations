#!/bin/bash
CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted
SR1_var=DNNoutput_pruned_bVeto #try other binnings
SR2_var=DNNoutput_pruned_bReq
cutDY1=DYcr_bVeto
cutSR1=SR_bVeto
cutDY2=DYcr_bTag
cutSR2=SR_bTag
Date=27Jan2022_2018
version=2018_dec21
DATACARD_NAME=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/combined_card_all_comb.txt




#echo "RUNNING WITH TOP CR FIT"
rm -rf Workspace/${CUT}
mkdir -p Workspace
mkdir Workspace/${CUT}
cardName=${CUT}


combineCards.py boosted_sr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR1}/${SR1_var}/datacard.txt boosted_DYcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt boosted_topcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR1_var}/datacard.txt boosted_sr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutSR2}/${SR2_var}/datacard.txt boosted_DYcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt boosted_topcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Boosted_topcr/${SR2_var}/datacard.txt resolved_sr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR1}/${SR1_var}/datacard.txt resolved_DYcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt resolved_topcr1=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR1_var}/datacard.txt resolved_sr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutSR2}/${SR2_var}/datacard.txt resolved_DYcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt resolved_topcr2=/afs/cern.ch/work/a/ahakimi/latinos_NN/PlotsConfigurations/Configurations/VBS_ZV/${version}/Datacards_${Date}/Resolved_topcr/${SR2_var}/datacard.txt> ${DATACARD_NAME}


cardNameWorkspace=Workspace/${CUT}
outputFolder=Workspace/${CUT}


text2workspace.py ${DATACARD_NAME} -o ${cardNameWorkspace}.root 
mkdir fit
mkdir fit/${VAR2}

outputFolder=Checks_${date}/${var2}
mkdir ${outputFolder}

combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0

combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1


combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json

plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  ${outputFolder}/impacts_t0
plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  ${outputFolder}/impacts_t1
cp -r ${outputFolder} /eos/user/a/ahakimi/www/ZV_analysis/Plots_${date}

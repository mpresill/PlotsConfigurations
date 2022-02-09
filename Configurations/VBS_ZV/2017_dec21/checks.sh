#!/bin/bash
folder=doublebin_v2
date=14Dec2021_2018
VAR1=DYfit_2D_bin_Resolved #DYfit_bin_Resolved #mjj_max, DNNoutput_All_years, Zleppt
VAR2=DNNoutput_full #try other binnings
CUT=Resolved_DYcr_bVeto
CUTSR=Resolved_SR_bVeto
CUTtop=Resolved_topcr
DATACARD_NAME=datacard_combined.txt




#echo "RUNNING WITH TOP CR FIT"
rm -rf Workspace/${CUT}
mkdir -p Workspace
mkdir Workspace/${CUT}
cardName=${CUT}

combineCards.py ${CUT}_${VAR1}=Datacards_${date}/${CUT}/${VAR1}/datacard.txt ${CUTSR}_${VAR2}=Datacards_${date}/${CUTSR}/${VAR2}/datacard.txt ${CUTtop}_${VAR2}=Datacards_${date}/${CUTtop}/${VAR2}/datacard.txt > ${DATACARD_NAME}

cardNameWorkspace=Workspace/${CUT}
outputFolder=Workspace/${CUT}


text2workspace.py ${DATACARD_NAME} -o ${cardNameWorkspace}.root --channel-masks
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

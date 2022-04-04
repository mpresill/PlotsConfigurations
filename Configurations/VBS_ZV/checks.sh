#!/bin/bash
date=Allyears_Mar22
mkdir ${date}
DATACARD_NAME=${date}/datacard_combined
DATE_18=14Feb2022_2018
DATE_17=01Mar2022_2017
DATE_16=14Feb2022_2016
combineCards.py Boosted_SR_bVeto_18=2018_Feb22/Datacards_${DATE_18}/Boosted_SR_bVeto/DNNoutput_pruned_bVeto/datacard.txt Boosted_SR_bTag_18=2018_Feb22/Datacards_${DATE_18}/Boosted_SR_bTag/DNNoutput_pruned_bReq/datacard.txt Boosted_DYcr_18=2018_Feb22/Datacards_${DATE_18}/Boosted_DYcr_bVeto/DYfit_Z_bin_Boosted/datacard.txt Boosted_topcr_18=2018_Feb22/Datacards_${DATE_18}/Boosted_topcr/DNNoutput_pruned_bVeto/datacard.txt Resolved_SR_bVeto_18=2018_Feb22/Datacards_${DATE_18}/Resolved_SR_bVeto/DNNoutput_pruned_bVeto/datacard.txt Resolved_SR_bTag_18=2018_Feb22/Datacards_${DATE_18}/Resolved_SR_bTag/DNNoutput_pruned_bReq/datacard.txt Resolved_DYcr_18=2018_Feb22/Datacards_${DATE_18}/Resolved_DYcr_bVeto/DYfit_2D_bin_Resolved/datacard.txt Resolved_topcr_18=2018_Feb22/Datacards_${DATE_18}/Resolved_topcr/DNNoutput_pruned_bVeto/datacard.txt Boosted_SR_bVeto_17=2017_Feb22/Datacards_${DATE_17}/Boosted_SR_bVeto/DNNoutput_pruned_bVeto/datacard.txt Boosted_SR_bTag_17=2017_Feb22/Datacards_${DATE_17}/Boosted_SR_bTag/DNNoutput_pruned_bReq/datacard.txt Boosted_DYcr_17=2017_Feb22/Datacards_${DATE_17}/Boosted_DYcr_bVeto/DYfit_Z_bin_Boosted/datacard.txt Resolved_SR_bVeto_17=2017_Feb22/Datacards_${DATE_17}/Resolved_SR_bVeto/DNNoutput_pruned_bVeto/datacard.txt Resolved_SR_bTag_17=2017_Feb22/Datacards_${DATE_17}/Resolved_SR_bTag/DNNoutput_pruned_bReq/datacard.txt Resolved_DYcr_17=2017_Feb22/Datacards_${DATE_17}/Resolved_DYcr_bVeto/DYfit_2D_bin_Resolved/datacard.txt Boosted_SR_bVeto_16=2016_Feb22/Datacards_${DATE_16}/Boosted_SR_bVeto/DNNoutput_pruned_bVeto/datacard.txt Boosted_SR_bTag_16=2016_Feb22/Datacards_${DATE_16}/Boosted_SR_bTag/DNNoutput_pruned_bReq/datacard.txt Boosted_DYcr_16=2016_Feb22/Datacards_${DATE_16}/Boosted_DYcr_bVeto/DYfit_Z_bin/datacard.txt Boosted_topcr_16=2016_Feb22/Datacards_${DATE_16}/Boosted_topcr/DNNoutput_pruned_bVeto/datacard.txt Resolved_SR_bVeto_16=2016_Feb22/Datacards_${DATE_16}/Resolved_SR_bVeto/DNNoutput_pruned_bVeto/datacard.txt Resolved_SR_bTag_16=2016_Feb22/Datacards_${DATE_16}/Resolved_SR_bTag/DNNoutput_pruned_bReq/datacard.txt Resolved_DYcr_16=2016_Feb22/Datacards_${DATE_16}/Resolved_DYcr_bVeto/DYfit_Z_bin/datacard.txt Resolved_topcr_16=2016_Feb22/Datacards_${DATE_16}/Resolved_topcr/DNNoutput_pruned_bVeto/datacard.txt > ${DATACARD_NAME}.txt
#cd 2018_SR
 
#echo "RUNNING WITH TOP CR FIT"
#rm -rf Checks/${DATACARD_NAME}
mkdir -p Checks
mkdir -p Checks/${date}
mkdir -p Checks/${DATACARD_NAME}
cardName=${DATACARD_NAME}
cardNameWorkspace=Checks/${DATACARD_NAME}
outputFolder=Checks/${DATACARD_NAME}
mkdir -p Checks/${DATACARD_NAME}
text2workspace.py ${cardName}.txt -o ${cardNameWorkspace}.root

combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0 

#combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0
#combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 
#combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1


combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json
#combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json

plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  ${outputFolder}/impacts_t0
#plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  ${outputFolder}/impacts_t1
cd ..

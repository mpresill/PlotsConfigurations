#!/bin/bash
folder=2016_dec21
date=24Dec2021_2016
VAR1=mjj #DYfit_bin_Resolved #mjj_max, DNNoutput_All_years, Zleppt
VAR2=mjj #try other binnings
CUT=Resolved_DYcr_bTag
CUTSR=Resolved_SR_bTag
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


text2workspace.py ${DATACARD_NAME} -o ${cardNameWorkspace}.root 
mkdir fit
mkdir fit/${VAR2}

#create toys
#combine -M GenerateOnly ${cardNameWorkspace}.root -t -1 --saveToys --toysFrequentist --setParameters mask_${CUTSR}_${VAR2}=1
#mv higgsCombineTest.GenerateOnly.mH120.123456.root fit/toys_${VAR2}.root

combine -M FitDiagnostics ${cardNameWorkspace}.root --out fit/${VAR2} --robustFit=1 --cminDefaultMinimizerStrategy 0 --rMin -20 --saveWithUncertainties --saveOverallShapes --plots --saveNormalizations -t -1 --expectSignal 1 --toysFreq  #--toysFreq --expectSignal 0
#cd Datacards_${date}



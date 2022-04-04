#!/bin/bash
folder=2016_Feb22
date=14Feb2022_2016
#VAR1=DYfit_2D_bin_Resolved #DYfit_bin_Resolved #mjj_max, DNNoutput_All_years, Zleppt
VAR1=DYfit_Z_bin
VAR2=DNNoutput_pruned_bVeto #try other binnings
CAT=Resolved
CUT=${CAT}_DYcr_bVeto
CUTSR=${CAT}_SR_bVeto
CUTtop=${CAT}_topcr
DATACARD_NAME=datacard_${CAT}_combined.txt




#echo "RUNNING WITH TOP CR FIT"
rm -rf Workspace/${CUT}
mkdir -p Workspace
mkdir Workspace/${CUT}
cardName=${CUT}

combineCards.py ${CUT}_${VAR1}=Datacards_${date}/${CUT}/${VAR1}/datacard.txt ${CUTSR}_${VAR2}=Datacards_${date}/${CUTSR}/${VAR2}/datacard.txt > ${DATACARD_NAME}
cardNameWorkspace=Workspace/${CUT}
outputFolder=Workspace/${CUT}


text2workspace.py Datacards_${date}/${CUT}/${VAR1}/datacard.txt -o ${cardNameWorkspace}.root
mkdir fit
mkdir fit/${CAT}
mkdir fit/${CAT}/${VAR2}

#create toys
#combine -M GenerateOnly ${cardNameWorkspace}.root -t -1 --saveToys --toysFrequentist --setParameters mask_${CUTSR}_${VAR2}=1
#mv higgsCombineTest.GenerateOnly.mH120.123456.root fit/toys_${VAR2}.root

combine -M FitDiagnostics ${cardNameWorkspace}.root --out fit/${CAT}/${VAR2} --robustFit=1 --cminDefaultMinimizerStrategy 0 --rMin -20 --saveWithUncertainties --saveOverallShapes --plots --saveNormalizations -t -1 --expectSignal 0 --toysFreq  #--setParameters mask_${CUTSR}_${VAR2}=1 --toysFile  fit/toys_${VAR2}.root #--toysFreq --expectSignal 0 --robustFit=1
#cd Datacards_${date}



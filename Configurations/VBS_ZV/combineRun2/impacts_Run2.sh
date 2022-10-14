#!/bin/bash

tag=ANv5
combinedFIT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/YearsCombination_${tag}/combined_card_all_comb
fitDiagFOLDER=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/YearsCombination_${tag}

cd ../tmp #created this temporary folder to aovoid issues with the eos path in the workspace produced

text2workspace.py ${combinedFIT}.txt -o impactWorkspace.root

#############################################
#                                           #
#         impact plots blind                #
#                                           #
#############################################

outputFolder=${fitDiagFOLDER}
mkdir -p ${fitDiagFOLDER}

combine -M FitDiagnostics -d impactWorkspace.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0 --cminDefaultMinimizerStrategy=0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0

combine -M FitDiagnostics -d impactWorkspace.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1 --cminDefaultMinimizerStrategy=0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1

combineTool.py -M Impacts -d impactWorkspace.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d impactWorkspace.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10

combineTool.py -M Impacts -d impactWorkspace.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d impactWorkspace.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10

combineTool.py -M Impacts -d impactWorkspace.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
combineTool.py -M Impacts -d impactWorkspace.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10
plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  impacts_t0
plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  impacts_t1
cp impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/YearsCombination_${tag}_impacts_t0.pdf
cp impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/YearsCombination_${tag}_impacts_t1.pdf
cp impacts_t0.pdf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/YearsCombination_${tag}/.
cp impacts_t1.pdf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/YearsCombination_${tag}/.



#############################################
#                                           #
#            DIFF NUISANCES                 #
#           PRE/POST FIT YIELDS             #
#                                           #
#############################################
combine -M FitDiagnostics impactWorkspace.root \
        --out ${fitDiagFOLDER} \
        -t -1 --toysFreq --robustFit=1 --rMin -10 \
        --cminDefaultMinimizerStrategy 0 \
        --saveNormalizations --saveWithUncertainties

python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html ${fitDiagFOLDER}//fitDiagnosticsTest.root > ${fitDiagFOLDER}/fit_YearsCombination_${tag}.html
cp ${fitDiagFOLDER}/fit_YearsCombination_${tag}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 

python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/mlfitNormsToText.py ${fitDiagFOLDER}/fitDiagnosticsTest.root > ${fitDiagFOLDER}/postfit_YearsCombination_${tag}_norm.txt
cp ${fitDiagFOLDER}/postfit_YearsCombination_${tag}_norm.txt /eos/user/m/mpresill/www/VBS/diffNuisances/. 
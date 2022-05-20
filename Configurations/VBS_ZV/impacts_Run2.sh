#!/bin/bash

date=8Apr2022_Run2 #_2017
combinedFIT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/YearsCombination_8Apr2022/combined_card_all_comb
#combinedFIT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_${date}/combined_card_all_comb_${date}
fitDiagFOLDER=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/${date}

cd tmp #created this temporary folder to aovoid issues with the eos path in the workspace produced

text2workspace.py ${combinedFIT}.txt -o impactWorkspace.root

#############################################
#                                           #
#         impact plots blind                #
#                                           #
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
cp impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${date}_impacts_t0.pdf
cp impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${date}_impacts_t1.pdf
cp impacts_t0.pdf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/${date}/.
cp impacts_t1.pdf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/${date}/.

cd ..

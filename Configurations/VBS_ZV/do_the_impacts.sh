#!/bin/bash
#this goes to Matteo's installation path of combine and makes impact plot from the chosen datacard/s.

DIR=$PWD
cd /afs/cern.ch/work/m/mpresill/Combine_limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/VBS/
cmsenv 


############################################
#####combine datacard for the specific year
DATACARD_NAME2016=_15Feb021_2016_btag 
VARIABLE=mjj_binned 
echo "======================================="
#echo "RUNNING boosted 2016 WITH TOP and DY CR FIT"
combineCards.py Boosted2016SR=${DATACARD_NAME2016}/Boosted_SR_tight/${VARIABLE}/datacard.txt \
                Boosted2016DY=${DATACARD_NAME2016}/Boosted_DYcr/events/datacard.txt \
                Boosted2016top=${DATACARD_NAME2016}/Boosted_topcr/events/datacard.txt \
                &> ${DATACARD_NAME2016}_${VARIABLE}_2016_boostedCRfit.txt

combine -M Significance ${DATACARD_NAME2016}_${VARIABLE}_2016_boostedCRfit.txt -t -1 --expectSignal=1
echo "======================================="
#echo "RUNNING 2016 resolved WITH TOP and DY CR FIT"
combineCards.py Resolved2016SR=${DATACARD_NAME2016}/Resolved_SR_tight/${VARIABLE}/datacard.txt  \
                Resolved2016DY=${DATACARD_NAME2016}/Resolved_DYcr/events/datacard.txt \
                Resolved2016top=${DATACARD_NAME2016}/Resolved_topcr/events/datacard.txt \
                &> ${DATACARD_NAME2016}_${VARIABLE}_2016_resolvedCRfit.txt

combine -M Significance ${DATACARD_NAME2016}_${VARIABLE}_2016_resolvedCRfit.txt -t -1 --expectSignal=1
echo "======================================="
#echo "RUNNING 2016 WITH TOP and DY CR FIT"
combineCards.py Boosted2016SR=${DATACARD_NAME2016}/Boosted_SR_tight/${VARIABLE}/datacard.txt \
                Resolved2016SR=${DATACARD_NAME2016}/Resolved_SR_tight/${VARIABLE}/datacard.txt  \
                Boosted2016DY=${DATACARD_NAME2016}/Boosted_DYcr/events/datacard.txt \
                Resolved2016DY=${DATACARD_NAME2016}/Resolved_DYcr/events/datacard.txt \
                Boosted2016top=${DATACARD_NAME2016}/Boosted_topcr/events/datacard.txt \
                Resolved2016top=${DATACARD_NAME2016}/Resolved_topcr/events/datacard.txt \
                &> ${DATACARD_NAME2016}_${VARIABLE}_2016_CRfit.txt

combine -M Significance ${DATACARD_NAME2016}_${VARIABLE}_2016_CRfit.txt -t -1 --expectSignal=1
############################################
############################################

##take the following name from the line above
DATACARD_NAME=${DATACARD_NAME2016}_${VARIABLE}_2016_CRfit


###########################################
#####running the impact
###########################################
rm -rf Checks/${DATACARD_NAME}
mkdir Checks/${DATACARD_NAME}
cardName=${DATACARD_NAME}
cardNameWorkspace=Checks/${DATACARD_NAME}
outputFolder=Checks/${DATACARD_NAME}

text2workspace.py ${cardName}.txt -o ${cardNameWorkspace}.root

combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0

combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10

combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10


combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10

plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  ${outputFolder}/impacts_t0
plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  ${outputFolder}/impacts_t1




cp ${outputFolder}/impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${CHANNEL}${DATACARD_NAME}_impacts_t0.pdf
cp ${outputFolder}/impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${CHANNEL}${DATACARD_NAME}_impacts_t1.pdf



cd ${DIR}
cmsenv
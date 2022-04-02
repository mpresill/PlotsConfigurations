#!/bin/bash
DATE=_22Feb2022_2016
VARIABLE=mjj


echo "=================================="
echo "combining SR b-veto and b-tag 2016"

combineCards.py Boosted2016_SR_bVeto=/2016_dec21/Datacards/${DATE}/Boosted_SR_bVeto/${VARIABLE}/datacard.txt \
                Boosted2016_SR_bTag=/2016_dec21/Datacards/${DATE}/Boosted_SR_bTag/${VARIABLE}/datacard.txt \
                Resolved2016_SR_bVeto=/2016_dec21/Datacards/${DATE}/Resolved_SR_bVeto/${VARIABLE}/datacard.txt \
                Resolved2016_SR_bTag=/2016_dec21/Datacards/${DATE}/Resolved_SR_bTag/${VARIABLE}/datacard.txt \
                &> ./2016_dec21/Datacards/${VARIABLE}${DATE}_2016_combined.txt

#echo "*********************************** "
#echo "   let's test blind significance    "
#combine -M Significance -t -1 ./2016_dec21/Datacards/${VARIABLE}${DATE}_2016_combined.txt








#############################################   outdated code follows!!!

############################################
#####combine datacard for the specific year
#DATACARD_NAME2016=_20Feb2021_2016_btag 
#DATACARD_NAME2017=_20Feb2021_2017_btag 
#DATACARD_NAME2018=_20Feb2021_2018_btag 
#VARIABLE=mjj_binned 
#####echo "======================================="
######echo "RUNNING boosted 2016 WITH TOP and DY CR FIT"
#####combineCards.py Boosted2016SR=${DATACARD_NAME2016}/Boosted_SR_Ram/${VARIABLE}/datacard.txt \
#####                Boosted2016DY=${DATACARD_NAME2016}/Boosted_DYcr/events/datacard.txt \
#####                Boosted2016top=${DATACARD_NAME2016}/Boosted_topcr/events/datacard.txt \
#####                &> ${DATACARD_NAME2016}_${VARIABLE}_2016_boostedCRfit.txt
#####
#####combine -M Significance ${DATACARD_NAME2016}_${VARIABLE}_2016_boostedCRfit.txt -t -1 --expectSignal=1
#####echo "===============BOOSTED================="
#####echo "======================================="
######echo "RUNNING 2016 resolved WITH TOP and DY CR FIT"
#####combineCards.py Resolved2016SR=${DATACARD_NAME2016}/Resolved_SR_Ram/${VARIABLE}/datacard.txt  \
#####                Resolved2016DY=${DATACARD_NAME2016}/Resolved_DYcr/events/datacard.txt \
#####                Resolved2016top=${DATACARD_NAME2016}/Resolved_topcr/events/datacard.txt \
#####                &> ${DATACARD_NAME2016}_${VARIABLE}_2016_resolvedCRfit.txt
#####
#####combine -M Significance ${DATACARD_NAME2016}_${VARIABLE}_2016_resolvedCRfit.txt -t -1 --expectSignal=1
#####echo "===============RESOLVED================"
#####echo "======================================="
######echo "RUNNING 2016 WITH TOP and DY CR FIT"
#####combineCards.py Boosted2016SR=${DATACARD_NAME2016}/Boosted_SR_Ram/${VARIABLE}/datacard.txt \
#####                Resolved2016SR=${DATACARD_NAME2016}/Resolved_SR_Ram/${VARIABLE}/datacard.txt  \
#####                Boosted2016DY=${DATACARD_NAME2016}/Boosted_DYcr/events/datacard.txt \
#####                Resolved2016DY=${DATACARD_NAME2016}/Resolved_DYcr/events/datacard.txt \
#####                Boosted2016top=${DATACARD_NAME2016}/Boosted_topcr/events/datacard.txt \
#####                Resolved2016top=${DATACARD_NAME2016}/Resolved_topcr/events/datacard.txt \
#####                &> ${DATACARD_NAME2016}_${VARIABLE}_2016_CRfit.txt
#####
#####combine -M Significance ${DATACARD_NAME2016}_${VARIABLE}_2016_CRfit.txt -t -1 --expectSignal=1
#################################################
#################################################
#####
#####
#####combineCards.py ${DATACARD_NAME2016}_${VARIABLE}_2016_CRfit.txt ${DATACARD_NAME2017}_${VARIABLE}_2017_CRfit.txt ${DATACARD_NAME2018}_${VARIABLE}_2018_CRfit.txt &> ${VARIABLE}_FullRun2_CRfit.txt




###########################################
#####running the post fit plotting
###########################################
#date=20Apr2021_2018bin_testBoosted
#category=Boosted
#
##fitting variable #1
#VAR=Zleppt
#CUT=Boosted_DYcr_bVeto
#DATACARD_NAME=_${date}/${CUT}/${VAR}_${category}/datacard
#
##fitting variable #2
#VAR2=mjj_max
#CUT2=Boosted_SR_bVeto
#DATACARD_NAME2=_${date}/${CUT2}/${VAR2}_${category}/datacard


#combineCards.py ${DATACARD_NAME}.txt \
#                ${DATACARD_NAME2}.txt \
#                &> ${data}.txt #
#
#

#echo "===============POSTFIT================"
#echo "======================================="
#echo "Text to workspace"
#text2workspace.py ${data}.txt -o ${data}.root#

##mkdir Fit
#outputFolder=Fit/${data}
#rm -rf ${outputFolder}
#mkdir ${outputFolder}
##################################
#echo "FitDiagnostic"
#combine -M FitDiagnostics ${data}.root \
#        --out ${outputFolder} \
#        --robustFit=1 --cminDefaultMinimizerStrategy 0 \
#        --rMin -10 --rMax 10 \
#        -t -1 --toysFreq
##################################
#echo "PostFitShapesFromWorkspace"
#PostFitShapesFromWorkspace \
#    -w ${date}.root \
#    -d ${date}.txt \
#    -o ${outputFolder}/output_${date}.root \
#    --postfit --sampling \
#    -f ${outputFolder}/fitDiagnostics.root:fit_s \
#    --total-shapes
##################################
#echo "mkPostFitCombinedPlot"
#
#cp -r ${outputFolder} ${DIR}/.
#cd ${DIR}
#cmsenv
#mkPostFitCombinedPlot.py \
#    --inputFilePostFitShapesFromWorkspace ${outputFolder}/output_${date}.root \
#    --outputFile postfit.root \
#    --kind P \
#    --cutName Boosted_SR_bVeto \
#    --variable Zleppt_Boosted \
#    --structureFile 2018_test/structure.py \
#    --plotFile 2018_test/plot_boost.py \
#    --lumiText '59.74/fb'
#echo "mkPlot"
#cp postfit.root 2018_test/.
#cd 2018_test
#mkPlot.py --pycfg=2018_test/configuration.py --inputFile postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000 
#
#rm -r postfit_${CUT}
#mkdir postfit_${CUT}
#mv plot_combined/* postfit_${CUT}
#rm -r plot_combined
#
#cp -r postfit_${CUT} /eos/home-a/ahakimi/www/ZV_analysis/Plots_31Mar2021_2018bintest



######take the following name from the line above
#####DATACARD_NAME=${data}.txt  #${DATACARD_NAME2016}_${VARIABLE}_2016_CRfit
####echo "===============COMBINED================"
####echo "======================================="
###############################################
#########running the impact
###############################################
####rm -rf Checks/${data}
####mkdir Checks/${data}
####cardName=${data}
####cardNameWorkspace=Checks/${data}
####outputFolder_impacts=Checks/${data}
####
####text2workspace.py ${cardName}.txt -o ${cardNameWorkspace}.root
####
####combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0 --cminDefaultMinimizerStrategy 0
####python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder_impacts}/fitResults_t0
####
####combine -M FitDiagnostics -d ${cardNameWorkspace}.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1 --cminDefaultMinimizerStrategy 0
####python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder_impacts}/fitResults_t1
####
####combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10
####combineTool.py -M Impacts -d ${cardNameWorkspace}.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10
####
####combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder_impacts}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10
####combineTool.py -M Impacts -d ${cardNameWorkspace}.root -o ${outputFolder_impacts}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10
####
####
####combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t0 -o ${outputFolder_impacts}/impacts_t0.json --parallel 10
####combineTool.py -M Impacts -d ${cardNameWorkspace}.root -m 1 -n t1 -o ${outputFolder_impacts}/impacts_t1.json --parallel 10
####
####plotImpacts.py -i  ${outputFolder_impacts}/impacts_t0.json -o  ${outputFolder_impacts}/impacts_t0
####plotImpacts.py -i  ${outputFolder_impacts}/impacts_t1.json -o  ${outputFolder_impacts}/impact
####cp ${outputFolder_impacts}/impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${data}_impacts_t0_Boosted2018test_binned.pdf
####cp ${outputFolder_impacts}/impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${data}_impacts_t1_Boosted2018test_binned.pdf
####cp ${outputFolder_impacts}/impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${data}_impacts_t0_Boosted2018test_binned.pdf
####cp ${outputFolder_impacts}/impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${data}_impacts_t1_Boosted2018test_binned.pdf
####
####
####
####cd ${DIR}
####cmsenv

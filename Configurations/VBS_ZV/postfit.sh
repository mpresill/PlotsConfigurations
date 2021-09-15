#!/bin/bash
folder=2018_test
cd ${folder}
date=29June2021_2018_bin1D

#  fitting variable
VAR1=DYfit_Z_bin_Resolved
CUT1=Resolved_DYcr_bVeto
DATACARD_FIT=Datacards/_${date}/${CUT1}/${VAR1}/datacard
echo "${DATACARD_FIT}"

#  plotting variable 
PLOTVAR=Zleppt
CUT2=Resolved_SR_bVeto #Boosted_SR_bVeto
DATACARD_PLOT=Datacards/_${date}/${CUT2}/${PLOTVAR}/datacard
echo "${DATACARD_PLOT}"
#
#########    combining datacards
combineCards.py binFit=${DATACARD_FIT}.txt \
                binSR=${DATACARD_PLOT}.txt \
                &> combined.txt 

#######     workspaces
text2workspace.py ${DATACARD_FIT}.txt -o ${DATACARD_FIT}.root
text2workspace.py ${DATACARD_PLOT}.txt -o ${DATACARD_PLOT}.root
text2workspace.py combined.txt -o combined.root

#######     fit
##mkdir fitDiagnosticsCombined
## -t -1 --expectSignal 0   -> this is for t0 Asimov, b-only
## -t -1 --expectSignal 1   -> this is for t1 Asimov, s+b
#combine -M FitDiagnostics combined.root  --out fitDiagnosticsCombined -t -1 --robustFit=1 --cminDefaultMinimizerStrategy 0 --rMin -20 --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 --plots #-v 2 # --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 --plots #--algo impact -P parameter #--cminDefaultMinimizerStrategy 1 # --robustHesse 1 #--X-rtd MINIMIZER_analytic #--robustHesse 1 # --forceRecreateNLL --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL #--robustFit=1 --cminDefaultMinimizerStrategy 0 #--minos all #--cminDefaultMinimizerTolerance 0.1 --minos poi 
#python ../../../../HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html fitDiagnosticsCombined/fitDiagnosticsTest.root > fit_${date}.html
#cp fit_${date}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 

#########PostfitfromWorkspace
PostFitShapesFromWorkspace \
    -w ${DATACARD_PLOT}.root \
    -d ${DATACARD_PLOT}.txt \
    -o output_histograms.root \
    --postfit --sampling \
    -f fitDiagnosticsCombined/fitDiagnosticsTest.root:fit_s \
    --total-shapes


mkPostFitCombinedPlot.py \
    --inputFilePostFitShapesFromWorkspace output_histograms.root \
    --outputFile output_postfit.root \
    --kind P \
    --cutName ${CUT2} \
    --variable ${PLOTVAR} \
    --structureFile structure.py \
    --plotFile plot.py \
    --lumiText '59.74/fb' #\
    #--nonFitVariable
       # --listOfFilesOriginal rootFile_${date}/plots_VBS_ZV_${data}.root \
    


rm -rf plot_combined
mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000
#
mkdir /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}_${VAR1}
mkdir -p /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}_${VAR1}

###uncomment for postfit
cp /eos/user/m/mpresill/www/VBS/2018_v7/index.php /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}_${VAR1}/.
cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}_${VAR1}/.
###uncomment for prefit
#cp /eos/user/m/mpresill/www/VBS/2018_v7/index.php /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}_${VAR1}/.
#cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}_${VAR1}/.


#rm -r postfit_${CUT}_${FITVAR}fit
#mv plot_combined postfit_${CUT}_${FITVAR}fit

#cp -r postfit_${CUT}_${FITVAR}fit /e


cd ..

#!/bin/bash
folder=2017_v7_2
cd ${folder}
date=19Oct2021_2017
region=bVeto


#############################################
#                                           #
#       FITTING CRs + SR MAIN VARIABLE      #
#             (mjj, DNN, ...)               #
#                                           #
#############################################

########     DYcr fitting variables
VAR1=DYfit_Z_vbs1_bin_Resolved   #DYfit_Z_bin_Boosted #DYfit_Z_vbs1_bin_Boosted
CUT1=Resolved_DYcr_${region}
DATACARD_FIT=Datacards/_${date}/${CUT1}/${VAR1}/datacard
echo "${DATACARD_FIT}"
########     SR fitting variable 
VAR1sr=mjj_max
CUT1sr=Resolved_SR_${region}
DATACARD_FITsr=Datacards/_${date}/${CUT1sr}/${VAR1sr}/datacard
echo "${DATACARD_FITsr}"
#########    eventually top cr can be added as well here

########    combining datacards
combineCards.py binDYcr=${DATACARD_FIT}.txt \
                binSR=${DATACARD_FITsr}.txt \
                &> combined_FIT.txt 
text2workspace.py combined_FIT.txt -o combined_FIT.root
#########     fit
mkdir -p fitDiagnosticsCombined_${VAR1}_${VAR1sr}_${CUT1sr}
## -t -1 --expectSignal 0   -> this is for t0 Asimov, b-only
## -t -1 --expectSignal 1   -> this is for t1 Asimov, s+b
combine -M FitDiagnostics combined.root  --out fitDiagnosticsCombined_${VAR1}_${VAR1sr}_${CUT1sr} -t -1 --toysFreq --robustFit=1 --rMin -10 --cminDefaultMinimizerStrategy 0 --saveNormalizations --saveWithUncertainties  #--saveOverallShapes --plots --numToysForShapes 200 #-v 2 # --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 --plots #--algo impact -P parameter #--cminDefaultMinimizerStrategy 1 # --robustHesse 1 #--X-rtd MINIMIZER_analytic #--robustHesse 1 # --forceRecreateNLL --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL #--robustFit=1 --cminDefaultMinimizerStrategy 0 #--minos all #--cminDefaultMinimizerTolerance 0.1 --minos poi 
python ../../../../HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html fitDiagnosticsCombined_${VAR1}_${VAR1sr}_${CUT1sr}/fitDiagnosticsTest.root > fit_${date}_${VAR1}_${VAR1sr}_${CUT1sr}.html
cp fit_${date}_${VAR1}_${VAR1sr}_${CUT1sr}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 




#############################################
#                                           #
#         impact plots blind                #
#                                           #
#                                           #
#############################################
#mkdir -p impacts
#mkdir -p impacts/${date}
#outputFolder=impacts/${date}
#combine -M FitDiagnostics -d combined_FIT.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0
#
#combine -M FitDiagnostics -d combined_FIT.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1
#
#combineTool.py -M Impacts -d combined_FIT.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10
#combineTool.py -M Impacts -d combined_FIT.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10
#
#combineTool.py -M Impacts -d combined_FIT.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10
#combineTool.py -M Impacts -d combined_FIT.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10
#
#combineTool.py -M Impacts -d combined_FIT.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
#combineTool.py -M Impacts -d combined_FIT.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10
#
#plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  ${outputFolder}/impacts_t0
#plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  ${outputFolder}/impacts_t1
#
#cp ${outputFolder}/impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${date}_${VAR1}_impacts_t0.pdf
#cp ${outputFolder}/impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${date}_${VAR1}_impacts_t1.pdf




#############################################
#                                           #
#         pre / post-fit      plotting      #
#         (mjj, DNN, any var.)              #
#                                           #
#############################################
#"
declare -a StringArray=("VBS_jet_pt1" "VBS_jet_pt2" "V_jet_pt1" "V_jet_pt2" "mjj_max" "detajj_mjjmax" "DYfit_Z_vbs1_bin_Resolved" "DYfit_Z_bin_Boosted" )        #looping
for val in "${StringArray[@]}"; do                                                                                 #looping

#  plotting variable 
PLOTVAR=${val}
CUT2=Resolved_SR_${region} 
DATACARD_PLOT=Datacards/_${date}/${CUT2}/${PLOTVAR}/datacard
echo "${DATACARD_PLOT}"
text2workspace.py ${DATACARD_PLOT}.txt -o ${DATACARD_PLOT}.root

#########PostfitfromWorkspace
PostFitShapesFromWorkspace \
    -w ${DATACARD_PLOT}.root \
    -d ${DATACARD_PLOT}.txt \
    -o output_histograms.root \
    --postfit --sampling \
    -f fitDiagnosticsCombined_${VAR1}_${VAR1sr}_${CUT1sr}/fitDiagnosticsTest.root:fit_s \
    --total-shapes


mkPostFitCombinedPlot.py \
    --inputFilePostFitShapesFromWorkspace output_histograms.root \
    --outputFile output_postfit.root \
    --kind P \
    --cutName ${CUT2} \
    --variable ${PLOTVAR} \
    --structureFile structure.py \
    --plotFile plot.py \
    --lumiText '59.74/fb' 
    #\--nonFitVariable
       # --listOfFilesOriginal rootFile_${date}/plots_VBS_ZV_${data}.root \
   


rm -rf *combined.py
mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000
#
mkdir -p /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}_${VAR1}
mkdir -p /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}_${VAR1}

###      uncomment for postfit   ######
cp /eos/user/m/mpresill/www/VBS/2017_v7/index.php /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}_${VAR1}/.
cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}_${VAR1}/.
cp -r *combined.py /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}_${VAR1}/.
###      uncomment for prefit   ######
#cp /eos/user/m/mpresill/www/VBS/2017_v7/index.php /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}_${VAR1}/.
#cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}_${VAR1}/.
#cp -r *combined.py /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}_${VAR1}/.

#rm -r postfit_${CUT}_${FITVAR}fit
#mv plot_combined postfit_${CUT}_${FITVAR}fit

#cp -r postfit_${CUT}_${FITVAR}fit /e

done 

cd ..

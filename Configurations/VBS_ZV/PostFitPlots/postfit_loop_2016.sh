#!/bin/bash

#
#   TO RUN IT LAUNCH LIKE:
#   sh postfit_loop_2016.sh date folder CATEGORY CUT VARIABLEtoPLOT
#
#   example: sh postfit_loop_2016.sh 11May2022_2016 2016_Apr22_v2 Resolved DYcr_bTag DNNoutput_pruned_bReq
#
#   note that the fitdiagnostic is automatically chosen as the full-year-combined in this script
#


date=$1
folder=$2
Category=$3
CUT2=$4
PLOTVAR=$5

#date=11May2022_2016
#folder=2016_Apr22_v2

    # variable to plot
#PLOTVAR=DNNoutput_pruned_bVeto_morebins         #### 1
#PLOTVAR=DNNoutput_pruned_bReq #_morebins          #### 2
#PLOTVAR=DYfit_Z_bin                             #### 3
#PLOTVAR=DYfit_Z_bin                             #### 4
#PLOTVAR=DNNoutput_pruned_bReq_morebins          #### 5
    # region to plot
#CUT2=SR_bVeto                                   #### 1
#CUT2=SR_bTag                                    #### 2
#CUT2=DYcr_bVeto                                 #### 3
#CUT2=DYcr_bTag                                  #### 4
#CUT2=topcr                                      #### 5

    # Category
#Category=Resolved
#Category=Boosted



    # path of the FitDiagnostic.root file 
FitDiagnosticPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/${date}/

        
DATACARD_PLOT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_${date}/${Category}_${CUT2}/${PLOTVAR}/datacard
echo "${DATACARD_PLOT}"
text2workspace.py ${DATACARD_PLOT}.txt -o ${DATACARD_PLOT}.root


DATACARD_FIT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_${date}/combined_card_all_comb_${date}
echo "${DATACARD_FIT}"
text2workspace.py ${DATACARD_FIT}.txt -o ${DATACARD_FIT}.root
combine -M FitDiagnostics ${DATACARD_FIT}.root \
        --out fit \
        -t -1 --toysFreq --rMin -10 \
        --saveNormalizations --saveWithUncertainties #\
    ##        --cminDefaultMinimizerStrategy 0 --robustFit=1
    ##        --expectSignal 1 \

##############################################
##                                           #
##         pre / post-fit      plotting      #
##         (mjj, DNN, any var.)              #
##                                           #
##############################################
#
########PostfitfromWorkspace
PostFitShapesFromWorkspace \
    -w ${DATACARD_PLOT}.root \
    -d ${DATACARD_PLOT}.txt \
    -o output_histograms.root \
    --postfit --sampling \
    -f fit/fitDiagnosticsTest.root:fit_s \
    --total-shapes

    # clean up local plotter folder
rm -r plot_combined/*

mkPostFitCombinedPlot.py \
   --inputFilePostFitShapesFromWorkspace output_histograms.root \
   --outputFile output_postfit.root \
   --kind P \
   --cutName ${CUT2} \
   --variable ${PLOTVAR} \
   --structureFile ../${folder}/structure.py \
   --plotFile ../${folder}/plot_v2.py \
   --lumiText '35.87/fb' 
   
mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000

        #    create the folders where to backup files
mkdir -p /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}
mkdir -p /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}

        ###      uncomment for postfit   ######
cp /eos/user/m/mpresill/www/VBS/2016_v7/index.php /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}/.
cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}/.
cp -r *combined.py /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}/.

###################################################################
        ###      uncomment for prefit   ######
mkPostFitCombinedPlot.py \
   --inputFilePostFitShapesFromWorkspace output_histograms.root \
   --outputFile output_postfit.root \
   --kind p \
   --cutName ${CUT2} \
   --variable ${PLOTVAR} \
   --structureFile ../${folder}/structure.py \
   --plotFile ../${folder}/plot_v2.py \
   --lumiText '35.87/fb' 

    # clean up local plotter folder
rm -r plot_combined/*

mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000

cp /eos/user/m/mpresill/www/VBS/2016_v7/index.php /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}/.
cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}/.
cp -r *combined.py /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${date}/${Category}/${CUT2}/${PLOTVAR}/.

#rm -r postfit_${CUT}_${FITVAR}fit
#mv plot_combined postfit_${CUT}_${FITVAR}fit

#cp -r postfit_${CUT}_${FITVAR}fit /e


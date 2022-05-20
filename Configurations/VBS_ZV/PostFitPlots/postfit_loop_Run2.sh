#!/bin/bash

    ##############################################################################################################
    #   TO RUN IT LAUNCH:
    #   sh postfit_loop_2017.sh date folder CATEGORY CUT VARIABLEtoPLOT
    #
    #   example: sh postfit_loop_2017.sh 11May2022_2017 2017_Apr22_v2 Resolved DYcr_bTag DNNoutput_pruned_bReq
    #
    #   note that the fitdiagnostic is automatically chosen as the full-year-combined in this script
    #
    ###############################################################################################################


Date2016=11May2022_2016
Date2017=11May2022_2017
Date2018=8Apr2022_2018

Category=Resolved
CUT=SR_bVeto
PLOTVAR=DNNoutput_pruned_bVeto_morebins


        # variable to plot
    #PLOTVAR=DNNoutput_pruned_bVeto_morebins         
    #PLOTVAR=DNNoutput_pruned_bReq #_morebins        
    #PLOTVAR=DYfit_Z_bin                             
    #PLOTVAR=DYfit_Z_bin                             
    #PLOTVAR=DNNoutput_pruned_bReq_morebins          
        # region to plot
    #CUT2=SR_bVeto                                   
    #CUT2=SR_bTag                                    
    #CUT2=DYcr_bVeto                                 
    #CUT2=DYcr_bTag                                  
    #CUT2=topcr                                      
        # Category
    #Category=Resolved
    #Category=Boosted

    #########################################################################
    #   combine the datacards of the signal regions we want to plot
    #
    #
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV

combineCards.py year2016=${DatacardPATH}/Datacards/Datacards_${Date2016}/${Category}_${CUT}/${PLOTVAR}/datacard.txt \
                year2017=${DatacardPATH}/Datacards/Datacards_${Date2017}/${Category}_${CUT}/${PLOTVAR}/datacard.txt \
                year2018=${DatacardPATH}/Datacards/Datacards_${Date2018}/${Category}_${CUT}/${PLOTVAR}/datacard.txt > datacardPLOT.txt

text2workspace.py datacardPLOT.txt -o datacardPLOT.root

    #########################################################################
    #   the fit is performed on all CRs and SRs of the three years, all categories
    #
    #
DATACARD_FIT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/YearsCombination_8Apr2022/combined_card_all_comb
echo "${DATACARD_FIT}"
#text2workspace.py ${DATACARD_FIT}.txt -o ${DATACARD_FIT}.root
#combine -M FitDiagnostics ${DATACARD_FIT}.root \
#        --out fitRun2 \
#        -t -1 --toysFreq --rMin -10 \
#        --saveNormalizations --saveWithUncertainties \
#        --expectSignal 1 --cminDefaultMinimizerStrategy 0 --robustFit=1
   

##############################################
##                                           #
##         pre / post-fit      plotting      #
##         (mjj, DNN, any var.)              #
##                                           #
##############################################
#
#########PostfitfromWorkspace
PostFitShapesFromWorkspace \
    -w datacardPLOT.root \
    -d datacardPLOT.txt \
    -o output_histogramsRUN2.root \
    --postfit --sampling \
    -f fitRun2/fitDiagnosticsTest.root:fit_s \
    --total-shapes

    # clean up local plotter folder
rm -r plot_combined/*

mkPostFitCombinedPlot.py \
   --inputFilePostFitShapesFromWorkspace output_histogramsRUN2.root \
   --outputFile output_postfit.root \
   --kind P \
   --cutName ${CUT} \
   --variable ${PLOTVAR} \
   --structureFile ../Run2/structure.py \
   --plotFile ../Run2/plot.py \
   --lumiText '138/fb' 
   
mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000

        #    create the folders where to backup files
mkdir -p /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_Run2_${Date2016}_${Date2017}_${Date2018}/${Category}/${CUT}/${PLOTVAR}
mkdir -p /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_Run2_${Date2016}_${Date2017}_${Date2018}/${Category}/${CUT}/${PLOTVAR}
cp /eos/user/m/mpresill/www/VBS/2017_v7/index.php /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_Run2_${Date2016}_${Date2017}_${Date2018}/${Category}/${CUT}/${PLOTVAR}/.
cp /eos/user/m/mpresill/www/VBS/2017_v7/index.php /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_Run2_${Date2016}_${Date2017}_${Date2018}/${Category}/${CUT}/${PLOTVAR}/.

cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_Run2_${Date2016}_${Date2017}_${Date2018}/${Category}/${CUT}/${PLOTVAR}/.

###################################################################
        ###      uncomment for prefit   ######
mkPostFitCombinedPlot.py \
   --inputFilePostFitShapesFromWorkspace output_histogramsRUN2.root \
   --outputFile output_postfit.root \
   --kind p \
   --cutName ${CUT} \
   --variable ${PLOTVAR} \
   --structureFile ../Run2/structure.py \
   --plotFile ../Run2/plot.py \
   --lumiText '138/fb' 

    # clean up local plotter folder
rm -r plot_combined/*

mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.1 --maxLogCratio=10000
cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_Run2_${Date2016}_${Date2017}_${Date2018}/${Category}/${CUT}/${PLOTVAR}/.

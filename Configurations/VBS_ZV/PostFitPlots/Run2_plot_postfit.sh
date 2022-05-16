#!/bin/bash


#############################################
#                                           #
#         pre / post-fit      plotting      #
#         (mjj, DNN, any var.)              #
#                                           #
#############################################

                ## select the datacard of the fit
#DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
#tag=8Apr2022          #this is a tag for the output folder for significances, impacts and post/pre-fit plots
                ## this is the full fit workspace
#combinedFIT=${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_card_all_comb
#text2workspace.py ${combinedFIT}.txt -o ${combinedFIT}.root             
#combine -M FitDiagnostics ${combinedFIT}.root --out fitDiagnosticsCombined --robustFit=1 --cminDefaultMinimizerStrategy 0 --rMin -10  -t -1 --toysFreq #--saveWithUncertainties --saveOverallShapes --plots --saveNormalizations


                ##  select the plotting variable and the plotting region
folder=2018_Apr22

lumi=59.74 #2017 is: 41.53 #2016 is: 35.87 #Full Run2 : 138

PLOTVAR=DYfit_2D_bin_Resolved 
#DYfit_Z_bin_Boosted #for 2017 and 2018 boosted
#DYfit_Z_bin #for 2016 boosted and resolved
#DNNoutput_pruned_bVeto #for top cr and sr
#DNNoutput_pruned_bReq #for top cr and sr

CUT=Resolved_SR_bVeto #Resolved_DYcr_bVeto #Resolved_DYcr_bTag #Boosted_DYcr_bVeto #Boosted_DYcr_bTag


#
DATACARD_PLOT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_8Apr2022_2018/bVeto_card_resolved_8Apr2022_2018
echo "datacard we want to plot: ${DATACARD_PLOT}"
text2workspace.py ${DATACARD_PLOT}.txt -o plotWorkspace.root         ### this is the plotting workspace

#######################################
##     PostfitfromWorkspace          ##
#######################################
PostFitShapesFromWorkspace \
    -w plotWorkspace.root \
    -o output_histograms.root \
    --postfit --sampling \
    -f fitDiagnosticsCombined/fitDiagnosticsTest.root:fit_s \
    --total-shapes


"""
#######################################
####      uncomment for postfit   #####
#######################################
mkPostFitCombinedPlot.py \
    --inputFilePostFitShapesFromWorkspace output_histograms.root \
    --outputFile output_postfit.root \
    --kind p \
    --cutName ${CUT} \
    --variable ${PLOTVAR} \
    --structureFile ../${folder}/structure.py \
    --plotFile ../${folder}/plot.py \
    --lumiText '${lumi}/fb' 


mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000

   #   back up to eos webpage
mkdir -p /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}
cp /eos/user/m/mpresill/www/VBS/2017_v7/index.php /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}/.
cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}/.
cp -r *combined.py /eos/user/m/mpresill/www/VBS/postfit/PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}/.


#######################################
####      uncomment for prefit   ######
#######################################
mkPostFitCombinedPlot.py \
    --inputFilePostFitShapesFromWorkspace output_histograms.root \
    --outputFile output_postfit.root \
    --kind p \
    --cutName ${CUT} \
    --variable ${PLOTVAR} \
    --structureFile ../${folder}/structure.py \
    --plotFile ../${folder}/plot.py \
    --lumiText '${lumi}/fb' 


mkPlot.py --pycfg=configuration_combined.py --inputFile=output_postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000


   #   back up to eos webpage
mkdir -p /eos/user/m/mpresill/www/VBS/prefit/PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}
cp /eos/user/m/mpresill/www/VBS/2017_v7/index.php /eos/user/m/mpresill/www/VBS/prefit//PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}/.
cp -r plot_combined/*png /eos/user/m/mpresill/www/VBS/prefit//PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}/.
cp -r *combined.py /eos/user/m/mpresill/www/VBS/prefit//PlotsVBS_ZV_${folder}_${PLOTVAR}_${CUT}/.

"""
#!/bin/bash
# combine model from Massiro: https://github.com/UniMiBAnalyses/D6EFTStudies 


DATE=21Oct2021_2018
year=2018_v7_2
CUT1=Boosted_SR_bVeto


##  to make datacard:
#cd ${year}
#mkDatacards.py --pycfg configuration.py --inputFile rootFile_${DATE}/plots_VBS_ZV_${DATE}.root 
#cd ..


#########################
# Looping on variables ##
#########################
declare -a StringArray=("VBS_jet_pt1" "VBS_jet_pt2" "V_jet_pt1" "V_jet_pt2" "mjj_max" "detajj_mjjmax"  )        #looping
for VAR in "${StringArray[@]}"; do   

VAR1=${VAR}
datacard=${year}/Datacards/_${DATE}/${CUT1}/${VAR1}/datacard


# create rootfit workspace from datacard
text2workspace.py  ${datacard}.txt \
    -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative \
    -o model_test.root \
    --X-allow-no-signal \
    --PO eftOperators=cT0,cT1,cT2,cT5,cT6,cT7,cT8,cT9


#text2workspace.py  2017_v7_2/Datacards/_31Sept2021_2017/Resolved_SR_bVeto_mjj500/mjj_max/datacard.txt -P HiggsAnalysis.AnalyticAnomalousCoupling.AnomalousCouplingEFTNegative:analiticAnomalousCouplingEFTNegative -o model_test.root --X-allow-no-signal --PO eftOperators=cT0,cT1


#########################
# Looping on operators ##
#########################
#declare -a StringArray=( "cT1" "cT2" "cT5" "cT6" "cT7" "cT8" "cT8" "cT9")      
#for OP in "${StringArray[@]}"; do                                      

OP=cT0
range=10

#######################################
#       run  for single operator:     #
#######################################    
#1. fit
combine -M MultiDimFit model_test.root \
    --algo=grid --points 2000 -m 125 -t -1 \
    --redefineSignalPOIs k_${OP} \
    --freezeParameters r,k_cT1,k_cT2,k_cT5,k_cT6,k_cT7,k_cT8,k_cT9,  \
    --setParameters r=1 \
    --setParameterRanges k_${OP}=-${range},${range} \
    --verbose -1
#2. plot the profile likelihood obtained
root -l -q  higgsCombineTest.MultiDimFit.mH125.root  \
        higgsCombineTest.MultiDimFit.mH125.root $CMSSW_BASE/src/HiggsAnalysis/AnalyticAnomalousCoupling/test/draw.cxx\(\"k_${OP}\"\)
#3. backup the plot to webpage
mkdir /eos/user/m/mpresill/www/VBS/EFTlimits/${year}_${DATE}_${CUT1}_${VAR1}
cp /eos/user/m/mpresill/www/VBS/EFTlimits/index.php /eos/user/m/mpresill/www/VBS/EFTlimits/${year}_${DATE}_${CUT1}_${VAR1}/.
cp ll.png /eos/user/m/mpresill/www/VBS/EFTlimits/${year}_${DATE}_${CUT1}_${VAR1}/${OP}.png

#######################################
#     run  for two operators a time:  #
####################################### 


#done  #end loop on operators

done  #end loop on variables
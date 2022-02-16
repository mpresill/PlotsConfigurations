#!/bin/bash

DATACARD_NAME=_L13000_M1000_sr              ### this is the name of the datacard
WEB_FOLDER=/eos/user/m/mpresill/www/VBS/    ### this the webfolder output
inputFOLDER=16-02-22                        ### path of the folder with datacard

#echo "RUNNING WITH TOP CR FIT"
outputFolder=histograms/${DATACARD_NAME} 
mkdir -p ${outputFolder}
cardName=${DATACARD_NAME}
cardNameWorkspace=${DATACARD_NAME}
#rm -rf ${cardNameWorkspace}.root

text2workspace.py ../${inputFOLDER}/${cardName}.txt -o ${cardNameWorkspace}.root




################################################################
####### calculating uncertainties by freezing nuisances ########
################################################################
    ## 1. Breakdown into stat. and syst.

    ## run postfit with all nuisances floating and store it in an output
combine ${cardNameWorkspace}.root -M MultiDimFit -t -1 --rMin -10 --rMax 10 --saveWorkspace -n ${CHANNEL}${DATACARD_NAME}.postfit
    ## run a scan from the postfit created
combine higgsCombine${CHANNEL}${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 -n ${CHANNEL}${DATACARD_NAME}.total --algo grid --snapshotName MultiDimFit 

    ## freeze theory unc.
combine higgsCombine${CHANNEL}${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups Theory -n ${CHANNEL}${DATACARD_NAME}.freeze_theory

    ## freeze all nuisances
combine higgsCombine${CHANNEL}${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --algo grid --snapshotName MultiDimFit \
    --freezeParameters allConstrainedNuisances -n ${CHANNEL}${DATACARD_NAME}.freeze_all

    ## plotting and copying to my webpage
plot1DScan.py higgsCombine${CHANNEL}${DATACARD_NAME}.total.MultiDimFit.mH120.root --main-label "Total Uncert."  \
    --others higgsCombine${CHANNEL}${DATACARD_NAME}.freeze_theory.MultiDimFit.mH120.root:"freeze theory":4 \
    higgsCombine${CHANNEL}${DATACARD_NAME}.freeze_all.MultiDimFit.mH120.root:"stat only":6  \
    -o freeze_th_exp_st --breakdown "theory,rest,stat"

cp freeze_th_exp_st.png ${WEB_FOLDER}/${inputFOLDER}/${CHANNEL}${DATACARD_NAME}_freeze_th_exp_st.png
cp freeze_th_exp_st.pdf ${WEB_FOLDER}/${inputFOLDER}/${CHANNEL}${DATACARD_NAME}_freeze_th_exp_st.pdf







#######################
    ## 2.  breakdown in several uncertainties

    ## run postfit with all nuisances floating and store it in an output
combine ${cardNameWorkspace}.root -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --saveWorkspace -n ${DATACARD_NAME}.postfit
    ## run a scan from the postfit created
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 -n ${DATACARD_NAME}.total --algo grid \
    --snapshotName MultiDimFit 


    ##  freezing lepton SFs
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups leptonSF -n ${DATACARD_NAME}.freeze_leptonSF

    ##  freezing JEC/JER
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups leptonSF,Jet -n ${DATACARD_NAME}.freeze_Jet

    ##  freezing PU 
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups leptonSF,Jet,PU -n ${DATACARD_NAME}.freeze_PU

    ##  freezing leptonEN 
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups leptonSF,Jet,PU,leptonEN -n ${DATACARD_NAME}.freeze_leptonEN


    ##  freezing TOP normalization  
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups leptonSF,Jet,PU,leptonEN,TOPnorm -n ${DATACARD_NAME}.freeze_TOPnorm

    ##  freezing DYestimate  
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups leptonSF,Jet,PU,leptonEN,TOPnorm,DYestimate -n ${DATACARD_NAME}.freeze_DYestimate

    ##  freezing theoretical uncertainties
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeNuisanceGroups leptonSF,Jet,PU,leptonEN,TOPnorm,DYestimate,Theory -n ${DATACARD_NAME}.freeze_Theory

    ##  freezing luminosity: we don't need to separate it, but if we want to add other splitting items, here is the way.
#combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
#    --freezeNuisanceGroups leptonSF,Jet,PU,leptonEN,TOPnorm,DYestimate,Theory,lumi -n ${DATACARD_NAME}.freeze_lumi


    ##  freezing all nuis: scan with all nuisances frozen (for the purely data-statistical component breakdown)
combine higgsCombine${DATACARD_NAME}.postfit.MultiDimFit.mH120.root \
    -M MultiDimFit -t -1 --rMin -10 --rMax 10 --cminDefaultMinimizerStrategy 0 --algo grid --snapshotName MultiDimFit \
    --freezeParameters allConstrainedNuisances -n ${DATACARD_NAME}.freeze_all


    ## plotting with different colours: overlay different likelihood scans with plot1DScan.py using the --others flag with arugment ‘root file:name:line colour’
plot1DScan.py higgsCombine${DATACARD_NAME}.total.MultiDimFit.mH120.root --main-label "Total uncert."  \
    --others higgsCombine${DATACARD_NAME}.freeze_leptonSF.MultiDimFit.mH120.root:"Freeze lepton SFs":3 \
    higgsCombine${DATACARD_NAME}.freeze_Jet.MultiDimFit.mH120.root:"Freeze JEC/R":4 \
    higgsCombine${DATACARD_NAME}.freeze_PU.MultiDimFit.mH120.root:"freeze PU":6 \
    higgsCombine${DATACARD_NAME}.freeze_leptonEN.MultiDimFit.mH120.root:"Freeze lepton en.":5 \
    higgsCombine${DATACARD_NAME}.freeze_TOPnorm.MultiDimFit.mH120.root:"Freeze TTtW norm.":10 \
    higgsCombine${DATACARD_NAME}.freeze_DYestimate.MultiDimFit.mH120.root:"Freeze DY estimate":7 \
    higgsCombine${DATACARD_NAME}.freeze_Theory.MultiDimFit.mH120.root:"Freeze theory":8 \
    higgsCombine${DATACARD_NAME}.freeze_all.MultiDimFit.mH120.root:"Stat only":2  \
    -o freeze_ALL_st --breakdown "leptonSF,Jet,PU,leptonEN,TOPnorm,DYestimate,Theory,Rest,Stat"
#higgsCombine${DATACARD_NAME}.freeze_lumi.MultiDimFit.mH120.root:"Freeze luminosity":9 \
    
cp freeze_ALL_st.png ${WEB_FOLDER}/${inputFOLDER}/${DATACARD_NAME}_FullBreakdown.png
cp freeze_ALL_st.pdf ${WEB_FOLDER}/${inputFOLDER}/${DATACARD_NAME}_FullBreakdown.pdf

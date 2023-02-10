#!/bin/bash

tag=13Jan2023
cd ../tmp
#text2workspace.py combinedFIT.txt -o impactWorkspace.root
             #################################################
              #                                               #
              #            uncertainty breakdown              #
              #                                               #
              #################################################
    ## run postfit with all nuisances floating and store it in an output
#cp ${inputCard}.root impactWorkspace.root

#combine impactWorkspace.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --saveWorkspace -n impactWorkspace.total --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0
#    #### theory
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory -n impactWorkspace.freeze_theory
#    ##### DYnorm
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm -n impactWorkspace.freeze_DYnorm
#    #### Topnorm
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm -n impactWorkspace.freeze_Topnorm
#    ### AK4
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet -n impactWorkspace.freeze_AK4jet
#    ### AK8
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet -n impactWorkspace.freeze_AK8jet
#    ### LEPTON
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton -n impactWorkspace.freeze_lepton
#    ### PU
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU -n impactWorkspace.freeze_PU
#    ### LUMI
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi -n impactWorkspace.freeze_lumi
#    ### FAKE
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake -n impactWorkspace.freeze_fake
#    ### TRIGGER
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger -n impactWorkspace.freeze_trigger
#
#    ### ALL
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0 \
#        --freezeParameters allConstrainedNuisances -n impactWorkspace.freeze_all
#
#
#    ## plotting and copying to my webpage
#plot1DScan.py higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root --main-label "Total Uncert."  \
#    --others \
#    'higgsCombineimpactWorkspace.freeze_theory.MultiDimFit.mH120.root:Freeze theory:600' \
#    'higgsCombineimpactWorkspace.freeze_DYnorm.MultiDimFit.mH120.root:Freeze DYnorm:920' \
#    'higgsCombineimpactWorkspace.freeze_Topnorm.MultiDimFit.mH120.root:Freeze Topnorm:416' \
#    'higgsCombineimpactWorkspace.freeze_AK4jet.MultiDimFit.mH120.root:Freeze AK4jet:400' \
#    'higgsCombineimpactWorkspace.freeze_AK8jet.MultiDimFit.mH120.root:Freeze AK8jet:616' \
#    'higgsCombineimpactWorkspace.freeze_lepton.MultiDimFit.mH120.root:Freeze lepton:432' \
#    'higgsCombineimpactWorkspace.freeze_PU.MultiDimFit.mH120.root:Freeze PU:800' \
#    'higgsCombineimpactWorkspace.freeze_lumi.MultiDimFit.mH120.root:Freeze lumi:820' \
#    'higgsCombineimpactWorkspace.freeze_fake.MultiDimFit.mH120.root:Freeze fake:840' \
#    'higgsCombineimpactWorkspace.freeze_trigger.MultiDimFit.mH120.root:Freeze trigger:860' \
#    'higgsCombineimpactWorkspace.freeze_all.MultiDimFit.mH120.root:Freeze all:840' \
#    -o freeze_th_exp_st \
#    --breakdown "theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger,rest,stat"
#
#cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/TEST-2016_boosted.png
#cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/TEST-2016_boosted.pdf



    #############################
    #### Splitting in  Rate Param, theory, MCstat, Experimental, data stat
    #############################

combine -M MultiDimFit impactWorkspace.root --toysFrequentist -t -1 --expectSignal=1 -m 120 --algo grid --points 30 --saveWorkspace -n impactWorkspace.total --rMin -0.5 --rMax 2.5
    #### nominal
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
        --snapshotName MultiDimFit -n impactWorkspace.nominal 
    ### ALL (non-floating nuisances)
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
        --freezeParameters allConstrainedNuisances --snapshotName MultiDimFit -n impactWorkspace.freeze_all

    ##### DYnorm
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
        --freezeNuisanceGroups DYnorm,Topnorm --snapshotName MultiDimFit -n impactWorkspace.freeze_RateParams 

    #### theory
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
        --freezeNuisanceGroups DYnorm,Topnorm,theory --snapshotName MultiDimFit -n impactWorkspace.freeze_theory 

    ### autoMCstats
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
        --freezeNuisanceGroups DYnorm,Topnorm,theory,autoMCStats  --snapshotName MultiDimFit -n impactWorkspace.freeze_MCstat

    ## plotting and copying to my webpage
plot1DScan.py higgsCombineimpactWorkspace.nominal.MultiDimFit.mH120.root --main-label "Total Uncert. (Asimov)"  \
    --others \
    'higgsCombineimpactWorkspace.freeze_RateParams.MultiDimFit.mH120.root:Freeze RateParams:920' \
    'higgsCombineimpactWorkspace.freeze_theory.MultiDimFit.mH120.root:Freeze RateParams+theory:600' \
    'higgsCombineimpactWorkspace.freeze_MCstat.MultiDimFit.mH120.root:Freeze RateParams+theory+MCstat:416' \
    'higgsCombineimpactWorkspace.freeze_all.MultiDimFit.mH120.root:Freeze all:632' \
    -o freeze_th_exp_st \
    --breakdown "RateParams,theory,MCstat,Exp,stat"

cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}.png
cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}.pdf



    ### further split for "Exp"
    ### AK4 jets related uncertainties
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups AK4jet  --snapshotName MultiDimFit -n impactWorkspace.freeze_AK4jet
#
#    ### AK8 jets related uncertainties
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups AK4jet,AK8jet  --snapshotName MultiDimFit -n impactWorkspace.freeze_AK8jet
#
#    ### lepton related uncertainties
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --expectSignal=1 -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups AK4jet,AK8jet,lepton  --snapshotName MultiDimFit -n impactWorkspace.freeze_lepton


#    ## plotting and copying to my webpage
#plot1DScan.py higgsCombineimpactWorkspace.freeze_MCstat.MultiDimFit.mH120.root --main-label "Total Exp Uncert. (Asimov)"  \
#    --others \
#    'higgsCombineimpactWorkspace.freeze_AK4jet.MultiDimFit.mH120.root:Freeze AK4 jet:416' \
#    'higgsCombineimpactWorkspace.freeze_AK8jet.MultiDimFit.mH120.root:Freeze AK4 jet + AK8 jet:416' \
#    'higgsCombineimpactWorkspace.freeze_lepton.MultiDimFit.mH120.root:Freeze AK4 jet + AK8 jet + lepton:416' \
#    'higgsCombineimpactWorkspace.freeze_all.MultiDimFit.mH120.root:Freeze all:632' \
#    -o freeze_th_exp_st \
#    --breakdown "Ak4jet,AK8jet,lepton,rest,stat"
##    'higgsCombineimpactWorkspace.freeze_MCstat.MultiDimFit.mH120.root:Freeze RateParams+theory+MCstat:416' \
##    'higgsCombineimpactWorkspace.freeze_theory.MultiDimFit.mH120.root:Freeze RateParams+theory:600' \
##    'higgsCombineimpactWorkspace.freeze_RateParams.MultiDimFit.mH120.root:Freeze RateParams:920' \
#
#cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}_Exp_splitting.png
#cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}_Exp_splitting.pdf




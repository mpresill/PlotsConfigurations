#!/bin/bash

tag=13Jan2023


cd ../tmp #created this temporary folder to aovoid issues with the eos path in the workspace produced

cp -r /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/YearsCombination_${tag}/combined_*.txt .

combineCards.py combined_boosted_bVeto.txt \
                combined_boosted_bTag.txt \
                combined_resolved_bVeto.txt \
                combined_resolved_bTag.txt > combinedFIT.txt

#combinedFIT=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/YearsCombination_${tag}/combined_card_all_comb
fitDiagFOLDER=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/YearsCombination_${tag}

text2workspace.py combinedFIT.txt -o impactWorkspace.root


#############################################
#                                           #
#         impact plots blind                #
#                                           #
#############################################

outputFolder=${fitDiagFOLDER}
mkdir -p ${fitDiagFOLDER}

combine -M FitDiagnostics -d impactWorkspace.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0 --cminDefaultMinimizerStrategy=0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0

combine -M FitDiagnostics -d impactWorkspace.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1 --cminDefaultMinimizerStrategy=0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1

combineTool.py -M Impacts -d impactWorkspace.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d impactWorkspace.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10

combineTool.py -M Impacts -d impactWorkspace.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d impactWorkspace.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10

combineTool.py -M Impacts -d impactWorkspace.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
combineTool.py -M Impacts -d impactWorkspace.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10
plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  impacts_t0
plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  impacts_t1
cp impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/YearsCombination_${tag}_impacts_t0.pdf
cp impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/YearsCombination_${tag}_impacts_t1.pdf
cp impacts_t0.pdf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/YearsCombination_${tag}/.
cp impacts_t1.pdf /eos/user/m/mpresill/CMS/VBS/VBS_ZV/fit/YearsCombination_${tag}/.



#############################################
#                                           #
#            DIFF NUISANCES                 #
#           PRE/POST FIT YIELDS             #
#                                           #
#############################################
combine -M FitDiagnostics impactWorkspace.root \
        --out ${fitDiagFOLDER} \
        -t -1 --toysFreq --robustFit=1 --rMin -10 \
        --cminDefaultMinimizerStrategy 0 \
        --saveNormalizations --saveWithUncertainties

python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html ${fitDiagFOLDER}//fitDiagnosticsTest.root > ${fitDiagFOLDER}/fit_YearsCombination_${tag}.html
cp ${fitDiagFOLDER}/fit_YearsCombination_${tag}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 

python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/mlfitNormsToText.py ${fitDiagFOLDER}/fitDiagnosticsTest.root > ${fitDiagFOLDER}/postfit_YearsCombination_${tag}_norm.txt
cp ${fitDiagFOLDER}/postfit_YearsCombination_${tag}_norm.txt /eos/user/m/mpresill/www/VBS/diffNuisances/. 



#################################################
#                                               #
#            uncertainty breakdown              #
#                                               #
#################################################
#    ## run postfit with all nuisances floating and store it in an output
#
#combine impactWorkspace.root -M MultiDimFit -t -1 -m 120 --points 100 --saveWorkspace -n ZV_ewk.total --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0
#    ##### DYnorm
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm -n ZV_ewk.freeze_DYnorm
#    #### Topnorm
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm -n ZV_ewk.freeze_Topnorm
#    #### theory
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory -n ZV_ewk.freeze_theory
#    ### AK4
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory,AK4jet -n ZV_ewk.freeze_AK4jet
#    ### AK8
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory,AK4jet,AK8jet -n ZV_ewk.freeze_AK8jet
#    ### LEPTON
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory,AK4jet,AK8jet,lepton -n ZV_ewk.freeze_lepton
#    ### PU
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory,AK4jet,AK8jet,lepton,PU -n ZV_ewk.freeze_PU
#    ### LUMI
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory,AK4jet,AK8jet,lepton,PU,lumi -n ZV_ewk.freeze_lumi
#    ### FAKE
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory,AK4jet,AK8jet,lepton,PU,lumi,fake -n ZV_ewk.freeze_fake
#    ### TRIGGER
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 100 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups DYnorm,Topnorm,theory,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger -n ZV_ewk.freeze_trigger
#
#    ### ALL
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 1000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0 \
#        --freezeParameters allConstrainedNuisances -n ZV_ewk.freeze_all
#
#
#    ## plotting and copying to my webpage
#plot1DScan.py higgsCombineZV_ewk.total.MultiDimFit.mH120.root --main-label "Total Uncert."  \
#    --others \
#    'higgsCombineZV_ewk.freeze_DYnorm.MultiDimFit.mH120.root:Freeze DYnorm:920' \
#    'higgsCombineZV_ewk.freeze_Topnorm.MultiDimFit.mH120.root:Freeze Topnorm:416' \
#    'higgsCombineZV_ewk.freeze_theory.MultiDimFit.mH120.root:Freeze theory:600' \
#    'higgsCombineZV_ewk.freeze_AK4jet.MultiDimFit.mH120.root:Freeze AK4jet:400' \
#    'higgsCombineZV_ewk.freeze_AK8jet.MultiDimFit.mH120.root:Freeze AK8jet:616' \
#    'higgsCombineZV_ewk.freeze_lepton.MultiDimFit.mH120.root:Freeze lepton:432' \
#    'higgsCombineZV_ewk.freeze_PU.MultiDimFit.mH120.root:Freeze PU:800' \
#    'higgsCombineZV_ewk.freeze_lumi.MultiDimFit.mH120.root:Freeze lumi:820' \
#    'higgsCombineZV_ewk.freeze_fake.MultiDimFit.mH120.root:Freeze fake:840' \
#    'higgsCombineZV_ewk.freeze_trigger.MultiDimFit.mH120.root:Freeze trigger:860' \
#    'higgsCombineZV_ewk.freeze_all.MultiDimFit.mH120.root:Freeze all:840' \
#    -o freeze_th_exp_st \
#    --breakdown "DYnorm,Topnorm,theory,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger,rest,stat"
#
#cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_nuisances_breakdown_${tag}.pdf
#cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_nuisances_breakdown_${tag}.png


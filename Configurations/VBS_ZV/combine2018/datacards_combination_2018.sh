#!/bin/bash
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance
Date2018=13Sep2022_2018

mkdir -p ${SigPATH}/${Date2018}

CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted
SR1_var=DNNoutput_pruned_bVeto_morebins   #DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq_morebins   #DNNoutput_pruned_bReq

TOPcr1_var=DNNoutput_pruned_bVeto_morebins
TOPcr2_var=DNNoutput_pruned_bReq_morebins


cutDY1=DYcr_bVeto
cutSR1=SR_bVeto

cutDY2=DYcr_bTag
cutSR2=SR_bTag


tag=ANv5            #thi is the state the version of the test

########################################################################################
                #### B-TAG BOOSTED
combineCards.py boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${TOPcr1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_boosted_${Date2018}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_boosted_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/boosted_bVeto_${tag}.txt 

                #### B-VETO BOOSTED
combineCards.py boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_boosted_${Date2018}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_boosted_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/boosted_bTag_${tag}.txt 

                #### COMBINATION BOOSTED 2018
combineCards.py boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${TOPcr1_var}/datacard.txt \
                boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}.txt
echo "======================================="
echo "produced boosted cat. 2018 card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/boosted_comb_${tag}.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2018}/boosted_comb.txt 

########################################################################
                #### B-TAG RESOLVED
combineCards.py resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${TOPcr1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_resolved_${Date2018}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_resolved_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/resolved_bVeto_${tag}.txt 

                #### B-VETO RESOLVED
combineCards.py resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_resolved_${Date2018}.txt
                
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_resolved_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/resolved_bTag_${tag}.txt 

                #### COMBINATION RESOLVED 2018
combineCards.py resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_${Date2018}.txt
echo "======================================="
echo "produced resolved cat. 2018 card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_${Date2018}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/resolved_comb_${tag}.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2018}/resolved_comb.txt 




#####################################################################
############# CATEGORIES COMBINATION 2018 
combineCards.py resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${TOPcr2_var}/datacard.txt \
                boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${TOPcr1_var}/datacard.txt \
                boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt
echo "======================================="
echo "produced 2018 combined card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/comb_${tag}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt -t -1 --expectSignal=1 --toysFreq &> ${SigPATH}/${Date2018}/comb_${tag}_toysFreq.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2018}/comb.txt 



             #################################################
              #                                               #
              #   doing the fit for the whole year combined   #
              #                                               #
              #################################################
#text2workspace.py ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt -o ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.root
#mkdir -p ${DatacardPATH}/fit/${Date2018}
#              ########     fit
#              ## -t -1 --expectSignal 0   -> this is for t0 Asimov, b-only
#              ## -t -1 --expectSignal 1   -> this is for t1 Asimov, s+b
#combine -M FitDiagnostics ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.root \
#        --out ${DatacardPATH}/fit/${Date2018} \
#        -t -1 --toysFreq --robustFit=1 --rMin -10 \
#        --cminDefaultMinimizerStrategy 0 \
#        --saveNormalizations --saveWithUncertainties  #--saveOverallShapes --plots --numToysForShapes 200 #-v 2 # --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 --plots #--algo impact -P parameter #--cminDefaultMinimizerStrategy 1 # --robustHesse 1 #--X-rtd MINIMIZER_analytic #--robustHesse 1 # --forceRecreateNLL --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL #--robustFit=1 --cminDefaultMinimizerStrategy 0 #--minos all #--cminDefaultMinimizerTolerance 0.1 --minos poi 
#
#echo " card path for impacts "
#echo " " ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.root
#echo " fitDiagnostic folder for plotting "
#echo " "  ${DatacardPATH}/fit/${Date2018}
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html ${DatacardPATH}/fit/${Date2018}/fitDiagnosticsTest.root > fit_${Date2018}.html
#cp fit_${Date2018}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 
#
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/mlfitNormsToText.py ${DatacardPATH}/fit/${Date2018}/fitDiagnosticsTest.root > postfit_${Date2018}_norm.txt
#cp postfit_${Date2018}_norm.txt /eos/user/m/mpresill/www/VBS/diffNuisances/. 


              ########################################################
              #                                                      #
              #   runnning impact plots on the whole year combined   #
              #                                                      #
              ########################################################
inputCard=${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}
#inputCard=${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}


text2workspace.py ${inputCard}.txt ${inputCard}.root

outputFolder=${DatacardPATH}/Datacards/Datacards_${Date2018}/impacts
mkdir -p ${outputFolder}

combine -M FitDiagnostics -d ${inputCard}.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0 --cminDefaultMinimizerStrategy=0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0

combine -M FitDiagnostics -d ${inputCard}.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1 --cminDefaultMinimizerStrategy=0
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1

combineTool.py -M Impacts -d ${inputCard}.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d ${inputCard}.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10

combineTool.py -M Impacts -d ${inputCard}.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10
combineTool.py -M Impacts -d ${inputCard}.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10

combineTool.py -M Impacts -d ${inputCard}.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
combineTool.py -M Impacts -d ${inputCard}.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10
plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  impacts_t0
plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  impacts_t1
cp impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${Date2018}_impacts_t0_${tag}.pdf
cp impacts_t0.pdf ${SigPATH}/${Date2018}/impacts_t0_${tag}.pdf
cp impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${Date2018}_impacts_t1_${tag}.pdf
cp impacts_t1.pdf ${SigPATH}/${Date2018}/impacts_t1_${tag}.pdf



             #################################################
              #                                               #
              #            uncertainty breakdown              #
              #                                               #
              #################################################
#
#    ## 2.  breakdown in several uncertainties. 
#    ##     N.b. be carefull on the --rMin and --rMax values you are using, they do not have to be too loose.
#
#    ## run postfit with all nuisances floating and store it in an output
#rm -rf local.root
#cp ${inputCard}.root local.root 
#combine local.root -M MultiDimFit --rMin -1 --rMax 1  --saveWorkspace -n 2018.postfit
#    ## run a scan from the postfit created
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  -n 2018.total --algo grid \
#    --points 200 \
#    --snapshotName MultiDimFit 
#
##    ##  freezing DY normalization  
##combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
##    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
##    --points 200 \
##    --freezeNuisanceGroups DYnorm -n 2018.freeze_DYnorm
##
##     ##  freezing TOP normalization  
##combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
##    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
##    --points 200 \
##    --freezeNuisanceGroups DYnorm,TOPnorm -n 2018.freeze_TOPnorm
##
#    ##  freezing theory  
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeNuisanceGroups theory -n 2018.freeze_theory
#
#    ##  freezing AK4 jet
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeNuisanceGroups theory,AK4jet -n 2018.freeze_AK4jet
# 
#    ##  freezing AK8 jet 
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeNuisanceGroups theory,AK4jet,AK8jet -n 2018.freeze_AK8jet
#
#    ##  freezing lepton Scale and Efficiency
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeNuisanceGroups theory,AK4jet,AK8jet,lepton -n 2018.freeze_lepton
#
#    ##  freezing PU
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeNuisanceGroups theory,AK4jet,AK8jet,lepton,PU -n 2018.freeze_PU
#
#    ##  freezing luminosity
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \ 
#    --freezeNuisanceGroups theory,AK4jet,AK8jet,lepton,PU,lumi -n 2018.freeze_lumi
#
#    ##  freezing fake 
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeNuisanceGroups theory,AK4jet,AK8jet,lepton,PU,lumi,fake -n 2018.freeze_fake
#
#    ##  freezing trigger
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeNuisanceGroups theory,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger -n 2018.freeze_trigger
#
#    ##  freezing all nuis: scan with all nuisances frozen (for the purely data-statistical component breakdown)
#combine higgsCombine2018.postfit.MultiDimFit.mH120.root \
#    -M MultiDimFit --rMin -1 --rMax 1  --algo grid --snapshotName MultiDimFit \
#    --points 200 \
#    --freezeParameters allConstrainedNuisances -n 2018.freeze_all
#
#
#    ## plotting with different colours: overlay different likelihood scans with plot1DScan.py using the --others flag with arugment ‘root file:name:line colour’
#plot1DScan.py higgsCombine2018.total.MultiDimFit.mH120.root --main-label "Total uncert." \
#    --others \
#    higgsCombine2018.freeze_theory.MultiDimFit.mH120.root:"Freeze theory":10 \
#    higgsCombine2018.freeze_AK4jet.MultiDimFit.mH120.root:"Freeze AK4 JEC/R, b-tag":4 \
#    higgsCombine2018.freeze_AK8jet.MultiDimFit.mH120.root:"freeze AK8 jet systematics":6 \
#    higgsCombine2018.freeze_lepton.MultiDimFit.mH120.root:"Freeze lepton SFs and momentum scales":3 \
#    higgsCombine2018.freeze_PU.MultiDimFit.mH120.root:"Freeze PU":9 \
#    higgsCombine2018.freeze_lumi.MultiDimFit.mH120.root:"Freeze luminosity":5 \
#    higgsCombine2018.freeze_fake.MultiDimFit.mH120.root:"Freeze fakes systematics":8 \
#    higgsCombine2018.freeze_trigger.MultiDimFit.mH120.root:"Freeze trigger systematics":2 \
#    higgsCombine2018.freeze_all.MultiDimFit.mH120.root:"Stat only":2  \
#    -o freeze_ALL_st --breakdown theory,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger,BinByBin,Stat
##   higgsCombine2018.freeze_TOPnorm.MultiDimFit.mH120.root:"Freeze top rate":6 \
##   higgsCombine2018.freeze_DYnorm.MultiDimFit.mH120.root:"Freeze DY rate":7 \
##    higgsCombine2018.freeze_DYestimate.MultiDimFit.mH120.root:"Freeze DY estimate":7 \
#    
##cp freeze_ALL_st.png /eos/user/m/mpresill/www/HN/postCWR_eejjM500.png #impacts/${inputFOLDER}/${inputCard}_breakdown_FreezeLumi_4July_DYsplit.png
#cp freeze_ALL_st.pdf  /eos/user/m/mpresill/www/VBS/impacts/${Date2018}_nuisances_breakdown_${tag}.pdf #impacts/${inputFOLDER}/${inputCard}_breakdown_FreezeLumi_4July_DYsplit.pdf

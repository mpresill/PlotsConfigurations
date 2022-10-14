#!/bin/bash
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance
Date2016=12Sep2022_2016

mkdir -p ${SigPATH}/${Date2016}

CR_var_res=DYfit_Z_bin
CR_var_boost=DYfit_Z_bin
SR1_var=DNNoutput_pruned_bVeto #_morebins   #DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq #_impacts_t1_morebins   #DNNoutput_pruned_bReq
cutDY1=DYcr_bVeto
cutSR1=SR_bVeto
cutDY2=DYcr_bTag
cutSR2=SR_bTag

#TOPcr1_var=events
#TOPcr2_var=events
TOPcr1_var=DNNoutput_pruned_bVeto 
TOPcr2_var=DNNoutput_pruned_bReq

tag=ANv5     

#######################################################################################
                #### B-veto BOOSTED
combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${TOPcr1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_boosted_${Date2016}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_boosted_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_bVeto_${tag}.txt 

                #### B-tag BOOSTED
combineCards.py boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_boosted_${Date2016}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_boosted_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_bTag_${tag}.txt 

                #### COMBINATION BOOSTED 2016
combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${TOPcr1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt
echo "======================================="
echo "produced boosted cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_comb_${tag}.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/boosted_comb.txt 

########################################################################
                #### B-TAG RESOLVED
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${TOPcr1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_resolved_${Date2016}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_resolved_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_bVeto_${tag}.txt 

                #### B-VETO RESOLVED
combineCards.py resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_resolved_${Date2016}.txt
                
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_resolved_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_bTag_${tag}.txt 

                #### COMBINATION RESOLVED 2016
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt
echo "======================================="
echo "produced resolved cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_comb_${tag}.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/resolved_comb.txt 




#####################################################################
############# CATEGORIES COMBINATION 2016 
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${TOPcr1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${TOPcr2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt
                
echo "======================================="
echo "produced 2016 combined card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/comb_${tag}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt -t -1  --expectSignal=1 --toysFreq &> ${SigPATH}/${Date2016}/comb_${tag}_toysFreq.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/comb.txt 


              #################################################
              #   doing the fit for the whole year combined   #
              #################################################
#text2workspace.py ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt -o ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.root
#mkdir -p ${DatacardPATH}/fit/${Date2016}
#              ########     fit
#              ## -t -1 --expectSignal 0   -> this is for t0 Asimov, b-only
#              ## -t -1 --expectSignal 1   -> this is for t1 Asimov, s+b
#combine -M FitDiagnostics ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.root \
#        --out ${DatacardPATH}/fit/${Date2016} \
#        -t -1 --toysFreq --rMin -10 \
#        --expectSignal=1 \
#        --saveNormalizations --saveWithUncertainties  #\
#        #        --cminDefaultMinimizerStrategy 0 --robustFit=1  \
#        #--saveOverallShapes --plots --numToysForShapes 200 #-v 2 # --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 --plots #--algo impact -P parameter #--cminDefaultMinimizerStrategy 1 # --robustHesse 1 #--X-rtd MINIMIZER_analytic #--robustHesse 1 # --forceRecreateNLL --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL #--robustFit=1 --cminDefaultMinimizerStrategy 0 #--minos all #--cminDefaultMinimizerTolerance 0.1 --minos poi 
#
#
#echo " card path for impacts "
#echo " " ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.root
#echo " fitDiagnostic folder for plotting "
#echo " "  ${DatacardPATH}/fit/${Date2016}
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html ${DatacardPATH}/fit/${Date2016}/fitDiagnosticsTest.root > fit_${Date2016}.html
#cp fit_${Date2016}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 
#
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/mlfitNormsToText.py ${DatacardPATH}/fit/${Date2016}/fitDiagnosticsTest.root > postfit_${Date2016}_norm.txt
#cp postfit_${Date2016}_norm.txt /eos/user/m/mpresill/www/VBS/diffNuisances/. 
#
#
#              ########################################################
#              #                                                      #
#              #   runnning impact plots on the whole year combined   #
#              #                                                      #
#              ########################################################
inputCard=${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}
#inputCard=${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}
text2workspace.py ${inputCard}.txt ${inputCard}.root

outputFolder=${DatacardPATH}/Datacards/Datacards_${Date2016}/impacts
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
cp impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${Date2016}_impacts_t0_${tag}.pdf
cp impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${Date2016}_impacts_t1_${tag}.pdf
cp impacts_t0.pdf ${SigPATH}/${Date2016}/impacts_t0_${tag}.pdf
cp impacts_t1.pdf ${SigPATH}/${Date2016}/impacts_t1_${tag}.pdf

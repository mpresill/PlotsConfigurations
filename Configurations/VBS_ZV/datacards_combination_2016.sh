#!/bin/bash
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance
Date2016=11May2022_2016

mkdir -p ${SigPATH}/${Date2016}

CR_var_res=DYfit_Z_bin
CR_var_boost=DYfit_Z_bin
SR1_var=DNNoutput_pruned_bVeto_morebins   #DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq_morebins   #DNNoutput_pruned_bReq
cutDY1=DYcr_bVeto
cutSR1=SR_bVeto
cutDY2=DYcr_bTag
cutSR2=SR_bTag

########################################################################################
                #### B-TAG BOOSTED
combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_boosted_${Date2016}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_boosted_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_bVeto.txt 

                #### B-VETO BOOSTED
combineCards.py boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_boosted_${Date2016}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_boosted_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_bTag.txt 

                #### COMBINATION BOOSTED 2016
combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt
echo "======================================="
echo "produced boosted cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_comb.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/boosted_comb.txt 

########################################################################
                #### B-TAG RESOLVED
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_resolved_${Date2016}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bVeto_card_resolved_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_bVeto.txt 

                #### B-VETO RESOLVED
combineCards.py resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_resolved_${Date2016}.txt
                
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/bTag_card_resolved_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_bTag.txt 

                #### COMBINATION RESOLVED 2016
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt
echo "======================================="
echo "produced resolved cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_comb.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/resolved_comb.txt 




#####################################################################
############# CATEGORIES COMBINATION 2016 
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt
                
echo "======================================="
echo "produced 2016 combined card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/comb.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/comb.txt 


              #################################################
              #   doing the fit for the whole year combined   #
              #################################################
text2workspace.py ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt -o ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.root
mkdir -p ${DatacardPATH}/fit/${Date2016}
              ########     fit
              ## -t -1 --expectSignal 0   -> this is for t0 Asimov, b-only
              ## -t -1 --expectSignal 1   -> this is for t1 Asimov, s+b
combine -M FitDiagnostics ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.root \
        --out ${DatacardPATH}/fit/${Date2016} \
        -t -1 --toysFreq --rMin -10 \
        --expectSignal=1 \
        --saveNormalizations --saveWithUncertainties  #\
        #        --cminDefaultMinimizerStrategy 0 --robustFit=1  \
        #--saveOverallShapes --plots --numToysForShapes 200 #-v 2 # --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 --plots #--algo impact -P parameter #--cminDefaultMinimizerStrategy 1 # --robustHesse 1 #--X-rtd MINIMIZER_analytic #--robustHesse 1 # --forceRecreateNLL --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL #--robustFit=1 --cminDefaultMinimizerStrategy 0 #--minos all #--cminDefaultMinimizerTolerance 0.1 --minos poi 


echo " card path for impacts "
echo " " ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.root
echo " fitDiagnostic folder for plotting "
echo " "  ${DatacardPATH}/fit/${Date2016}
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html ${DatacardPATH}/fit/${Date2016}/fitDiagnosticsTest.root > fit_${Date2016}.html
cp fit_${Date2016}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 
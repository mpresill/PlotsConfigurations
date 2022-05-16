#!/bin/bash
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance
Date2018=8Apr2022_2018

mkdir -p ${SigPATH}/${Date2018}

CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted
SR1_var=DNNoutput_pruned_bVeto_morebins   #DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq_morebins   #DNNoutput_pruned_bReq

cutDY1=DYcr_bVeto
cutSR1=SR_bVeto

cutDY2=DYcr_bTag
cutSR2=SR_bTag

########################################################################################
                #### B-TAG BOOSTED
combineCards.py boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_boosted_${Date2018}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_boosted_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/boosted_bVeto.txt 

                #### B-VETO BOOSTED
combineCards.py boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_boosted_${Date2018}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_boosted_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/boosted_bTag.txt 

                #### COMBINATION BOOSTED 2018
combineCards.py boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}.txt
echo "======================================="
echo "produced boosted cat. 2018 card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/boosted_comb.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2018}/boosted_comb.txt 

########################################################################
                #### B-TAG RESOLVED
combineCards.py resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_resolved_${Date2018}.txt

combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bVeto_card_resolved_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/resolved_bVeto.txt 

                #### B-VETO RESOLVED
combineCards.py resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_resolved_${Date2018}.txt
                
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/bTag_card_resolved_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/resolved_bTag.txt 

                #### COMBINATION RESOLVED 2018
combineCards.py resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_${Date2018}.txt
echo "======================================="
echo "produced resolved cat. 2018 card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_${Date2018}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/resolved_comb.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2018}/resolved_comb.txt 




#####################################################################
############# CATEGORIES COMBINATION 2018 
combineCards.py resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt \
                boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt
echo "======================================="
echo "produced 2018 combined card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2018}/comb.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2018}/comb.txt 

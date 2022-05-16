#!/bin/bash
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance
Date2016=8Apr2022_2016
Date2017=8Apr2022_2017
Date2018=8Apr2022_2018

CR_var_res=DYfit_Z_bin
CR_var_boost=DYfit_Z_bin
SR1_var=DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq
cutDY1=DYcr_bVeto
cutSR1=SR_bVeto
cutDY2=DYcr_bTag
cutSR2=SR_bTag

########################################################################################
#################           #         ###   
#################         # #        #   
#################       #   #       #   
#################           #       #####
#################           #       #   #
#################           #        ###
########################################################################################
############# BOOSTED CATEGORY 2016
combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt
echo "======================================="
echo "produced boosted cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_boosted_comb_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_boosted_comb_${Date2016}.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/significance_boosted_comb_${Date2016}.txt 
############# RESOLVED CATEGORY 2016
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt
echo "======================================="
echo "produced resolved cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_resolved_comb_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_resolved_comb_${Date2016}.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/significance_resolved_comb_${Date2016}.txt 
############# COMBINATION 2016 
combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt \
                resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR2_var}/datacard.txt> ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt
echo "======================================="
echo "produced 2016 combined card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_${Date2016}.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_comb_${Date2016}.txt 
echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/significance_comb_${Date2016}.txt 
########################################################################################
#################           #      #######   
#################         # #            #
#################       #   #           #
#################           #          #
#################           #          #
#################           #          #
########################################################################################
CR_var_res_2017=DYfit_2D_bin_Resolved
CR_var_boost_2017=DYfit_Z_bin_Boosted
############# BOOSTED CATEGORY 2017
combineCards.py boosted_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY1}/${CR_var_boost_2017}/datacard.txt \
                boosted_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY2}/${CR_var_boost_2017}/datacard.txt \
                boosted_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_boosted_comb_2017.txt
echo "======================================="
echo "produced boosted cat. 2017 card:" ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_boosted_comb_2017.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_boosted_comb_${Date2017}.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_boosted_comb_${Date2017}.txt 
echo "whose significance (blind) is here: " ${SigPATH}/significance_boosted_comb_${Date2017}.txt 
############# RESOLVED CATEGORY 2017
combineCards.py resolved_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY1}/${CR_var_res_2017}/datacard.txt \
                resolved_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY2}/${CR_var_res_2017}/datacard.txt  \
                resolved_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_resolved_comb_2017.txt
echo "======================================="
echo "produced resolved cat. 2017 card:" ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_resolved_comb_${Date2017}.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_resolved_comb_2017.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_resolved_comb_${Date2017}.txt 
echo "whose significance (blind) is here: " ${SigPATH}/significance_resolved_comb_${Date2017}.txt 
############# COMBINATION 2017 
combineCards.py boosted_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY1}/${CR_var_boost_2017}/datacard.txt \
                boosted_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY2}/${CR_var_boost_2017}/datacard.txt \
                boosted_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR2_var}/datacard.txt \
                resolved_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY1}/${CR_var_res_2017}/datacard.txt \
                resolved_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY2}/${CR_var_res_2017}/datacard.txt \
                resolved_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR2_var}/datacard.txt> ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_all_comb_2017.txt
echo "======================================="
echo "produced 2017 combined card:" ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_all_comb_2017.txt 
combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_all_comb_2017.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_comb_${Date2017}.txt 
echo "whose significance (blind) is here: " ${SigPATH}/significance_comb_${Date2017}.txt 
#########################################################################################
##################           #       #####   
##################         # #       #   #
##################       #   #        ###
##################           #       #####
##################           #       #   #
##################           #        ###
#########################################################################################
############## BOOSTED CATEGORY 2018
#combineCards.py boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
#                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost_2017}/datacard.txt \
#                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt \
#                boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
#                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost_2017}/datacard.txt \
#                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_2018.txt
#echo "======================================="
#echo "produced boosted cat. 2018 card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_2018.txt 
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_boosted_comb_${Date2018}.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_boosted_comb_${Date2018}.txt 
#echo "whose significance (blind) is here: " ${SigPATH}/significance_boosted_comb_${Date2018}.txt 
############## RESOLVED CATEGORY 2018
#combineCards.py resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res_2017}/datacard.txt \
#                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt \
#                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res_2017}/datacard.txt  \
#                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_2018.txt
#echo "======================================="
#echo "produced resolved cat. 2018 card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_${Date2018}.txt 
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_resolved_comb_2018.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_resolved_comb_${Date2018}.txt 
#echo "whose significance (blind) is here: " ${SigPATH}/significance_resolved_comb_${Date2018}.txt 
############## COMBINATION 2018 
#combineCards.py boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
#                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost_2017}/datacard.txt \
#                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt \
#                boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
#                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost_2017}/datacard.txt \
#                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt \
#                resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res_2017}/datacard.txt \
#                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt \
#                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res_2017}/datacard.txt \
#                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt> ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_2018.txt
#echo "======================================="
#echo "produced 2018 combined card:" ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_2018.txt 
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_2018.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_comb_${Date2018}.txt 
#echo "whose significance (blind) is here: " ${SigPATH}/significance_comb_${Date2018}.txt 
#
#
#
#
#echo "======================================="
#echo "======================================="
#######################
#### full RUN 2 ######
#######################
#combineCards.py ${DatacardPATH}/Datacards/Datacards_${Date2016}/combined_card_all_comb_2016.txt \
#                ${DatacardPATH}/Datacards/Datacards_${Date2017}/combined_card_all_comb_2017.txt \
#                ${DatacardPATH}/Datacards/Datacards_${Date2018}/combined_card_all_comb_2018.txt> ${DatacardPATH}/Datacards/FullRun2_${Date2018}/combined_card.txt
#combine -M Significance ${DatacardPATH}/Datacards/FullRun2_${Date2018}/combined_card.txt -t -1 --expectSignal=1 &> ${SigPATH}/significance_comb_${Date2018}.txt 
#echo "FULL RUN 2 significance (blind) is here: " ${SigPATH}/significance_comb_${Date2018}.txt 

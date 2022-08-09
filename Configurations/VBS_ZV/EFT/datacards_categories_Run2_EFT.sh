#!/bin/bash

localPATH=$PWD


DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance

declare -a StringArray=("cT0" "cT1" "cT2" "cT5" "cT6" "cT7" "cT8" "cT9")        #looping
for OP in "${StringArray[@]}"; do  

Date2016=14Jul2022_2016_${OP}
Date2017=18Jul2022_2017_${OP}
Date2018=18Jul2022_2018_${OP}

tag=Jul2022          #this is a tag for the output folder for significances, impacts and post/pre-fit plots

#mkdir -p ${SigPATH}/FullRun2_${tag}
mkdir -p ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}

CR_var_res_16=DYfit_Z_bin
CR_var_boost_16=DYfit_Z_bin

CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted

SR1_var=ZV_mass   #DNNoutput_pruned_bVeto 
SR2_var=ZV_mass   #DNNoutput_pruned_bReq

cutDY1=DYcr_bVeto
cutSR1=SR_bVeto

cutDY2=DYcr_bTag
cutSR2=SR_bTag

########################################################################################
                #### B-veto BOOSTED
combineCards.py boosted_bveto_2016_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_bveto_2016_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost_16}/datacard.txt \
                boosted_bveto_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_bveto_2017_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_bveto_2017_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_bveto_2017_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_bveto_2018_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_bveto_2018_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_bveto_2018_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt  > ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted_bVeto.txt
echo "===="
echo "datacard b-veto boosted: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted_bVeto.txt 
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted_bVeto.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted_bVeto.txt 

                #### B-tag BOOSTED
combineCards.py boosted_btag_2016_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_btag_2016_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost_16}/datacard.txt \
                boosted_btag_2016_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt \
                boosted_btag_2017_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_btag_2017_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_btag_2017_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_topcr/${SR2_var}/datacard.txt \
                boosted_btag_2018_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_btag_2018_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_btag_2018_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt  > ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted_bTag.txt
echo "===="
echo "datacard b-tag boosted: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted_bTag.txt
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted_bTag.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted_bTag.txt 


                #### COMBINATION BOOSTED 
combineCards.py boosted_2016_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2017_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2017_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2017_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2018_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt  \
                boosted_2016_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt \
                boosted_2017_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2017_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2017_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Boosted_topcr/${SR2_var}/datacard.txt \
                boosted_2018_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted.txt
echo "===="
echo "datacards boosted combination: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted.txt
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_boosted.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted.txt 
#
#########################################################################
#                #### B-veto RESOLVED
#combineCards.py resolved_2016_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2016_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res_16}/datacard.txt \
#                resolved_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt \
#                resolved_2017_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2017_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
#                resolved_2017_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_topcr/${SR1_var}/datacard.txt \
#                resolved_2018_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2018_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
#                resolved_2018_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt  > ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved_bVeto.txt
#echo "===="
#echo "datacard b-veto resolved: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved_bVeto.txt
##combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved_bVeto.txt 
##echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved_bVeto.txt 
#
#
#                #### B-tag RESOLVED
#combineCards.py resolved_2016_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2016_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res_16}/datacard.txt \
#                resolved_2017_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2017_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
#                resolved_2017_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_topcr/${SR2_var}/datacard.txt \
#                resolved_2018_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2018_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
#                resolved_2018_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt  > ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved_bTag.txt
#echo "===="
#echo "datacard b-tag resolved: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved_bTag.txt
##combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved_bTag.txt 
##echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved_bTag.txt 
#
#
#                #### COMBINATION RESOLVED 
#combineCards.py resolved_2016_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2016_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res_16}/datacard.txt \
#                resolved_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt \
#                resolved_2017_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2017_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
#                resolved_2017_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_topcr/${SR1_var}/datacard.txt \
#                resolved_2018_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2018_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
#                resolved_2018_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt  \
#                resolved_2016_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2016_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res_16}/datacard.txt \
#                resolved_2017_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2017_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
#                resolved_2017_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2017}/Resolved_topcr/${SR2_var}/datacard.txt \
#                resolved_2018_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2018_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
#                resolved_2018_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved.txt
#
#echo "===="
#echo "datacard combination resolved: "  ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved.txt
##combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_resolved.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved.txt 
##echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved.txt 
#
#
#
#
#cd ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}
#
#combineCards.py combined_boosted_bVeto.txt combined_resolved_bVeto.txt > combined_bVeto.txt     
#echo "===="
#echo "b-veto: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_bVeto.txt
##combine -M Significance combined_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_bVeto.txt        
#
#combineCards.py combined_boosted_bTag.txt combined_resolved_bTag.txt > combined_bTag.txt                        
##combine -M Significance combined_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_bTag.txt
#echo "===="
#echo "b-tag: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_bTag.txt
#
#combineCards.py combined_boosted_bVeto.txt combined_resolved_bVeto.txt \
#                combined_boosted_bTag.txt combined_resolved_bTag.txt > combined_card_all_comb.txt      
#echo "===="
#echo "RUN 2: " ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}_${OP}/combined_card_all_comb.txt       
##combine -M Significance combined_card_all_comb.txt -t -1 --toysFreq --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined.txt
#
#cd ${localPATH}


done
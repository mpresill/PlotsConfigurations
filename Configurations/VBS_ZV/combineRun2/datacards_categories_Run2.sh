#!/bin/bash

####
####   this script computed significance for the full Run 2
####   given the datacards of the three years and a tag for output name
####           

####    BE CAREFULL ON THE REFERENCE PATHS/cuts/regions

localPATH=$PWD


DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance

Date2016=13Jan2023_2016
Date2017=13Jan2023_2017
Date2018=13Jan2023_2018

tag=13Jan2023          #this is a tag for the output folder for significances, impacts and post/pre-fit plots

mkdir -p ${SigPATH}/FullRun2_${tag}
mkdir -p ${DatacardPATH}/Datacards/YearsCombination_${tag}

CR_var_res_16=DYfit_Z_bin
CR_var_boost_16=DYfit_Z_bin

CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted

SR1_var=DNNoutput_pruned_bVeto_morebins   #DNNoutput_pruned_bVeto 
SR1_var_2016=DNNoutput_pruned_bVeto   #DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq_morebins   #DNNoutput_pruned_bReq
SR2_var_2016=DNNoutput_pruned_bReq  #DNNoutput_pruned_bReq


#TOPcr1_var=events
#TOPcr2_var=events


cutDY1=DYcr_bVeto
cutSR1=SR_bVeto

cutDY2=DYcr_bTag
cutSR2=SR_bTag

########################################################################################
                #### B-veto BOOSTED
combineCards.py boosted_bveto_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var_2016}/datacard.txt \
                boosted_bveto_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost_16}/datacard.txt \
                boosted_bveto_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var_2016}/datacard.txt \
                boosted_bveto_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_bveto_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_bveto_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_bveto_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_bveto_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_bveto_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt  > ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_boosted_bVeto.txt

combine -M Significance ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_boosted_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted_bVeto.txt 
echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted_bVeto.txt 

                #### B-tag BOOSTED
combineCards.py boosted_btag_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var_2016}/datacard.txt \
                boosted_btag_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost_16}/datacard.txt \
                boosted_btag_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var_2016}/datacard.txt \
                boosted_btag_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_btag_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_btag_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR2_var}/datacard.txt \
                boosted_btag_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_btag_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_btag_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt  > ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_boosted_bTag.txt

combine -M Significance ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_boosted_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted_bTag.txt 
echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted_bTag.txt 


                #### COMBINATION BOOSTED 
combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var_2016}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var_2016}/datacard.txt \
                boosted_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR1_var}/datacard.txt  \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var_2016}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var_2016}/datacard.txt \
                boosted_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR2_var}/datacard.txt \
                boosted_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_boosted.txt

combine -M Significance ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_boosted.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted.txt 
echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted.txt 

########################################################################
                #### B-veto RESOLVED
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var_2016}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res_16}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var_2016}/datacard.txt \
                resolved_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt  > ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_resolved_bVeto.txt

combine -M Significance ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_resolved_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved_bVeto.txt 
echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved_bVeto.txt 


                #### B-tag RESOLVED
combineCards.py resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var_2016}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res_16}/datacard.txt \
                resolved_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR2_var_2016}/datacard.txt \
                resolved_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
                resolved_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR2_var}/datacard.txt \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt  > ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_resolved_bTag.txt

combine -M Significance ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_resolved_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved_bTag.txt 
echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved_bTag.txt 


                #### COMBINATION RESOLVED 
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var_2016}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res_16}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var_2016}/datacard.txt \
                resolved_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2018_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR1_var}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var_2016}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res_16}/datacard.txt \
                resolved_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR2_var_2016}/datacard.txt \
                resolved_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
                resolved_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR2_var}/datacard.txt \
                resolved_2018_sr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2018_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
                resolved_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_resolved.txt

combine -M Significance ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_resolved.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved.txt 
echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved.txt 




cd ${DatacardPATH}/Datacards/YearsCombination_${tag}

combineCards.py combined_boosted_bVeto.txt combined_resolved_bVeto.txt > combined_bVeto.txt                     
combine -M Significance combined_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_bVeto.txt        

combineCards.py combined_boosted_bTag.txt combined_resolved_bTag.txt > combined_bTag.txt                        
combine -M Significance combined_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_bTag.txt

combineCards.py combined_boosted_bVeto.txt combined_resolved_bVeto.txt \
                combined_boosted_bTag.txt combined_resolved_bTag.txt > combined_card_all_comb.txt               
combine -M Significance combined_card_all_comb.txt -t -1 --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined.txt
combine -M Significance combined_card_all_comb.txt -t -1 --expectSignal=1 --toysFreq &> ${SigPATH}/FullRun2_${tag}/combined_toysFreq.txt

cd ${localPATH}
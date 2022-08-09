#!/bin/bash

localPATH=$PWD


DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance



    #\\\ 
    #\\\ Loop on different operators datacards to make them all
    #\\\ #"14Jul2022_2016_cT1" "14Jul2022_2016_cT2" "14Jul2022_2016_cT5" "14Jul2022_2016_cT6" "14Jul2022_2016_cT7" "14Jul2022_2016_cT8" "14Jul2022_2016_cT9"

declare -a StringArray=("14Jul2022_2016_cT0" "14Jul2022_2016_cT1" "14Jul2022_2016_cT2" "14Jul2022_2016_cT5" "14Jul2022_2016_cT6" "14Jul2022_2016_cT7" "14Jul2022_2016_cT8" "14Jul2022_2016_cT9")        #looping
for Date2016 in "${StringArray[@]}"; do  

#Date2016=14Jul2022_2016_cT9
tag=8June2022          #this is a tag for the output folder for significances, impacts and post/pre-fit plots

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
                boosted_bveto_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt > ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_boosted_bVeto.txt
echo "===="
echo "datacard b-veto boosted: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_boosted_bVeto.txt 
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}/combined_boosted_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted_bVeto.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted_bVeto.txt 

                #### B-tag BOOSTED
combineCards.py boosted_btag_2016_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_btag_2016_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost_16}/datacard.txt \
                boosted_btag_2016_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_boosted_bTag.txt
echo "===="
echo "datacard b-tag boosted: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_boosted_bTag.txt
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}/combined_boosted_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted_bTag.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted_bTag.txt 


                #### COMBINATION BOOSTED 
combineCards.py boosted_2016_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_boosted.txt
echo "===="
echo "datacards boosted combination: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_boosted.txt
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}/combined_boosted.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_boosted.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_boosted.txt 

########################################################################
                #### B-veto RESOLVED
combineCards.py resolved_2016_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res_16}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt > ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_resolved_bVeto.txt
echo "===="
echo "datacard b-veto resolved: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_resolved_bVeto.txt
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}/combined_resolved_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved_bVeto.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved_bVeto.txt 


                #### B-tag RESOLVED
combineCards.py resolved_2016_sr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res_16}/datacard.txt > ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_resolved_bTag.txt
echo "===="
echo "datacard b-tag resolved: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_resolved_bTag.txt
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}/combined_resolved_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved_bTag.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved_bTag.txt 


                #### COMBINATION RESOLVED 
combineCards.py resolved_2016_sr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res_16}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt > ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_resolved.txt

echo "===="
echo "datacard combination resolved: "  ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_resolved.txt
#combine -M Significance ${DatacardPATH}/DatacardsEFT/YearsCombination_${tag}/combined_resolved.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_resolved.txt 
#echo "significance " ${SigPATH}/FullRun2_${tag}/combined_resolved.txt 




cd ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}

combineCards.py ../Datacards_${Date2016}/combined_boosted_bVeto.txt ../Datacards_${Date2016}/combined_resolved_bVeto.txt > combined_bVeto.txt     
echo "===="
echo "b-veto: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_bVeto.txt
#combine -M Significance combined_bVeto.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_bVeto.txt        

combineCards.py ../Datacards_${Date2016}/combined_boosted_bTag.txt ../Datacards_${Date2016}/combined_resolved_bTag.txt > combined_bTag.txt                        
#combine -M Significance combined_bTag.txt -t -1  --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined_bTag.txt
echo "===="
echo "b-tag: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_bTag.txt

combineCards.py ../Datacards_${Date2016}/combined_boosted_bVeto.txt ../Datacards_${Date2016}/combined_resolved_bVeto.txt \
                ../Datacards_${Date2016}/combined_boosted_bTag.txt ../Datacards_${Date2016}/combined_resolved_bTag.txt > combined_card_all_comb.txt      
echo "===="
echo "RUN 2: " ${DatacardPATH}/DatacardsEFT/Datacards_${Date2016}/combined_card_all_comb.txt       
#combine -M Significance combined_card_all_comb.txt -t -1 --toysFreq --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/combined.txt

cd ${localPATH}


echo ">>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>         avanti un altro..."
done     #end looping
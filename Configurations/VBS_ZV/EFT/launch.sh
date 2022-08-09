#!/bin/bash


array=( "cT0" "cT1" "cT2" "cT5" "cT6" "cT7" "cT8" "cT9" )
array2=( "2"  "2"   "2"   "4"   "4"   "5"   "5"   "10" )

for i in "${!array[@]}"; do
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_14Jul2022_2016_${array[i]}/combined_boosted_bVeto.txt     ${array[i]} boosted_bVeto           ${array2[i]}   2016
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_14Jul2022_2016_${array[i]}/combined_boosted_bTag.txt      ${array[i]} boosted_bTag            ${array2[i]}   2016
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_14Jul2022_2016_${array[i]}/combined_boosted.txt           ${array[i]} combined_boosted        ${array2[i]}   2016
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_14Jul2022_2016_${array[i]}/combined_resolved_bVeto.txt    ${array[i]} resolved_bVeto          ${array2[i]}   2016
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_14Jul2022_2016_${array[i]}/combined_resolved_bTag.txt     ${array[i]} resolved_bTag           ${array2[i]}   2016
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_14Jul2022_2016_${array[i]}/combined_resolved.txt          ${array[i]} combined_resolved       ${array2[i]}   2016
done

for i in "${!array[@]}"; do
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_18Jul2022_2017_${array[i]}/combined_boosted_bVeto.txt     ${array[i]} boosted_bVeto           ${array2[i]}   2017
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_18Jul2022_2017_${array[i]}/combined_boosted_bTag.txt      ${array[i]} boosted_bTag            ${array2[i]}   2017
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_18Jul2022_2017_${array[i]}/combined_boosted.txt           ${array[i]} combined_boosted        ${array2[i]}   2017
done

for i in "${!array[@]}"; do
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_18Jul2022_2018_${array[i]}/combined_boosted_bVeto.txt     ${array[i]} boosted_bVeto           ${array2[i]}   2018
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_18Jul2022_2018_${array[i]}/combined_boosted_bTag.txt      ${array[i]} boosted_bTag            ${array2[i]}   2018
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards_18Jul2022_2018_${array[i]}/combined_boosted.txt           ${array[i]} combined_boosted        ${array2[i]}   2018
done

for i in "${!array[@]}"; do
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/YearsCombination_Jul2022_${array[i]}/combined_boosted_bVeto.txt     ${array[i]} boosted_bVeto           ${array2[i]}   Run2
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/YearsCombination_Jul2022_${array[i]}/combined_boosted_bTag.txt      ${array[i]} boosted_bTag            ${array2[i]}   Run2
      sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/YearsCombination_Jul2022_${array[i]}/combined_boosted.txt           ${array[i]} combined_boosted        ${array2[i]}   Run2
done



#!/bin/bash
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance


CR_var_res_16=DYfit_Z_bin
CR_var_boost_16=DYfit_Z_bin
#
CR_var_res=DYfit_2D_bin_Resolved
CR_var_boost=DYfit_Z_bin_Boosted
#
SR1_var=DNNoutput_pruned_bVeto_morebins   #DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq_morebins   #DNNoutput_pruned_bReq
cutDY1=DYcr_bVeto
cutSR1=SR_bVeto
cutDY2=DYcr_bTag
cutSR2=SR_bTag


Date2016=11May2022_2016
Date2017=11May2022_2017
Date2018=8Apr2022_2018

tag=8Apr2022          #this is a tag for the output folder for significances, impacts and post/pre-fit plots

mkdir -p ${SigPATH}/FullRun2_${tag}
mkdir -p ${DatacardPATH}/Datacards/YearsCombination_${tag}

combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY1}/${CR_var_res_16}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutDY2}/${CR_var_res_16}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY1}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_${cutDY2}/${CR_var_boost_16}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}/Boosted_topcr/${SR2_var}/datacard.txt \
                resolved_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR1_var}/datacard.txt \
                resolved_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Resolved_topcr/${SR2_var}/datacard.txt \
                boosted_2017_sr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2017_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2017_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR1_var}/datacard.txt \
                boosted_2017_sr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2017_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2017_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2017}/Boosted_topcr/${SR2_var}/datacard.txt \
                resolved_2018_sr1=${DatacardPATH}/Datacards/Datacards_${Date2018}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
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
                boosted_2018_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2018}/Boosted_topcr/${SR2_var}/datacard.txt > ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_card_all_comb.txt


echo "combined datacard " ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_card_all_comb.txt

combine -M Significance ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_card_all_comb.txt -t -1 --expectSignal=1 &> ${SigPATH}/FullRun2_${tag}/comb.txt 

echo "significance " ${SigPATH}/FullRun2_${tag}/comb.txt 



#             #################################################
#              #                                               #
#              #   doing the fit for the whole year combined   #
#              #                                               #
#              #################################################
#text2workspace.py ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_card_all_comb.txt -o ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_card_all_comb.root
#              ########     fit
#              ## -t -1 --expectSignal 0   -> this is for t0 Asimov, b-only
#              ## -t -1 --expectSignal 1   -> this is for t1 Asimov, s+b
#combine -M FitDiagnostics ${DatacardPATH}/Datacards/YearsCombination_${tag}/combined_card_all_comb.root \
#        --out ${DatacardPATH}/Datacards/YearsCombination_${tag} \
#        -t -1 --toysFreq --robustFit=1 --rMin -10 \
#        --cminDefaultMinimizerStrategy 0 \
#        --saveNormalizations --saveWithUncertainties  #--saveOverallShapes --plots --numToysForShapes 200 #-v 2 # --saveWithUncertainties --saveOverallShapes --numToysForShapes 200 --plots #--algo impact -P parameter #--cminDefaultMinimizerStrategy 1 # --robustHesse 1 #--X-rtd MINIMIZER_analytic #--robustHesse 1 # --forceRecreateNLL --saveNormalizations --saveShapes --saveWithUncertainties --saveNLL #--robustFit=1 --cminDefaultMinimizerStrategy 0 #--minos all #--cminDefaultMinimizerTolerance 0.1 --minos poi 
#
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html ${DatacardPATH}/Datacards/YearsCombination_${tag}/fitDiagnosticsTest.root > fit_YearsCombination_${tag}.html
#cp fit_YearsCombination_${tag}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 
#
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/mlfitNormsToText.py ${DatacardPATH}/Datacards/YearsCombination_${tag}/fitDiagnosticsTest.root > postfit_YearsCombination_${tag}_norm.txt
#cp postfit_YearsCombination_${tag}_norm.txt /eos/user/m/mpresill/www/VBS/diffNuisances/. 
#
#
#              ########################################################
#              #                                                      #
#              #   runnning impact plots on the whole year combined   #
#              #                                                      #
#              ########################################################
#outputFolder=${DatacardPATH}/Datacards/YearsCombination_${tag}/impacts
#mkdir -p ${outputFolder}
#impactWorkspace=${DatacardPATH}/Datacards/YearsCombination_${tag}
#
#combine -M FitDiagnostics -d ${impactWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0 --cminDefaultMinimizerStrategy=0
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0
#
#combine -M FitDiagnostics -d ${impactWorkspace}.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1 --cminDefaultMinimizerStrategy=0
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1
#
#combineTool.py -M Impacts -d ${impactWorkspace}.root -t -1 --expectSignal 0 --rMin -10 --doInitialFit --allPars -m 1 -n t0 --parallel 10
#combineTool.py -M Impacts -d ${impactWorkspace}.root -t -1 --expectSignal 1 --rMin -10 --doInitialFit --allPars -m 1 -n t1 --parallel 10
#
#combineTool.py -M Impacts -d ${impactWorkspace}.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -10 --doFits -m 1 -n t0 --parallel 10
#combineTool.py -M Impacts -d ${impactWorkspace}.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -10 --doFits -m 1 -n t1 --parallel 10
#
#combineTool.py -M Impacts -d ${impactWorkspace}.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
#combineTool.py -M Impacts -d ${impactWorkspace}.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10
#plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  impacts_t0
#plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  impacts_t1
#cp impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/YearsCombination_${tag}_impacts_t0.pdf
#cp impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/YearsCombination_${tag}_impacts_t1.pdf

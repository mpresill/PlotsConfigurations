#!/bin/bash
DatacardPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV
SigPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Significance
Date2016=6Dec2023_2016

mkdir -p ${SigPATH}/${Date2016}

CR_var_res=DYfit_Z_bin
CR_var_boost=DYfit_Z_bin
SR1_var=DNNoutput_pruned_bVeto_morebins   #DNNoutput_pruned_bVeto 
SR2_var=DNNoutput_pruned_bReq_morebins #_impacts_t1_morebins   #DNNoutput_pruned_bReq
cutDY1=DYcr_bVeto
cutSR1=SR_bVeto
cutDY2=DYcr_bTag
cutSR2=SR_bTag

TOPcr2_var_boost=events #DNNoutput_pruned_bReq #_morebins #events
TOPcr1_var_boost=events #DNNoutput_pruned_bVeto #_morebins #events
TOPcr1_var=DNNoutput_pruned_bVeto_morebins #DNNoutput_pruned_bVeto_morebins 
TOPcr2_var=DNNoutput_pruned_bReq_morebins

#tag=21Aug2023_QCDscale_DY_top_corr_lnDY_wPS    
tagCARDS=_QCDscaleDY_ln #_morebins #6Dec2023 #_morebins
tagOUTPUT=_QCDscaleDY_ln_morebins #6Dec2023 #_morebins #_wJes_QCDscale_corr_noPSdy
######################################################################################
#                #### B-veto BOOSTED
#combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
#                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
#                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_topcr/${TOPcr1_var_boost}/datacard.txt \
#                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bVeto_card_boosted_${Date2016}.txt
#
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bVeto_card_boosted_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_bVeto_${tagOUTPUT}.txt 
#
#                #### B-tag BOOSTED
#combineCards.py boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
#                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
#                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_topcr/${TOPcr2_var_boost}/datacard.txt \
#                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bTag_card_boosted_${Date2016}.txt
#
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bTag_card_boosted_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_bTag_${tagOUTPUT}.txt 
#
#                #### COMBINATION BOOSTED 2016
#combineCards.py boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
#                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
#                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_topcr/${TOPcr1_var_boost}/datacard.txt \
#                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
#                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
#                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_topcr/${TOPcr2_var_boost}/datacard.txt \
#                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_boosted_comb_${Date2016}.txt
#echo "======================================="
#echo "produced boosted cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_boosted_comb_${Date2016}.txt 
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_boosted_comb_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/boosted_comb_${tagOUTPUT}.txt 
#echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/boosted_comb.txt 
#
#########################################################################
#                #### B-veto RESOLVED
#combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
#                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
#                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bVeto_card_resolved_${Date2016}.txt
#
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bVeto_card_resolved_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_bVeto_${tagOUTPUT}.txt 
#
#                #### B-tag RESOLVED
#combineCards.py resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
#                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_topcr/${TOPcr2_var}/datacard.txt \
#                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bTag_card_resolved_${Date2016}.txt

#text2workspace.py ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bTag_card_resolved_${Date2016}.txt -o ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bTag_card_resolved_${Date2016}.root
#combine -M FitDiagnostics ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bTag_card_resolved_${Date2016}.root \
#        --out . \
#        --rMin -10 \
#        --saveNormalizations --saveWithUncertainties \
#        --cminDefaultMinimizerStrategy 0
#
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/bTag_card_resolved_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_bTag_${tagOUTPUT}.txt 
#
                #### COMBINATION RESOLVED 2016
#combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
#                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
#                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt \
#                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                resolved_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_topcr/${TOPcr2_var}/datacard.txt \
#                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt
#echo "======================================="
#echo "produced resolved cat. 2016 card:" ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_resolved_comb_${Date2016}.txt 
#combine -M Significance ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_resolved_comb_${Date2016}.txt -t -1  --expectSignal=1 &> ${SigPATH}/${Date2016}/resolved_comb_${tagOUTPUT}.txt 
#echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/resolved_comb.txt 




#####################################################################
############# CATEGORIES COMBINATION 2016 
combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
                resolved_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_topcr/${TOPcr2_var}/datacard.txt \
                boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_topcr/${TOPcr1_var_boost}/datacard.txt \
                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
                boosted_2016_topcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_topcr/${TOPcr2_var_boost}/datacard.txt \
                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt
####### rmeoving TOP cr duplicates:
############ CATEGORIES COMBINATION 2016 
#combineCards.py resolved_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR1}/${SR1_var}/datacard.txt \
#                resolved_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY1}/${CR_var_res}/datacard.txt \
#                resolved_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_topcr/${TOPcr1_var}/datacard.txt \
#                resolved_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutDY2}/${CR_var_res}/datacard.txt  \
#                resolved_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Resolved_${cutSR2}/${SR2_var}/datacard.txt \
#                boosted_2016_sr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR1}/${SR1_var}/datacard.txt \
#                boosted_2016_DYcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY1}/${CR_var_boost}/datacard.txt \
#                boosted_2016_topcr1=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_topcr/${TOPcr1_var_boost}/datacard.txt \
#                boosted_2016_sr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutSR2}/${SR2_var}/datacard.txt \
#                boosted_2016_DYcr2=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/Boosted_${cutDY2}/${CR_var_boost}/datacard.txt \
#                > ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt
#echo "======================================="
#echo "produced 2016 combined card:" /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt 
combine -M Significance /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt -t -1 --expectSignal=1 &> ${SigPATH}/${Date2016}/comb_${tagOUTPUT}.txt 
combine -M Significance /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt &> ${SigPATH}/${Date2016}/comb_${tagOUTPUT}_data.txt 
#combine -M Significance /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt -t -1 --expectSignal=1 --toysFreq &> ${SigPATH}/${Date2016}/comb_${tagOUTPUT}_toysFreq.txt 
#echo ">>>>>>>>>>>>>>>>>>>>>>>>>   whose significance (blind) is here: " ${SigPATH}/${Date2016}/comb.txt 
             #################################################
             #   doing the fit for the whole year combined   #
              #################################################
text2workspace.py ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.txt -o ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.root
mkdir -p ${DatacardPATH}/fit/${Date2016}${tagOUTPUT}
        ########     fit diagnostic
        ## -t -1 --expectSignal 0   -> this is for t0 Asimov, b-only
        ## -t -1 --expectSignal 1   -> this is for t1 Asimov, s+b
combine -M FitDiagnostics ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.root \
        --out ${DatacardPATH}/fit/${Date2016}${tagOUTPUT} \
        --rMin -2 --rMax 2 \
        --saveNormalizations --saveWithUncertainties \
        --setParameterRanges 'rgx{.*norm_.*}'=-2,4 \
        --robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --setRobustFitTolerance 0.2 --stepSize=0.001 #--X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND  #\
        # diff nuisances
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html ${DatacardPATH}/fit/${Date2016}${tagOUTPUT}/fitDiagnosticsTest.root > fit_${Date2016}${tagOUTPUT}.html
cp fit_${Date2016}${tagOUTPUT}.html /eos/user/m/mpresill/www/VBS/diffNuisances/. 
        # normalization 
python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/mlfitNormsToText.py ${DatacardPATH}/fit/${Date2016}${tagOUTPUT}/fitDiagnosticsTest.root > postfit_${Date2016}${tagOUTPUT}_norm.txt
cp postfit_${Date2016}${tagOUTPUT}_norm.txt /eos/user/m/mpresill/www/VBS/diffNuisances/. 
        # Nuisance Report

        # fast scan
combineTool.py -M FastScan -w ${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.root:w 
cp nll.pdf /eos/user/m/mpresill/www/VBS/diffNuisances/FastScan_${Date2016}${tagOUTPUT}.pdf

###        ###############
echo "Finished ****************************************************** "
echo "FitDiagnostic file : "${DatacardPATH}/fit/${Date2016}${tagOUTPUT}/fitDiagnosticsTest.root 
echo "following workspace was used: "${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_all_comb_${Date2016}${tagOUTPUT}.root 

##
##
##              ########################################################
#              #                                                      #
#              #   runnning impact plots on the whole year combined   #
#              #                                                      #
#              ########################################################
#inputCard=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/combined_card_resolved_comb_${Date2016}
#              ########################################################
#              #   updating the rateparameters for DY samples in the  #
#              #   combined datacards that will be used for impacts   #
#              ########################################################
#python ../scripts/Utilities_nuisances/update_rateParam_initialization_16.py /eos/user/m/mpresill/www/VBS/diffNuisances/fit_${Date2016}.html ${inputCard}.txt
#echo "  "
#echo " INITIALIZED RATE PARAMETERS IN THE CARD!!! "
#echo "  "
#
#echo "${inputCard}" 
#text2workspace.py ${inputCard}.txt ${inputCard}.root
#
#outputFolder=${DatacardPATH}/Datacards/Datacards_${Date2016}${tagCARDS}/impacts
#mkdir -p ${outputFolder}
#
#fitOptions="--robustFit=1 --cminDefaultMinimizerStrategy 0 --X-rtd MINIMIZER_MaxCalls=9999999 --cminFallbackAlgo Minuit2,Migrad,0:0.2  --X-rtd FITTER_NEW_CROSSING_ALGO --X-rtd FITTER_NEVER_GIVE_UP --X-rtd FITTER_BOUND --setRobustFitTolerance 0.2 --stepSize=0.001"
#fitRange=

#combine -M FitDiagnostics -d ${inputCard}.root -t -1 --expectSignal 0 --rMin -10 --forceRecreateNLL -n _t0 --cminDefaultMinimizerStrategy=0
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t0.root -g plots_t0.root >> ${outputFolder}/fitResults_t0
#
#combine -M FitDiagnostics -d ${inputCard}.root -t -1 --expectSignal 1  --forceRecreateNLL -n _t1 --cminDefaultMinimizerStrategy=0
#python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py  -a fitDiagnostics_t1.root -g plots_t1.root >> ${outputFolder}/fitResults_t1
#
#combineTool.py -M Impacts -d ${inputCard}.root -t -1 --expectSignal 0 --rMin -2 ${fitOptions} --doInitialFit --allPars -m 1 -n t0 --parallel 10
#combineTool.py -M Impacts -d ${inputCard}.root -t -1 --expectSignal 1 --rMin -2 ${fitOptions} --doInitialFit --allPars -m 1 -n t1 --parallel 10
#
#combineTool.py -M Impacts -d ${inputCard}.root -o ${outputFolder}/impacts_t0.json -t -1 --expectSignal 0 --rMin -2 ${fitOptions} --doFits -m 1 -n t0 --parallel 10
#combineTool.py -M Impacts -d ${inputCard}.root -o ${outputFolder}/impacts_t1.json -t -1 --expectSignal 1 --rMin -2 ${fitOptions} --doFits -m 1 -n t1 --parallel 10
#
#combineTool.py -M Impacts -d ${inputCard}.root -m 1 -n t0 -o ${outputFolder}/impacts_t0.json --parallel 10
#combineTool.py -M Impacts -d ${inputCard}.root -m 1 -n t1 -o ${outputFolder}/impacts_t1.json --parallel 10
#plotImpacts.py -i  ${outputFolder}/impacts_t0.json -o  impacts_t0
#plotImpacts.py -i  ${outputFolder}/impacts_t1.json -o  impacts_t1
#cp impacts_t0.pdf /eos/user/m/mpresill/www/VBS/impacts/${Date2016}_impacts_t0_${tagOUTPUT}.pdf
#cp impacts_t1.pdf /eos/user/m/mpresill/www/VBS/impacts/${Date2016}_impacts_t1_${tagOUTPUT}.pdf
#cp impacts_t0.pdf ${SigPATH}/${Date2016}/impacts_t0_${tagOUTPUT}.pdf
#cp impacts_t1.pdf ${SigPATH}/${Date2016}/impacts_t1_${tagOUTPUT}.pdf


        ####unblinded
#combineTool.py -M Impacts -d ${inputCard}.root --rMin -3 ${fitOptions} --doInitialFit --allPars -m 1 -n data --parallel 15
#combineTool.py -M Impacts -d ${inputCard}.root -o ${outputFolder}/impacts_data.json --rMin -3 ${fitOptions} --doFits -m 1 -n data --parallel 15
#combineTool.py -M Impacts -d ${inputCard}.root -m 1 -n data -o ${outputFolder}/impacts_data.json --parallel 15
#plotImpacts.py -i  ${outputFolder}/impacts_data.json -o  impacts_data
#cp impacts_data.pdf /eos/user/m/mpresill/www/VBS/impacts/${Date2016}_impacts_data_${tagOUTPUT}.pdf


             #################################################
              #                                               #
              #            uncertainty breakdown              #
              #                                               #
              #################################################
    ## run postfit with all nuisances floating and store it in an output
#rm -rf local.root
#cp ${inputCard}.root ZV_ewk.root
#
#combine ZV_ewk.root -M MultiDimFit -t -1 -m 120 --points 2000 --saveWorkspace -n ZV_ewk.total --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0
#    #### theory
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory -n ZV_ewk.freeze_theory
#    ##### DYnorm
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm -n ZV_ewk.freeze_DYnorm
#    #### Topnorm
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm -n ZV_ewk.freeze_Topnorm
#    ### AK4
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet -n ZV_ewk.freeze_AK4jet
#    ### AK8
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet -n ZV_ewk.freeze_AK8jet
#    ### LEPTON
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton -n ZV_ewk.freeze_lepton
#    ### PU
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU -n ZV_ewk.freeze_PU
#    ### LUMI
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi -n ZV_ewk.freeze_lumi
#    ### FAKE
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake -n ZV_ewk.freeze_fake
#    ### TRIGGER
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger -n ZV_ewk.freeze_trigger
#
#    ### ALL
#combine higgsCombineZV_ewk.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 -m 120 --points 2000 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0 \
#        --freezeParameters allConstrainedNuisances -n ZV_ewk.freeze_all
#
#
#    ## plotting and copying to my webpage
#plot1DScan.py higgsCombineZV_ewk.total.MultiDimFit.mH120.root --main-label "Total Uncert."  \
#    --others \
#    'higgsCombineZV_ewk.freeze_theory.MultiDimFit.mH120.root:Freeze theory:600' \
#    'higgsCombineZV_ewk.freeze_DYnorm.MultiDimFit.mH120.root:Freeze DYnorm:920' \
#    'higgsCombineZV_ewk.freeze_Topnorm.MultiDimFit.mH120.root:Freeze Topnorm:416' \
#    'higgsCombineZV_ewk.freeze_AK4jet.MultiDimFit.mH120.root:Freeze AK4jet:400' \
#    'higgsCombineZV_ewk.freeze_AK8jet.MultiDimFit.mH120.root:Freeze AK8jet:616' \
#    'higgsCombineZV_ewk.freeze_lepton.MultiDimFit.mH120.root:Freeze lepton:432' \
#    'higgsCombineZV_ewk.freeze_PU.MultiDimFit.mH120.root:Freeze PU:800' \
#    'higgsCombineZV_ewk.freeze_lumi.MultiDimFit.mH120.root:Freeze lumi:820' \
#    'higgsCombineZV_ewk.freeze_fake.MultiDimFit.mH120.root:Freeze fake:840' \
#    'higgsCombineZV_ewk.freeze_trigger.MultiDimFit.mH120.root:Freeze trigger:860' \
#    'higgsCombineZV_ewk.freeze_all.MultiDimFit.mH120.root:Freeze all:840' \
#    -o freeze_th_exp_st \
#    --breakdown "theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger,rest,stat"
#
#cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/${Date2016}_nuisances_breakdown_${tagOUTPUT}.png
#cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/${Date2016}_nuisances_breakdown_${tagOUTPUT}.pdf


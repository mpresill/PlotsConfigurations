#!/bin/bash

tag=6Dec2023_QCDscaleDY_corr_ln_2018btagDNNfrom2017_DNN_bReq_resolved_topcr__finalUnblinded__13March2024
cd ../tmp
#text2workspace.py combinedFIT_theory_group_v2.txt -o impactWorkspace.root
#cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/YearsCombination_6Dec2023_QCDscaleDY_corr_ln_2018btagDNNfrom2017_DNN_bReq_resolved_topcr__finalUnblinded__13March2024/combined.txt impactWorkspace.txt
text2workspace.py impactWorkspace.txt -o impactWorkspace.root
             #################################################
              #                                               #
              #            uncertainty breakdown              #
              #                                               #
              #################################################
    ## run postfit with all nuisances floating and store it in an output
#cp ${inputCard}.root impactWorkspace.root

#combine impactWorkspace.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --saveWorkspace -n impactWorkspace.total --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0
#    #### theory
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory -n impactWorkspace.freeze_theory
#    ##### DYnorm
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm -n impactWorkspace.freeze_DYnorm
#    #### Topnorm
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm -n impactWorkspace.freeze_Topnorm
#    ### AK4
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet -n impactWorkspace.freeze_AK4jet
#    ### AK8
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet -n impactWorkspace.freeze_AK8jet
#    ### LEPTON
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton -n impactWorkspace.freeze_lepton
#    ### PU
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU -n impactWorkspace.freeze_PU
#    ### LUMI
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi -n impactWorkspace.freeze_lumi
#    ### FAKE
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake -n impactWorkspace.freeze_fake
#    ### TRIGGER
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5 --cminDefaultMinimizerStrategy=0 \
#        --freezeNuisanceGroups theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger -n impactWorkspace.freeze_trigger
#
#    ### ALL
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit -t -1 --toysFreq -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -5 --rMax 5  --cminDefaultMinimizerStrategy=0 \
#        --freezeParameters allConstrainedNuisances -n impactWorkspace.freeze_all
#
#
#    ## plotting and copying to my webpage
#plot1DScan.py higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root --main-label "Total Uncert."  \
#    --others \
#    'higgsCombineimpactWorkspace.freeze_theory.MultiDimFit.mH120.root:Freeze theory:600' \
#    'higgsCombineimpactWorkspace.freeze_DYnorm.MultiDimFit.mH120.root:Freeze DYnorm:920' \
#    'higgsCombineimpactWorkspace.freeze_Topnorm.MultiDimFit.mH120.root:Freeze Topnorm:416' \
#    'higgsCombineimpactWorkspace.freeze_AK4jet.MultiDimFit.mH120.root:Freeze AK4jet:400' \
#    'higgsCombineimpactWorkspace.freeze_AK8jet.MultiDimFit.mH120.root:Freeze AK8jet:616' \
#    'higgsCombineimpactWorkspace.freeze_lepton.MultiDimFit.mH120.root:Freeze lepton:432' \
#    'higgsCombineimpactWorkspace.freeze_PU.MultiDimFit.mH120.root:Freeze PU:800' \
#    'higgsCombineimpactWorkspace.freeze_lumi.MultiDimFit.mH120.root:Freeze lumi:820' \
#    'higgsCombineimpactWorkspace.freeze_fake.MultiDimFit.mH120.root:Freeze fake:840' \
#    'higgsCombineimpactWorkspace.freeze_trigger.MultiDimFit.mH120.root:Freeze trigger:860' \
#    'higgsCombineimpactWorkspace.freeze_all.MultiDimFit.mH120.root:Freeze all:840' \
#    -o freeze_th_exp_st \
#    --breakdown "theory,DYnorm,Topnorm,AK4jet,AK8jet,lepton,PU,lumi,fake,trigger,rest,stat"
#
#cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/TEST-2016_boosted.png
#cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/TEST-2016_boosted.pdf



    #############################
    #### Splitting in  Rate Param, theory, MCstat, Experimental, data stat
    #############################

combine -M MultiDimFit impactWorkspace.root --toysFrequentist  -m 120 --algo grid --points 30 --saveWorkspace -n impactWorkspace.total --rMin -0.5 --rMax 2.5
    #### nominal
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
        --snapshotName MultiDimFit -n impactWorkspace.nominal 

####################        
    ### ALL (non-floating nuisances)
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
        --freezeParameters allConstrainedNuisances --snapshotName MultiDimFit -n impactWorkspace.freeze_all


####################        
    ##### DYnorm
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
        --freezeNuisanceGroups DYnorm,Topnorm --snapshotName MultiDimFit -n impactWorkspace.freeze_RateParams 

    #### theory
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
        --freezeNuisanceGroups DYnorm,Topnorm,theory --snapshotName MultiDimFit -n impactWorkspace.freeze_theory 

#    #### theory: QCD scale for VBS/F processes, signal included
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups DYnorm,Topnorm,QCDscaleVV --snapshotName MultiDimFit -n impactWorkspace.freeze_QCDscaleVV 
#
#    #### theory: PS
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups DYnorm,Topnorm,QCDscaleVV,PS --snapshotName MultiDimFit -n impactWorkspace.freeze_PS 
#
#    #### theory: QCDscale for other processes
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups DYnorm,Topnorm,QCDscaleVV,PS,QCDscaleOther --snapshotName MultiDimFit -n impactWorkspace.freeze_QCDscaleOther 

    ### autoMCstats
combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
        --freezeNuisanceGroups DYnorm,Topnorm,theory,autoMCStats  --snapshotName MultiDimFit -n impactWorkspace.freeze_MCstat
#        --freezeNuisanceGroups DYnorm,Topnorm,QCDscaleVV,PS,QCDscaleOther,autoMCStats  --snapshotName MultiDimFit -n impactWorkspace.freeze_MCstat


####################        
    ## plotting and copying to my webpage
#plot1DScan.py higgsCombineimpactWorkspace.nominal.MultiDimFit.mH120.root --main-label "Total Uncert. (Asimov)"  \
#    --others \
#    'higgsCombineimpactWorkspace.freeze_RateParams.MultiDimFit.mH120.root:Freeze RateParams:920' \
#    'higgsCombineimpactWorkspace.freeze_QCDscaleVV.MultiDimFit.mH120.root:Freeze RateParams+QCDscaleVV:600' \
#    'higgsCombineimpactWorkspace.freeze_PS.MultiDimFit.mH120.root:Freeze RateParams+QCDscaleVV+PS:500' \
#    'higgsCombineimpactWorkspace.freeze_QCDscaleOther.MultiDimFit.mH120.root:Freeze RateParams+PS+QCDscale:800' \
#    'higgsCombineimpactWorkspace.freeze_MCstat.MultiDimFit.mH120.root:Freeze RateParams+PS+QCDscale+MCstat:416' \
#    'higgsCombineimpactWorkspace.freeze_all.MultiDimFit.mH120.root:Freeze all:632' \
#    -o freeze_th_exp_st \
#    --breakdown "RateParams,QCDscaleVV,PS,otherQCDscale,MCstat,rest,stat"
plot1DScan.py higgsCombineimpactWorkspace.nominal.MultiDimFit.mH120.root --main-label "Total Uncert. (Asimov)"  \
    --others \
    'higgsCombineimpactWorkspace.freeze_RateParams.MultiDimFit.mH120.root:Freeze RateParams:920' \
    'higgsCombineimpactWorkspace.freeze_theory.MultiDimFit.mH120.root:Freeze RateParams+theory:600' \
    'higgsCombineimpactWorkspace.freeze_MCstat.MultiDimFit.mH120.root:Freeze RateParams+theory+MCstat:416' \
    'higgsCombineimpactWorkspace.freeze_all.MultiDimFit.mH120.root:Freeze all:632' \
    -o freeze_th_exp_st \
    --breakdown "RateParams,theory,MCstat,other,stat"


cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}_observed_CWR.png
cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}_observed_CWR.pdf



    ### further split for "Exp"
    ### AK4 jets related uncertainties
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups AK4jet  --snapshotName MultiDimFit -n impactWorkspace.freeze_AK4jet
#
#    ### AK8 jets related uncertainties
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups AK4jet,AK8jet  --snapshotName MultiDimFit -n impactWorkspace.freeze_AK8jet
#
#    ### lepton related uncertainties
#combine higgsCombineimpactWorkspace.total.MultiDimFit.mH120.root -M MultiDimFit  -m 120 --points 30 --algo grid  --autoBoundsPOIs r --rMin -0.5 --rMax 2.5 \
#        --freezeNuisanceGroups AK4jet,AK8jet,lepton  --snapshotName MultiDimFit -n impactWorkspace.freeze_lepton


#    ## plotting and copying to my webpage
#plot1DScan.py higgsCombineimpactWorkspace.freeze_MCstat.MultiDimFit.mH120.root --main-label "Total Exp Uncert. (Asimov)"  \
#    --others \
#    'higgsCombineimpactWorkspace.freeze_AK4jet.MultiDimFit.mH120.root:Freeze AK4 jet:416' \
#    'higgsCombineimpactWorkspace.freeze_AK8jet.MultiDimFit.mH120.root:Freeze AK4 jet + AK8 jet:416' \
#    'higgsCombineimpactWorkspace.freeze_lepton.MultiDimFit.mH120.root:Freeze AK4 jet + AK8 jet + lepton:416' \
#    'higgsCombineimpactWorkspace.freeze_all.MultiDimFit.mH120.root:Freeze all:632' \
#    -o freeze_th_exp_st \
#    --breakdown "Ak4jet,AK8jet,lepton,rest,stat"
##    'higgsCombineimpactWorkspace.freeze_MCstat.MultiDimFit.mH120.root:Freeze RateParams+theory+MCstat:416' \
##    'higgsCombineimpactWorkspace.freeze_theory.MultiDimFit.mH120.root:Freeze RateParams+theory:600' \
##    'higgsCombineimpactWorkspace.freeze_RateParams.MultiDimFit.mH120.root:Freeze RateParams:920' \
#
#cp freeze_th_exp_st.png /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}_Exp_splitting.png
#cp freeze_th_exp_st.pdf /eos/user/m/mpresill/www/VBS/impacts/breakdown/YearsCombination_${tag}_Exp_splitting.pdf








############## memorandum of the lines to be pasted for grouping full run 2:

#AK8jet group = CMS_scale_mVjer_2017 CMS_scale_mVjer_2016 CMS_scale_mVjer_2018 CMS_scale_cleanfatJES_2017 CMS_scale_cleanfatJES_2016 CMS_scale_cleanfatJES_2018 CMS_scale_cleanfatJER_2016 CMS_scale_cleanfatJER_2017 CMS_scale_mVjesTotal_2017 CMS_scale_mVjesTotal_2016 CMS_scale_mVjms_2018 CMS_scale_mVjms_2016 CMS_scale_mVjms_2017 CMS_scale_mVjesTotal_2018 CMS_scale_cleanfatJER_2018 CMS_scale_mVjmr_2018 CMS_scale_mVjmr_2017 CMS_scale_mVjmr_2016
#theory group = QCDscale_ZZlep QCDscale_tZq QCDscale_sm_dipole QCDscale_top QCDscale_VgS UE_CP5 QCDscale_VVV PS_ISR CMS_topPtRew QCDscale_WJets PS_FSR QCDscale_DY pdf_1718 QCDscale_VBS_VV_QCD UE_CUETP8 QCDscale_VBF-V QCDscale_Vg PS_FSR_DY PS_FSR_top PS_ISR_DY PS_ISR_top
#PU group = CMS_PU_2016 CMS_PU_2018 CMS_PU_2017
#fake group = CMS_fake_syst_em CMS_fake_e_2018 CMS_fake_syst CMS_fake_m_2016 CMS_fake_e_2016 CMS_fake_stat_m_2016 CMS_fake_stat_e_2018 CMS_fake_stat_e_2016 CMS_fake_stat_m_2018 CMS_fake_m_2018
#Topnorm group = Topnorm_boosted_2016 Topnorm_boosted_2017 Topnorm_resolved_2017 Topnorm_resolved_2018 Topnorm_boosted_2018 Topnorm_resolved_2016
#lepton group = CMS_scale_e_2016 CMS_eff_m_2018 CMS_scale_m_2018 CMS_eff_e_2016 CMS_scale_m_2016 CMS_eff_e_2018 CMS_eff_prefiring_2016 CMS_scale_e_2018 CMS_eff_m_2016
#trigger group = CMS_eff_hwwtrigger_2018 CMS_eff_trigger_2016
#lumi group = lumi_13TeV_2018 lumi_13TeV_XYFact lumi_13TeV_CurrCalib lumi_13TeV_LSCale lumi_13TeV_2016 lumi_13TeV_Ghosts
#DYnorm group = CMS_DY_Resolved_2d_12_norm_res_Z_bTag_2017 CMS_DY_Resolved_2d_5_norm_res_Z_bVeto_2018 CMS_DY_Boosted_Z_2_norm_boost_Z_bTag_2017 CMS_DY_Resolved_2d_5_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_7_norm_res_Z_bVeto_2018 CMS_DY_bin1_norm_res_Z_bTag_2016 CMS_DY_Boosted_Z_1_norm_boost_bTag_2018 CMS_DY_Resolved_2d_9_norm_res_Z_bTag_2017 CMS_DY_bin5_norm_res_Z_bTag_2016 CMS_DY_bin2_norm_boost_Z_bVeto_2016 CMS_DY_Boosted_Z_5_norm_boost_bVeto_2018 CMS_DY_bin5_norm_boost_Z_bTag_2016 CMS_DY_Resolved_2d_5_norm_res_Z_btag_2018 CMS_DY_bin1_norm_boost_Z_bTag_2016 CMS_DY_Resolved_2d_2_norm_res_Z_bTag_2017 CMS_DY_Boosted_Z_4_norm_boost_Z_bVeto_2017 CMS_DY_Resolved_2d_1_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_1_norm_res_Z_bVeto_2018 CMS_DY_Resolved_2d_6_norm_res_Z_bTag_2017 CMS_DY_Resolved_2d_5_norm_res_Z_bTag_2017 CMS_DY_bin4_norm_res_Z_bTag_2016 CMS_DY_Resolved_2d_12_norm_res_Z_bVeto_2018 CMS_DY_Boosted_Z_1_norm_boost_Z_bVeto_2017 CMS_DY_Resolved_2d_12_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_7_norm_res_Z_btag_2018 CMS_DY_Resolved_2d_4_norm_res_Z_btag_2018 CMS_DY_bin1_norm_res_Z_bVeto_2016 CMS_DY_bin2_norm_res_Z_bTag_2016 CMS_DY_bin4_norm_boost_Z_bTag_2016 CMS_DY_Boosted_Z_2_norm_boost_bTag_2018 CMS_DY_Resolved_2d_1_norm_res_Z_bTag_2017 CMS_DY_Boosted_Z_4_norm_boost_Z_bTag_2017 CMS_DY_Resolved_2d_6_norm_res_Z_btag_2018 CMS_DY_Resolved_2d_12_norm_res_Z_btag_2018 CMS_DY_bin4_norm_res_Z_bVeto_2016 CMS_DY_Boosted_Z_3_norm_boost_bVeto_2018 CMS_DY_Resolved_2d_8_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_6_norm_res_Z_bVeto_2017 CMS_DY_Boosted_Z_4_norm_boost_bTag_2018 CMS_DY_bin2_norm_res_Z_bVeto_2016 CMS_DY_bin4_norm_boost_Z_bVeto_2016 CMS_DY_Boosted_Z_1_norm_boost_bVeto_2018 CMS_DY_Boosted_Z_2_norm_boost_Z_bVeto_2017 CMS_DY_Resolved_2d_1_norm_res_Z_btag_2018 CMS_DY_Resolved_2d_7_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_6_norm_res_Z_bVeto_2018 CMS_DY_Boosted_Z_4_norm_boost_bVeto_2018 CMS_DY_Boosted_Z_5_norm_boost_Z_bTag_2017 CMS_DY_Resolved_2d_3_norm_res_Z_bTag_2017 CMS_DY_Resolved_2d_3_norm_res_Z_btag_2018 CMS_DY_Resolved_2d_8_norm_res_Z_btag_2018 CMS_DY_Resolved_2d_9_norm_res_Z_bVeto_2018 CMS_DY_Resolved_2d_7_norm_res_Z_bTag_2017 CMS_DY_bin3_norm_boost_Z_bVeto_2016 CMS_DY_bin3_norm_res_Z_bVeto_2016 CMS_DY_Resolved_2d_9_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_10_norm_res_Z_btag_2018 CMS_DY_Boosted_Z_3_norm_boost_bTag_2018 CMS_DY_Resolved_2d_9_norm_res_Z_btag_2018 CMS_DY_Resolved_2d_8_norm_res_Z_bTag_2017 CMS_DY_bin2_norm_boost_Z_bTag_2016 CMS_DY_bin5_norm_res_Z_bVeto_2016 CMS_DY_Resolved_2d_11_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_10_norm_res_Z_bVeto_2018 CMS_DY_bin3_norm_boost_Z_bTag_2016 CMS_DY_Boosted_Z_3_norm_boost_Z_bTag_2017 CMS_DY_Resolved_2d_3_norm_res_Z_bVeto_2018 CMS_DY_Boosted_Z_1_norm_boost_Z_bTag_2017 CMS_DY_Resolved_2d_3_norm_res_Z_bVeto_2017 CMS_DY_bin3_norm_res_Z_bTag_2016 CMS_DY_Boosted_Z_5_norm_boost_Z_bVeto_2017 CMS_DY_Resolved_2d_10_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_11_norm_res_Z_bVeto_2018 CMS_DY_Resolved_2d_11_norm_res_Z_btag_2018 CMS_DY_Boosted_Z_5_norm_boost_bTag_2018 CMS_DY_Boosted_Z_3_norm_boost_Z_bVeto_2017 CMS_DY_Boosted_Z_2_norm_boost_bVeto_2018 CMS_DY_Resolved_2d_10_norm_res_Z_bTag_2017 CMS_DY_Resolved_2d_2_norm_res_Z_bVeto_2018 CMS_DY_Resolved_2d_8_norm_res_Z_bVeto_2018 CMS_DY_bin1_norm_boost_Z_bVeto_2016 CMS_DY_Resolved_2d_2_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_2_norm_res_Z_btag_2018 CMS_DY_Resolved_2d_11_norm_res_Z_bTag_2017 CMS_DY_Resolved_2d_4_norm_res_Z_bVeto_2017 CMS_DY_Resolved_2d_4_norm_res_Z_bVeto_2018 CMS_DY_Resolved_2d_4_norm_res_Z_bTag_2017 CMS_DY_bin5_norm_boost_Z_bVeto_2016
#AK4jet group = CMS_btag_lfstats2_2018 CMS_scale_JESBBEC1 CMS_scale_JESEC2 CMS_scale_JESFlavorQCD CMS_btag_hfstats2_2018 CMS_btag_hfstats2_2016 CMS_scale_JESAbsolute_2016 CMS_jetpuid_2016 CMS_scale_JESHF_2018 CMS_scale_JESAbsolute_2018 CMS_jetpuid_2018 CMS_btag_jes CMS_scale_JESEC2_2016 CMS_scale_JESHF CMS_btag_lf CMS_btag_lfstats2_2016 CMS_scale_JESEC2_2018 CMS_scale_JESAbsolute CMS_btag_lfstats1_2018 CMS_scale_JESBBEC1_2016 CMS_scale_JESRelativeSample_2016 CMS_scale_JESRelativeSample_2018 CMS_scale_JESBBEC1_2018 CMS_btag_lfstats1_2016 CMS_btag_cferr1 CMS_btag_cferr2 CMS_btag_hfstats1_2018 CMS_btag_hf CMS_scale_JESRelativeBal CMS_res_j_2018 CMS_btag_hfstats1_2016 CMS_scale_JESHF_2016



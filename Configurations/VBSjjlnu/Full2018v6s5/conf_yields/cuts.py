# cuts

# Second lepton veto already done in post-processing 
#and Lepton WP setup in samples.py
supercut = '(   (abs(Lepton_pdgId[0])==11 && Lepton_pt[0]>35)\
             || (abs(Lepton_pdgId[0])==13 && Lepton_pt[0]>30 ) ) \
            && vbs_0_pt > 50 && vbs_1_pt > 30 \
            && PuppiMET_pt > 30 \
            && deltaeta_vbs >= 2.5  \
            && mjj_vbs >= 500 \
            '


#########################################################################
###############|----------------------------------|######################
###############|          Resolved category       |######################
###############|----------------------------------|######################
#########################################################################

#####################################
##  W-onshell, bveto --> Signal

cuts["res_sig_dnnall"] = 'VBS_category==1 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && mjj_vjet > 65 && mjj_vjet < 105 \
                        && bVeto \
                        && whad_pt < 200 \
                        && Mtw_lep < 185 \
                        '

cuts["res_sig_dnnhigh"] = 'VBS_category==1 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && mjj_vjet > 65 && mjj_vjet < 105 \
                        && bVeto \
                        && whad_pt < 200 \
                        && Mtw_lep < 185 \
                        && DNNoutput_resolved > 0.3 \
                        '

cuts["res_sig_fnal"] = 'VBS_category==1 \
                        && vbs_0_pt > 50 && vbs_1_pt > 50 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && mjj_vjet > 65 && mjj_vjet < 105 \
                        && bVeto \
                        && whad_pt < 200 \
                        && abs(whad_eta) < 2.5 \
                        '


##################################
# Won-shell, btag ---> top region

cuts["res_topcr_dnnall"] = 'VBS_category==1 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && mjj_vjet > 65 && mjj_vjet < 105 \
                        && bReq \
                        && whad_pt < 200 \
                        && Mtw_lep < 185 \
                        '

cuts["res_topcr_dnnhigh"] = 'VBS_category==1 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && mjj_vjet > 65 && mjj_vjet < 105 \
                        && bReq \
                        && whad_pt < 200 \
                        && Mtw_lep < 185 \
                        && DNNoutput_resolved > 0.3 \
                        '

cuts["res_topcr_fnal"] = 'VBS_category==1 \
                        && vbs_0_pt > 50 && vbs_1_pt > 50 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && mjj_vjet > 65 && mjj_vjet < 105 \
                        && bReq \
                        && whad_pt < 200 \
                        && abs(whad_eta) < 2.5 \
                        '

##################################
# Woff shell, bveto ---> WJet region

cuts["res_wjetcr_dnnall"] = 'VBS_category==1 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && (mjj_vjet <= 65 || mjj_vjet >= 105)  \
                        && bVeto \
                        && whad_pt < 200 \
                        && Mtw_lep < 185 \
                        '

cuts["res_wjetcr_dnnhigh"] = 'VBS_category==1 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && (mjj_vjet <= 65 || mjj_vjet >= 105)  \
                        && bVeto \
                        && whad_pt < 200 \
                        && Mtw_lep < 185 \
                        && DNNoutput_resolved > 0.3 \
                        '

cuts["res_wjetcr_fnal"] = 'VBS_category==1 \
                        && vbs_0_pt > 50 && vbs_1_pt > 50 \
                        && vjet_0_pt > 30 && vjet_1_pt > 30 \
                        && (mjj_vjet <= 65 || mjj_vjet >= 105)  \
                        && bVeto \
                        && whad_pt < 200 \
                        && abs(whad_eta) < 2.5 \
                        '


#########################################################################
###############|----------------------------------|######################
###############|          Boosted category       |######################
###############|----------------------------------|######################
#########################################################################


cuts["boost_sig_dnnall"] = 'VBS_category==0 \
                            && vjet_0_pt > 200 \
                            && mjj_vjet > 65 && mjj_vjet < 105 \
                            && bVeto \
                            '

cuts["boost_sig_dnnhigh"] = 'VBS_category==0 \
                            && vjet_0_pt > 200 \
                            && mjj_vjet > 65 && mjj_vjet < 105 \
                            && bVeto \
                            && DNNoutput_boosted > 0.3 \
                            '

cuts["boost_sig_fnal"] = 'VBS_category==0 \
                            && vbs_0_pt > 50 && vbs_1_pt > 50 \
                            && vjet_0_pt > 200 \
                            && mjj_vjet > 65 && mjj_vjet < 105 \
                            && bVeto \
                            '


###############################################
# Wjets

cuts["boost_topcr_dnnall"] = 'VBS_category==0 \
                            && vjet_0_pt > 200 \
                            && mjj_vjet > 65 && mjj_vjet < 105 \
                            && bReq \
                            '

cuts["boost_topcr_dnnhigh"] = 'VBS_category==0 \
                            && vjet_0_pt > 200 \
                            && mjj_vjet > 65 && mjj_vjet < 105 \
                            && bReq \
                            && DNNoutput_boosted > 0.3 \
                            '

cuts["boost_topcr_fnal"] = 'VBS_category==0 \
                            && vbs_0_pt > 50 && vbs_1_pt > 50 \
                            && vjet_0_pt > 200 \
                            && mjj_vjet > 65 && mjj_vjet < 105 \
                            && bReq \
                            '



###############################################
#Top

cuts["boost_wjetcr_dnnall"] = 'VBS_category==0 \
                            && vjet_0_pt > 200 \
                            &&  (mjj_vjet <= 65 || mjj_vjet >= 105) \
                            && bVeto \
                            '

cuts["boost_wjetcr_dnnhigh"] = 'VBS_category==0 \
                            && vjet_0_pt > 200 \
                            &&  (mjj_vjet <= 65 || mjj_vjet >= 105) \
                            && bVeto \
                            && DNNoutput_boosted > 0.3 \
                            '

cuts["boost_wjetcr_fnal"] = 'VBS_category==0 \
                            && vbs_0_pt > 50 && vbs_1_pt > 50 \
                            && vjet_0_pt > 200 \
                            &&  (mjj_vjet <= 65 || mjj_vjet >= 105) \
                            && bVeto \
                            '

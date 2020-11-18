# cuts

#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>25. \
            && Lepton_pt[1]>20. \
            && mll >76. && mll <106. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt[CleanJetNotFat_jetIdx],-9999.))>30. && fabs(Alt$(CleanJet_eta[CleanJetNotFat_jetIdx],-9999.))<5.0 \
            && mjj_max > 200 && detajj_mjjmax > 2.5 \
            '
#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet
cuts['preselection'] = '1.'

#######################################
#
#   BOOSTED CATEGORY
#   vbs_category = 0 (at least one FJ)
#######################################
cuts['Boosted_topcr']  = 'vbs_category==0 && nCleanFatJet==1 && Vjet_mass >65 && Vjet_mass<105 && bReqTight && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Boosted_DYcr']  = 'vbs_category==0 &&  nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Boosted_SR']  = 'vbs_category==0 && nCleanFatJet==1 && Vjet_mass > 65 && Vjet_mass<105 && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) '

#CR e SR without bReq or bVeto
#cuts['Boosted_topcr_noBtag']  = 'vbs_category==0 && nCleanFatJet==1 && Vjet_mass >65 && Vjet_mass<105  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

#cuts['Boosted_DYcr_noBveto']  = 'vbs_category==0 &&  nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105)  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Boosted_SR_tight']  = 'vbs_category==0 && nCleanFatJet==1 && Vjet_mass > 65 && Vjet_mass<105  && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Lepton_pt[0]>40.&& fabs(Alt$(CleanJet_pt[vbs_jet_0],-9999.))>80. && mjj_max>350'

#######################################
#
#   RESOLVED CATEGORY
#   vbs_category = 1
#######################################
cuts['Resolved_topcr']  = 'vbs_category==1 && bReqTight && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Resolved_DYcr']  = 'vbs_category==1 && bVeto && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Resolved_SR']  = 'vbs_category==1  && bVeto && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

#CR e SR without bReq or bVeto
#cuts['Resolved_topcr_noBtag']  = 'vbs_category==1  && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

#cuts['Resolved_DYcr_noBveto']  = 'vbs_category==1  && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Resolved_SR_tight']  = 'vbs_category==1  && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Lepton_pt[0]>40. && fabs(Alt$(CleanJet_pt[vbs_jet_0],-9999.))>80. && mjj_max>350'





# cuts

#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>35. \
            && Lepton_pt[1]>20. \
            && mll >76. && mll <106. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2  \
            && mjj_max > 500 && detajj_mjjmax > 2.5 \
            && vbs_category==0 \
            '

#&& fabs(Alt$(CleanJet_pt[CleanJetNotFat_jetIdx],-9999.))>30. && fabs(Alt$(CleanJet_eta[CleanJetNotFat_jetIdx],-9999.))<5.0


#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet
#cuts['preselection'] = '1.'

#######################################
#
#   BOOSTED CATEGORY
#   vbs_category = 0 (at least one FJ)
#######################################
cuts['Boosted_topcr']  = 'nCleanFatJet==1 && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'
#cuts['Boosted_DYcr_bVeto']  = 'bVeto && nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#cuts['Boosted_DYcr_bTag']  = 'bReq && nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#cuts['Boosted_SR_bVeto']  = 'bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Vjet_mass > 65 && Vjet_mass <105'
#cuts['Boosted_SR_bTag']  = 'bReq && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Vjet_mass > 65 && Vjet_mass <105'


#cuts['Boosted_DYcr_bVeto_ext']  = 'bVeto && nCleanFatJet==1 && ( Vjet_mass<50 || Vjet_mass>150) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#cuts['Boosted_DYcr_bVeto_int']  = 'bVeto && nCleanFatJet==1 && ( (Vjet_mass>50 && Vjet_mass<65) || (Vjet_mass>105 && Vjet_mass<150) ) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#cuts['Boosted_DYcr_bTag_ext']  = 'bReq && nCleanFatJet==1 && ( Vjet_mass<50 || Vjet_mass>150) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'
#cuts['Boosted_DYcr_bTag_int']  = 'bReq && nCleanFatJet==1 && ( (Vjet_mass>50 && Vjet_mass<65) || (Vjet_mass>105 && Vjet_mass<150) ) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

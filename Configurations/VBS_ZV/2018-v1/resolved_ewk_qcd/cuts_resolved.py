# cuts

#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>35. \
            && Lepton_pt[1]>20. \
            && mll >76. && mll <106. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2  \
            && mjj_max > 500 && detajj_mjjmax > 2.5 \
            && vbs_category==1 \
            '

#&& fabs(Alt$(CleanJet_pt[CleanJetNotFat_jetIdx],-9999.))>30. && fabs(Alt$(CleanJet_eta[CleanJetNotFat_jetIdx],-9999.))<5.0


#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet
#cuts['preselection'] = '1.'

#######################################
#
#   RESOLVED CATEGORY
#   vbs_category = 1
#######################################
cuts['Resolved_topcr']  = 'Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'


cuts['Resolved_DYcr_bVeto']  = 'bVeto && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Resolved_DYcr_bTag']  = 'bReq && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'


cuts['Resolved_SR_bVeto']  = 'bVeto &&(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Vjet_mass > 65 && Vjet_mass <105'

cuts['Resolved_SR_bTag']  = 'bReq &&(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13) && Vjet_mass > 65 && Vjet_mass <105'
#commented out for this year since the DNN model was bugged, check "testDNN" folder > this was true for 6Dec2023 release, then I updated the aliases.py to just include the correct model for resoolved b-tag 2018 

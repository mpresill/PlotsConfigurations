# cuts

#cuts = {}
supercut = '   nLepton == 2 \
            && Lepton_pt[0]>25. \
            && Lepton_pt[1]>15. \
            && mll >60. && mll <120. \
            && abs(Lepton_eta[0])<2.5 && abs(Lepton_eta[1])<2.5 \
            && nCleanJetNotFat >= 2 && fabs(Alt$(CleanJet_pt[CleanJetNotFat_jetIdx],-9999.))>30. && fabs(Alt$(CleanJet_eta[CleanJetNotFat_jetIdx],-9999.))<5.0 \
            && mjj_max > 200 && detajj_mjjmax > 2.0 \
            '
#I have considered all CleanedJetNotFat, i.e. cleaned from AK8, since in the case in which nCleanFatJet==0 => nCleanJetNotFat = NCleanJet
cuts['preselection'] = '1.'

#this part is for a cutflow study in selection:
#cuts['Lepton_pt[0]_40']='Lepton_pt[0]>40'
#cuts['mjj_max_400']='400'
#cuts['Zlep1_0.7']='fabs(( Lepton_eta[0]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax) < 0.7'
#cuts['Zlep2_0.5']='fabs(( Lepton_eta[1]-0.5*(CleanJet_eta[vbs_jet_0]+CleanJet_eta[vbs_jet_1]) )/detajj_mjjmax) < 0.5'
#cuts['ptVBSjet1_50']='CleanJet_pt[v_jet_0]>50'
#cuts['bVeto']='bVeto'
#cuts['Vjet_mass_window']='Vjet_mass >65 && Vjet_mass<105'


#######################################
#
#   BOOSTED CATEGORY
#   vbs_category = 0 (at least one FJ)
#######################################
cuts['Boosted_topcr']  = 'vbs_category==0 && nCleanFatJet==1 && Vjet_mass >65 && Vjet_mass<105 && bReqTight && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Boosted_DYcr']  = 'vbs_category==0 &&  nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105) && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Boosted_topcr_noBtag']  = 'vbs_category==0 && nCleanFatJet==1 && Vjet_mass >65 && Vjet_mass<105 &&(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Boosted_DYcr_noBVeto']  = 'vbs_category==0 &&  nCleanFatJet==1 && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'




#PUT SOME TIGHTER CUTS ON SR 

#cuts['Boosted_SR']  = 'vbs_category==0 &&  mll>76. && mll<106. && nCleanFatJet==1 && Vjet_mass > 65 && Vjet_mass<105 && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

#cuts['Boosted_SR_tight']  = 'vbs_category==0 && mjj_max > 350 && mll>76. && mll<106. && nCleanFatJet==1 && Vjet_mass > 65 && Vjet_mass<105 && bVeto && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

#######################################
#
#   RESOLVED CATEGORY
#   vbs_category = 1
#######################################
cuts['Resolved_topcr']  = 'vbs_category==1 && bReqTight && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Resolved_DYcr']  = 'vbs_category==1 && bVeto && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

cuts['Resolved_topcr_noBtag']  = 'vbs_category==1 && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'

cuts['Resolved_DYcr_noBVeto']  = 'vbs_category==1 && ( Vjet_mass<65 || Vjet_mass>105) && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

#cuts['Resolved_SR']  = 'vbs_category==1 && mll>76. && mll<106. && bVeto && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'

#cuts['Resolved_SR_tight']  = 'vbs_category==1 && mjj_max > 350 && mll>76. && mll<106. && bVeto && Vjet_mass >65 && Vjet_mass<105 && (Lepton_pdgId[0]*Lepton_pdgId[1] == -11*11 || Lepton_pdgId[0]*Lepton_pdgId[1] == -13*13)'


# 11 = e
# 13 = mu

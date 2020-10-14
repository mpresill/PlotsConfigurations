 # VH2j cuts


#-------------------------------------------------------------------------------
# supercut
#-------------------------------------------------------------------------------
_tmp = [
     'Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13',
     'Lepton_pt[0] > 25.',
     'Lepton_pt[1] > 10.',
     '(abs(Lepton_pdgId[1]) == 13 || Lepton_pt[1] > 13.)',
     '(nLepton >= 2 && Alt$(Lepton_pt[2], 0) < 10.)',
     'mll > 12.',
     'ptll > 30.',
     'PuppiMET_pt > 20.', 
     ]

supercut = ' && '.join(_tmp)


def addcut(name, exprs):
    cuts[name] = ' && '.join(exprs)


#-------------------------------------------------------------------------------
# VH_2j_em
#-------------------------------------------------------------------------------
_tmp = [
     'Alt$(CleanJet_pt[1], 0) > 30.', 
     'abs(CleanJet_eta[0]) < 2.5',
     'abs(CleanJet_eta[1]) < 2.5',
     'mth > 60.',
     'mth < 125.',
     'drll < 2.',
     'mjj > 65.',
     'mjj < 105.',
     'detajj < 3.5',
     'bVeto',
     #'Jet_qgl[CleanJet_jetIdx[0]] > 0.4',
     #'Jet_qgl[CleanJet_jetIdx[1]] > 0.3',
     ]

addcut('VH_2j_emu', _tmp)


#-------------------------------------------------------------------------------
# VH_2j_topemu
#-------------------------------------------------------------------------------
_tmp = [
     'Alt$(CleanJet_pt[1], 0) > 30.',  
     'abs(CleanJet_eta[0]) < 2.5',
     'abs(CleanJet_eta[1]) < 2.5',
     'mjj > 65.',
     'mjj < 105.',
     'detajj < 3.5', 
     'bReq',
     'mll > 50.',
     ]

addcut('VH_2j_topemu', _tmp)


#-------------------------------------------------------------------------------
# VH_2j_DYtautau
#-------------------------------------------------------------------------------
_tmp = [
     'Alt$(CleanJet_pt[1], 0) > 30.',  
     'abs(CleanJet_eta[0]) < 2.5',
     'abs(CleanJet_eta[1]) < 2.5',
     'mth < 60.',
     'drll < 2.',
     'bVetoDY',
     'mjj > 65.',
     'mjj < 105.',
     'detajj < 3.5',
     'mll > 40.',
     'mll < 80.',
     ]

addcut('VH_2j_DYtautau', _tmp)

import os
import copy
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

#aliases = {}

# imported from samples.py:
# samples, signals

mc = [skey for skey in samples if skey not in ('Fake', 'DATA', 'Dyemb')]
mc_emb = [skey for skey in samples if skey not in ('Fake', 'DATA')]

eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'

newEleWP = 'mvaFall17V1Iso_WP90' # same as nominal
#newEleWP = 'mvaFall17V1Iso_WP90_tthmva_70'
newMuWP = 'cut_Tight_HWWW_tthmva_80'

aliases['LepWPCut'] = {
    ### eleWP + muWP combination
    #'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    ### eleWP + newMuWP combination
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP+'*((abs(Lepton_pdgId[0])==11 || Muon_mvaTTH[Lepton_muonIdx[0]]>0.8) && (abs(Lepton_pdgId[1])==11 || Muon_mvaTTH[Lepton_muonIdx[1]]>0.8))',
    ### newEleWP + newMuWP combination
    #'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP+'*((abs(Lepton_pdgId[0])==11 || Muon_mvaTTH[Lepton_muonIdx[0]]>0.8) && (abs(Lepton_pdgId[1])==11 || Muon_mvaTTH[Lepton_muonIdx[1]]>0.8) && (abs(Lepton_pdgId[0])==13 || Electron_mvaTTH[Lepton_electronIdx[0]]>0.70) && (abs(Lepton_pdgId[1])==13 || Electron_mvaTTH[Lepton_electronIdx[1]]>0.70))',
    'samples': mc_emb + ['DATA']
}

aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

aliases['embedtotal'] = {
    'expr': 'embed_total_WP90V1',  # wrt. eleWP
    'samples': 'Dyemb'
}

# Fake leptons transfer factor 
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+newMuWP+'_statMuDown',
    'samples': ['Fake']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top', 'Dyveto']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top', 'Dyveto']
}

aliases['topGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}


# Obtained from Dennis on 2020/06/26
aliases['Top_pTrw'] = {
    #'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + isSingleTop',
    'expr': '(topGenPt * antitopGenPt > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPt) - 0.000134*topGenPt + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPt) - 0.000134*antitopGenPt + 0.973))) + (topGenPt * antitopGenPt <= 0.)',
    'samples': ['top']
}


# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

# No jet with pt > 30 GeV
aliases['zeroJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) < 30.'
}

aliases['oneJet'] = {
    'expr': 'Alt$(CleanJet_pt[0], 0) > 30.'
}

aliases['multiJet'] = {
    'expr': 'Alt$(CleanJet_pt[1], 0) > 30.'
}

# B tagging

aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0) && mth > 60' }


aliases['bVetoDY'] = {                                                                                                              
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0) && mth < 60'                       
}

aliases['bReq'] = {    
    'expr': 'Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1'
}




# B tag scale factors

aliases['bVetoSF'] = {
'expr': '( TMath::Exp(Sum$( TMath::Log( (CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<20 || abs(CleanJet_eta)>2.5) ) ) ) )',
'samples': mc
}


aliases['bVetoDYSF'] = {                                                                                                            
'expr': '( TMath::Exp(Sum$( TMath::Log( (CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_shape[CleanJet_jetIdx]+1*(CleanJet_pt<30 || abs(CleanJet_eta)>2.5) ) ) ) )',
'samples': mc
}                                                                                                                                    
aliases['bReqSF'] = {
'expr': '( ( ( Alt$(CleanJet_pt[0], 0)>30 && Alt$(abs(CleanJet_eta[0]),99)<2.5 )*( Alt$(Jet_btagSF_shape[CleanJet_jetIdx[0]], 1) ) + ( Alt$(CleanJet_pt[0], 0)<30 || Alt$(abs(CleanJet_eta[0]),99)>2.5 ) )* \
           ( ( Alt$(CleanJet_pt[1], 0)>30 && Alt$(abs(CleanJet_eta[1]),99)<2.5 )*( Alt$(Jet_btagSF_shape[CleanJet_jetIdx[1]], 1) ) + ( Alt$(CleanJet_pt[1], 0)<30 || Alt$(abs(CleanJet_eta[1]),99)>2.5 ) ) )\
        ',
'samples': mc
}


aliases['btagSF'] = {
  'expr': '( bVetoSF*bVeto +  bVetoDYSF*bVetoDY + bReqSF*bReq + ( (!bVeto) && (!bVetoDY) &&  (!bReq) ) )',
'samples': mc
}



for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

    for targ in ['bVeto', 'bVetoDY', 'bReq']:
        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)

        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)

    aliases['btagSF%sup' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
        'samples': mc
    }

    aliases['btagSF%sdown' % shift] = {
        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
        'samples': mc
    }

# PU jet Id SF

puidSFSource = '{}/patches/PUID_80XTraining_EffSFandUncties.root'.format(configurations)

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/patches/pujetidsf_event_new.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, '2018', 'loose'),
    'samples': mc
}

# data/MC scale factors
aliases['ttHMVA_SF_2l'] = {   'linesToAdd': ['.L %s/patches/compute_SF.C+' % configurations],
                        'class': 'compute_SF',
                        'args' : ('2018', 2, 'total_SF'),
                        'samples': mc_emb
}

aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'ttHMVA_SF_2l', 'LepWPCut', 'btagSF','PUJetIdSF']),
    'samples': mc
}

# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc_emb
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc_emb
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc_emb
}


aliases['ttHMVA_SF_Up_0'] = {'linesToAdd': ['.L %s/patches/compute_SF.C+' % configurations],
                             'class': 'compute_SF',
                             'args' : ('2018', 2, 'single_SF_up', 0),
                             'samples': mc_emb
                            }
aliases['ttHMVA_SF_Up_1'] = {'linesToAdd': ['.L %s/patches/compute_SF.C+' % configurations],
                             'class': 'compute_SF',
                             'args' : ('2018', 2, 'single_SF_up', 1),
                             'samples': mc_emb
                            }
aliases['ttHMVA_SF_Down_0'] = {'linesToAdd': ['.L %s/patches/compute_SF.C+' % configurations],
                               'class': 'compute_SF',
                               'args' : ('2018', 2, 'single_SF_down', 0),
                               'samples': mc_emb
                              }
aliases['ttHMVA_SF_Down_1'] = {'linesToAdd': ['.L %s/patches/compute_SF.C+' % configurations],
                               'class': 'compute_SF',
                               'args' : ('2018', 2, 'single_SF_down', 1),
                               'samples': mc_emb
                              }
aliases['ttHMVA_2l_mu_SF_Up'] = {'expr' : '(ttHMVA_SF_Up_0*(TMath::Abs(Lepton_pdgId[0]) == 13) + (TMath::Abs(Lepton_pdgId[0]) == 11)) *\
                                           (ttHMVA_SF_Up_1*(TMath::Abs(Lepton_pdgId[1]) == 13) + (TMath::Abs(Lepton_pdgId[1]) == 11))',
                                 'samples': mc_emb
                                }
aliases['ttHMVA_2l_mu_SF_Down'] = {'expr' : '(ttHMVA_SF_Down_0*(TMath::Abs(Lepton_pdgId[0]) == 13) + (TMath::Abs(Lepton_pdgId[0]) == 11)) *\
                                             (ttHMVA_SF_Down_1*(TMath::Abs(Lepton_pdgId[1]) == 13) + (TMath::Abs(Lepton_pdgId[1]) == 11))',
                                   'samples': mc_emb
                                  }

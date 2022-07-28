import os
import copy
import inspect



configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2016
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations


# imported from samples.py:
# samples, signals
mc = [skey for skey in samples if skey not in ('Fake', 'DATA')]


eleWP='mvaFall17V1Iso_WP90'
muWP='cut_Tight_HWWW'


aliases['LepWPCut'] = {
    'expr': 'LepCut2l__ele_'+eleWP+'__mu_'+muWP,
    'samples': mc + ['DATA']
}

# gen-matching to prompt only (GenLepMatch2l matches to *any* gen lepton)
aliases['PromptGenLepMatch2l'] = {
    'expr': 'Alt$(Lepton_promptgenmatched[0]*Lepton_promptgenmatched[1], 0)',
    'samples': mc
}

##additional variables for VgS
aliases['gstarLow'] = {
    'expr': 'Gen_ZGstar_mass >0 && Gen_ZGstar_mass < 4',
    'samples': 'VgS'
}

aliases['gstarHigh'] = {
    'expr': 'Gen_ZGstar_mass <0 || Gen_ZGstar_mass > 4',
    'samples': 'VgS'
}

###########################################################
################fakes
###########################################################
# Fake leptons transfer factor
aliases['fakeW'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP,
    'samples': ['Fake']
}
# And variations - already divided by central values in formulas !
aliases['fakeWEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleUp',
    'samples': ['Fake']
}
aliases['fakeWEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_EleDown',
    'samples': ['Fake']
}
aliases['fakeWMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuUp',
    'samples': ['Fake']
}
aliases['fakeWMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_MuDown',
    'samples': ['Fake']
}
aliases['fakeWStatEleUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleUp',
    'samples': ['Fake']
}
aliases['fakeWStatEleDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statEleDown',
    'samples': ['Fake']
}
aliases['fakeWStatMuUp'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuUp',
    'samples': ['Fake']
}
aliases['fakeWStatMuDown'] = {
    'expr': 'fakeW2l_ele_'+eleWP+'_mu_'+muWP+'_statMuDown',
    'samples': ['Fake']
}





############################################################
############# VBS variables for jet pairing
############################################################
mva_reader_path = '%s/Configurations/VBS_ZV/mva_macros/' % configurations
models_path = '/eos/home-a/ahakimi/www/ZV_analysis/Models/All_years_nobtag'
#models_path = '/eos/user/m/mpresill/www/VBS/Numpy/Alex/'
models_path_pruned = '/eos/home-a/ahakimi/www/ZV_analysis/Models/pruned_SR'

aliases['vbs_category'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned.cc+' % configurations 
    ],
    'class': 'jets_cat_dnn',
    'args': ('vbs_category','2018',models_path,models_path_pruned, False)
}

aliases['vbs_jet_0'] = {
   'class': 'jets_cat_dnn',
    'args': ('vbs_jet_0','2018', models_path,models_path_pruned, False)
}

aliases['vbs_jet_1'] = {
    'class': 'jets_cat_dnn',
    'args': ('vbs_jet_1','2018', models_path,models_path_pruned, False)
}

aliases['v_jet_0'] = {
   'class': 'jets_cat_dnn',
    'args': ('v_jet_0','2018', models_path,models_path_pruned, False)
}

aliases['v_jet_1'] = {
   'class': 'jets_cat_dnn',
    'args': ('v_jet_1','2018', models_path,models_path_pruned, False)
}


aliases['mjj_max'] = {
   'class': 'jets_cat_dnn',
    'args': ('mjj_max','2018', models_path,models_path_pruned, False)
}

aliases['detajj_mjjmax'] = {
   'class': 'jets_cat_dnn',
    'args': ('detajj_mjjmax','2018', models_path,models_path_pruned, False)
}

aliases['dphijj_mjjmax'] = {
   'class': 'jets_cat_dnn',
    'args': ('dphijj_mjjmax','2018', models_path,models_path_pruned, False)
}

aliases['Vjet_mass'] = {
   'class': 'jets_cat_dnn',
    'args': ('Vjet_mass','2018', models_path,models_path_pruned, False)
}

aliases['njet30'] = {
   'class': 'jets_cat_dnn',
    'args': ('njet30','2018', models_path, models_path_pruned,False)
}

aliases['nbtag'] = {
   'class': 'jets_cat_dnn',
    'args': ('nbtag','2018', models_path,models_path_pruned, False)
}

aliases['Zleppt'] = {
   'class': 'jets_cat_dnn',
    'args': ('Zleppt','2018', models_path,models_path_pruned, False)
}

aliases['Vpt'] = {
   'class': 'jets_cat_dnn',
    'args': ('Vpt','2018', models_path,models_path_pruned, False)
}
 
aliases['V_jet_mass'] = {
    'expr': 'Vjet_mass'
}
###########################################################
##############  fitting phase space
###########################################################

#fitting 2D with VBS pt2 and Z pt binning
aliases['fit_Z_vbs1_bin_Resolved'] = {
    'expr': '(vbs_category==1)*( \
            1*(  CleanJet_pt[vbs_jet_1] < 50                                          && Zleppt < 350  ) +\
            2*(  CleanJet_pt[vbs_jet_1] >= 50   &&  CleanJet_pt[vbs_jet_1] < 120      && Zleppt < 350  ) +\
            3*(  CleanJet_pt[vbs_jet_1] >= 120  &&  CleanJet_pt[vbs_jet_1] < 150      && Zleppt < 350  ) +\
            4*(  CleanJet_pt[vbs_jet_1] >= 150  &&  CleanJet_pt[vbs_jet_1] < 200      && Zleppt < 350  ) +\
            5*(  CleanJet_pt[vbs_jet_1] >= 200                                        && Zleppt < 350  ) +\
            6*(  Zleppt >= 350                                                                         ) \
            ) + (vbs_category==0)*(-1)'
}


#fitting with Z pt binning
aliases['fit_Z_bin_Resolved'] = {
    'expr': '(vbs_category==1)*( \
            1*(  Zleppt < 50                           ) +\
            2*(  Zleppt >= 50   &&  Zleppt < 100       ) +\
            3*(  Zleppt >= 100  &&  Zleppt < 150       ) +\
            4*(  Zleppt >= 150  && Zleppt < 250        ) +\
            5*(  Zleppt >= 250  && Zleppt < 500        ) +\
            6*(  Zleppt >= 500                         ) \
            ) + (vbs_category==0)*(-1)'
}

aliases['fit_Z_bin_Boosted'] = {
    'expr': '(vbs_category==0)*( \
            1*(  Zleppt < 50                           ) +\
            2*(  Zleppt >= 50   &&  Zleppt < 100       ) +\
            3*(  Zleppt >= 100  &&  Zleppt < 150       ) +\
            4*(  Zleppt >= 150  && Zleppt < 250        ) +\
            5*(  Zleppt >= 250  && Zleppt < 500        ) +\
            6*(  Zleppt >= 500                         ) \
            ) + (vbs_category==1)*(-1)'
}


#fitting using laeding VBS jet pt 
aliases['fit_vbs0_bin_Resolved'] = {
    'expr': '(vbs_category==1)*( \
            1*(  CleanJet_pt[vbs_jet_0] < 50                                            ) +\
            2*(  CleanJet_pt[vbs_jet_0] >= 50   &&  CleanJet_pt[vbs_jet_0] < 120        ) +\
            3*(  CleanJet_pt[vbs_jet_0] >= 120  &&  CleanJet_pt[vbs_jet_0] < 200        ) +\
            4*(  CleanJet_pt[vbs_jet_0] >= 200  &&  CleanJet_pt[vbs_jet_0] < 300        ) +\
            5*(  CleanJet_pt[vbs_jet_0] >= 300  &&  CleanJet_pt[vbs_jet_0] < 400        ) +\
            6*(  CleanJet_pt[vbs_jet_0] >= 400                                          ) \
            ) + (vbs_category==0)*(-1)'
}

#fitting using sub-leading VBS jet pt 
aliases['fit_vbs1_bin_Resolved'] = {
    'expr': '(vbs_category==1)*( \
            1*(  CleanJet_pt[vbs_jet_1] < 50                                            ) +\
            2*(  CleanJet_pt[vbs_jet_1] >= 50   &&  CleanJet_pt[vbs_jet_1] < 120        ) +\
            3*(  CleanJet_pt[vbs_jet_1] >= 120  &&  CleanJet_pt[vbs_jet_1] < 150        ) +\
            4*(  CleanJet_pt[vbs_jet_1] >= 150  &&  CleanJet_pt[vbs_jet_1] < 200        ) +\
            5*(  CleanJet_pt[vbs_jet_1] >= 200  &&  CleanJet_pt[vbs_jet_1] < 250        ) +\
            6*(  CleanJet_pt[vbs_jet_1] >= 250                                          ) \
            ) + (vbs_category==0)*(-1)'
}

#fitting using Delta Eta VBS jets
aliases['fit_detajj_bin_Resolved'] = {
    'expr': '(vbs_category==1)*( \
            1*(  detajj_mjjmax < 3.5                                             ) +\
            2*(  detajj_mjjmax >= 3.5 &&  detajj_mjjmax < 4.5                    ) +\
            3*(  detajj_mjjmax >= 4.5 &&  detajj_mjjmax < 5.5                    ) +\
            4*(  detajj_mjjmax >= 5.5 &&  detajj_mjjmax < 6.5                    ) +\
            5*(  detajj_mjjmax >= 6.5 &&  detajj_mjjmax < 7.5                    ) +\
            6*(  detajj_mjjmax >= 7.5                                            ) \
            ) + (vbs_category==0)*(-1)'
}


############################################################
############################################################

# PostProcessing did not create (anti)topGenPt for ST samples with _ext1
lastcopy = (1 << 13)

aliases['isTTbar'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 2' % lastcopy,
    'samples': ['top']
}

aliases['isSingleTop'] = {
    'expr': 'Sum$(TMath::Abs(GenPart_pdgId) == 6 && TMath::Odd(GenPart_statusFlags / %d)) == 1' % lastcopy,
    'samples': ['top']
}
#added 20.11
aliases['topGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}
#added 20.11
aliases['antitopGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}


aliases['Top_pTrw'] = {
	    # New Top PAG added 20.11
    'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) * (TMath::Sqrt(TMath::Exp(1.61468e-03 + 3.46659e-06*topGenPtOTF - 8.90557e-08*topGenPtOTF*topGenPtOTF) * TMath::Exp(1.61468e-03 + 3.46659e-06*antitopGenPtOTF - 8.90557e-08*antitopGenPtOTF*antitopGenPtOTF))) + (topGenPtOTF * antitopGenPtOTF <= 0.)', # Same Reweighting as other years, but with additional fix for tune CUET -> CP5
 #'expr': 'isTTbar * (TMath::Sqrt(TMath::Exp(0.0615 - 0.0005 * topGenPt) * TMath::Exp(0.0615 - 0.0005 * antitopGenPt))) + isSingleTop',
    'samples': ['top']
}



# Jet bins
# using Alt$(CleanJet_pt[n], 0) instead of Sum$(CleanJet_pt >= 30) because jet pt ordering is not strictly followed in JES-varied samples

############b tag
# B tagging
#loose 0.1241
#tight 0.7527
aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1241) >= 1)'
}

aliases['bReqTight'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.7527) >= 1)'
}

aliases['bVetoSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>20 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=20 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['bReqSF'] = {
    'expr': 'TMath::Exp(Sum$(TMath::Log((CleanJet_pt>30 && abs(CleanJet_eta)<2.5)*Jet_btagSF_deepcsv_shape[CleanJet_jetIdx]+1*(CleanJet_pt<=30 || abs(CleanJet_eta)>=2.5))))',
    'samples': mc
}

aliases['btagSF'] = {
    'expr': 'bVeto*bVetoSF + bReqTight *bReqSF',
    'samples': mc
}


systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
  aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
  aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc }

"""
for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:

    for targ in ['bVeto', 'bReq']:
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
"""
#########################################################################################

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/src/PlotsConfigurations/Configurations/Differential/ngenjet.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'CountGenJet',
    'samples': mc
}

##### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'getGenZpt',
    'samples': ['DY']
}
handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2018']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2018']['LO'].replace('x', 'getGenZpt_OTF')+')*(nCleanGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}


###########################################################################################
# PU jet Id SF

# PU jet Id SF

puidSFSource = '{}/Configurations/patches/PUID_81XTraining_EffSFandUncties.root'.format(configurations)

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/Configurations/VBS_ZV/patches/pujetidsf_event_new.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, "2018", "loose"),
    'samples': mc
}

# PU jet Id SF ALTERNATIVE IMPLEMENTATION
aliases['Jet_PUIDSF'] = { 
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose)))',
  'samples': mc
}

aliases['Jet_PUIDSF_up'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_up)))',
  'samples': mc
}

aliases['Jet_PUIDSF_down'] = {
  'expr' : 'TMath::Exp(Sum$((Jet_jetId>=2)*TMath::Log(Jet_PUIDSF_loose_down)))',
  'samples': mc
}



# data/MC scale factors
"""aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut', 'btagSF','PUJetIdSF']),
    'samples': mc
}
"""
#nobtag sf test
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l', 'LepSF2l__ele_' + eleWP + '__mu_' + muWP, 'LepWPCut','PUJetIdSF', 'btagSF' ]),
    'samples': mc
}
# variations
aliases['SFweightEleUp'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Up',
    'samples': mc
}
aliases['SFweightEleDown'] = {
    'expr': 'LepSF2l__ele_'+eleWP+'__Do',
    'samples': mc
}
aliases['SFweightMuUp'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Up',
    'samples': mc
}
aliases['SFweightMuDown'] = {
    'expr': 'LepSF2l__mu_'+muWP+'__Do',
    'samples': mc
}


models_path_pruned = '/eos/home-a/ahakimi/www/ZV_analysis/Models/pruned_oldSR'
models_path_full = '/eos/home-a/ahakimi/www/ZV_analysis/Models/full_oldSR'
aliases['DNNoutput_full'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('dnn_output','2018', models_path_full,models_path_pruned, False)
}


mva_reader_path = '%s/Configurations/VBS_ZV/mva_macros/' % configurations
models_path_pruned = '/eos/home-a/ahakimi/www/ZV_analysis/Models/pruned_SR'

aliases['DNNoutput_pruned'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn_pruned.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('dnn_output_pruned','2018', models_path,models_path_pruned, False)
}



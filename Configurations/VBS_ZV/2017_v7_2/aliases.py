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

#aliases['LepWPSF'] = {
#    'expr': 'LepSF2l__ele_'+eleWP+'__mu_'+muWP,
#    'samples': mc
#}

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



aliases['vbs_category'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations 
    ],
    'class': 'jets_cat_dnn',
    'args': ('vbs_category','2017',models_path, True)
}

aliases['vbs_jet_0'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('vbs_jet_0','2017', models_path, True)
}

aliases['vbs_jet_1'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('vbs_jet_1','2017', models_path, True)
}

aliases['v_jet_0'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('v_jet_0','2017', models_path, True)
}

aliases['v_jet_1'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('v_jet_1','2017', models_path, True)
}


aliases['mjj_max'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('mjj_max','2017', models_path, True)
}

aliases['detajj_mjjmax'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
	],
    'class': 'jets_cat_dnn',
    'args': ('detajj_mjjmax','2017', models_path, True)
}

aliases['dphijj_mjjmax'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('dphijj_mjjmax','2017', models_path, True)
}

aliases['Vjet_mass'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('Vjet_mass','2017', models_path, True)
}

aliases['njet30'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('njet30','2017', models_path, True)
}

aliases['nbtag'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('nbtag','2017', models_path, True)
}

aliases['Zleppt'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('Zleppt','2017', models_path, True)
}


aliases['V_jet_mass'] = {
    'expr': 'Vjet_mass'
}


###########################################################
##############  fitting phase space
###########################################################
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
#aliases['fit_vbs0_bin_Resolved'] = {
#    'expr': '(vbs_category==1)*( \
#            1*(  CleanJet_pt[vbs_jet_0] < 50                                            ) +\
#            2*(  CleanJet_pt[vbs_jet_0] >= 50   &&  CleanJet_pt[vbs_jet_0] < 120        ) +\
#            3*(  CleanJet_pt[vbs_jet_0] >= 120  &&  CleanJet_pt[vbs_jet_0] < 200        ) +\
#            4*(  CleanJet_pt[vbs_jet_0] >= 200  &&  CleanJet_pt[vbs_jet_0] < 300        ) +\
#            5*(  CleanJet_pt[vbs_jet_0] >= 300  &&  CleanJet_pt[vbs_jet_0] < 400        ) +\
#            6*(  CleanJet_pt[vbs_jet_0] >= 400                                          ) \
#            ) + (vbs_category==0)*(-1)'
#}

#fitting using sub-leading VBS jet pt 
#aliases['fit_vbs1_bin_Resolved'] = {
#    'expr': '(vbs_category==1)*( \
#            1*(  CleanJet_pt[vbs_jet_1] < 50                                            ) +\
#            2*(  CleanJet_pt[vbs_jet_1] >= 50   &&  CleanJet_pt[vbs_jet_1] < 120        ) +\
#            3*(  CleanJet_pt[vbs_jet_1] >= 120  &&  CleanJet_pt[vbs_jet_1] < 150        ) +\
#            4*(  CleanJet_pt[vbs_jet_1] >= 150  &&  CleanJet_pt[vbs_jet_1] < 200        ) +\
#            5*(  CleanJet_pt[vbs_jet_1] >= 200  &&  CleanJet_pt[vbs_jet_1] < 250        ) +\
#            6*(  CleanJet_pt[vbs_jet_1] >= 250                                          ) \
#            ) + (vbs_category==0)*(-1)'
#}



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

aliases['topGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == 6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}

aliases['antitopGenPtOTF'] = {
    'expr': 'Sum$((GenPart_pdgId == -6 && TMath::Odd(GenPart_statusFlags / %d)) * GenPart_pt)' % lastcopy,
    'samples': ['top']
}
aliases['Top_pTrw'] = {
    'expr': '(topGenPtOTF * antitopGenPtOTF > 0.) * (TMath::Sqrt((0.103*TMath::Exp(-0.0118*topGenPtOTF) - 0.000134*topGenPtOTF + 0.973) * (0.103*TMath::Exp(-0.0118*antitopGenPtOTF) - 0.000134*antitopGenPtOTF + 0.973))) + (topGenPtOTF * antitopGenPtOTF <= 0.)',
    'samples': ['top']
}

#########################################################################################
############  b tag
#########################################################################################

# B tagging 2017:
# https://twiki.cern.ch/twiki/bin/viewauth/CMS/BtagRecommendation94X 
#loose 0.1522
#tight 0.8001

aliases['bVeto'] = {
    'expr': '(Sum$(CleanJet_pt > 20. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) == 0)'
}

aliases['bReq'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.1522) >= 1)'
}

aliases['bReqTight'] = {
    'expr': '(Sum$(CleanJet_pt > 30. && abs(CleanJet_eta) < 2.5 && Jet_btagDeepB[CleanJet_jetIdx] > 0.8001) >= 1)'
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
    'expr': 'bVeto*bVetoSF + bReq *bReqSF',
    'samples': mc
}

systs = ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']

for s in systs:
  aliases['btagSF'+s+'up'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_up_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_up_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc  }
  aliases['btagSF'+s+'down'] = { 'expr': '(bVeto*'+aliases['bVetoSF']['expr'].replace('shape','shape_down_'+s)+'+bReq*'+aliases['bReqSF']['expr'].replace('shape','shape_down_'+s)+'+ ( (!bVeto) && (!bReq) ))', 'samples':mc }



#for shift in ['jes','lf','hf','lfstats1','lfstats2','hfstats1','hfstats2','cferr1','cferr2']:
#
#    for targ in ['bVeto', 'bReq']:
#        alias = aliases['%sSF%sup' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_up_%s' % shift)
#
#        alias = aliases['%sSF%sdown' % (targ, shift)] = copy.deepcopy(aliases['%sSF' % targ])
#        alias['expr'] = alias['expr'].replace('btagSF_shape', 'btagSF_shape_down_%s' % shift)
#
#    aliases['btagSF%sup' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'up'),
#        'samples': mc
#    }
#
#    aliases['btagSF%sdown' % shift] = {
#        'expr': aliases['btagSF']['expr'].replace('SF', 'SF' + shift + 'down'),
#        'samples': mc
#    }

#########################################################################################
##### DY pt reweigthing: what is the source of this correctin? EW/QCD NLO? not sure
#########################################################################################

#### DY Z pT reweighting
aliases['getGenZpt_OTF'] = {
    'linesToAdd':['.L %s/src/PlotsConfigurations/Configurations/patches/getGenZpt.cc+' % os.getenv('CMSSW_BASE')],
    'class': 'getGenZpt',
    'samples': ['DY']
}

aliases['nCleanGenJet'] = {
    'linesToAdd': ['.L %s/Configurations/Differential/ngenjet.cc+' % configurations],
    'class': 'CountGenJet',
    'samples': mc
}

handle = open('%s/src/PlotsConfigurations/Configurations/patches/DYrew30.py' % os.getenv('CMSSW_BASE'),'r')
exec(handle)
handle.close()
aliases['DY_NLO_pTllrw'] = {
    'expr': '('+DYrew['2017']['NLO'].replace('x', 'getGenZpt_OTF')+')*(nGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}
aliases['DY_LO_pTllrw'] = {
    'expr': '('+DYrew['2017']['LO'].replace('x', 'getGenZpt_OTF')+')*(nGenJet == 0)+1.0*(nCleanGenJet > 0)',
    'samples': ['DY']
}


###########################################################################################
# PU jet Id SF
###########################################################################################
puidSFSource = '{}/Configurations/patches/PUID_81XTraining_EffSFandUncties.root'.format(configurations)

aliases['PUJetIdSF'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        '.L %s/Configurations/VBS_ZV/patches/pujetidsf_event_new.cc+' % configurations
    ],
    'class': 'PUJetIdEventSF',
    'args': (puidSFSource, "2017", "loose"),
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




# data/MC scale factors  for now removed Jet PU id since it was not working. For we keep the loose one...
aliases['SFweight'] = {
    'expr': ' * '.join(['SFweight2l','LepWPCut','LepSF2l__ele_' + eleWP + '__mu_' + muWP,'PrefireWeight','btagSF', 'Jet_PUIDSF']),
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



#mva_reader_path = '%s/Configurations/VBS_ZV/mva_macros/' % configurations
#models_path = '/eos/home-a/ahakimi/www/ZV_analysis/Models/All_years_nobtag_SR'
#models_path = '/eos/user/m/mpresill/www/VBS/Numpy/Alex/'

"""
aliases['DNNoutput_boosted'] = {
    'class': 'MVAReaderBoosted_v70',
   'args': ( models_path +'2018_SR/Boosted_SR/DNN/', True, 0),
    'linesToAdd':[
      'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mva_Boosted.cc+',
    ],
}

aliases['DNNoutput_resolved'] = {
    'class': 'MVAReaderResolved_v70',
    'args': ( models_path+ '2018_SR/Resolved_SR/DNN/', False, 1),
    'linesToAdd':[
        'gSystem->Load("libLatinoAnalysisMultiDraw.so")',
        'gSystem->Load("libDNNEvaluator.so")',
        '.L ' + mva_reader_path + 'mva_Resolved.cc+',
    ],
}

aliases['DNNoutput'] = {
    'expr': '(vbs_category==0)*(DNNoutput_boosted) + (vbs_category==1)*(DNNoutput_resolved)'

}


aliases['DNNoutput_18'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
	'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('dnn_output','2018_allfeats', models_path, False)
}

aliases['DNNoutput_All_years'] = {
    'linesToAdd': [
        'gSystem->AddIncludePath("-I%s/src");' % os.getenv('CMSSW_BASE'),
        'gSystem->Load("libDNNEvaluator.so")',
        '.L %s/Configurations/VBS_ZV/macros/jets_cat_dnn.cc+' % configurations
    ],
    'class': 'jets_cat_dnn',
    'args': ('dnn_output','2018', models_path, False)
}
"""
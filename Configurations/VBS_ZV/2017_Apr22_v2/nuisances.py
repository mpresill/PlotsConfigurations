# nuisances
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

def nanoGetSampleFiles(inputDir, Sample):
    return getSampleFiles(inputDir, Sample, False, 'nanoLatino_')

try:
    mc = [skey for skey in samples if skey != 'DATA' and not skey.startswith('Fake')]
except NameError:
    mc = []
    cuts = {}
    nuisances = {}
    def makeMCDirectory(x=''):
        return ''

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()

#mc = [ "DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","VBF-V","VBS_ZV", "tZq", "VBS_VV_QCD" ]
#mc_common = [ "DY","tZq", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","VBF-V"]
#mc_eos = ["VBS_ZV",  "VBS_VV_QCD"]

EFT_samples = ["quad_cS0","sm_lin_quad_cS0",  "quad_cS1","sm_lin_quad_cS1",   "quad_cM0","sm_lin_quad_cM0",  "quad_cM1","sm_lin_quad_cM1",   "quad_cM2","sm_lin_quad_cM2",   "quad_cM3","sm_lin_quad_cM3",   "quad_cM4","sm_lin_quad_cM4",   "quad_cM5","sm_lin_quad_cM5",   "quad_cM7","sm_lin_quad_cM7",   "quad_cT0","sm_lin_quad_cT0",   "quad_cT1","sm_lin_quad_cT1",   "quad_cT2","sm_lin_quad_cT2",   "quad_cT5","sm_lin_quad_cT5",   "quad_cT6","sm_lin_quad_cT6",   "quad_cT7","sm_lin_quad_cT7",   "quad_cT8","sm_lin_quad_cT8",   "quad_cT9","sm_lin_quad_cT9"  ]
mc_common = ["DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","tZq", "VBF-V"] 
mc_eos    = ["sm", "VBS_VV_QCD"] #+ EFT_samples

mc        = mc_common + mc_eos


DirectorySMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7'

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2017',
#    'type': 'lnN',
#    'samples': dict((skey, '1.023') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2017',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.008') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_BBDefl'] = {
    'name': 'lumi_13TeV_BBDefl',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_DynBeta'] = {
    'name': 'lumi_13TeV_DynBeta',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst_em',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}


##### B-tagger

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2017'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
         'samples': dict((skey, btag_syst) for skey in mc), 
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_trigger_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc), 
}


####### Pre firing 2017 syst
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc), 
    #'AsLnN': '1',
}

##### Electron Efficiency and energy scale REMOVED VBS EW AND QCD FOR THE MOMENT

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc),
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc_common),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    #'AsLnN': '1'
}
#this is for the signals since they are in a different eos folder
nuisances['electronpt_SMPeos'] = {
    'name': 'CMS_scale_e_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos ),
    'folderUp': makeMCDirectorySMPeos('ElepTup_suffix'),
    'folderDown': makeMCDirectorySMPeos('ElepTdo_suffix'),
    #'AsLnN': '1'
}

##### Muon Efficiency and energy scale REMOVED VBS EW AND QCD FOR THE MOMENT

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc),
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc_common),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    #'AsLnN': '1'
}
#this is for the signals
nuisances['muonpt_SMPeos'] = {
    'name': 'CMS_scale_m_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos),
    'folderUp': makeMCDirectorySMPeos('MupTup_suffix'),
    'folderDown': makeMCDirectorySMPeos('MupTdo_suffix'),
    #'AsLnN': '1'
}

##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2017','JESBBEC1','JESBBEC1_2017','JESEC2',
            'JESEC2_2017','JESFlavorQCD','JESHF','JESHF_2017','JESRelativeBal',
            'JESRelativeSample_2017']

folderup = ""
folderdo = ""
folderup_signal = ""
folderdo_signal = ""


for js in jes_systs:
  if 'Absolute' in js:
    folderup = makeMCDirectory('JESAbsoluteup_suffix')
    folderdo = makeMCDirectory('JESAbsolutedo_suffix')
  elif 'BBEC1' in js:
    folderup = makeMCDirectory('JESBBEC1up_suffix')
    folderdo = makeMCDirectory('JESBBEC1do_suffix')
  elif 'EC2' in js:
    folderup = makeMCDirectory('JESEC2up_suffix')
    folderdo = makeMCDirectory('JESEC2do_suffix')
  elif 'HF' in js:
    folderup = makeMCDirectory('JESHFup_suffix')
    folderdo = makeMCDirectory('JESHFdo_suffix')
  elif 'Relative' in js:
    folderup = makeMCDirectory('JESRelativeup_suffix')
    folderdo = makeMCDirectory('JESRelativedo_suffix')
  elif 'FlavorQCD' in js:
    folderup = makeMCDirectory('JESFlavorQCDup_suffix')
    folderdo = makeMCDirectory('JESFlavorQCDdo_suffix')

for js in jes_systs:
    nuisances[js]  = {
                    'name': 'CMS_j_scale_'+js,
                    'kind': 'suffix',
                    'type': 'shape',
                    'mapUp': js+'up',
                    'mapDown': js+'do',
                    'samples': dict((skey, ['1.','1.']) for skey in mc_common),
                    'folderUp' : folderup,
                    'folderDown' : folderdo,
                    #'AsLnN'      : '1',
                    
    }

#this is for signals
for js_VBS_ZV in jes_systs:
  if 'Absolute' in js_VBS_ZV: 
    folderup_signal = DirectorySMPeos+'__JESAbsoluteup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESAbsolutedo_suffix'
  elif 'BBEC1' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESBBEC1up_suffix'
    folderdo_signal = DirectorySMPeos+'__JESBBEC1do_suffix'
  elif 'EC2' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESEC2up_suffix'
    folderdo_signal = DirectorySMPeos+'__JESEC2do_suffix'
  elif 'HF' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESHFup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESHFdo_suffix'
  elif 'Relative' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESRelativeup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESRelativedo_suffix'
  elif 'FlavorQCD' in js_VBS_ZV:
    folderup_signal = DirectorySMPeos+'__JESFlavorQCDup_suffix'
    folderdo_signal = DirectorySMPeos+'__JESFlavorQCDdo_suffix'

  nuisances[js_VBS_ZV] = {
      'name': 'CMS_scale_'+js_VBS_ZV,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js_VBS_ZV+'up',
      'mapDown': js_VBS_ZV+'do',
      'samples': dict((skey, ['1','1']) for skey in mc_eos),
      'folderUp': folderup_signal,
      'folderDown': folderdo_signal,
#      'AsLnN': '1'
  }

##### Jet energy resolution

nuisances['JER']  = {
                'name': 'CMS_res_j_2017',
                'kind': 'suffix',
                'type': 'shape',
                'mapUp': 'JERup',
                'mapDown': 'JERdo',
                'samples': dict((skey, ['1.','1.']) for skey in mc_common),
                'folderUp' : makeMCDirectory('JERup_suffix'),
                'folderDown' : makeMCDirectory('JERdo_suffix'),
                #'AsLnN'      : '1',
}
#this is for the signal
nuisances['JER_SMPeos'] = {
    'name': 'CMS_res_j_2017',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos if skey not in ["sm"]), ####WHY REMOVING SIGNAL?
    'folderUp': makeMCDirectorySMPeos('JERup_suffix'),
    'folderDown': makeMCDirectorySMPeos('JERdo_suffix'),
    #'AsLnN': '1'
}
#pb with tZq here? (memory leak)

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples'  : dict ( (skey, [ '(puWeightUp/puWeight)','(puWeightDown/puWeight)']) for skey in mc ),
#    'samples': {
#        'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
#        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
#        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
#    },
    #'AsLnN': '1',
}

### PU ID SF uncertainty
"""
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2017',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}
"""

nuisances['jetPUID']  = {
                'name'  : 'CMS_jetpuid_2017',
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : dict((skey, ['PUJetIdSF_up/PUJetIdSF','PUJetIdSF_down/PUJetIdSF']) for skey in mc ),
}

##########   fat jet uncertainties

#nuisances['cfj_pt_JESTotal'] = {
#    'name': 'CMS_scale_cleanfatJES_2017',
#    'kind': 'tree',
#    'type': 'shape',
#    'auxname': 'FatJet',
#    'mapUp' : 'pt_jesTotalUp',
#    'mapDown': 'pt_jesTotalDown',
#    'samples': dict((skey, ['1', '1']) for skey in mc_common),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
#    'AsLnN': '1'
#}
#
#nuisances['cfj_pt_JER'] = {
#    'name': 'CMS_scale_cleanfatJER_2017',
#    'type': 'shape',
#    'kind': 'tree',
#    'auxname':'FatJet',
#    'mapUp' : 'pt_jerUp',
#    'mapDown': 'pt_jerDown',
#    'samples': dict((skey, ['1', '1']) for skey in mc_common),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
#    'AsLnN': '1'
#}
#nuisances['mV_jms'] = {
#    'name': 'CMS_scale_mVjms_2017',
#    'type': 'shape',
#    'kind': 'tree',
#    'auxname': 'FatJet_msoftdrop',
#    'mapUp' : 'jmsUp',
#    'mapDown': 'jmsDown',
#    'samples': dict((skey, ['1', '1']) for skey in mc_common),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
#    'AsLnN': '1'
#}
#nuisances['mV_jmr'] = {
#    'name': 'CMS_scale_mVjmr_2017',
#    'type': 'shape',
#    'kind': 'tree',
#    'auxname': 'FatJet_msoftdrop',
#    'mapUp': 'jmrUp',
#    'mapDown': 'jmrDown',
#    'samples': dict((skey, ['1', '1']) for skey in mc_common),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
#    'AsLnN': '1'
#}
#
#nuisances['mV_jesTotal'] = {
#    'name': 'CMS_scale_mVjesTotal_2017',
#    'type': 'shape',
#    'kind': 'tree',
#    'auxname': 'FatJet_msoftdrop',
#    'mapUp' : 'jesTotalUp',
#    'mapDown': 'jesTotalDown',
#    'samples': dict((skey, ['1', '1']) for skey in mc_common),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
#    'AsLnN': '1'
#}
#
#nuisances['mV_jer'] = {
#    'name': 'CMS_scale_mVjer_2017',
#    'type': 'shape',
#    'kind': 'tree',
#    'auxname': 'FatJet_msoftdrop',
#    'mapUp' : 'jerUp',
#    'mapDown': 'jerDown',
#    'samples': dict((skey, ['1', '1']) for skey in mc_common),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
#    'AsLnN': '1'
#}






###########################################
#############  PARTON SHOWER ##############
###########################################
#samples_PS = ['VBS_ZV','VV','Vg','VgS','VBF-V'] #samples_PS_lnN= ['VBS_VV_QCD', 'VVV', 'ggWW', 'top'] 
# -> alternative implementation here: https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/VBS_OS/Full2017_v7/SF/nuisances.py#L280-L318 
#for sample in mc :
#    if sample in ["tZq","DY"]: continue 
#    nuisances['PS_ISR_'+sample]  = {
#                'name'  : 'CMS_PS_ISR_'+sample,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                    sample : ['PSWeight[2]', 'PSWeight[0]'],
#           		},
#		#'AsLnN': '1' ##
#    }
#    nuisances['PS_FSR_'+sample]  = {
#                'name'  : 'CMS_PS_FSR_'+sample,
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  : {
#                    sample :  ['PSWeight[3]', 'PSWeight[1]'], 
#                },
#		#'AsLnN': '1' ##
#    }

    # ---- for signal samples (with dipole recoil option) we have correctly defined the PS weights in 16/17

"""for sample in mc_eos:                        BUGGY NUISANCE FOR SIGNALS!!! TO BE FIXED
    nuisances['PS_ISR_'+sample]  = {
                'name'  : 'CMS_PSroot -l_ISR_'+sample,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    sample : ['PSWeight[2]', 'PSWeight[0]'],
           		},
    }
    nuisances['PS_FSR_'+sample]  = {
                'name'  : 'CMS_PS_FSR_'+sample,
                'kind'  : 'weight',
                'type'  : 'shape',
                'samples'  : {
                    sample :  ['PSWeight[3]', 'PSWeight[1]'], 
                },
    }"""

        # --- for bkg samples the PS weights were not available for 2016 and 2017, so they are retrieved with this parameterization measured here: 
        #      https://indico.cern.ch/event/904975/contributions/3826788/attachments/2020329/3377936/Update_on_PS_uncertainties_.pdf 
samples_PS = ['Vg','VgS','ggWW','WW','top','DY','VVV']
for sample in samples_PS:
    nuisances['PS_ISR']  = {
        'name': 'PS_ISR',
        'kind': 'weight',
        'type': 'shape',
        'samples': {
            'Vg'     : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
            'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
            'ggWW'   : ['1.040233912070831*(nCleanGenJet==0) + 0.9611236379290876*(nCleanGenJet==1) + 0.9014289294088699*(nCleanGenJet==2) + 0.864310738090035*(nCleanGenJet>=3)', '0.9510305474211223*(nCleanGenJet==0) + 1.0433432942960381*(nCleanGenJet==1) + 1.1271383507266095*(nCleanGenJet==2) + 1.1885756983901514*(nCleanGenJet>=3)'],
            'WW'     : ['1.0005237869294796*(nCleanGenJet==0) + 1.0157425373134328*(nCleanGenJet==1) + 0.9644598124510606*(nCleanGenJet==2) + 0.9271488926223369*(nCleanGenJet>=3)', '0.9993553300024391*(nCleanGenJet==0) + 0.9806102300995024*(nCleanGenJet==1) + 1.042603303739856*(nCleanGenJet==2) + 1.0950369125887705*(nCleanGenJet>=3)'],
            'top'    : ['1.0020618369910668*(nCleanGenJet==0) + 1.0063081530771556*(nCleanGenJet==1) + 1.0094298425968304*(nCleanGenJet==2) + 0.9854207999040726*(nCleanGenJet>=3)', '0.9974340279269026*(nCleanGenJet==0) + 0.9920634820709106*(nCleanGenJet==1) + 0.988226385054923*(nCleanGenJet==2) + 1.017968568319235*(nCleanGenJet>=3)'],
            'DY'     : ['0.9998177685645392*(nCleanGenJet==0) + 1.0080838149428026*(nCleanGenJet==1) + 1.0057948912950987*(nCleanGenJet==2) + 0.9721358221196619*(nCleanGenJet>=3)', '1.0003244155266309*(nCleanGenJet==0) + 0.9897992135367016*(nCleanGenJet==1) + 0.9928782069009531*(nCleanGenJet==2) + 1.0348902921423981*(nCleanGenJet>=3)'],
            'VVV'    : ['1.0270826786253018*(nCleanGenJet==0) + 1.0198703447307862*(nCleanGenJet==1) + 1.0109191915514344*(nCleanGenJet==2) + 0.9838184220287978*(nCleanGenJet>=3)', '0.9661665482954546*(nCleanGenJet==0) + 0.9751744967838527*(nCleanGenJet==1) + 0.9859624782745712*(nCleanGenJet==2) + 1.0202995039288625*(nCleanGenJet>=3)'],
        },
    }
    nuisances['PS_FSR']  = {
        'name': 'PS_FSR',
        'kind': 'weight',
        'type': 'shape',
        'samples': {
            'Vg'     : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
            'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
            'ggWW'   : ['0.9910563426395067*(nCleanGenJet==0) + 1.0069894351287263*(nCleanGenJet==1) + 1.016616376034912*(nCleanGenJet==2) + 1.015902717074592*(nCleanGenJet>=3)', '1.0147395976461193*(nCleanGenJet==0) + 0.9860219489006646*(nCleanGenJet==1) + 0.9694680606617647*(nCleanGenJet==2) + 0.9489845115821678*(nCleanGenJet>=3)'],
            'WW'     : ['0.995462478372054*(nCleanGenJet==0) + 1.0052129975124378*(nCleanGenJet==1) + 1.008836750560578*(nCleanGenJet==2) + 0.9984120564941189*(nCleanGenJet>=3)', '1.008927720738437*(nCleanGenJet==0) + 0.995163868159204*(nCleanGenJet==1) + 0.9911024228315418*(nCleanGenJet==2) + 0.9763787172658678*(nCleanGenJet>=3)'],
            'top'    : ['0.9910899786333963*(nCleanGenJet==0) + 0.9990635702054794*(nCleanGenJet==1) + 1.002141744200183*(nCleanGenJet==2) + 1.0129742776372779*(nCleanGenJet>=3)', '1.0068843378231833*(nCleanGenJet==0) + 0.998988498438759*(nCleanGenJet==1) + 0.9952696584115224*(nCleanGenJet==2) + 0.9790955840673237*(nCleanGenJet>=3)'],
            'DY'     : ['0.9958763409773141*(nCleanGenJet==0) + 1.0041335498093422*(nCleanGenJet==1) + 1.0163363150953029*(nCleanGenJet==2) + 1.0296733670670226*(nCleanGenJet>=3)', '1.0066775262249232*(nCleanGenJet==0) + 0.9945601465681602*(nCleanGenJet==1) + 0.9662459619335311*(nCleanGenJet==2) + 0.9479423453563661*(nCleanGenJet>=3)'],
            'VVV'    : ['0.9809047855490748*(nCleanGenJet==0) + 0.9823641498350338*(nCleanGenJet==1) + 0.9976414629808243*(nCleanGenJet==2) + 1.0077953569413387*(nCleanGenJet>=3)', '1.035388723727876*(nCleanGenJet==0) + 1.0347339790465233*(nCleanGenJet==1) + 1.0017058788771533*(nCleanGenJet==2) + 0.9829344116371653*(nCleanGenJet>=3)'],
        },
    }

###########################################
#############    QCD scale   ##############
###########################################
## Shape nuisance due to QCD scale variations for DY
## LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
## DY has 8 LHEScaleWeights; all others have 9 or 0
## DYvariations = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[4],1)', 'Alt$(LHEScaleWeight[6],1)', 'Alt$(LHEScaleWeight[7],1)']
## variations   = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[5],1)', 'Alt$(LHEScaleWeight[7],1)', 'Alt$(LHEScaleWeight[8],1)']
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

for sample in mc_common :
    if sample in ["ggWW"]: continue   #this sample apparently doesn't have LHE weights, but it's real minor for us
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
	    #'AsLnN': '1'    ##
    }

for sample in mc_eos :
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
	    #'AsLnN': '1'    ##
    }

    # QCD acceptance on signal samples
nuisances['QCDscale_ewk_ZV_accept'] = {
            'name'  : 'QCDscale_ewk_ZV_accept',
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { "sm": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"] }
            #'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in mc_eos }
        }

    # UNCOMMENT FOR EFT analysis
#nuisances['QCD_scale_VBS_EFT_accept'] = {
#            'name'  : 'QCD_scale_VBS_EFT_accept',
#            'kind'  : 'weight',
#            'type'  : 'shape',
#           # 'samples'  :  { "sm": ["QCDscale_normalized[0]", "QCDscale_normalized[8]"] }
#            'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in EFT_samples }
#        }




###########################################
#############    PDF WEIGHT  ##############
###########################################

nuisances['pdf_weight'] = { # --> Now save also the normalization one for the signal
    'name'  : 'pdf_1718',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["DY","top"]}, #-> here we reomve bkgs measured on, as well as BSM signals (PHDF4LHC prescription for BSM measurement)
    'AsLnN':  '1'
}

    # pdf uncertainty on signal acceptance
nuisances['pdf_ewk_ZV_accept'] = {
    'name'  : 'pdf_ewk_ZV_1718_accept',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples': { k : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] for k in ["sm"]}
}


###########################################
#############    UE         ##############
###########################################
# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ['DY','top']), ########### removed fot top and DY, which are measured in CRs 
}



####### Generic "cross section uncertainties"

## Top pT reweighting uncertainty
nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': { 
       'top': [
        'isSingleTop * 1.0816 + isTTbar',
        'isSingleTop * 0.9184 + isTTbar']
      }
}

nuisances['TopPtRew'] = {
   'name': 'CMS_topPtRew',   # Theory uncertainty
   'kind': 'weight',
   'type': 'shape',
   'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
   'symmetrize': True
}


nuisances['VgStar'] = {
    'name': 'CMS_VgStarScale',
    'type': 'lnN',
    'samples': {
        'VgS_L': '1.25'
    }
}

nuisances['VZ'] = {
    'name': 'CMS_VZScale',
    'type': 'lnN',
    'samples': {
        'VgS_H': '1.16'
    }
}




################
## rate parameters
nuisances['Topnorm_boosted']  = {
               'name'  : 'Topnorm_boosted_2017',
               'samples'  : {
                   'top' : '1.0',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Boosted_topcr',
                   'Boosted_SR_bVeto',
                   'Boosted_SR_bTag',
                   ]
              }

nuisances['Topnorm_resolved']  = {
               'name'  : 'Topnorm_resolved_2017',
               'samples'  : {
                   'top' : '1.',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Resolved_topcr',
                   'Boosted_SR_bVeto',
                   'Resolved_SR_bTag',
                   ]
              }              


DY_bins = []

for bin in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] :
        DY_bins.append("DY_Resolved_2d_" + bin)
        #DY_bins.append("DY_Boosted_Z_" + str(bin))
for bin in range(1,6):
        DY_bins.append("DY_Boosted_Z_bin" + str(bin))
#DYrates=[0.899,0.874,0.774,0.631,0.69,0.514,1,1,1,1,1]

for i,DYbin in enumerate(DY_bins):
        if "Resolved_2d_" in DYbin:
                nuisances["{}_norm_res_Z_bVeto_2017".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_res_Z_bVeto_2017'.format(DYbin),
                'samples'  : {DYbin: '1.' },
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bVeto',
                   #'Boosted_DYcr_nobVeto',
                   'Resolved_SR_bVeto',
                   #'Resolved_SR_blind',
                   #'Resolved_DYcr_bVeto_mjj200',
                   #'Boosted_DYcr_nobVeto',
                   #'Resolved_SR_bVeto_mjj200',
                   #'Boosted_SR_nobVeto'

                   ]
            	}
		nuisances["{}_norm_res_Z_bTag_2017".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_res_Z_bTag_2017'.format(DYbin),
                'samples'  : {DYbin: '1.' },
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bTag',
                   #'Boosted_DYcr_nobVeto',
                   'Resolved_SR_bTag',
                   #'Resolved_SR_blind',
                   #'Resolved_DYcr_bVeto_mjj200',
                   #'Boosted_DYcr_nobVeto',
                   #'Resolved_SR_bVeto_mjj200',
                   #'Boosted_SR_nobVeto'

                   ]
                }
        if "Boosted_Z_" in DYbin:
                nuisances["{}_norm_boost_Z_bVeto_2017".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_boost_Z_bVeto_2017'.format(DYbin),
                'samples'  : {DYbin: '1.' },
                'type'  : 'rateParam',
                'cuts'  : [
                   #'Resolved_DYcr_bVeto',
                   'Boosted_DYcr_bVeto',
                   #'Resolved_SR_bVeto',
                   #'Resolved_SR_blind',
                   #'Resolved_DYcr_bVeto_mjj200',
                   #'Boosted_DYcr_nobVeto',
                   #'Resolved_SR_bVeto_mjj200',
                   'Boosted_SR_bVeto'

                   ]
                }
                nuisances["{}_norm_boost_Z_bTag_2017".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_boost_Z_bTag_2017'.format(DYbin),
                'samples'  : {DYbin: '1.' },
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bTag',
                   #'Boosted_DYcr_nobVeto',
                   'Boosted_SR_bTag',
                   #'Resolved_SR_blind',
                   #'Resolved_DYcr_bVeto_mjj200',
                   #'Boosted_DYcr_nobVeto',
                   #'Resolved_SR_bVeto_mjj200',
                   #'Boosted_SR_nobVeto'

                   ]
	}



## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}


#for n in nuisances.values():
#    n['skipCMS'] = 1

#print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))

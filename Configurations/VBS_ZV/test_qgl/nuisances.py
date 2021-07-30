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

# redefine sampels
mc = ["WGJJ", "DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","VBF-V","VBS_ZV", "tZq", "VBS_VV_QCD" ]
mc_common = ["WGJJ","tZq", "DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","VBF-V"] 
mc_eos = ["VBS_ZV", "VBS_VV_QCD"]



################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2018',
#    'type': 'lnN',
#    'samples': dict((skey, '1.023') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top',"DY"] )
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top',"DY"] )
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top',"DY"] )
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top',"DY"] )
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
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    }
}

##### B-tagger
"""
for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        'samples': dict((skey, btag_syst) for skey in mc),
    }
"""
##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc), 
}



##### Electron Efficiency and energy scale  
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc), 
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
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
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos),
    'folderUp': DirectorySMPeos+'__ElepTup_suffix',
    'folderDown': DirectorySMPeos+'__ElepTdo_suffix',
    #'AsLnN': '1'
}


##### Muon Efficiency and energy scale  
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc),
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
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
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos),
    'folderUp': DirectorySMPeos+'__MupTup_suffix',
    'folderDown': DirectorySMPeos+'__MupTdo_suffix',
    #'AsLnN': '1'
}



##### Jet energy scale and reso for AK4
##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']
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

  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc_common),
      'folderUp': folderup,
      'folderDown': folderdo,
#      'AsLnN': '1'
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
      'samples':  dict((skey, ['1','1']) for skey in mc_eos),
      'folderUp': folderup_signal,
      'folderDown': folderdo_signal,
#      'AsLnN': '1'
  }



##### Jet energy resolution

##### Jet energy resolution

nuisances['JER'] = {
    'name': 'CMS_res_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    'samples': dict((skey, ['1', '1']) for skey in mc_common),
    'folderUp': makeMCDirectory('JERup_suffix'),
    'folderDown': makeMCDirectory('JERdo_suffix'),
#    'AsLnN': '1'
}

#this is for the signal
nuisances['JER_SMPeos'] = {
    'name': 'CMS_res_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos),
    'folderUp': DirectorySMPeos+'__JERup_suffix',
    'folderDown': DirectorySMPeos+'__JERdo_suffix',
#    'AsLnN': '1'
}#add QCD_VV when ready



# ##### Pileup
pu_syst = '(puWeightUp/puWeight)', '(puWeightDown/puWeight)'

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
#    'AsLnN': '1',
}


##### PS: all these Psweights need to be updated 
samples_PS = ['VBS_ZV','top','VV','VVV','Vg','VgS','VBF-V','ggWW']  #add VBS_QCD_VV when ready on SMP eos
#DY removed for binning for now

for sample in samples_PS:
    nuisances['PS_ISR_'+sample]  = {
                    'name'  : 'CMS_PS_ISR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample : ['PSWeight[2]', 'PSWeight[0]'],
                    }
                }
    nuisances['PS_FSR_'+sample]  = {
                    'name'  : 'CMS_PS_FSR_'+sample,
                    'kind'  : 'weight',
                    'type'  : 'shape',
                    'samples'  : {
                        sample :  ['PSWeight[3]', 'PSWeight[1]'], 
                    }
                }


# # Theory nuisance: QCD scale
## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
#qcdscale_variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
#for sample in mc :
#    if sample == 'VBS_ZV' :
#        nuisances['QCD_scale_VBS'] = {
#            'name'  : 'QCDscale_'+sample,
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
#        }
for sample in mc :
    if sample == "ggWW": continue   #this sample apparently doesn't have LHE weights...
    #if sample == "VBS_VV_QCD": continue
	   ##once SMP eos VBS_VV_QCD are ready comment out 
    nuisances['QCD_scale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind'  : 'weight',
            'type'  : 'shape',
            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] }
        }









# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CP5',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc), 
}

####### Generic "cross section uncertainties"
"""
apply_on = {
    'top': [
        '(topGenPt * antitopGenPt <= 0.) * 1.0816 + (topGenPt * antitopGenPt > 0.)',
        '(topGenPt * antitopGenPt <= 0.) * 0.9184 + (topGenPt * antitopGenPt > 0.)'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}
"""
## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True
}

nuisances['VgStar'] = {
    'name': 'CMS_hww_VgStarScale',
    'type': 'lnN',
    'samples': {
        'VgS_L': '1.25'
    }
}

nuisances['VZ'] = {
    'name': 'CMS_hww_VZScale',
    'type': 'lnN',
    'samples': {
        'VgS_H': '1.16'
    }
}

nuisances['pdf']  = {
               'name'  : 'pdf',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW'    : '1.05',
                   'WW'      : '1.04',
                   'Vg'      : '1.04',
                   'VZ'      : '1.04',
                   'VgS'     : '1.04',
                   #'DY_B_bin1'      : '1.002', 
                   },
              }



## rate parameters

nuisances['Topnorm_boosted']  = {
               'name'  : 'Topnorm_boosted_2018',
               'samples'  : {
                   'top' : '1.0',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Boosted_topcr',
                   'Boosted_SR_bVeto',
                   'Boosted_SR_nobVeto',
                   ]
              }

nuisances['Topnorm_resolved']  = {
               'name'  : 'Topnorm_resolved_2018',
               'samples'  : {
                   'top' : '1.0',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Resolved_topcr',
                   'Resolved_SR_bVeto',
                   'Resolved_SR_nobVeto',
                   ]
              }              
"""              
DY_bins = []
for bin in range(1,7):
        DY_bins.append("DY_R_bin" + str(bin))
for bin in range(1,6):
        DY_bins.append("DY_B_bin" + str(bin))
DYrates=[0.899,0.874,0.774,0.631,0.69,0.514,1,1,1,1,1]

for i,DYbin in enumerate(DY_bins):
	if "_B_" in DYbin:
		nuisances["{}_norm_boost_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_boost_bVeto_2018'.format(DYbin),
                'samples'  : {DYbin: DYrates[i]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bVeto',
                   #'Boosted_DYcr_nobVeto',
		   'Boosted_SR_bVeto',
		   #'Boosted_SR_nobVeto'
		
                   ]
            }
		nuisances["{}_norm_boost_nobVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_boost_nobVeto_2018'.format(DYbin),
                'samples'  : {DYbin: DYrates[i]},
                'type'  : 'rateParam',
                'cuts'  : [
                   #'Boosted_DYcr_bVeto',
                   'Boosted_DYcr_nobVeto',
                   #'Boosted_SR_bVeto',
                   'Boosted_SR_nobVeto'

                   ]
            }



	elif "_R_" in DYbin:
		nuisances["{}_norm_res_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_res_bVeto_2018'.format(DYbin),
                'samples'  : {DYbin: '1.00'},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bVeto',
                   #'Resolved_DYcr_nobVeto',
                   'Resolved_SR_bVeto',
                   #'Resolved_SR_nobVeto'

                   ]
            }
                nuisances["{}_norm_res_nobVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_res_nobVeto_2018'.format(DYbin),
                'samples'  : {DYbin: '1.00'},
                'type'  : 'rateParam',
                'cuts'  : [
                   #'Resolved_DYcr_bVeto',
                   'Resolved_DYcr_nobVeto',
                   #'Resolved_SR_bVeto',
                   'Resolved_SR_nobVeto'

                   ]
            }
"""
## Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {}
}

for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))

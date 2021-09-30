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


mc        = ["WGJJ", "DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","tZq", "VBS_ZV", "VBS_VV_QCD" ]#,"VBS_ZV_aQGCs", "VBF-V missing
mc_common = ["WGJJ", "DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","tZq"] #"VBF-V", missing
mc_eos    = ["VBS_ZV", "VBS_VV_QCD"]#,"VBS_ZV_aQGCs"


################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.022') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.009') for skey in mc if skey not in ['WW', 'top', 'DY'])
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

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
    #'cutspost': lambda self, cuts: [cut for cut in cuts if '20em' not in cut],
    #'perRecoBin': True
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    }
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    }
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    }
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2016',
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
        name += '_2016'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
         'samples': dict((skey, btag_syst) for skey in mc), 
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc), 
}


####### Pre firing 2016 syst
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc), 

}


##### Electron Efficiency and energy scale


##### Electron Efficiency and energy scale
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc),#if skey not in ['VBS_ZV','VBS_VV_QCD']
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2016',
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
    'name': 'CMS_scale_e_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos if skey not in ['VBS_ZV']),
    'folderUp': DirectorySMPeos+'__ElepTup_suffix',
    'folderDown': DirectorySMPeos+'__ElepTdo_suffix',
    #'AsLnN': '1'
}

##### Muon Efficiency and energy scale
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc),# if skey not in ['VBS_ZV','VBS_VV_QCD']
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2016',
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
    'name': 'CMS_scale_m_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos  if skey not in ['VBS_ZV']),
    'folderUp': DirectorySMPeos+'__MupTup_suffix',
    'folderDown': DirectorySMPeos+'__MupTdo_suffix',
    #'AsLnN': '1'
}
#### Jet energy scale for AK4   MANY OF THESE ARE UNDER PROCESSING AGAIN....
"""
nuisances['jes'] = {
    'name': 'CMS_scale_j_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JESup',
    'mapDown': 'JESdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('JESup_suffix'),
    'folderDown': makeMCDirectory('JESdo_suffix'),
    'AsLnN': '1'
}
######## Jet energy resolution for AK4
nuisances['jer'] = {
    'name': 'CMS_resolution_j_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'folderUp': makeMCDirectory('JERup_suffix'),
    'folderDown': makeMCDirectory('JERdo_suffix'),
    'AsLnN': '1'
}
"""


##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2016','JESBBEC1','JESBBEC1_2016','JESEC2','JESEC2_2016','JESFlavorQCD','JESHF','JESHF_2016','JESRelativeBal','JESRelativeSample_2016']
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
      'samples': dict((skey, ['1', '1']) for skey in mc_common),  # if skey not in ['DY'] ###CHECK IF THIS IS STILL TRUE: Do we have all the DY samples shapes UP/DOWN for this available?
      'folderUp': folderup,
      'folderDown': folderdo,
     # 'AsLnN': '1'
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
##### Pileup
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_PUID_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc)
}



##### PS and UE missing
##### PS: taken from 2017, need to update to 2016

samples_PS = ['VBS_ZV','VV','Vg','VgS','VBF-V'] 
#DY removed for binning for now
#VBS_VV_QCD, VVV, ggWW,top missing

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
""" #this one maybe can be resumed with no issues
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

## PDF

nuisances['pdf']  = {
               'name'  : 'pdf',
               'type'  : 'lnN',
               'samples'  : {
                   'ggWW'    : '1.05',
                   'WW'      : '1.04',
                   'Vg'      : '1.04',
                   'VZ'      : '1.04',
                   'VgS'     : '1.04',
                   #'DY'      : '1.002', # For HM category, no DY CR
                   },
              }


## rate parameters
nuisances['Topnorm_boosted']  = {
               'name'  : 'Topnorm_boosted_2016',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Boosted_topcr',
                   'Boosted_SR',
                   ]
              }

nuisances['Topnorm_resolved']  = {
               'name'  : 'Topnorm_resolved_2016',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Resolved_topcr',
                   'Resolved_SR',
                   ]
              }
DY_bins=[]
for bin in range(1,7):
        DY_bins.append("DY_Resolved_Z_" + str(bin))
        DY_bins.append("DY_Boosted_Z_" + str(bin))
#for bin in range(1,6):
#        DY_bins.append("DY_B_bin" + str(bin))
#DYrates=[0.899,0.874,0.774,0.631,0.69,0.514,1,1,1,1,1]

for i,DYbin in enumerate(DY_bins):
        if "Resolved_Z_" in DYbin:
                nuisances["{}_norm_res_Z_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_res_Z_bVeto_2018'.format(DYbin),
                'samples'  : {DYbin: '1.0'},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bVeto',
                   #'Boosted_DYcr_nobVeto',
                   'Resolved_SR_bVeto',
                   #'Resolved_DYcr_bVeto_mjj200',
                   #'Boosted_DYcr_nobVeto',
                   #'Resolved_SR_bVeto_mjj200',
                   #'Boosted_SR_nobVeto'

                   ]
            }
        elif "Boosted_Z_" in DYbin:
                nuisances["{}_norm_boost_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_{}_norm_boost_bVeto_2018'.format(DYbin),
                'samples'  : {DYbin: '1.0'},
                'type'  : 'rateParam',
                'cuts'  : [
                   #'Boosted_DYcr_bVeto',
                   'Boosted_DYcr_bVeto',
                   #'Boosted_SR_bVeto',
                   'Boosted_SR_bVeto',
                   #'Boosted_DYcr_bVeto_mjj200',
                   #'Boosted_SR_bVeto_mjj200',

                   ]
            }
              
# Use the following if you want to apply the automatic combine MC stat nuisances.
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

#print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))

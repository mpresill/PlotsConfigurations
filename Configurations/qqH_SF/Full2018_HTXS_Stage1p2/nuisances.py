# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

import os

if os.path.exists('HTXS_stage1_categories.py') :
  handle = open('HTXS_stage1_categories.py','r')
  exec(handle)
  handle.close()

if os.path.exists('thuNormFactors.py') :
  handle = open('thuNormFactors.py','r')
  exec(handle)
  handle.close()

if os.path.exists('thuVBFNormFactors.py') :
  handle = open('thuVBFNormFactors.py','r')
  exec(handle)
  handle.close()


sampleNames = []
for cat in HTXSStage1_1Categories:
  if 'GG2H_' in cat:
    sampleNames.append(cat.replace('GG2H','ggH_hww'))
    sampleNames.append(cat.replace('GG2H','ggH_htt'))
  elif 'QQ2HQQ_' in cat:
    sampleNames.append(cat.replace('QQ2HQQ','qqH_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','qqH_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','WH_had_htt'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_hww'))
    sampleNames.append(cat.replace('QQ2HQQ','ZH_had_htt'))
  elif 'QQ2HLNU_' in cat:
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLNU','WH_lep_htt'))
  elif 'QQ2HLL_' in cat:
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_hww'))
    sampleNames.append(cat.replace('QQ2HLL','ZH_lep_htt'))
  elif 'GG2HLL_' in cat:
    sampleNames.append(cat.replace('GG2HLL','ggZH_lep_hww'))
  elif 'TTH' in cat:
    sampleNames.append(cat.replace('TTH','ttH_hww'))
  elif 'BBH' in cat:
    sampleNames.append(cat.replace('BBH','bbH_hww'))


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

print("MC samples:")
for qqq in mc:
  print(qqq)

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()


cuts0j  = []
cuts1j  = []
cuts2j  = []

for k in cuts:
  for cat in cuts[k]['categories']:
    if '0j' in cat: cuts0j.append(k+'_'+cat)
    elif '1j' in cat: cuts1j.append(k+'_'+cat)
    elif '2j' in cat: cuts2j.append(k+'_'+cat)
    else: print 'WARNING: name of category does not contain either 0j,1j,2j'

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity

#nuisances['lumi'] = {
#    'name': 'lumi_13TeV_2018',
#    'type': 'lnN',
#    'samples': dict((skey, '1.025') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}

nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top', 'DY'])
}

#### FAKES

nuisances['fake_syst_ee'] = {
    'name': 'CMS_fake_syst_ee',
    'type': 'lnN',
    'samples': {
        'Fake_ee': '1.3'
    },
    'cutspost': lambda self, cuts: [cut for cut in cuts if 'ee' in cut],
    'perRecoBin': True
}

nuisances['fake_syst_mm'] = {
    'name': 'CMS_fake_syst_mm',
    'type': 'lnN',
    'samples': {
        'Fake_mm': '1.3'
    },
    'cutspost': lambda self, cuts: [cut for cut in cuts if 'mm' in cut],
    'perRecoBin': True
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

for shift in ['jes', 'lf', 'hf', 'hfstats1', 'hfstats2', 'lfstats1', 'lfstats2', 'cferr1', 'cferr2']:
    btag_syst = ['(btagSF%sup)/(btagSF)' % shift, '(btagSF%sdown)/(btagSF)' % shift]

    name = 'CMS_btag_%s' % shift
    if 'stats' in shift:
        name += '_2018'

    nuisances['btag_shape_%s' % shift] = {
        'name': name,
        'kind': 'weight',
        'type': 'shape',
        #'samples': dict((skey, btag_syst) for skey in mc),
        'samples': dict((skey, btag_syst) for skey in mc if skey not in ['DY']),
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc if skey not in ['WW', 'top', 'DY'])
}

##### Electron Efficiency and energy scale

nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    #'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc if skey not in ['WW', 'top', 'DY'])
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc if skey not in ['DY'])
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    #'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['WW', 'top', 'DY']),
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['DY']), 
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
    'AsLnN': '1'
}

##### Muon Efficiency and energy scale

nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['ttHMVA_2l_mu_SF_Up', 'ttHMVA_2l_mu_SF_Down']) for skey in mc if skey not in ['DY'])
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    #    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['WW', 'top', 'DY']),
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['DY']),
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
    'AsLnN': '1'
}

##### Jet energy scale
jes_systs = ['JESAbsolute','JESAbsolute_2018','JESBBEC1','JESBBEC1_2018','JESEC2','JESEC2_2018','JESFlavorQCD','JESHF','JESHF_2018','JESRelativeBal','JESRelativeSample_2018']

for js in jes_systs:
 nuisances[js] = {
     'name': 'CMS_scale_'+js,
     'kind': 'suffix',
     'type': 'shape',
     'mapUp': js+'up',
     'mapDown': js+'do',
     #'samples': dict((skey, ['1', '1']) for skey in mc),
     'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['WW', 'top', 'DY','VZ','Vg','VgS','WWewk','ggWW']+signals),
     'folderUp': makeMCDirectory('JESup_suffix'),
     'folderDown': makeMCDirectory('JESdo_suffix'),
     'AsLnN': '1'
}

# nuisances['jes0j']  = {
#                 'name'  : 'CMS_scale_j_2018',
#                 'skipCMS' : 1,
#                 'type': 'lnN',
#                 'samples': dict((skey, '1.08') for skey in mc if skey not in ['WW', 'top', 'DY','VZ','Vg','VgS']),
#                 'cuts'     : cuts0j
# }

# nuisances['jes1j']  = {
#                 'name'  : 'CMS_scale_j_2018',
#                 'skipCMS' : 1,
#                 'type': 'lnN',
#                 'samples': dict((skey, '1.05') for skey in mc if skey not in ['WW', 'top', 'DY','VZ','Vg','VgS']),
#                 'cuts'     : cuts0j
# }

# nuisances['jes2j']  = {
#                 'name'  : 'CMS_scale_j_2018',
#                 'skipCMS' : 1,
#                 'type': 'lnN',
#                 'samples': dict((skey, '1.12') for skey in mc if skey not in ['WW', 'top', 'DY','VZ','Vg','VgS']),
#                 'cuts'     : cuts2j
# }


##### MET energy scale

nuisances['met'] = {
    'name': 'CMS_scale_met_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'METup',
    'mapDown': 'METdo',
    #'samples': dict((skey, ['1', '1']) for skey in mc),
    #'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['WW', 'top', 'DY']),
    'samples': dict((skey, ['1', '1']) for skey in mc if skey not in ['DY']), #['WW', 'top', 'DY']),
    'folderUp': makeMCDirectory('METup_suffix'),
    'folderDown': makeMCDirectory('METdo_suffix'),
    'AsLnN': '1'
}

##### Pileup

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'DY': ['0.993259983266*(puWeightUp/puWeight)', '0.997656381501*(puWeightDown/puWeight)'],
        'top': ['1.00331969187*(puWeightUp/puWeight)', '0.999199609528*(puWeightDown/puWeight)'],
        'WW': ['1.0033022059*(puWeightUp/puWeight)', '0.997085330608*(puWeightDown/puWeight)'],
        'ggH_hww': ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)'],
        'qqH_hww': ['1.00374694528*(puWeightUp/puWeight)', '0.995878596852*(puWeightDown/puWeight)'],
    },
    'AsLnN': '1',
}
for name in sampleNames:
  if 'ggH_hww' in name:
    nuisances['PU']['samples'].update({name: ['1.0036768006*(puWeightUp/puWeight)', '0.995996570285*(puWeightDown/puWeight)']})

##### PS and UE
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS','WWewk','DY']), #PSWeights are buggy for some samples, we add them back by hand below
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS','WWewk','DY']), #PSWeights are buggy for some samples, we add them back by hand below
}

## PS nuisances computed by hand as a function of nCleanGenJets using alternative samples (when available). Needed if nominal samples have buggy PSWeights
nuisances['PS_ISR_ForBuggySamples']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
    },
}

nuisances['PS_FSR_ForBuggySamples']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
    },
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

apply_on = {
    'top': [
        'isSingleTop * 1.0816 + isTTbar',
        'isSingleTop * 0.9184 + isTTbar'
    ]
}

nuisances['singleTopToTTbar'] = {
    'name': 'singleTopToTTbar',
    'skipCMS': 1,
    'kind': 'weight',
    'type': 'shape',
    'samples': apply_on
}

## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["Top_pTrw*Top_pTrw", "1."]},
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

###### pdf uncertainties

valuesggh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggH','125.09','pdf','sm')
valuesggzh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','pdf','sm')
valuesbbh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','bbH','125.09','pdf','sm')

nuisances['pdf_Higgs_gg'] = {
    'name': 'pdf_Higgs_gg',
    'samples': {
        #'ggH_hww': valuesggh,
        'ggH_htt': valuesggh,
        #'ggZH_hww': valuesggzh,
        'bbH_hww': valuesbbh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','pdf','sm')

nuisances['pdf_Higgs_ttH'] = {
    'name': 'pdf_Higgs_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

valuesqqh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','pdf','sm')
valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','pdf','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','pdf','sm')

nuisances['pdf_Higgs_qqbar'] = {
    'name': 'pdf_Higgs_qqbar',
    'type': 'lnN',
    'samples': {
        #'qqH_hww': valuesqqh,
        'qqH_htt': valuesqqh,
        #'WH_hww': valueswh,
        'WH_htt': valueswh,
        #'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
}

nuisances['pdf_qqbar'] = {
    'name': 'pdf_qqbar',
    'type': 'lnN',
    'samples': {
        'Vg': '1.04',
        'VZ': '1.04',  # PDF: 0.0064 / 0.1427 = 0.0448493
        'VgS': '1.04', # PDF: 0.0064 / 0.1427 = 0.0448493
    },
}

nuisances['pdf_Higgs_gg_ACCEPT'] = {
    'name': 'pdf_Higgs_gg_ACCEPT',
    'samples': {
        #'ggH_hww': '1.006',
        'ggH_htt': '1.006',
        #'ggZH_hww': '1.006',
        'bbH_hww': '1.006'
    },
    'type': 'lnN',
}

nuisances['pdf_gg_ACCEPT'] = {
    'name': 'pdf_gg_ACCEPT',
    'samples': {
        'ggWW': '1.006',
    },
    'type': 'lnN',
}

nuisances['pdf_Higgs_qqbar_ACCEPT'] = {
    'name': 'pdf_Higgs_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        #'qqH_hww': '1.002',
        'qqH_htt': '1.002',
        #'WH_hww': '1.003',
        'WH_htt': '1.003',
        #'ZH_hww': '1.002',
        'ZH_htt': '1.002',
    },
}

nuisances['pdf_qqbar_ACCEPT'] = {
    'name': 'pdf_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        'VZ': '1.001',
    },
}

##### Renormalization & factorization scales

## Shape nuisance due to QCD scale variations for DY
# LHE scale variation weights (w_var / w_nominal)

## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

# nuisances['QCDscale_V'] = {
#     'name': 'QCDscale_V',
#     'skipCMS': 1,
#     'kind': 'weight_envelope',
#     'type': 'shape',
#     'samples': {'DY': variations},
#     'AsLnN': '0'
# }

nuisances['QCDscale_VV'] = {
    'name': 'QCDscale_VV',
    'kind': 'weight_envelope',
    'type': 'shape',
    'samples': {
        'Vg': variations,
        'VZ': variations,
        'VgS': variations
    }
}

# ggww and interference
nuisances['QCDscale_ggVV'] = {
    'name': 'QCDscale_ggVV',
    'type': 'lnN',
    'samples': {
        'ggWW': '1.15',
    },
}

##### Renormalization & factorization scales                                                                                                  
# nuisances['WWresum0j']  = {
#   'name'  : 'CMS_hww_WWresum_0j',
#   'skipCMS' : 1,
#   'kind'  : 'weight',
#   'type'  : 'shape',
#   'samples'  : {
#      'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
#    },
#   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
# }

# nuisances['WWqscale0j']  = {
#    'name'  : 'CMS_hww_WWqscale_0j',
#    'skipCMS' : 1,
#    'kind'  : 'weight',
#    'type'  : 'shape',
#    'samples'  : {
#       'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
#     },
#    'cutspost'  : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
# }

# nuisances['WWresum1j']  = {
#   'name'  : 'CMS_hww_WWresum_1j',
#   'skipCMS' : 1,
#   'kind'  : 'weight',
#   'type'  : 'shape',
#   'samples'  : {
#      'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
#    },
#   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
# }

# nuisances['WWqscale1j']  = {
#    'name'  : 'CMS_hww_WWqscale_1j',
#    'skipCMS' : 1,
#    'kind'  : 'weight',
#    'type'  : 'shape',
#    'samples'  : {
#       'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
#     },
#    'cutspost'  : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
# }

nuisances['WWresum2j']  = {
  'name'  : 'CMS_hww_WWresum_2j',
  'skipCMS' : 1,
  'kind'  : 'weight',
  'type'  : 'shape',
  'samples'  : {
     'WW'   : ['nllW_Rup/nllW', 'nllW_Rdown/nllW'],
   },
  'cutspost'  : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
}

nuisances['WWqscale2j']  = {
   'name'  : 'CMS_hww_WWqscale_2j',
   'skipCMS' : 1,
   'kind'  : 'weight',
   'type'  : 'shape',
   'samples'  : {
      'WW'   : ['nllW_Qup/nllW', 'nllW_Qdown/nllW'],
    },
   'cutspost'  : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_WW'] = {
    'name': 'CMS_hww_CRSR_accept_WW',
    'type': 'lnN',
    'samples': {'WW': '1.01'},
    #'samples': {'DY': '1.1'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    #'cutspost': (lambda self, cuts: [cut for cut in cuts if '_DY_' in cut and cut in self['cuts']]),
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_WW_' in cut]),
    #'perRecoBin': True
}

# Uncertainty on SR/CR ratio
nuisances['CRSR_accept_top'] = {
    'name': 'CMS_hww_CRSR_accept_top',
    'type': 'lnN',
    'samples': {'top': '1.01'},
    #'samples': {'top': '1.05'},
    'cuts': [cut for cut in cuts if '_CR_' in cut],
    'cutspost': (lambda self, cuts: [cut for cut in cuts if '_top_' in cut]),
}

# Let's comment ggH uncertainties for the moment

# Theory uncertainty for ggH
#
#
#   THU_ggH_Mu, THU_ggH_Res, THU_ggH_Mig01, THU_ggH_Mig12, THU_ggH_VBF2j, THU_ggH_VBF3j, THU_ggH_PT60, THU_ggH_PT120, THU_ggH_qmtop
#
#   see https://twiki.cern.ch/twiki/bin/viewauth/CMS/HiggsWG/SignalModelingTools

# thus = [
# #    ('THU_ggH_Mu', 'ggH_mu'),
# #    ('THU_ggH_Res', 'ggH_res'),
#     ('THU_ggH_Mig01', 'ggH_mig01'),
#     ('THU_ggH_Mig12', 'ggH_mig12'),
#     ('THU_ggH_VBF2j', 'ggH_VBF2j'),
#     ('THU_ggH_VBF3j', 'ggH_VBF3j'),
#     ('THU_ggH_PT60', 'ggH_pT60'),
#     ('THU_ggH_PT120', 'ggH_pT120'),
#     ('THU_ggH_qmtop', 'ggH_qmtop')
# ]

# for name, vname in thus:
#     updown = [vname, '2.-%s' % vname]
    
#     nuisances[name] = {
#         'name': name,
#         'skipCMS': 1,
#         'kind': 'weight',
#         'type': 'shape',
#         'samples': {
#           'ggH_hww': updown,
#           #'ggH_htt': updown
#         }
#     }
#     for sname in sampleNames:
#         if 'ggH_hww' in sname:
#           if 'GT200' not in sname:
#             #print globals()                                                                                                                   
#             normthu = globals()[name.replace("THU_","thuNormFactors_")][sname.replace('ggH_hww','GG2H')][0]
#             nuisances[name]['samples'].update({sname : [vname+'/'+normthu,'2.-'+vname+'/'+normthu]})
#           else:
#             nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_200_300'][0]
#             ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_200_300'][0]]})
#             nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_300_450'][0]
#             ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_300_450'][0]]})
#             nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_450_650'][0]
#             ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_450_650'][0]]})
#             nuisances[name]['samples'].update({name : [vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_GT650'][0]
#             ,'2.-'+vname+'/'+globals()[name.replace("THU_","thuNormFactors_")]['GG2H_PTH_GT650'][0]]})

# Theory uncertainty for qqH 
#
#
#   see https://gitlab.cern.ch/LHCHIGGSXS/LHCHXSWG2/STXS/VBF-Uncertainties/-/blob/master/qq2Hqq_uncert_scheme.cpp

thusQQH = [
  ("THU_qqH_PTH200","qqH_PTH200"),
  ("THU_qqH_Mjj60","qqH_Mjj60"),
  ("THU_qqH_Mjj120","qqH_Mjj120"),
  ("THU_qqH_Mjj350","qqH_Mjj350"),
  ("THU_qqH_Mjj700","qqH_Mjj700"),
  ("THU_qqH_Mjj1000","qqH_Mjj1000"),
  ("THU_qqH_Mjj1500","qqH_Mjj1500"),
  ("THU_qqH_PTH25","qqH_PTH25"),
  ("THU_qqH_JET01","qqH_JET01"),
  ("THU_qqH_EWK","qqH_EWK"),
]

for name, vname in thusQQH:
    updown = [vname, '2.-%s' % vname]
    
    nuisances[name] = {
        'name': name,
        'skipCMS': 1,
        'kind': 'weight',
        'type': 'shape',
        'samples': {
          'qqH_hww': updown,
        }
    }
    for sname in sampleNames:
        if 'qqH_hww' in sname:
          normthu = globals()[name.replace("THU_","thuNormFactors_")][sname.replace('qqH_hww','QQ2HQQ')][0]
          nuisances[name]['samples'].update({sname : [vname+'/'+normthu,'2.-'+vname+'/'+normthu]})
    print nuisances[name]

                                                                                                                          
# nuisances['ggH_scale_0jet'] = {                                                                                                  
#                'name'  : 'ggH_scale_0jet',                                                                                       
#                'samples'  : { 
#                    'ggH_hww_0J_PTH_0_10' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_0J_PTH_0_10'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_0J_PTH_0_10'][1]],
#                    'ggH_hww_0J_PTH_GT10' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_0J_PTH_GT10'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_0J_PTH_GT10'][1]],
#                   },                                                                                                              
#                'type'  : 'shape',                                                                                                             
#                'kind'  : 'weight',                                                                                                            
#               }         

# nuisances['ggH_scale_1jet_lowpt'] = {                                                                                          
#                'name'  : 'ggH_scale_1jet_lowpt',                                                                                
#                'samples'  : { 
#                    'ggH_hww_1J_PTH_0_60' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_0_60'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_0_60'][1]],
#                    'ggH_hww_1J_PTH_60_120' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_60_120'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_60_120'][1]],
#                    'ggH_hww_1J_PTH_120_200' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_1J_PTH_120_200'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_1J_PTH_120_200'][1]],
#                   },                                                                                                              
#                'type'  : 'shape',                                                                                                             
#                'kind'  : 'weight',                                                                                                            
#               }         

nuisances['ggH_scale_2jet_lowpt'] = {                                                                                          
               'name'  : 'ggH_scale_2jet_lowpt',                                                                                 
               'samples'  : { 
                   'ggH_hww_GE2J_MJJ_0_350_PTH_0_60' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_0_60'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_0_60'][1]],
                   'ggH_hww_GE2J_MJJ_0_350_PTH_60_120' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_60_120'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_60_120'][1]],
                   'ggH_hww_GE2J_MJJ_0_350_PTH_120_200' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_120_200'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_0_350_PTH_120_200'][1]],
                  },                                                                                                             
               'type'  : 'shape',                                                                                                             
               'kind'  : 'weight',                                                                                                            
              }         

nuisances['ggH_scale_highpt'] = {                                                                                          
               'name'  : 'ggH_scale_highpt',                                                                                 
               'samples'  : { 
                   'ggH_hww_PTH_200_300' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_200_300'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_200_300'][1]],
                   'ggH_hww_PTH_300_450' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_300_450'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_300_450'][1]], 
                  },  
               'type'  : 'shape',                                                                                                             
               'kind'  : 'weight',                                                                                                            
              }  

nuisances['ggH_scale_very_highpt'] = {                                                                                        
               'name'  : 'ggH_scale_very_highpt',                                                                             
               'samples'  : { 
                   'ggH_hww_PTH_450_650' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_450_650'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_450_650'][1]],
                   'ggH_hww_PTH_GT650' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_PTH_GT650'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_PTH_GT650'][1]],
                  },                                                       
               'type'  : 'shape',                                                                                                             
               'kind'  : 'weight',                                                                                                            
              }  
               
nuisances['ggH_scale_vbf'] = {                                                                                          
               'name'  : 'ggH_scale_vbf',                                                                             
               'samples'  : { 
                   'ggH_hww_GE2J_MJJ_350_700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_0_25'][1]],
                   'ggH_hww_GE2J_MJJ_350_700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_350_700_PTHJJ_GT25'][1]],
                   'ggH_hww_GE2J_MJJ_GT700_PTHJJ_0_25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_0_25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_0_25'][1]],
                   'ggH_hww_GE2J_MJJ_GT700_PTHJJ_GT25' : ['LHEScaleWeight[8]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_GT25'][0], 'LHEScaleWeight[0]/'+QCDScaleFactors['GG2H_GE2J_MJJ_GT700_PTHJJ_GT25'][1]], 
                  },
               'type'  : 'shape',                                                                                                             
               'kind'  : 'weight',                                                                                                            
              }         

#### QCD scale uncertainties for Higgs signals other than ggH

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','vbfH','125.09','scale','sm')

nuisances['QCDscale_qqH'] = {
    'name': 'QCDscale_qqH', 
    'samples': {
        #'qqH_hww': values,
        'qqH_htt': values
    },
    'type': 'lnN'
}

valueswh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','WH','125.09','scale','sm')
valueszh = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ZH','125.09','scale','sm')

nuisances['QCDscale_VH'] = {
    'name': 'QCDscale_VH', 
    'samples': {
        #'WH_hww': valueswh,
        'WH_htt': valueswh,
        #'ZH_hww': valueszh,
        'ZH_htt': valueszh
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ggZH','125.09','scale','sm')

nuisances['QCDscale_ggZH'] = {
    'name': 'QCDscale_ggZH', 
    'samples': {
        #'ggZH_hww': values
    },
    'type': 'lnN',
}

values = HiggsXS.GetHiggsProdXSNP('YR4','13TeV','ttH','125.09','scale','sm')

nuisances['QCDscale_ttH'] = {
    'name': 'QCDscale_ttH',
    'samples': {
        'ttH_hww': values
    },
    'type': 'lnN',
}

nuisances['QCDscale_WWewk'] = {
    'name': 'QCDscale_WWewk',
    'samples': {
        'WWewk': '1.11',
    },
    'type': 'lnN'
}

nuisances['QCDscale_qqbar_ACCEPT'] = {
    'name': 'QCDscale_qqbar_ACCEPT',
    'type': 'lnN',
    'samples': {
        #'qqH_hww': '1.003',
        'qqH_htt': '1.003',
        #'WH_hww': '1.010',
        'WH_htt': '1.010',
        #'ZH_hww': '1.015',
        'ZH_htt': '1.015',
    }
}

nuisances['QCDscale_gg_ACCEPT'] = {
    'name': 'QCDscale_gg_ACCEPT',
    'samples': {
        'ggH_htt': '1.012',
        #'ggH_hww': '1.012',
        #'ggZH_hww': '1.012',
        'ggWW': '1.012',
    },
    'type': 'lnN',
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

##rate parameters

# nuisances['WWnorm0j']  = {
#    'name'     : 'CMS_hww_WWnorm0j',
#    'samples'  : {
#       'WW'    : '1.00',
#       },
#    'type'     : 'rateParam',
#    #'cutspost' : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
#    'cuts'     : cuts0j
# }

# nuisances['WWnorm1j']  = {
#    'name'     : 'CMS_hww_WWnorm1j',
#    'samples'  : {
#       'WW'    : '1.00',
#       },
#    'type'     : 'rateParam',
#    #'cutspost' : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
#    'cuts'     : cuts1j
# }

nuisances['WWnorm2j']  = {
   'name'     : 'CMS_hww_WWnorm2j',
   'samples'  : {
      'WW'    : '1.00',
      },
   'type'     : 'rateParam',
   #'cutspost' : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
   'cuts'     : cuts2j
}

# nuisances['ggWWnorm0j']  = {
#   'name'     : 'CMS_hww_ggWWnorm0j',
#   'samples'  : {
#      'ggWW'  : '1.00',
#      },
#   'type'     : 'rateParam', 
#   #'cutspost' : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
#   'cuts'     : cuts0j
# }

# nuisances['ggWWnorm1j']  = {
#   'name'     : 'CMS_hww_ggWWnorm1j',
#   'samples'  : {
#      'ggWW'  : '1.00',
#      },
#   'type'     : 'rateParam',
#   #'cutspost' : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
#   'cuts'     : cuts1j
# }

nuisances['ggWWnorm2j']  = {
  'name'     : 'CMS_hww_ggWWnorm2j',
  'samples'  : {
     'ggWW'  : '1.00',
     },
  'type'     : 'rateParam',
  #'cutspost' : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
  'cuts'     : cuts2j
}

# nuisances['Topnorm0j']  = {
#    'name'     : 'CMS_hww_Topnorm0j',
#    'samples'  : {
#       'top'   : '1.00',
#       },
#    'type'     : 'rateParam',
#    #'cutspost' : lambda self, cuts: [cut for cut in cuts if '0j' in cut]
#    'cuts'     : cuts0j
# }

# nuisances['Topnorm1j']  = {
#    'name'     : 'CMS_hww_Topnorm1j',
#    'samples'  : {
#       'top'   : '1.00',
#       },
#    'type'     : 'rateParam',
#    #'cutspost' : lambda self, cuts: [cut for cut in cuts if '1j' in cut]
#    'cuts'     : cuts1j
# }

nuisances['Topnorm2j']  = {
   'name'     : 'CMS_hww_Topnorm2j',
   'samples'  : {
      'top'   : '1.00',
      },
   'type'     : 'rateParam',
   #'cutspost' : lambda self, cuts: [cut for cut in cuts if '2j' in cut]
   'cuts'     : cuts2j
}

#DYestim norm

# nuisances['DYeenorm0j']  = {
#    'name'     : 'DYeenorm0j',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    #'cuts'     : [cut for cut in cuts0j if 'ee' in cut]
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if '0j' in cut and 'ee' in cut]
# }

# nuisances['DYmmnorm0j']  = {
#    'name'     : 'DYmmnorm0j',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    #'cuts'     : [cut for cut in cuts0j if 'mm' in cut]
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if '0j' in cut and 'mm' in cut]
# }

# nuisances['DYeenorm1j']  = {
#    'name'     : 'DYeenorm1j',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    #'cuts'     : [cut for cut in cuts1j if 'ee' in cut]
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if '1j' in cut and 'ee' in cut]
# }

# nuisances['DYmmnorm1j']  = {
#    'name'     : 'DYmmnorm1j',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    #'cuts'     : [cut for cut in cuts1j if 'mm' in cut]
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if '1j' in cut and 'mm' in cut]
# }


##### DY norms

nuisances['DYeenorm2j']  = {
   'name'     : 'DYeenorm2j',
   'kind'     : 'weight',
   'type'     : 'shape',
   'samples'  : {
      'DY'    : ['1.','1.'] ,
      },
   #'cuts'     : [cut for cut in cuts2j if 'ee' in cut and 'vbf' not in cut and 'vh' not in cut]
   'cutspost' : lambda self, cuts: [cut for cut in cuts if '2j' in cut and 'ee' in cut] # and 'vh' not in cut and 'vbf' not in cut and 'hpt' not in cut]
}

nuisances['DYmmnorm2j']  = {
   'name'     : 'DYmmnorm2j',
   'kind'     : 'weight',
   'type'     : 'shape',
   'samples'  : {
      'DY'    : ['1.','1.'] ,
      },
   #'cuts'     : [cut for cut in cuts2j if 'mm' in cut and 'vbf' not in cut and 'vh' not in cut]
   'cutspost' : lambda self, cuts: [cut for cut in cuts if '2j' in cut and 'mm' in cut] # and 'vh' not in cut and 'vbf' not in cut and 'hpt' not in cut]
}

# nuisances['DYeenormvh']  = {
#    'name'     : 'DYeenormvh',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if 'vh' in cut and 'ee' in cut]
#    #'cuts'     : [cut for cut in cutsvh if 'ee' in cut]
# }

# nuisances['DYmmnormvh']  = {
#    'name'     : 'DYmmnormvh',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if 'vh' in cut and 'mm' in cut]
#    #'cuts'     : [cut for cut in cutsvh if 'mm' in cut]
# }

# nuisances['DYeenormvbf']  = {
#    'name'     : 'DYeenormvbf',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if 'vbf' in cut and 'ee' in cut]
#    #'cuts'     : [cut for cut in cutsvbf if 'ee' in cut]
# }

# nuisances['DYmmnormvbf']  = {
#    'name'     : 'DYmmnormvbf',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if 'vbf' in cut and 'mm' in cut]
#    #'cuts'     : [cut for cut in cutsvbf if 'mm' in cut]
# }

# nuisances['DYeenormhpt']  = {
#    'name'     : 'DYeenormhpt',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if 'hpt' in cut and 'ee' in cut]
#    #'cuts'     : [cut for cut in cutsvbf if 'ee' in cut]
# }

# nuisances['DYmmnormhpt']  = {
#    'name'     : 'DYmmnormhpt',
#    'kind'     : 'weight',
#    'type'     : 'shape',
#    'samples'  : {
#       'DY'    : ['1.','1.'] ,
#       },
#    'cutspost' : lambda self, cuts: [cut for cut in cuts if 'hpt' in cut and 'mm' in cut]
#    #'cuts'     : [cut for cut in cutsvbf if 'mm' in cut]
# }

########################################################

for n in nuisances.values():
    n['skipCMS'] = 1

print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))

# try:
#   for iNP in nuisances:
#     if 'cuts' in nuisances[iNP] :
#       newCuts = []
#       for iCut in nuisances[iNP]['cuts']:
#         for iOptim in optim:
#            newCuts.append(iCut)
#       nuisances[iNP]['cuts'] = newCuts
# except:
#   print "No optim dictionary"

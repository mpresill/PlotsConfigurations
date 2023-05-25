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



EFT_samples = ["quad_cS0","sm_lin_quad_cS0",  "quad_cS1","sm_lin_quad_cS1",   "quad_cM0","sm_lin_quad_cM0",  "quad_cM1","sm_lin_quad_cM1",   "quad_cM2","sm_lin_quad_cM2",   "quad_cM3","sm_lin_quad_cM3",   "quad_cM4","sm_lin_quad_cM4",   "quad_cM5","sm_lin_quad_cM5",   "quad_cM7","sm_lin_quad_cM7",   "quad_cT0","sm_lin_quad_cT0",   "quad_cT1","sm_lin_quad_cT1",   "quad_cT2","sm_lin_quad_cT2",   "quad_cT5","sm_lin_quad_cT5",   "quad_cT6","sm_lin_quad_cT6",   "quad_cT7","sm_lin_quad_cT7",   "quad_cT8","sm_lin_quad_cT8",   "quad_cT9","sm_lin_quad_cT9"  ]
mc_common = ["DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS", "VZ", "VVV","tZq_ll", "VBF-V","ZZlep"] 
mc_signal= ["sm_dipole"] #"sm","ewk_WpZ","ewk_WmZ","ewk_ZZ"]
mc_eos    = ["VBS_VV_QCD","tZq"] + mc_signal #+ EFT_samples

mc        = mc_common + mc_eos



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
    'samples': dict((skey, '1.015') for skey in mc if skey not in ['WW', 'top',"DY"] ),
   'group': 'lumi',
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ['WW', 'top',"DY"] ),
   'group': 'lumi',
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top',"DY"] ),
   'group': 'lumi',
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['WW', 'top',"DY"] ),
   'group': 'lumi',
}

#### FAKES
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst_em',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
   'group': 'fake',
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    },
   'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    },
   'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    },
   'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    },
   'group': 'fake',
#    'AsLnN': '1'
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
        'samples': dict((skey, btag_syst) for skey in mc),
       'group':'AK4jet',
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_hwwtrigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc), 
   'group':'trigger',
}



##### Electron Efficiency and energy scale  
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc), 
   'group':'lepton'
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc_common if skey not in ["WJets"]),
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
   'group':'lepton',
    #'AsLnN': '1'
}
#this is for the signals since they are in a different eos folder
nuisances['electronpt_SMPeos'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos), # if skey not in ["sm"], why was removed!?
    'folderUp': DirectorySMPeos+'__ElepTup_suffix',
    'folderDown': DirectorySMPeos+'__ElepTdo_suffix',
   'group':'lepton',
    #'AsLnN': '1'
}


##### Muon Efficiency and energy scale  
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc),
   'group':'lepton',
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
   'group':'lepton',
    #'AsLnN': '1'
}
#this is for the signals
nuisances['muonpt_SMPeos'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos), # if skey not in ["sm"], why was removed!?
    'folderUp': DirectorySMPeos+'__MupTup_suffix',
    'folderDown': DirectorySMPeos+'__MupTdo_suffix',
   'group':'lepton',
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
     'group': 'AK4jet',
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
     'group': 'AK4jet',
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
   'group': 'AK4jet',
#    'AsLnN': '1'
}

#this is for the signal
nuisances['JER_SMPeos'] = {
    'name': 'CMS_res_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos if skey not in mc_signal),  ####      WHY REMOVING SIGNAL?
    'folderUp': DirectorySMPeos+'__JERup_suffix',
    'folderDown': DirectorySMPeos+'__JERdo_suffix',
   'group': 'AK4jet',
#    'AsLnN': '1'
}



# ##### Pileup
pu_syst = '(puWeightUp/puWeight)', '(puWeightDown/puWeight)'

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
   'group': 'PU',
#    'AsLnN': '1',
}

### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_jetpuid_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc),
   'group': 'AK4jet',
}


#############################
###      fat jet - NEW     ##
#############################

nuisances['cfj_pt_JESTotal'] = {
    'name': 'CMS_scale_cleanfatJES_2018',
    'kind': 'tree',
    'type': 'shape',
    'auxname': 'FatJet',
    'mapUp' : 'pt_jesTotalUp',
    'mapDown': 'pt_jesTotalDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   'group' : 'AK8jet',
            #'AsLnN': '1'
}

nuisances['cfj_pt_JER'] = {
    'name': 'CMS_scale_cleanfatJER_2018',
    'type': 'shape',
    'kind': 'tree',
    'auxname':'FatJet',
    'mapUp' : 'pt_jerUp',
    'mapDown': 'pt_jerDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   'group' : 'AK8jet',
            #'AsLnN': '1'
}
nuisances['mV_jms'] = {
    'name': 'CMS_scale_mVjms_2018',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp' : 'jmsUp',
    'mapDown': 'jmsDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   'group' : 'AK8jet',
             #'AsLnN': '1'
}
nuisances['mV_jmr'] = {
    'name': 'CMS_scale_mVjmr_2018',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp': 'jmrUp',
    'mapDown': 'jmrDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   'group' : 'AK8jet',
            #'AsLnN': '1'
}

nuisances['mV_jesTotal'] = {
    'name': 'CMS_scale_mVjesTotal_2018',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp' : 'jesTotalUp',
    'mapDown': 'jesTotalDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   'group' : 'AK8jet',
            #'AsLnN': '1'
}

nuisances['mV_jer'] = {
    'name': 'CMS_scale_mVjer_2018',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp' : 'jerUp',
    'mapDown': 'jerDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
#    'folderUp': makeMCDirectory(''),
#    'folderDown': makeMCDirectory(''),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   'group' : 'AK8jet',
            #'AsLnN': '1'
}






###########################################
#############  PARTON SHOWER ##############
###########################################

nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS']), #PSWeights are buggy for some samples, we add them back by hand below
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS']), #PSWeights are buggy for some samples, we add them back by hand below
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
    if sample in ["ggWW","WW"]: continue   #this sample apparently doesn't have LHE weights, but it's real minor for us
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
           'group' : 'theory',
	        #'AsLnN': '1'    ##
    }

for sample in mc_eos :
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
           'group' : 'theory',
	        #'AsLnN': '1'    ##
    }

    # QCD acceptance on signal samples: this is needed only for SIGMA measurement, not for MU!
#nuisances['QCDscale_ewk_ZV_accept'] = {
#            'name'  : 'QCDscale_ewk_ZV_accept',
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples'  :  { k : ["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in mc_signal},
#            'AsLnN': '1',
#           'group' : 'theory',
#            #'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in mc_eos }
#        }


    # UNCOMMENT FOR EFT analysis NOt added for the moment to stay minimal: maybe not needed at all for EFT
#nuisances['QCDscale_VBS_EFT_accept'] = {
#            'name'  : 'QCDscale_VBS_EFT_accept',
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
   'group' : 'theory',
    #'AsLnN':  '1'
}

#    # pdf uncertainty on signal acceptance: this is needed only for SIGMA measurement, not for MU!
#nuisances['pdf_ewk_ZV_accept'] = {
#    'name'  : 'pdf_ewk_ZV_1718_accept',
#    'kind'  : 'weight_envelope',
#    'type'  : 'shape',
#    'samples': { k : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] for k in mc_signal},
#    'AsLnN': '1'  
#}

    # pdf uncertainty on signal acceptance  NOt added for the moment to stay minimal: maybe not needed at all for EFT
#nuisances['pdf_VBS_EFT_accept'] = {
#    'name'  : 'pdf_VBS_EFT_1718_accept',
#    'kind'  : 'weight_envelope',
#    'type'  : 'shape',
#    'samples': { k : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] for k in EFT_samples}
#}


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
               'group' : 'theory',
}


####### Generic "cross section uncertainties"
## Top pT reweighting uncertainty

nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True,
   'group' : 'theory',
}

#nuisances['VgStar'] = {
#    'name': 'CMS_hww_VgStarScale',
#    'type': 'lnN',
#    'samples': {
#        'VgS_L': '1.25'
#    },
#   'group' : 'theory',
#}
#
#nuisances['VZ'] = {
#    'name': 'CMS_hww_VZScale',
#    'type': 'lnN',
#    'samples': {
#        'VgS_H': '1.16'
#    },
#   'group' : 'theory',
#}


## rate parameters
"""nuisances['Topnorm_boosted_bVeto']  = {
               'name'  : 'Topnorm_boosted_bVeto_2018',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Boosted_topcr',
                   'Boosted_SR_bVeto',
                   ],
               'group' : 'Topnorm',
              }
nuisances['Topnorm_boosted_bTag']  = {
               'name'  : 'Topnorm_boosted_bTag_2018',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Boosted_topcr',
                   'Boosted_SR_bTag',
                   ],
               'group' : 'Topnorm',
              }

nuisances['Topnorm_resolved_bTag']  = {
               'name'  : 'Topnorm_resolved_bTag_2018',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Resolved_topcr',
		           'Resolved_SR_bTag'
                   ],
               'group' : 'Topnorm',
              }
nuisances['Topnorm_resolved_bVeto']  = {
               'name'  : 'Topnorm_resolved_bVeto_2018',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Resolved_topcr',
		           'Resolved_SR_bVeto'
                   ],
               'group' : 'Topnorm',
              }
"""


nuisances['Topnorm_boosted']  = {
               'name'  : 'Topnorm_boosted_2018',
               'samples'  : {
                   'top' : '1.0',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Boosted_topcr',
                   'Boosted_SR_bVeto',
                   'Boosted_SR_bTag',
                   ],
               'group' : 'Topnorm',
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
                   'Resolved_SR_bTag',
                   ],
               'group' : 'Topnorm',
              }         
              
DY_bins_res = []
DY_bins_boos = []
#DY_init= [1.13,1.22,1.10,1.10,0.96,1.0,0.85,0.69,0.79,0.49,0.48,0.58]
for bin in ['01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12'] :
        DY_bins_res.append("DY_Resolved_2d_" + bin)
        #DY_bins.append("DY_Boosted_Z_" + str(bin))
for bin in range(1,6):
        DY_bins_boos.append("DY_Boosted_Z_" + str(bin))

    # DY rateparams are initialized to the pre-fit value
res_bVeto_2018=['1.05', '1.19', '1.08', '1.06', '0.93', '0.96', '0.82', '0.68', '0.76', '0.45', '0.46', '0.55']
res_btag_2018=['1.10', '1.33', '1.10', '1.15', '1.03', '1.10', '0.90', '0.73', '0.83', '0.56', '0.57', '0.80']
boos_bVeto_2018=['0.64', '0.74', '0.64', '0.57', '0.51']
boos_bTag_2018=['0.77', '0.73', '0.58', '0.63', '0.52']

for DYbin in range(1,13):
		nuisances["DY_Resolved_2d_{}_norm_res_Z_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Resolved_2d_{}_norm_res_Z_bVeto_2018'.format(DYbin),
                #'samples'  : {DYbin: DY_init[i] },
                'samples'  : {DY_bins_res[DYbin-1]:res_bVeto_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bVeto',
		            'Resolved_SR_bVeto',
                   ],
               'group' : 'DYnorm',

            	}
		nuisances["DY_Resolved_2d_{}_norm_res_Z_btag_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Resolved_2d_{}_norm_res_Z_btag_2018'.format(DYbin),
                #'samples'  : {DYbin: DY_init[i] },
                'samples'  : {DY_bins_res[DYbin-1]:res_btag_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bTag',
                   'Resolved_SR_bTag',
                   ],
               'group' : 'DYnorm',
                 }
                
for DYbin in range(1,6):
		nuisances["DY_Boosted_Z_{}_norm_boost_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Boosted_Z_{}_norm_boost_bVeto_2018'.format(DYbin),
                'samples'  : {DY_bins_boos[DYbin-1]:boos_bVeto_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bVeto',
                   'Boosted_SR_bVeto',
                   ],
               'group' : 'DYnorm',
            }
		nuisances["DY_Boosted_Z_{}_norm_boost_bTag_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Boosted_Z_{}_norm_boost_bTag_2018'.format(DYbin),
                'samples'  : {DY_bins_boos[DYbin-1]:boos_bTag_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bTag',
                   'Boosted_SR_bTag',
                   ],
               'group' : 'DYnorm',
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

for n in nuisances.values():
    n['skipCMS'] = 1

#print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))

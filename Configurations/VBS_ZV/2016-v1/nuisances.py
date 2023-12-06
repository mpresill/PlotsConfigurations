# nuisances
# nuisances

#nuisances = {}

# name of samples here must match keys in samples.py 

# imported from samples.py:
# samples, treeBaseDir, mcProduction, mcSteps
# imported from cuts.py
# cuts

from re import M
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


############ Load norm factors / differential binning to normalize signal ####################
#import os
#import json
#configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
#configurations = os.path.dirname(configurations) # inclusive
#nfdict = json.load(open("%s/VBS_ZV/2016_Jul22/VBS_VV_QCD_QCDscale.json"%configurations))

#########################################################################

EFT_samples = ["quad_cS0","sm_lin_quad_cS0",  "quad_cS1","sm_lin_quad_cS1",   "quad_cM0","sm_lin_quad_cM0",  "quad_cM1","sm_lin_quad_cM1",   "quad_cM2","sm_lin_quad_cM2",   "quad_cM3","sm_lin_quad_cM3",   "quad_cM4","sm_lin_quad_cM4",   "quad_cM5","sm_lin_quad_cM5",   "quad_cM7","sm_lin_quad_cM7",   "quad_cT0","sm_lin_quad_cT0",   "quad_cT1","sm_lin_quad_cT1",   "quad_cT2","sm_lin_quad_cT2",   "quad_cT5","sm_lin_quad_cT5",   "quad_cT6","sm_lin_quad_cT6",   "quad_cT7","sm_lin_quad_cT7",   "quad_cT8","sm_lin_quad_cT8",   "quad_cT9","sm_lin_quad_cT9"  ]

mc_common = ["DY", "top", "WJets", "WW", "ggWW", "Vg", "VgS",  "VVV","VBF-V","ZZlep"] #"VZ","tZq_ll",  LEFT OUT ONLY FOR DATACARDS, if needed we'll introduce them back
mc_signal= ["sm_dipole"] #"sm","ewk_WpZ","ewk_WmZ","ewk_ZZ"]
mc_eos    = ["VBS_VV_QCD","tZq"] + mc_signal #+ EFT_samples

mc        = mc_common + mc_eos

################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity: old prescription commented
#nuisances['lumi_Uncorrelated'] = {
#    'name': 'lumi_13TeV_2016',
#    'type': 'lnN',
#    'samples': dict((skey, '1.022') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}
#
#nuisances['lumi_XYFact'] = {
#    'name': 'lumi_13TeV_XYFact',
#    'type': 'lnN',
#    'samples': dict((skey, '1.009') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}
#
#nuisances['lumi_BBDefl'] = {
#    'name': 'lumi_13TeV_BBDefl',
#    'type': 'lnN',
#    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}
#
#nuisances['lumi_DynBeta'] = {
#    'name': 'lumi_13TeV_DynBeta',
#    'type': 'lnN',
#    'samples': dict((skey, '1.005') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}
#
#nuisances['lumi_Ghosts'] = {
#    'name': 'lumi_13TeV_Ghosts',
#    'type': 'lnN',
#    'samples': dict((skey, '1.004') for skey in mc if skey not in ['WW', 'top', 'DY'])
#}
nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2016',
    'type': 'lnN',
    'samples': dict((skey, '1.01') for skey in mc if skey not in ['DY', 'top']),
   #'group': 'lumi',
}


nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ['top', "DY"]),
   #'group': 'lumi',
}

nuisances['lumi_Ghosts'] = {
    'name': 'lumi_13TeV_Ghosts',
    'type': 'lnN',
    'samples': dict((skey, '1.001') for skey in mc if skey not in ['DY', 'top']),
   #'group': 'lumi',
}


nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.003') for skey in mc if skey not in ['top', "DY"]),
   #'group': 'lumi',
}


nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.005') for skey in mc if skey not in ['DY', 'top']),
   #'group': 'lumi',
}


#### FAKES
nuisances['fake_syst'] = {
    'name': 'CMS_fake_syst_em',
    'type': 'lnN',
    'samples': {
        'Fake': '1.3'
    },
   #'group': 'fake',    
}

nuisances['fake_ele'] = {
    'name': 'CMS_fake_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    },
   #'group': 'fake',    
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    },
   #'group': 'fake',    
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    },
   #'group': 'fake',    
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    },
   #'group': 'fake',    
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
       #'group':'AK4jet',
        'AsLnN': '1',
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_trigger_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc), 
   #'group':'trigger',
}


####### Pre firing 2016 syst
prefire_syst = ['PrefireWeight_Up/PrefireWeight', 'PrefireWeight_Down/PrefireWeight']

nuisances['prefire'] = {
    'name': 'CMS_eff_prefiring_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, prefire_syst) for skey in mc), 
   #'group':'lepton'
#   'AsLnN': '1' #
}


##### Electron Efficiency and energy scale
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc),#if skey not in ['VBS_ZV','VBS_VV_QCD']
   # 'AsLnN': '1'
   #'group':'lepton'    
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
   #'group':'lepton'
    #'AsLnN': '1' #
}
#this is for the signals since they are in a different eos folder
nuisances['electronpt_SMPeos'] = {
    'name': 'CMS_scale_e_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos ),
    'folderUp': DirectorySMPeos+'__ElepTup_suffix',
    'folderDown': DirectorySMPeos+'__ElepTdo_suffix',
   #'group':'lepton'
    #'AsLnN': '1'
}

##### Muon Efficiency and energy scale
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc),# if skey not in ['VBS_ZV','VBS_VV_QCD']
    'AsLnN': '1'
   #'group':'lepton'
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
   #'group':'lepton'
   #'AsLnN': '1' 
}
#this is for the signals
nuisances['muonpt_SMPeos'] = {
    'name': 'CMS_scale_m_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos),
    'folderUp': DirectorySMPeos+'__MupTup_suffix',
    'folderDown': DirectorySMPeos+'__MupTdo_suffix',
   #'group':'lepton'
    #'AsLnN': '1'
}

##### Jet energy scale (AK4jets)
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
      'samples': dict((skey, ['1', '1']) for skey in mc_common if skey not in ['ggWW']),  # if skey not in ['DY'] ###CHECK IF THIS IS STILL TRUE: Do we have all the DY samples shapes UP/DOWN for this available?
      'folderUp': folderup,
      'folderDown': folderdo,
     #'group': 'AK4jet',
      'AsLnN': '1' 
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
     #'group': 'AK4jet',
      'AsLnN': '1' #
  }


##### PU 
pu_syst = '(puWeightUp/puWeight)', '(puWeightDown/puWeight)'

nuisances['PU'] = {
    'name': 'CMS_PU_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
   #'group': 'PU',
    'AsLnN': '1',
}


##### jet Pileup id
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_jetpuid_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc if skey not in ['ggWW']),
   #'group': 'AK4jet',
    #'AsLnN': '1', ##
	
}



#############################
###      fat jet - NEW     ##
#############################

##### Clean Fat jets ####
nuisances['cfj_pt_JESTotal'] = {
    'name': 'CMS_scale_cleanfatJES_2016',
    'kind': 'tree',
    'type': 'shape',
    'auxname': 'FatJet',
    'mapUp' : 'pt_jesTotalUp',
    'mapDown': 'pt_jesTotalDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   #'group': 'AK8jet',
   # 'AsLnN': '1'
}

nuisances['cfj_pt_JER'] = {
    'name': 'CMS_scale_cleanfatJER_2016',
    'type': 'shape',
    'kind': 'tree',
    'auxname':'FatJet',
    'mapUp' : 'pt_jerUp',
    'mapDown': 'pt_jerDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   #'group': 'AK8jet',

   # 'AsLnN': '1'
}

nuisances['mV_jmr'] = {
    'name': 'CMS_scale_mVjmr_2016',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp': 'jmrUp',
    'mapDown': 'jmrDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   #'group': 'AK8jet',
   # 'AsLnN': '1'
}
nuisances['mV_jms'] = {
    'name': 'CMS_scale_mVjms_2016',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp' : 'jmsUp',
    'mapDown': 'jmsDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   #'group': 'AK8jet',
   # 'AsLnN': '1'
}

nuisances['mV_jesTotal'] = {
    'name': 'CMS_scale_mVjesTotal_2016',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp' : 'jesTotalUp',
    'mapDown': 'jesTotalDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
   #'group': 'AK8jet',
   # 'AsLnN': '1'
}

nuisances['mV_jer'] = {
    'name': 'CMS_scale_mVjer_2016',
    'type': 'shape',
    'kind': 'tree',
    'auxname': 'FatJet_msoftdrop',
    'mapUp' : 'jerUp',
    'mapDown': 'jerDown',
    'samples': dict((skey, ['1', '1']) for skey in mc),
    'cuts'  : [
                'Boosted_topcr',
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
              ],
    #'group': 'AK8jet',
   # 'AsLnN': '1'
}

###########################################
#############  PARTON SHOWER ##############
###########################################
        # REF: https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/VBS_OS/Full2016_v7/SF/nuisances.py#L280-L318 
        # --- for bkg samples the PS weights were not available for 2016 and 2017, so they are retrieved with this parameterization measured here: 
        #      https://indico.cern.ch/event/904975/contributions/3826788/attachments/2020329/3377936/Update_on_PS_uncertainties_.pdf 

#nuisances['PS_ISR']  = {
#    'name': 'PS_ISR',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': {
#            'Vg'         : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
#            'VgS'        : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
#            'tZq'        : ['1.00123165501*(nCleanGenJet==0) + 1.01386556526*(nCleanGenJet==1) + 1.02245887029*(nCleanGenJet==2) + 0.993205603674*(nCleanGenJet>=3)', '0.999494407393*(nCleanGenJet==0) + 0.984238444469*(nCleanGenJet==1) + 0.974141312621*(nCleanGenJet==2) + 1.01048072654*(nCleanGenJet>=3)'],
#            'sm_dipole'  : ['0.979569717524*(nCleanGenJet==0) + 0.99503542437*(nCleanGenJet==1) + 1.00702800175*(nCleanGenJet==2) + 1.01557509829*(nCleanGenJet==3) + 1.00124263931*(nCleanGenJet==4) + 0.965308045922*(nCleanGenJet>=5)', '1.02785860625*(nCleanGenJet==0) + 1.00782611641*(nCleanGenJet==1) + 0.992182160138*(nCleanGenJet==2) + 0.981484686156*(nCleanGenJet==3) + 0.999384703588*(nCleanGenJet==4) + 1.04536761457*(nCleanGenJet>=5)'],
#            'VBS_VV_QCD' : ['1.033603111*(nCleanGenJet==0) + 1.03366298306*(nCleanGenJet==1) + 1.03100663409*(nCleanGenJet==2) + 1.01763474818*(nCleanGenJet==3) + 0.99426701155*(nCleanGenJet==4) + 0.966395594522*(nCleanGenJet>=5)', '0.959719184123*(nCleanGenJet==0) + 0.958964445419*(nCleanGenJet==1) + 0.96258655446*(nCleanGenJet==2) + 0.978302950012*(nCleanGenJet==3) + 1.00689068392*(nCleanGenJet==4) + 1.04258143888*(nCleanGenJet>=5)'],
#            'DY'         : ['1.00289159668*(nCleanGenJet==0) + 1.02256590902*(nCleanGenJet==1) + 1.04370416265*(nCleanGenJet==2) + 1.04166611447*(nCleanGenJet==3) + 1.02543300978*(nCleanGenJet==4) + 1.00040336474*(nCleanGenJet>=5)', '0.996818834245*(nCleanGenJet==0) + 0.972999502309*(nCleanGenJet==1) + 0.947458999127*(nCleanGenJet==2) + 0.949578764223*(nCleanGenJet==3) + 0.968788941761*(nCleanGenJet==4) + 0.998919620361*(nCleanGenJet>=5)'],
#            'top'        : ['1.00339242529*(nCleanGenJet==0) + 1.00513980583*(nCleanGenJet==1) + 1.0094119789*(nCleanGenJet==2) + 0.994131527355*(nCleanGenJet>=3)', '0.996310428955*(nCleanGenJet==0) + 0.994223875452*(nCleanGenJet==1) + 0.989098747875*(nCleanGenJet==2) + 1.00817548136*(nCleanGenJet>=3)'],
#            'WJets'      : ['1.05215433399*(nCleanGenJet==0) + 1.06536650299*(nCleanGenJet==1) + 1.0632742001*(nCleanGenJet==2) + 1.04221231583*(nCleanGenJet>=3)', '0.954088099736*(nCleanGenJet==0) + 0.930844901487*(nCleanGenJet==1) + 0.93295137745*(nCleanGenJet==2) + 0.960121099889*(nCleanGenJet>=3)'],
#            'WW'         : ['1.03101943713*(nCleanGenJet==0) + 1.03352892176*(nCleanGenJet==1) + 1.01657315368*(nCleanGenJet==2) + 0.963437033747*(nCleanGenJet>=3)', '0.963570054648*(nCleanGenJet==0) + 0.959757644902*(nCleanGenJet==1) + 0.979824433523*(nCleanGenJet==2) + 1.04747147855*(nCleanGenJet>=3)'],
#            'ggWW'       : ['1.04241595114*(nCleanGenJet==0) + 0.972206252477*(nCleanGenJet==1) + 0.919004494295*(nCleanGenJet==2) + 0.876108152332*(nCleanGenJet>=3)', '0.949147308259*(nCleanGenJet==0) + 1.03101332712*(nCleanGenJet==1) + 1.10360565656*(nCleanGenJet==2) + 1.17113578081*(nCleanGenJet>=3)'],
#            'VZ'         : ['1.00739576519*(nCleanGenJet==0) + 1.02184914983*(nCleanGenJet==1) + 1.01801973722*(nCleanGenJet==2) + 0.989499687334*(nCleanGenJet>=3)', '0.991105068149*(nCleanGenJet==0) + 0.973774126163*(nCleanGenJet==1) + 0.978781564346*(nCleanGenJet==2) + 1.01475324898*(nCleanGenJet>=3)'],
#            'VVV'        : ['1.02987133969*(nCleanGenJet==0) + 1.0213904525*(nCleanGenJet==1) + 1.00886979738*(nCleanGenJet==2) + 0.977642000383*(nCleanGenJet>=3)', '0.965150589752*(nCleanGenJet==0) + 0.975475697908*(nCleanGenJet==1) + 0.990942215976*(nCleanGenJet==2) + 1.03132089972*(nCleanGenJet>=3)'],
#            'VBF-V'      : ['1.01495587791*(nCleanGenJet==0) + 1.01951555507*(nCleanGenJet==1) + 1.00929038995*(nCleanGenJet==2) + 0.950747494733*(nCleanGenJet>=3)', '0.981420072505*(nCleanGenJet==0) + 0.975841901281*(nCleanGenJet==1) + 0.9885517861*(nCleanGenJet==2) + 1.06360527002*(nCleanGenJet>=3)'],
#    },
#       #'group' : 'theory',
#       #'AsLnN': '1'
#}
#nuisances['PS_FSR']  = {
#    'name': 'PS_FSR',
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': {
#            'Vg'         : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
#            'VgS'        : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
#            'tZq'        : ['0.961221752589*(nCleanGenJet==0) + 0.983278638281*(nCleanGenJet==1) + 0.991150343983*(nCleanGenJet==2) + 1.00622125886*(nCleanGenJet>=3)', '1.06974795763*(nCleanGenJet==0) + 1.032213123*(nCleanGenJet==1) + 1.01827374992*(nCleanGenJet==2) + 0.991873655896*(nCleanGenJet>=3)'],
#            'sm_dipole'  : ['0.963536426385*(nCleanGenJet==0) + 0.968991322002*(nCleanGenJet==1) + 0.986170589563*(nCleanGenJet==2) + 0.996037996564*(nCleanGenJet==3) + 1.00816310034*(nCleanGenJet==4) + 1.01093247383*(nCleanGenJet>=5)', '1.03892466353*(nCleanGenJet==0) + 1.05009520269*(nCleanGenJet==1) + 1.02266914861*(nCleanGenJet==2) + 1.00845339263*(nCleanGenJet==3) + 0.986637115763*(nCleanGenJet==4) + 0.983642554866*(nCleanGenJet>=5)'],
#            'VBS_VV_QCD' : ['0.945066815425*(nCleanGenJet==0) + 0.972582735071*(nCleanGenJet==1) + 0.988523690437*(nCleanGenJet==2) + 1.00287575468*(nCleanGenJet==3) + 1.01165856367*(nCleanGenJet==4) + 1.01119365683*(nCleanGenJet>=5)', '1.06441660683*(nCleanGenJet==0) + 1.04911902766*(nCleanGenJet==1) + 1.0237203683*(nCleanGenJet==2) + 0.998012061778*(nCleanGenJet==3) + 0.983111991115*(nCleanGenJet==4) + 0.983710782617*(nCleanGenJet>=5)'],
#            'DY'         : ['0.998620763476*(nCleanGenJet==0) + 1.00956012608*(nCleanGenJet==1) + 1.02787599245*(nCleanGenJet==2) + 1.04226084427*(nCleanGenJet==3) + 1.04341062373*(nCleanGenJet==4) + 1.02959783311*(nCleanGenJet>=5)', '1.00312586596*(nCleanGenJet==0) + 0.985563617582*(nCleanGenJet==1) + 0.95955848683*(nCleanGenJet==2) + 0.941502022199*(nCleanGenJet==3) + 0.937712403253*(nCleanGenJet==4) + 0.957383919958*(nCleanGenJet>=5)'],
#            'top'        : ['0.970429299854*(nCleanGenJet==0) + 0.986465401741*(nCleanGenJet==1) + 1.00080524025*(nCleanGenJet==2) + 1.00980469124*(nCleanGenJet>=3)', '1.04891800551*(nCleanGenJet==0) + 1.02346219356*(nCleanGenJet==1) + 1.00155162521*(nCleanGenJet==2) + 0.984571569893*(nCleanGenJet>=3)'],
#            'WJets'      : ['0.980101832*(nCleanGenJet==0) + 0.993410570508*(nCleanGenJet==1) + 1.03173250496*(nCleanGenJet==2) + 1.02961854606*(nCleanGenJet>=3)', '0.982638237774*(nCleanGenJet==0) + 1.02048105914*(nCleanGenJet==1) + 0.946930160368*(nCleanGenJet==2) + 0.964520317878*(nCleanGenJet>=3)'],
#            'WW'         : ['0.983464048003*(nCleanGenJet==0) + 0.991168431592*(nCleanGenJet==1) + 1.00478489204*(nCleanGenJet==2) + 1.00321455714*(nCleanGenJet>=3)', '1.0276527499*(nCleanGenJet==0) + 1.01532278571*(nCleanGenJet==1) + 0.995535543759*(nCleanGenJet==2) + 0.994113673109*(nCleanGenJet>=3)'],
#            'ggWW'       : ['0.994239997364*(nCleanGenJet==0) + 1.00698249813*(nCleanGenJet==1) + 1.01502187729*(nCleanGenJet==2) + 1.01798950084*(nCleanGenJet>=3)', '1.00915505169*(nCleanGenJet==0) + 0.990489065307*(nCleanGenJet==1) + 0.976616522192*(nCleanGenJet==2) + 0.957600504788*(nCleanGenJet>=3)'],
#            'VZ'         : ['0.987078514784*(nCleanGenJet==0) + 0.992789093337*(nCleanGenJet==1) + 1.01089890954*(nCleanGenJet==2) + 1.01396456475*(nCleanGenJet>=3)', '1.02127788102*(nCleanGenJet==0) + 1.01167746531*(nCleanGenJet==1) + 0.985347627847*(nCleanGenJet==2) + 0.980038365955*(nCleanGenJet>=3)'],
#            'VVV'        : ['0.990288829498*(nCleanGenJet==0) + 0.984316494274*(nCleanGenJet==1) + 1.00232605296*(nCleanGenJet==2) + 1.01362602415*(nCleanGenJet>=3)', '1.02171399302*(nCleanGenJet==0) + 1.04053330541*(nCleanGenJet==1) + 1.00018227094*(nCleanGenJet==2) + 0.976478139211*(nCleanGenJet>=3)'],
#            'VBF-V'      : ['0.974946339917*(nCleanGenJet==0) + 0.992423768259*(nCleanGenJet==1) + 1.00895839758*(nCleanGenJet==2) + 1.01090197115*(nCleanGenJet>=3)', '1.04219975267*(nCleanGenJet==0) + 1.01342193253*(nCleanGenJet==1) + 0.988282087395*(nCleanGenJet==2) + 0.980232687856*(nCleanGenJet>=3)'],
#    },
#        #'group' : 'theory',
#        #'AsLnN': '1'
#}
"""for sample in mc:
    if sample in ["top"]: 
        nuisances['PS_ISR']  = {
            'name': 'PS_ISR',
            'kind': 'weight',
            'type': 'shape',
            'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS','DY']), #PSWeights are buggy for some samples, we add them back by hand below
            #'AsLnN': '1',
        }
        nuisances['PS_FSR']  = {
            'name': 'PS_FSR',
            'kind': 'weight',
            'type': 'shape',
            'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS','DY']), #PSWeights are buggy for some samples, we add them back by hand below
            #'AsLnN': '1',
        }
    else:
        nuisances['PS_ISR']  = {
            'name': 'PS_ISR',
            'kind': 'weight',
            'type': 'shape',
            'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS','DY','WJets']), #PSWeights are buggy for some samples, we add them back by hand below
            'cuts'  : [
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
                'Resolved_SR_bVeto',
                'Resolved_SR_bTag',
                'Resolved_DYcr_bVeto',
		        'Resolved_DYcr_bTag',
              ],
            #'AsLnN': '1',
        }
        nuisances['PS_FSR']  = {
            'name': 'PS_FSR',
            'kind': 'weight',
            'type': 'shape',
            'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS','DY','WJets']), #PSWeights are buggy for some samples, we add them back by hand below
            'cuts'  : [
                'Boosted_SR_bVeto',
                'Boosted_SR_bTag',
                'Boosted_DYcr_bVeto',
		        'Boosted_DYcr_bTag',
                'Resolved_SR_bVeto',
                'Resolved_SR_bTag',
                'Resolved_DYcr_bVeto',
		        'Resolved_DYcr_bTag',
              ],
            #'AsLnN': '1',
        }
        ####### removed top cr PS for other MCs, as they proked bugus norm for very low-stat

"""
###########################################
#############    QCD scale   ##############
###########################################
## Shape nuisance due to QCD scale variations for DY
## LHE scale variation weights (w_var / w_nominal)
## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
#qcdscale_variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
### method 1:
#for sample in mc_common :
#    if sample in ["ggWW"]+mc_eos: continue   #this sample apparently doesn't have LHE weights, but it's real minor for us
#    nuisances['QCD_scale_'+sample] = {
#            'name'  : 'QCDscale_'+sample,
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] },
#	    #'AsLnN': '1'    ##
#    }
#
#nuisances['QCD_scale_VBS_ZV'] = {
#            'name'  : 'QCDscale_VBS_ZV',
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in ["sm"] }
#        }
#
#nuisances['QCD_scale_VBS_VV_QCD'] = {
#            'name'  : 'QCDscale_VBS_ZV',
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples': { k:["LHEScaleWeight[0]", "LHEScaleWeight[8]"] for k in ["VBS_VV_QCD"] }
#        }
#
#for sample in EFT_samples : ## this maybe needs to be on acceptance only
#    nuisances['QCD_scale_'+sample] = {
#            'name'  : 'QCDscale_'+sample,
#            'kind'  : 'weight',
#            'type'  : 'shape',
#            'samples'  :  { sample: ["LHEScaleWeight[0]", "LHEScaleWeight[8]"] },
#    	    #'AsLnN': '1'    ##
#    }

nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS','WJets','WW','ggWW']), #PSWeights are buggy for some samples, we add them back by hand below, for DY, they are negligible. NB: rimuovere ,'tZq','sm_dipole','VBF-V' per topcr BOGUS NORM
    'cuts'  : [
                   'Boosted_SR_bVeto',
                   'Boosted_SR_bTag',
                   'Resolved_SR_bVeto',
                   'Resolved_SR_bTag',
                   'Boosted_DYcr_bVeto',
                   'Boosted_DYcr_bTag',
                   'Resolved_DYcr_bVeto',
                   'Resolved_DYcr_bTag',
                   ],
#'AsLnN': '1',
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS','WJets','WW','ggWW']), #PSWeights are buggy for some samples, we add them back by hand below, for DY, they are negligible. NB: rimuovere ,'tZq','sm_dipole','VBF-V' per topcr BOGUS NORM
    'cuts'  : [
                   'Boosted_SR_bVeto',
                   'Boosted_SR_bTag',
                   'Resolved_SR_bVeto',
                   'Resolved_SR_bTag',
                   'Boosted_DYcr_bVeto',
                   'Boosted_DYcr_bTag',
                   'Resolved_DYcr_bVeto',
                   'Resolved_DYcr_bTag',
                   ],
#'AsLnN': '1',
}

# method 2
## -> alternative implementation with envelope (used is VBS OSww https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/VBS_OS/Full2016_v7/SF/nuisances.py#L461-L502)

## All 2016 samples have either 0 or 9 LHEScaleWeights
#variations = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[5],1)', 'Alt$(LHEScaleWeight[7],1)', 'Alt$(LHEScaleWeight[8],1)']
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

for sample in mc_common :
    if sample in ["ggWW", "WW","WJets","VgS","DY"]: continue   #,"DY","top" #this sample apparently doesn't have LHE weights, but it's real minor for us
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
            #'group' : 'theory',
	        #'AsLnN': '1'    ##
    }
## maybe top needs particular care, see e.g. https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/WW/FullRunII/Full2016_v7/inclusive/nuisances.py#L552-L604 

for sample in ["DY"] :
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
            #'group' : 'theory',
            'cuts'  : [
                   'Boosted_SR_bVeto',
                   'Boosted_SR_bTag',
                   'Resolved_SR_bVeto',
                   'Resolved_SR_bTag',
                   'Boosted_DYcr_bVeto',
                   'Boosted_DYcr_bTag',
                   'Resolved_DYcr_bVeto',
                   'Resolved_DYcr_bTag',
                   ],
	        'AsLnN': '1'    ##
    }


#for sample in mc_eos :
for sample in ["sm_dipole"] :       #### VBS_VV_QCD has bugged QCDscale weights for 2016!!!
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
            #'group' : 'theory',
	       # 'AsLnN': '1'    ##
    }

#for sample in mc_eos :
#for sample in ["VBS_VV_QCD"] :       #### VBS_VV_QCD has bugged QCDscale weights for 2016, it is extracted as normalization factors from 2018
#    nuisances['QCDscale_'+sample] = {
#            'name'  : 'QCDscale_'+sample,
#            'type': 'lnN',
#            'samples'  :  { sample: '1.30/0.78' },
#            #'group' : 'theory',
#	        #'AsLnN': '1'    ##
#    }
for sample in ["VBS_VV_QCD"] :       #### VBS_VV_QCD has bugged QCDscale weights for 2016, it is extracted as normalization factors from 2018
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
            'cuts'  : [
                   'Boosted_SR_bVeto',
                   'Boosted_SR_bTag',
                   'Resolved_SR_bVeto',
                   'Resolved_SR_bTag',
                   'Boosted_DYcr_bVeto',
                   'Boosted_DYcr_bTag',
                   'Resolved_DYcr_bVeto',
                   'Resolved_DYcr_bTag',
                   ],
#            'samples'  :  dict((skey, ['1', '1']) for skey in ["VBS_VV_QCD"]), #{ sample: variations },
            #'group' : 'theory',
	       # 'AsLnN': '1'    ##
    }

# for VBS VV QCD 2016 the sets of QCDscale weights are bugged
# for an alternative implementation see: https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/VBS_OS/DNN/2016/comb_paper/nuisances.py#L522-L551 
#VBSScaleNormFactors2j = {
#    'Alt$(LHEScaleWeight[0],1)': 1.04499,
#    'Alt$(LHEScaleWeight[1],1)': 1.06296,
#    'Alt$(LHEScaleWeight[3],1)': 0.943058,
#    'Alt$(LHEScaleWeight[5],1)': 1.01909,
#    'Alt$(LHEScaleWeight[7],1)': 0.94859,
#    'Alt$(LHEScaleWeight[8],1)': 0.98728
#}
#for var in topvariations:
#  WWvars2j.append(var+'/'+str(WWScaleNormFactors2j[var]))
#
#nuisances['QCDscale_WW_2j']  = {
#    'name'  : 'QCDscale_WW_2j',
#    'skipCMS' : 1,
#    'kind'  : 'weight_envelope',
#    'type'  : 'shape',
#    #'cutspost' : lambda self, cuts: [cut for cut in cuts if '2j' in cut],
#    'samples'  : {
#       'WW' : WWvars2j,
#    }
#}





# -> Davide also considered an uncertainty on the acceptance for signals: https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/VBSjjlnu_v7/Configurations/VBSjjlnu/Full2016v7/conf_fit_v4.5/nuisances_datacard_split.py#L509-L525
# >>>next iteration....
## QCD acceptance
#for sample in mc_signal :
#    nuisances['QCDscale_'+sample+'_accept'] = {
#                'name'  : 'QCDscale_'+sample+'_accept',
#                'kind'  : 'weight',
#                'type'  : 'shape',
#                'samples'  :  { sample : ["QCDscale_normalized[0]", "QCDscale_normalized[8]"] },
#                'AsLnN': '1'    ##
#                #'samples': { k:["QCDscale_normalized[0]", "QCDscale_normalized[8]"] for k in mc_eos }
#            }

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
#pdf_variations = ["LHEPdfWeight[%d]" %i for i in range(100)]
nuisances['pdf_weight_16'] = { ### UPDATED FOR 2016 SAMPLES: NEED TO USE RMS HERE!!!
    'name'  : 'pdf_16',
    'kind'  : 'weight_rms',    
    'type'  : 'shape',
    'samples' :  { s: ["LHEPdfWeight[%d]" %i for i in range(100)] for s in mc_common if s not in ["DY","top","WW","ggWW"]+mc_signal+EFT_samples}, #-> here we reomve bkgs measured in CR, as well as BSM signals (PHDF4LHC prescription for BSM measurement)
    #'group' : 'theory',
    'AsLnN':  '1'
}
#nuisances['pdf_weight'] = { ### UPDATED FOR 2016 SAMPLES: NEED TO USE RMS HERE!!!
#    'name'  : 'pdf_16',
#    #'kind'  : 'weight_rms',    
#    #'type'  : 'shape',
#    'kind': 'weight',
#    'type'  : 'shape',
#    'samples'  :  dict((skey, ['1', '1']) for skey in mc), #{ sample: variations },
#    #'group' : 'theory',
#    'AsLnN':  '1'
#}


nuisances['pdf_weight'] = { ###TO BE UPDATED FOR 2016 SIGNAL: here we generated with NNPDF3.1, so it should be correlated with 2017 and 2018 instead
    'name'  : 'pdf_1718',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc_signal}, #-> here we reomve bkgs measured in CR, as well as BSM signals (PHDF4LHC prescription for BSM measurement)
    #'group' : 'theory',
    'AsLnN':  '1'
}
    # pdf uncertainty on signal acceptance
#for sample in mc_signal :
#    nuisances['pdf_'+sample+'_accept'] = {
#        'name'  : 'pdf_'+sample+'_16_accept',
#        'kind'  : 'weight_envelope',
#        'type'  : 'shape',
#        'samples': { sample : [ 'Alt$(PDFweight_normalized['+str(i)+'], 1.)' for i in range(0,103) ] },
#        'AsLnN': '1'    ##
#    }


######  UE: THIS NEEDS TO BE FIXED 
# An overall 1.5% UE uncertainty will cover all the UEup/UEdo variations
# And we don't observe any dependency of UE variations on njet
nuisances['UE']  = {
                'name'  : 'UE_CUETP8',
                'skipCMS' : 1,
                'type': 'lnN',
                'samples': dict((skey, '1.015') for skey in mc if skey not in ['DY','top']),########### removed fot top and DY, which are measured in CRs 
                #'group' : 'theory',
}



####### Generic "cross section uncertainties"
#nuisances['singleTopToTTbar'] = {
#    'name': 'singleTopToTTbar',
#    'skipCMS': 1,
#    'kind': 'weight',
#    'type': 'shape',
#    'samples': { 
#       'top': [
#        'isSingleTop * 1.0816 + isTTbar',
#        'isSingleTop * 0.9184 + isTTbar']
#      }
#}


## Top pT reweighting uncertainty
nuisances['TopPtRew'] = {
    'name': 'CMS_topPtRew',   # Theory uncertainty
    'kind': 'weight',
    'type': 'shape',
    'samples': {'top': ["1.", "1./Top_pTrw"]},
    'symmetrize': True,
#    'AsLnN': '1'
    #'group' : 'theory',
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
                   'Boosted_SR_bVeto',
		           'Boosted_SR_bTag'
                   ],
                #'group' : 'Topnorm',
              }

nuisances['Topnorm_resolved']  = {
               'name'  : 'Topnorm_resolved_2016',
               'samples'  : {
                   'top' : '1.00',
                   },
               'type'  : 'rateParam',
               'cuts'  : [
                   'Resolved_topcr',
                   'Resolved_SR_bVeto',
		           'Resolved_SR_bTag'
                   ],
                #'group' : 'Topnorm',
              }

DY_bins=[]
for bin in range(1,6):
        DY_bins.append("DY_bin" + str(bin))

    # DY rateparams are initialized to the pre-fit value
res_bVeto_2016=['1.13', '1.12', '1.21', '0.93', '0.87']
res_bTag_2016=['1.24', '1.16', '1.14', '1.17', '0.85']
boos_bVeto_2016=['0.99', '0.86', '0.96', '0.73', '0.51']
boos_bTag_2016=['0.95', '0.99', '0.97', '0.76', '0.55']

for DYbin in range(1,6):
        nuisances["DY_bin{}_norm_res_Z_bVeto_2016".format(DYbin)]  = {
                'name'  : 'CMS_DY_bin{}_norm_res_Z_bVeto_2016'.format(DYbin),
                'samples'  : {DY_bins[DYbin-1]:'1.00'},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bVeto',
                   'Resolved_SR_bVeto',
                   ],
                #'group' : 'DYnorm',
            }
        
        
        nuisances["DY_bin{}_norm_res_Z_bTag_2016".format(DYbin)]  = {
                'name'  : 'CMS_DY_bin{}_norm_res_Z_bTag_2016'.format(DYbin),
                'samples'  : {DY_bins[DYbin-1]:'1.00'},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bTag',
                   'Resolved_SR_bTag',
                   ],
                #'group' : 'DYnorm',
            }
        
        nuisances["DY_bin{}_norm_boost_Z_bVeto_2016".format(DYbin)]  = {
                'name'  : 'CMS_DY_bin{}_norm_boost_Z_bVeto_2016'.format(DYbin),    
                'samples'  : {DY_bins[DYbin-1]:'1.00'},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bVeto',
                   'Boosted_SR_bVeto',
                   ],
                #'group' : 'DYnorm',
            }
        
        nuisances["DY_bin{}_norm_boost_Z_bTag_2016".format(DYbin)]  = {
                'name'  : 'CMS_DY_bin{}_norm_boost_Z_bTag_2016'.format(DYbin),    
                'samples'  : {DY_bins[DYbin-1]:'1.00'},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bTag',
                   'Boosted_SR_bTag',
                   ],
                #'group' : 'DYnorm',
            }
             
# Use the following if you want to apply the automatic combine MC stat nuisances.
nuisances['stat'] = {
    'type': 'auto',
    'maxPoiss': '10',
    'includeSignal': '0',
    #  nuisance ['maxPoiss'] =  Number of threshold events for Poisson modelling
    #  nuisance ['includeSignal'] =  Include MC stat nuisances on signal processes (1=True, 0=False)
    'samples': {},
}


for n in nuisances.values():
    n['skipCMS'] = 1

#print ' '.join(nuis['name'] for nname, nuis in nuisances.iteritems() if nname not in ('lumi', 'stat'))


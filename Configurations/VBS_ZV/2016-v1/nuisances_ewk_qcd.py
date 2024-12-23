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

#EFT_samples = ["quad_cS0","sm_lin_quad_cS0",  "quad_cS1","sm_lin_quad_cS1",   "quad_cM0","sm_lin_quad_cM0",  "quad_cM1","sm_lin_quad_cM1",   "quad_cM2","sm_lin_quad_cM2",   "quad_cM3","sm_lin_quad_cM3",   "quad_cM4","sm_lin_quad_cM4",   "quad_cM5","sm_lin_quad_cM5",   "quad_cM7","sm_lin_quad_cM7",   "quad_cT0","sm_lin_quad_cT0",   "quad_cT1","sm_lin_quad_cT1",   "quad_cT2","sm_lin_quad_cT2",   "quad_cT5","sm_lin_quad_cT5",   "quad_cT6","sm_lin_quad_cT6",   "quad_cT7","sm_lin_quad_cT7",   "quad_cT8","sm_lin_quad_cT8",   "quad_cT9","sm_lin_quad_cT9"  ]

mc_common = ["DY", "top", "other", "Vg", "VgS", "VBF-V"] #"VZ","tZq_ll",  LEFT OUT ONLY FOR DATACARDS, if needed we'll introduce them back
mc_signal= ["ZVjj_QCD","sm_dipole"] #"sm","ewk_WpZ","ewk_WmZ","ewk_ZZ"]
mc_eos    = ["VBS_WV_QCD","tZq","tZq_QCD"] + mc_signal #+ EFT_samples

mc        = mc_common + mc_eos

################################ EXPERIMENTAL UNCERTAINTIES  #################################

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
#        'AsLnN': '1',
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
    'folderUp': 'root://eoscms.cern.ch/'+makeMCDirectory('ElepTup_suffix'),
    'folderDown': 'root://eoscms.cern.ch/'+makeMCDirectory('ElepTdo_suffix'),
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
    'folderUp': 'root://eoscms.cern.ch/'+DirectorySMPeos+'__ElepTup_suffix',
    'folderDown': 'root://eoscms.cern.ch/'+DirectorySMPeos+'__ElepTdo_suffix',
   #'group':'lepton'
    #'AsLnN': '1'
}

##### Muon Efficiency and energy scale
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2016',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc),# if skey not in ['VBS_ZV','VBS_VV_QCD']
    #'AsLnN': '1'
   #'group':'lepton'
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2016',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc_common),
    'folderUp': 'root://eoscms.cern.ch/'+makeMCDirectory('MupTup_suffix'),
    'folderDown': 'root://eoscms.cern.ch/'+makeMCDirectory('MupTdo_suffix'),
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
    'folderUp': 'root://eoscms.cern.ch/'+DirectorySMPeos+'__MupTup_suffix',
    'folderDown': 'root://eoscms.cern.ch/'+DirectorySMPeos+'__MupTdo_suffix',
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
    folderup = 'root://eoscms.cern.ch/'+makeMCDirectory('JESAbsoluteup_suffix')
    folderdo = 'root://eoscms.cern.ch/'+makeMCDirectory('JESAbsolutedo_suffix')
  elif 'BBEC1' in js:
    folderup = 'root://eoscms.cern.ch/'+makeMCDirectory('JESBBEC1up_suffix')
    folderdo = 'root://eoscms.cern.ch/'+makeMCDirectory('JESBBEC1do_suffix')
  elif 'EC2' in js:
    folderup = 'root://eoscms.cern.ch/'+makeMCDirectory('JESEC2up_suffix')
    folderdo = 'root://eoscms.cern.ch/'+makeMCDirectory('JESEC2do_suffix')
  elif 'HF' in js:
    folderup = 'root://eoscms.cern.ch/'+makeMCDirectory('JESHFup_suffix')
    folderdo = 'root://eoscms.cern.ch/'+makeMCDirectory('JESHFdo_suffix')
  elif 'Relative' in js:
    folderup = 'root://eoscms.cern.ch/'+makeMCDirectory('JESRelativeup_suffix')
    folderdo = 'root://eoscms.cern.ch/'+makeMCDirectory('JESRelativedo_suffix')
  elif 'FlavorQCD' in js:
    folderup = 'root://eoscms.cern.ch/'+makeMCDirectory('JESFlavorQCDup_suffix')
    folderdo = 'root://eoscms.cern.ch/'+makeMCDirectory('JESFlavorQCDdo_suffix')

  nuisances[js] = {
      'name': 'CMS_scale_'+js,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js+'up',
      'mapDown': js+'do',
      'samples': dict((skey, ['1', '1']) for skey in mc_common),  # if skey not in ['ggWW'] ### if skey not in ['DY'] ###CHECK IF THIS IS STILL TRUE: Do we have all the DY samples shapes UP/DOWN for this available?
      'folderUp': folderup,
      'folderDown': folderdo,
     #'group': 'AK4jet',
     # 'AsLnN': '1' 
  }



#this is for signals
for js_VBS_ZV in jes_systs:
  if 'Absolute' in js_VBS_ZV: 
    folderup_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESAbsoluteup_suffix'
    folderdo_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESAbsolutedo_suffix'
  elif 'BBEC1' in js_VBS_ZV:
    folderup_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESBBEC1up_suffix'
    folderdo_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESBBEC1do_suffix'
  elif 'EC2' in js_VBS_ZV:
    folderup_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESEC2up_suffix'
    folderdo_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESEC2do_suffix'
  elif 'HF' in js_VBS_ZV:
    folderup_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESHFup_suffix'
    folderdo_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESHFdo_suffix'
  elif 'Relative' in js_VBS_ZV:
    folderup_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESRelativeup_suffix'
    folderdo_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESRelativedo_suffix'
  elif 'FlavorQCD' in js_VBS_ZV:
    folderup_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESFlavorQCDup_suffix'
    folderdo_signal = 'root://eoscms.cern.ch/'+DirectorySMPeos+'__JESFlavorQCDdo_suffix'

  nuisances[js_VBS_ZV+'_SMPeos'] = {
      'name': 'CMS_scale_'+js_VBS_ZV,
      'kind': 'suffix',
      'type': 'shape',
      'mapUp': js_VBS_ZV+'up',
      'mapDown': js_VBS_ZV+'do',
      'samples':  dict((skey, ['1','1']) for skey in mc_eos),
      'folderUp': folderup_signal,
      'folderDown': folderdo_signal,
     #'group': 'AK4jet',
     # 'AsLnN': '1' #
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
    'samples': dict((skey, puid_syst) for skey in mc), ## if skey not in ['ggWW']
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
nuisances['PS_ISR_latinos']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
        'top'    : ['1.0020618369910668*(nCleanGenJet==0) + 1.0063081530771556*(nCleanGenJet==1) + 1.0094298425968304*(nCleanGenJet==2) + 0.9854207999040726*(nCleanGenJet>=3)', '0.9974340279269026*(nCleanGenJet==0) + 0.9920634820709106*(nCleanGenJet==1) + 0.988226385054923*(nCleanGenJet==2) + 1.017968568319235*(nCleanGenJet>=3)'],
        'DY'     : ['0.9998177685645392*(nCleanGenJet==0) + 1.0080838149428026*(nCleanGenJet==1) + 1.0057948912950987*(nCleanGenJet==2) + 0.9721358221196619*(nCleanGenJet>=3)', '1.0003244155266309*(nCleanGenJet==0) + 0.9897992135367016*(nCleanGenJet==1) + 0.9928782069009531*(nCleanGenJet==2) + 1.0348902921423981*(nCleanGenJet>=3)'],
    },
    'rename':True,
    'newName':'PS_ISR_latinos'
}

nuisances['PS_FSR_latinos']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
        'top'    : ['0.9910899786333963*(nCleanGenJet==0) + 0.9990635702054794*(nCleanGenJet==1) + 1.002141744200183*(nCleanGenJet==2) + 1.0129742776372779*(nCleanGenJet>=3)', '1.0068843378231833*(nCleanGenJet==0) + 0.998988498438759*(nCleanGenJet==1) + 0.9952696584115224*(nCleanGenJet==2) + 0.9790955840673237*(nCleanGenJet>=3)'],
        'DY'     : ['0.9958763409773141*(nCleanGenJet==0) + 1.0041335498093422*(nCleanGenJet==1) + 1.0163363150953029*(nCleanGenJet==2) + 1.0296733670670226*(nCleanGenJet>=3)', '1.0066775262249232*(nCleanGenJet==0) + 0.9945601465681602*(nCleanGenJet==1) + 0.9662459619335311*(nCleanGenJet==2) + 0.9479423453563661*(nCleanGenJet>=3)'],
    },
    'rename':True,
    'newName':'PS_FSR_latinos'
}

#*************************************************#
### uncommenting the following lines at the moment of datacard making
### for signal, VBF-V, VBS VV QCD, we extrapolate them from 2018 uncommenting the following lines at the moment of datacard making
nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS','DY','top']), #PSWeights are buggy for some samples, we add them back by hand below, for DY, they are negligible. NB: rimuovere ,'tZq','sm_dipole','VBF-V' per topcr BOGUS NORM
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
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS','DY','top']), #PSWeights are buggy for some samples, we add them back by hand below, for DY, they are negligible. NB: rimuovere ,'tZq','sm_dipole','VBF-V' per topcr BOGUS NORM
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
#*************************************************#


###########################################
#############    QCD scale   ##############
###########################################
## Shape nuisance due to QCD scale variations for DY
## LHE scale variation weights (w_var / w_nominal)
## This should work for samples with either 8 or 9 LHE scale weights (Length$(LHEScaleWeight) == 8 or 9)
#qcdscale_variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']
# method 2
## -> alternative implementation with envelope (used is VBS OSww https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/VBS_OS/Full2016_v7/SF/nuisances.py#L461-L502)
## All 2016 samples have either 0 or 9 LHEScaleWeights
#variations = ['Alt$(LHEScaleWeight[0],1)', 'Alt$(LHEScaleWeight[1],1)', 'Alt$(LHEScaleWeight[3],1)', 'Alt$(LHEScaleWeight[5],1)', 'Alt$(LHEScaleWeight[7],1)', 'Alt$(LHEScaleWeight[8],1)']
variations = ['LHEScaleWeight[0]', 'LHEScaleWeight[1]', 'LHEScaleWeight[3]', 'LHEScaleWeight[Length$(LHEScaleWeight)-4]', 'LHEScaleWeight[Length$(LHEScaleWeight)-2]', 'LHEScaleWeight[Length$(LHEScaleWeight)-1]']

for sample in mc :
    if sample in ["other","VgS","DY","tZq_QCD","VBS_WV_QCD","ZVjj_QCD"]: continue   #this sample apparently doesn't have LHE weights, but it's real minor for us
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
#            'cuts'  : [
#                   'Boosted_SR_bVeto',
#                   'Boosted_SR_bTag',
#                   'Resolved_SR_bVeto',
#                   'Resolved_SR_bTag',
#                   'Boosted_DYcr_bVeto',
#                   'Boosted_DYcr_bTag',
#                   'Resolved_DYcr_bVeto',
#                   'Resolved_DYcr_bTag',
#                   ],
	        'AsLnN': '1'    ##
    }

#for sample in mc_eos :
#for sample in ["tZq_QCD","VBS_WV_QCD","ZVjj_QCD"] :       #### VBS_VV_QCD has bugged QCDscale weights for 2016!!!     AT THE PRODUCTION STEP I DON'T PRODUCE QCD SCALE NUISANCES FOR THE BUGGED SAMPELS
#    nuisances['QCDscale_'+sample] = {
#            'name'  : 'QCDscale_'+sample,
#            'kind': 'weight_envelope',
#            'type'  : 'shape',
#            'samples'  :  { sample: variations },
#            #'group' : 'theory',
#	       # 'AsLnN': '1'    ##
#    }

#*************************************************#
### for VBS VV QCD we extrapolate them from 2018 
### uncommenting the following lines at the moment of datacard making
for sample in ["VBS_WV_QCD",] :       #### VBS_VV_QCD has bugged QCDscale weights for 2016, it is extracted as normalization factors from 2018
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
#            'cuts'  : [
#                   'Boosted_SR_bVeto',
#                   'Boosted_SR_bTag',
#                   'Resolved_SR_bVeto',
#                   'Resolved_SR_bTag',
#                   'Boosted_DYcr_bVeto',
#                   'Boosted_DYcr_bTag',
#                   'Resolved_DYcr_bVeto',
#                   'Resolved_DYcr_bTag',
#                   ],
#            'samples'  :  dict((skey, ['1', '1']) for skey in ["VBS_VV_QCD"]), #{ sample: variations },
            'group' : 'theory',
	       # 'AsLnN': '1'    ##
    }
#*************************************************#



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
pdf_variations = ["LHEPdfWeight[%d]" %i for i in range(100)]
nuisances['pdf_weight'] = { ### UPDATED FOR 2016 SAMPLES: NEED TO USE RMS HERE!!!
    'name'  : 'pdf_16',
    'kind'  : 'weight_rms',    
    'type'  : 'shape',
    'samples' :  { s: ["LHEPdfWeight[%d]" %i for i in range(100)] for s in ["Vg", "VgS","VBF-V","VBS_VV_QCD"] }, #-> here we reomve bkgs measured in CR (DY and top, and WW for which weights are bugged), as well as BSM signals (PHDF4LHC prescription for BSM measurement)
    #'group' : 'theory',
    'AsLnN':  '1'
}

nuisances['pdf_weight_1718'] = { ###TO BE UPDATED FOR 2016 SIGNAL: here we generated with NNPDF3.1, so it should be correlated with 2017 and 2018 instead
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
		           'Boosted_SR_bTag',
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
		           'Resolved_SR_bTag',
                   ],
                #'group' : 'Topnorm',
              }

DY_bins=[]
for bin in range(1,6):
        DY_bins.append("DY_bin" + str(bin))

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


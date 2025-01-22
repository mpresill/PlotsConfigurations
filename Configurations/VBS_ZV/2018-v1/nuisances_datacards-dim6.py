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



EFT_samples = ['sm',
 'sm_lin_quad_cW',
 'quad_cW',
 'sm_lin_quad_mixed_cW_cHWB',
 'sm_lin_quad_mixed_cW_cHbox',
 'sm_lin_quad_mixed_cW_cHW',
 'sm_lin_quad_mixed_cW_cHl1',
 'sm_lin_quad_mixed_cW_cHB',
 'sm_lin_quad_mixed_cW_cHQ1',
 'sm_lin_quad_mixed_cW_cHj1',
 'sm_lin_quad_cHWB',
 'quad_cHWB',
 'sm_lin_quad_mixed_cHWB_cHbox',
 'sm_lin_quad_mixed_cHWB_cHW',
 'sm_lin_quad_mixed_cHWB_cHl1',
 'sm_lin_quad_mixed_cHWB_cHB',
 'sm_lin_quad_mixed_cHWB_cHQ1',
 'sm_lin_quad_mixed_cHWB_cHj1',
 'sm_lin_quad_cHbox',
 'quad_cHbox',
 'sm_lin_quad_mixed_cHbox_cHW',
 'sm_lin_quad_mixed_cHbox_cHl1',
 'sm_lin_quad_mixed_cHbox_cHB',
 'sm_lin_quad_mixed_cHbox_cHQ1',
 'sm_lin_quad_mixed_cHbox_cHj1',
 'sm_lin_quad_cHW',
 'quad_cHW',
 'sm_lin_quad_mixed_cHW_cHl1',
 'sm_lin_quad_mixed_cHW_cHB',
 'sm_lin_quad_mixed_cHW_cHQ1',
 'sm_lin_quad_mixed_cHW_cHj1',
 'sm_lin_quad_cHl1',
 'quad_cHl1',
 'sm_lin_quad_mixed_cHl1_cHB',
 'sm_lin_quad_mixed_cHl1_cHQ1',
 'sm_lin_quad_mixed_cHl1_cHj1',
 'sm_lin_quad_cHB',
 'quad_cHB',
 'sm_lin_quad_mixed_cHB_cHQ1',
 'sm_lin_quad_mixed_cHB_cHj1',
 'sm_lin_quad_cHQ1',
 'quad_cHQ1',
 'sm_lin_quad_mixed_cHQ1_cHj1',
 'sm_lin_quad_cHj1',
 'quad_cHj1']
 
mc_common = ["DY", "top", "other", "Vg", "VgS", "VBF-V"] # "VZ","tZq_ll", 
#mc_signal= ["sm_dipole"] #"sm","ewk_WpZ","ewk_WmZ","ewk_ZZ"]
mc_eos    = ["VBS_VV_QCD","tZq"] + EFT_samples

mc        = mc_common + mc_eos



################################ EXPERIMENTAL UNCERTAINTIES  #################################

#### Luminosity


nuisances['lumi_Uncorrelated'] = {
    'name': 'lumi_13TeV_2018',
    'type': 'lnN',
    'samples': dict((skey, '1.015') for skey in mc if skey not in ["top","DY"] ),
   #'group': 'lumi',
}

nuisances['lumi_XYFact'] = {
    'name': 'lumi_13TeV_XYFact',
    'type': 'lnN',
    'samples': dict((skey, '1.02') for skey in mc if skey not in ["top","DY"] ),
   #'group': 'lumi',
}

nuisances['lumi_LScale'] = {
    'name': 'lumi_13TeV_LSCale',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ["top","DY"] ),
   #'group': 'lumi',
}

nuisances['lumi_CurrCalib'] = {
    'name': 'lumi_13TeV_CurrCalib',
    'type': 'lnN',
    'samples': dict((skey, '1.002') for skey in mc if skey not in ["top","DY"] ),
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
    'name': 'CMS_fake_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWEleUp', 'fakeWEleDown'],
    },
   #'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_ele_stat'] = {
    'name': 'CMS_fake_stat_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatEleUp', 'fakeWStatEleDown']
    },
   #'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_mu'] = {
    'name': 'CMS_fake_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWMuUp', 'fakeWMuDown'],
    },
   #'group': 'fake',
#    'AsLnN': '1'
}

nuisances['fake_mu_stat'] = {
    'name': 'CMS_fake_stat_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Fake': ['fakeWStatMuUp', 'fakeWStatMuDown'],
    },
   #'group': 'fake',
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
       #'group':'AK4jet',
       # 'AsLnN': '1'
    }

##### Trigger Efficiency

trig_syst = ['((TriggerEffWeight_2l_u)/(TriggerEffWeight_2l))*(TriggerEffWeight_2l>0.02) + (TriggerEffWeight_2l<=0.02)', '(TriggerEffWeight_2l_d)/(TriggerEffWeight_2l)']

nuisances['trigg'] = {
    'name': 'CMS_eff_trigger_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, trig_syst) for skey in mc), 
   #'group':'trigger',
}



##### Electron Efficiency and energy scale  
nuisances['eff_e'] = {
    'name': 'CMS_eff_e_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightEleUp', 'SFweightEleDown']) for skey in mc), 
   #'group':'lepton'
}

nuisances['electronpt'] = {
    'name': 'CMS_scale_e_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'ElepTup',
    'mapDown': 'ElepTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc_common if skey not in ["other"]), ##removed WJets as is corrupted, plus not really relevant for us.
    'folderUp': makeMCDirectory('ElepTup_suffix'),
    'folderDown': makeMCDirectory('ElepTdo_suffix'),
   #'group':'lepton',
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
   #'group':'lepton',
    #'AsLnN': '1'
}


##### Muon Efficiency and energy scale  
nuisances['eff_m'] = {
    'name': 'CMS_eff_m_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['SFweightMuUp', 'SFweightMuDown']) for skey in mc),
   #'group':'lepton',
}

nuisances['muonpt'] = {
    'name': 'CMS_scale_m_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'MupTup',
    'mapDown': 'MupTdo',
    'samples': dict((skey, ['1', '1']) for skey in mc_common if skey not in ["other"]), ##removed WJets as is corrupted, plus not really relevant for us.
    'folderUp': makeMCDirectory('MupTup_suffix'),
    'folderDown': makeMCDirectory('MupTdo_suffix'),
   #'group':'lepton',
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
   #'group':'lepton',
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
     #'group': 'AK4jet',
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
     # 'AsLnN': '1'
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
   #'group': 'AK4jet',
   # 'AsLnN': '1'
}

#this is for the signal
nuisances['JER_SMPeos'] = {
    'name': 'CMS_res_j_2018',
    'kind': 'suffix',
    'type': 'shape',
    'mapUp': 'JERup',
    'mapDown': 'JERdo',
    'samples': dict((skey, ['1','1']) for skey in mc_eos),  ####      WHY REMOVING SIGNAL?
    'folderUp': DirectorySMPeos+'__JERup_suffix',
    'folderDown': DirectorySMPeos+'__JERdo_suffix',
   #'group': 'AK4jet',
   # 'AsLnN': '1'
}



# ##### Pileup
pu_syst = '(puWeightUp/puWeight)', '(puWeightDown/puWeight)'

nuisances['PU'] = {
    'name': 'CMS_PU_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, pu_syst) for skey in mc),
   #'group': 'PU',
    'AsLnN': '1',
}

### PU ID SF uncertainty
puid_syst = ['Jet_PUIDSF_up/Jet_PUIDSF', 'Jet_PUIDSF_down/Jet_PUIDSF']

nuisances['jetPUID'] = {
    'name': 'CMS_jetpuid_2018',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, puid_syst) for skey in mc),
   #'group': 'AK4jet',
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
   #'group' : 'AK8jet',
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
   #'group' : 'AK8jet',
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
   #'group' : 'AK8jet',
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
   #'group' : 'AK8jet',
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
   #'group' : 'AK8jet',
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
   #'group' : 'AK8jet',
            #'AsLnN': '1'
}






###########################################
#############  PARTON SHOWER ##############
###########################################
nuisances['PS_ISR_latinos']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['1.00227428567253*(nCleanGenJet==0) + 1.00572014989997*(nCleanGenJet==1) + 0.970824885256465*(nCleanGenJet==2) + 0.927346068071086*(nCleanGenJet>=3)', '0.996488506572636*(nCleanGenJet==0) + 0.993582795375765*(nCleanGenJet==1) + 1.03643678934568*(nCleanGenJet==2) + 1.09735277266955*(nCleanGenJet>=3)'],
        'VgS'    : ['1.0000536116408023*(nCleanGenJet==0) + 1.0100100693580492*(nCleanGenJet==1) + 0.959068359375*(nCleanGenJet==2) + 0.9117049260469496*(nCleanGenJet>=3)', '0.9999367833485968*(nCleanGenJet==0) + 0.9873682892005163*(nCleanGenJet==1) + 1.0492717737268518*(nCleanGenJet==2) + 1.1176958835210322*(nCleanGenJet>=3)'],
    },
}

nuisances['PS_FSR_latinos']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'Vg'     : ['0.999935529935028*(nCleanGenJet==0) + 0.997948255568351*(nCleanGenJet==1) + 1.00561645493085*(nCleanGenJet==2) + 1.0212896960035*(nCleanGenJet>=3)', '1.00757702771109*(nCleanGenJet==0) + 1.00256681166083*(nCleanGenJet==1) + 0.93676371569867*(nCleanGenJet==2) + 0.956448336052435*(nCleanGenJet>=3)'],
        'VgS'    : ['0.9976593177227735*(nCleanGenJet==0) + 1.0016125187585532*(nCleanGenJet==1) + 1.0049344618055556*(nCleanGenJet==2) + 1.0195631514301164*(nCleanGenJet>=3)', '1.0026951855766457*(nCleanGenJet==0) + 1.0008132148661049*(nCleanGenJet==1) + 1.003949291087963*(nCleanGenJet==2) + 0.9708160910230832*(nCleanGenJet>=3)'],
    },
}
###this was just a test
nuisances['PS_ISR_latinos_dy_top']  = {
    'name': 'PS_ISR_latinos',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'top'    : ['1.0020618369910668*(nCleanGenJet==0) + 1.0063081530771556*(nCleanGenJet==1) + 1.0094298425968304*(nCleanGenJet==2) + 0.9854207999040726*(nCleanGenJet>=3)', '0.9974340279269026*(nCleanGenJet==0) + 0.9920634820709106*(nCleanGenJet==1) + 0.988226385054923*(nCleanGenJet==2) + 1.017968568319235*(nCleanGenJet>=3)'],
        'DY'     : ['0.9998177685645392*(nCleanGenJet==0) + 1.0080838149428026*(nCleanGenJet==1) + 1.0057948912950987*(nCleanGenJet==2) + 0.9721358221196619*(nCleanGenJet>=3)', '1.0003244155266309*(nCleanGenJet==0) + 0.9897992135367016*(nCleanGenJet==1) + 0.9928782069009531*(nCleanGenJet==2) + 1.0348902921423981*(nCleanGenJet>=3)'],
    },
}

nuisances['PS_FSR_latinos_dy_top']  = {
    'name': 'PS_FSR_latinos',
    'kind': 'weight',
    'type': 'shape',
    'samples': {
        'top'    : ['0.9910899786333963*(nCleanGenJet==0) + 0.9990635702054794*(nCleanGenJet==1) + 1.002141744200183*(nCleanGenJet==2) + 1.0129742776372779*(nCleanGenJet>=3)', '1.0068843378231833*(nCleanGenJet==0) + 0.998988498438759*(nCleanGenJet==1) + 0.9952696584115224*(nCleanGenJet==2) + 0.9790955840673237*(nCleanGenJet>=3)'],
        'DY'     : ['0.9958763409773141*(nCleanGenJet==0) + 1.0041335498093422*(nCleanGenJet==1) + 1.0163363150953029*(nCleanGenJet==2) + 1.0296733670670226*(nCleanGenJet>=3)', '1.0066775262249232*(nCleanGenJet==0) + 0.9945601465681602*(nCleanGenJet==1) + 0.9662459619335311*(nCleanGenJet==2) + 0.9479423453563661*(nCleanGenJet>=3)'],
    },
}


nuisances['PS_ISR']  = {
    'name': 'PS_ISR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[2]', 'PSWeight[0]']) for skey in mc if skey not in ['Vg','VgS','DY','top']), #PSWeights are buggy for some samples (like WW, ggWW, so we remove PS from other as basically negligible for such small processes)
    #'AsLnN': '1',
}

nuisances['PS_FSR']  = {
    'name': 'PS_FSR',
    'kind': 'weight',
    'type': 'shape',
    'samples': dict((skey, ['PSWeight[3]', 'PSWeight[1]']) for skey in mc if skey not in ['Vg','VgS','DY','top']), #PSWeights are buggy for some samples (like WW, ggWW, so we remove PS from other as basically negligible for such small processes)
    #'AsLnN': '1',
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
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
           #'group' : 'theory',
	        #'AsLnN': '1'    ##
    }

for sample in ["VBS_VV_QCD","tZq"] :
    nuisances['QCDscale_'+sample] = {
            'name'  : 'QCDscale_'+sample,
            'kind': 'weight_envelope',
            'type'  : 'shape',
            'samples'  :  { sample: variations },
           #'group' : 'theory',
	        #'AsLnN': '1'    ##
    }

#for sample in mc_eos :
nuisances['QCDscale_ZVjj']  = {
    'name': 'QCDscale_ZVjj',
    'kind': 'weight_envelope',
    'type'  : 'shape',
    'samples'  :   {skey : variations  for skey in EFT_samples},
#    'samples'  :   dict((skey: variations ) for skey in mc_eos),
    #'samples'  :  { sample: variations },
    #'AsLnN': '1',
}



###########################################
#############    PDF WEIGHT  ##############
###########################################

nuisances['pdf_weight'] = { # --> Now save also the normalization one for the signal
    'name'  : 'pdf_1718',
    'kind'  : 'weight_envelope',
    'type'  : 'shape',
    'samples' :  { s: [' Alt$(LHEPdfWeight['+str(i)+'], 1.)' for i in range(0,103)] for s in mc if s not in ["DY","top"]+EFT_samples}, #-> here we reomve bkgs measured on, as well as BSM signals (PHDF4LHC prescription for BSM measurement)
   #'group' : 'theory',
    'AsLnN':  '1'
}
#### removed EFT_samples from this nuisance as we found out that the weights are bugged.
#### since we use it as a log normal nuisace, we will introduce the flat number from SM ewk sample

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
   #'group' : 'theory',
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
                   'Boosted_SR_bTag',
                   #'Boosted_DYcr_bVeto', ### EDITED
                   #'Boosted_DYcr_bTag', ### EDITED
                   ],
               #'group' : 'Topnorm',
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
                   #'Resolved_DYcr_bVeto', ### EDITED
                   #'Resolved_DYcr_bTag',  ### EDITED
                   ],
               #'group' : 'Topnorm',
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
res_btag_2018=['1.10', '1.33', '1.10', '1.15', '1.03', '1.10', '0.90', '0.73', '0.83', '0.56', '0.57', '0.80']
res_bVeto_2018=['1.05', '1.19', '1.08', '1.06', '0.93', '0.96', '0.82', '0.68', '0.76', '0.45', '0.46', '0.55']
boos_bTag_2018=['0.77', '0.73', '0.58', '0.63', '0.52']
boos_bVeto_2018=['0.64', '0.74', '0.64', '0.57', '0.51']

for DYbin in range(1,13):
		nuisances["DY_Resolved_2d_{}_norm_res_Z_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Resolved_2d_{}_norm_res_Z_bVeto_2018'.format(DYbin),
                'samples'  : {DY_bins_res[DYbin-1]: '1.0' },
                #'samples'  : {DY_bins_res[DYbin-1]:res_bVeto_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bVeto',
		            'Resolved_SR_bVeto',
                   ],
               #'group' : 'DYnorm',

            	}
		nuisances["DY_Resolved_2d_{}_norm_res_Z_btag_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Resolved_2d_{}_norm_res_Z_btag_2018'.format(DYbin),
                'samples'  : {DY_bins_res[DYbin-1]: '1.0' },
                #'samples'  : {DY_bins_res[DYbin-1]:res_btag_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Resolved_DYcr_bTag',
                   'Resolved_SR_bTag',
                   ],
               #'group' : 'DYnorm',
                 }
                
for DYbin in range(1,6):
		nuisances["DY_Boosted_Z_{}_norm_boost_bVeto_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Boosted_Z_{}_norm_boost_bVeto_2018'.format(DYbin),
                'samples'  : {DY_bins_boos[DYbin-1]:'1.0'},
#                'samples'  : {DY_bins_boos[DYbin-1]:boos_bVeto_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bVeto',
                   'Boosted_SR_bVeto',
                   ],
               #'group' : 'DYnorm',
            }
		nuisances["DY_Boosted_Z_{}_norm_boost_bTag_2018".format(DYbin)]  = {
                'name'  : 'CMS_DY_Boosted_Z_{}_norm_boost_bTag_2018'.format(DYbin),
                'samples'  : {DY_bins_boos[DYbin-1]:'1.0'},
#                'samples'  : {DY_bins_boos[DYbin-1]:boos_bTag_2018[DYbin-1]},
                'type'  : 'rateParam',
                'cuts'  : [
                   'Boosted_DYcr_bTag',
                   'Boosted_SR_bTag',
                   ],
               #'group' : 'DYnorm',
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

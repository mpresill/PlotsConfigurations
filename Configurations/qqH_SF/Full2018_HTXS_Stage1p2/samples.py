import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, addSampleWeight, getBaseWnAOD

def nanoGetSampleFiles(inputDir, sample):
    try:
        if _samples_noload:
            return []
    except NameError:
        pass

    return getSampleFiles(inputDir, sample, True, 'nanoLatino_')

# samples

try:
    len(samples)
except NameError:
    import collections
    samples = collections.OrderedDict()

################################################
################# SKIMS ########################
################################################

mcProduction = 'Autumn18_102X_nAODv6_Full2018v6'

dataReco = 'Run2018_102X_nAODv6_Full2018v6'

fakeReco = 'Run2018_102X_nAODv6_Full2018v6_ForNewWPs'

mcSteps = 'MCl1loose2018v6__MCCorr2018v6__l2loose__l2tightOR2018v6{var}'

fakeSteps = 'DATAl1loose2018v6__l2loose__fakeW__DYMVA'

dataSteps = 'DATAl1loose2018v6__l2loose__l2tightOR2018v6'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['A','Run2018A-Nano25Oct2019-v1'] ,
            ['B','Run2018B-Nano25Oct2019-v1'] ,
            ['C','Run2018C-Nano25Oct2019-v1'] ,
            ['D','Run2018D-Nano25Oct2019_ver2-v1'] ,
          ]

DataSets = ['MuonEG','DoubleMuon','SingleMuon','EGamma']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'EGamma'         : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && (Trigger_sngEl || Trigger_dblEl)' ,
           }


#########################################
############ MC COMMON ##################
#########################################

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################

###### DY #######

ptllDYW_NLO = '(0.87*(gen_ptll<10)+(0.379119+0.099744*gen_ptll-0.00487351*gen_ptll**2+9.19509e-05*gen_ptll**3-6.0212e-07*gen_ptll**4)*(gen_ptll>=10 && gen_ptll<45)+(9.12137e-01+1.11957e-04*gen_ptll-3.15325e-06*gen_ptll**2-4.29708e-09*gen_ptll**3+3.35791e-11*gen_ptll**4)*(gen_ptll>=45 && gen_ptll<200) + 1*(gen_ptll>200))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useDYtt = False
useDYHT = True

if useDYtt :

    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
            nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')
    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                     Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
        'FilesPerJob': 6,
        'suppressNegative' :['all'],
        'suppressNegativeNuisances' :['all'],
    }
    addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50' ,ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)

else:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
            nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO') + \
            nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')

    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                     Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )',
        'FilesPerJob': 6,
        'suppressNegative' :['all'],
        'suppressNegativeNuisances' :['all'],
    }

    # ... Add DY HT Samples
    if useDYHT :
        samples['DY']['name'] +=     nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-200to400' ) \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-400to600' ) \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-600toInf') \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-70to100') \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600') \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200')  \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') \
                                   + nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf')

    M10baseW = getBaseWnAOD(mcDirectory,'Autumn18_102X_nAODv6_Full2018v6',['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-10to50-LO_ext1'])

    addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2'        ,ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO'      ,ptllDYW_LO +'*'+M10baseW+'/baseW')
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1' ,ptllDYW_LO +'*'+M10baseW+'/baseW')

    if useDYHT :
        # Remove high HT from inclusive samples
        addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1', '(LHE_HT<100)')
        addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO'     , '(LHE_HT<100)')
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext2'       , '(LHE_HT<70)')
        # pt_ll weight
        addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200',ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400',ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600',ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf',ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-70to100'    ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200'   ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400'   ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600'   ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800'   ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200'  ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500' ,ptllDYW_LO)
        addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf'  ,ptllDYW_LO)


###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 2,
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')

###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WWTo2L2Nu'),
    'weight': mcCommonWeight + '*nllW',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 3
}

samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK'),
    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)', #filter tops and Higgs
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

# k-factor 1.4 already taken into account in XSWeight
files = nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
    nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN')

samples['ggWW'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(Gen_ZGstar_mass <= 0)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}
# the following is needed in both v5 and v6
addSampleWeight(samples, 'Vg', 'ZGToLLG', '0.448')

######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'ZGToLLG') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4,
    'subsamples': {
      'L': 'gstarLow',
      'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'ZGToLLG', '(Gen_ZGstar_mass > 0)*0.448')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')
#+ nanoGetSampleFiles(mcDirectory, 'WWG'), #should this be included? or is it already taken into account in the WW sample?

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    'FilesPerJob': 4
}

###########################################
#############   SIGNALS  ##################
###########################################
signals = []
if os.path.exists('HTXS_stage1_categories.py') :
  handle = open('HTXS_stage1_categories.py','r')
  exec(handle)
  handle.close()

## STXS bins                    

for cat,num in HTXSStage1_1Categories.iteritems():
    ## ggH
    if 'GG2H_' in cat:
        if 'PTH_GT200' not in cat:
            samples['ggH_hww_'+cat.replace('GG2H_','')]  = {  'name': nanoGetSampleFiles(mcDirectory,'GluGluHToWWTo2L2Nu_M125')+nanoGetSampleFiles(mcDirectory, 'GGHjjToWWTo2L2Nu_minloHJJ_M125'),
                                                              'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')',
                                                              'FilesPerJob': 1,
                                                              'suppressNegative' :['all'],
                                                              'suppressNegativeNuisances' :['all'],
            }
            addSampleWeight(samples, 'ggH_hww_'+cat.replace('GG2H_',''), 'GluGluHToWWTo2L2Nu_M125', '(HTXS_stage1_1_cat_pTjet30GeV<107)*Weight2MINLO*1092.7640/1073.2567')
            addSampleWeight(samples, 'ggH_hww_'+cat.replace('GG2H_',''), 'GGHjjToWWTo2L2Nu_minloHJJ_M125', '(HTXS_stage1_1_cat_pTjet30GeV>106)*1092.7640/1073.2567')
            signals.append('ggH_hww_'+cat.replace('GG2H_',''))


    ## VBF and VH had.
    elif 'QQ2HQQ_' in cat:
      if '0J'  not in cat or '1J' not in cat:
        samples['qqH_hww_'+cat.replace('QQ2HQQ_','')]  = {  'name' : nanoGetSampleFiles(mcDirectory,'VBFHToWWTo2L2Nu_M125'),
                                                            'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')' ,
                                                            'suppressNegative' :['all'],
                                                            'suppressNegativeNuisances' :['all'],
                                                         }
        signals.append('qqH_hww_'+cat.replace('QQ2HQQ_',''))

        if 'MJJ_0_60' in cat or 'MJJ_60_120' in cat or 'MJJ_120_350' in cat:
            samples['WH_had_hww_'+cat.replace('QQ2HQQ_','')]   = {  'name' :   nanoGetSampleFiles(mcDirectory,'HWminusJ_HToWW_M125')
                                                                             + nanoGetSampleFiles(mcDirectory,'HWplusJ_HToWW_M125')  ,
                                                                    'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')' ,
                                                                    'suppressNegative' :['all'],
                                                                    'suppressNegativeNuisances' :['all'],
                                                                 }
            signals.append('WH_had_hww_'+cat.replace('QQ2HQQ_',''))

            samples['ZH_had_hww_'+cat.replace('QQ2HQQ_','')]  = { 'name' :  nanoGetSampleFiles(mcDirectory,'HZJ_HToWW_M125') ,
                                                                  'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')' ,
                                                                  'suppressNegative' :['all'],
                                                                  'suppressNegativeNuisances' :['all'],
                                                                }
            signals.append('ZH_had_hww_'+cat.replace('QQ2HQQ_',''))


    ## WH lep.
    elif 'QQ2HLNU_' in cat:
      samples['WH_lep_hww_'+cat.replace('QQ2HLNU_','')] = { 'name' :   nanoGetSampleFiles(mcDirectory,'HWminusJ_HToWW_M125')
                                                                     + nanoGetSampleFiles(mcDirectory,'HWplusJ_HToWW_M125')  ,
                                                            'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')' ,
                                                            'suppressNegative' :['all'],
                                                            'suppressNegativeNuisances' :['all'],
                                                          }
      signals.append('WH_lep_hww_'+cat.replace('QQ2HLNU_',''))

    ## qqZH lep.
    elif 'QQ2HLL_' in cat:
      samples['ZH_lep_hww_'+cat.replace('QQ2HLL_','')]  = { 'name' :  nanoGetSampleFiles(mcDirectory,'HZJ_HToWW_M125') ,
                                                            'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')' ,
                                                            'suppressNegative' :['all'],
                                                            'suppressNegativeNuisances' :['all'],
                                                          }
      signals.append('ZH_lep_hww_'+cat.replace('QQ2HLL_',''))


    ## ggZH lep
    elif 'GG2HLL_' in cat:
      samples['ggZH_lep_hww_'+cat.replace('GG2HLL_','')]  = {  'name': nanoGetSampleFiles(mcDirectory,'GluGluZH_HToWWTo2L2Nu_M125'),
                                                           'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV=='+str(num)+')',
                                                           'suppressNegative' :['all'],
                                                           'suppressNegativeNuisances' :['all'],
                                                        }
      signals.append('ggZH_lep_hww_'+cat.replace('GG2HLL_',''))



# Stage 1.2 binning for high pTH bin                                                                                                         
                                                                                                                                              
samples['ggH_hww_PTH_200_300']  = {  'name': nanoGetSampleFiles(mcDirectory,'GluGluHToWWTo2L2Nu_M125'),
                                     'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV==101)*(HTXS_Higgs_pt>200)*(HTXS_Higgs_pt<=300)*Weight2MINLO',
                                     'FilesPerJob': 1,
                                     'suppressNegative' :['all'],
                                     'suppressNegativeNuisances' :['all'],
                                  }
signals.append('ggH_hww_PTH_200_300')

samples['ggH_hww_PTH_300_450']  = {  'name': nanoGetSampleFiles(mcDirectory,'GluGluHToWWTo2L2Nu_M125'),
                                     'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV==101)*(HTXS_Higgs_pt>300)*(HTXS_Higgs_pt<=450)*Weight2MINLO',
                                     'FilesPerJob': 1,
                                     'suppressNegative' :['all'],
                                     'suppressNegativeNuisances' :['all'],
                                  }
signals.append('ggH_hww_PTH_300_450')

samples['ggH_hww_PTH_450_650']  = {  'name': nanoGetSampleFiles(mcDirectory,'GluGluHToWWTo2L2Nu_M125'),
                                     'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV==101)*(HTXS_Higgs_pt>450)*(HTXS_Higgs_pt<=650)*Weight2MINLO',
                                     'FilesPerJob': 1,
                                     'suppressNegative' :['all'],
                                     'suppressNegativeNuisances' :['all'],
                                  }
signals.append('ggH_hww_PTH_450_650')

samples['ggH_hww_PTH_GT650']  = {  'name': nanoGetSampleFiles(mcDirectory,'GluGluHToWWTo2L2Nu_M125'),
                                   'weight': mcCommonWeight+'*(HTXS_stage1_1_cat_pTjet30GeV==101)*(HTXS_Higgs_pt>650)*Weight2MINLO',
                                   'FilesPerJob': 1,
                                   'suppressNegative' :['all'],
                                   'suppressNegativeNuisances' :['all'],
                                  }
signals.append('ggH_hww_PTH_GT650')


############ ttH ############

samples['ttH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 1
}

signals.append('ttH_hww')

############ H->TauTau ############

samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 20
}

signals.append('ggH_htt')

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 10
}

signals.append('qqH_htt')

samples['ZH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('ZH_htt')

samples['WH_htt'] = {
    'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 4
}

signals.append('WH_htt')


# ###########################################
# #############   SIGNALS  ##################
# ###########################################

# signals = []

# #### ggH -> WW

# samples['ggH_hww'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWTo2L2NuPowheg_M125'),
#     'weight': [mcCommonWeight, {'class': 'Weight2MINLO', 'args': '%s/src/LatinoAnalysis/Gardener/python/data/powheg2minlo/NNLOPS_reweight.root' % os.getenv('CMSSW_BASE')}],
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 1,
#     'linesToAdd': ['.L %s/Differential/weight2MINLO.cc+' % configurations]
# }

# signals.append('ggH_hww')

# ############ VBF H->WW ############
# samples['qqH_hww'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWTo2L2Nu_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 4
# }

# signals.append('qqH_hww')

# ############ ZH H->WW ############

# samples['ZH_hww'] = {
#     'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWW_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 4
# }

# signals.append('ZH_hww')

# samples['ggZH_hww'] = {
#     'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWWTo2L2Nu_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 4
# }

# signals.append('ggZH_hww')

# ############ WH H->WW ############

# samples['WH_hww'] = {
#     'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 4
# }

# signals.append('WH_hww')

# ############ ttH ############

# samples['ttH_hww'] = {
#     'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 1
# }

# signals.append('ttH_hww')

# ############ H->TauTau ############

# samples['ggH_htt'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 20
# }

# signals.append('ggH_htt')

# samples['qqH_htt'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 10
# }

# signals.append('qqH_htt')

# samples['ZH_htt'] = {
#     'name': nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 4
# }

# signals.append('ZH_htt')

# samples['WH_htt'] = {
#     'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
#     'weight': mcCommonWeight,
#     'suppressNegative' :['all'],
#     'suppressNegativeNuisances' :['all'],
#     'FilesPerJob': 4
# }

# signals.append('WH_htt')


###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
   'suppressNegative' :['all'],
   'suppressNegativeNuisances' :['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake']['subsamples'] = {
  'ee': 'abs(Lepton_pdgId[0]) == 11 && abs(Lepton_pdgId[1]) == 11',
  'mm': 'abs(Lepton_pdgId[0]) == 13 && abs(Lepton_pdgId[1]) == 13',
  'df': '(Lepton_pdgId[0]*Lepton_pdgId[1] == -11*13)'
}

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # Full2017
configurations = os.path.dirname(configurations) # HWWSemiLepHighMass
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, getBaseWnAOD, addSampleWeight

from LatinoAnalysis.Tools.HiggsXSection import HiggsXSection
HiggsXS = HiggsXSection()

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
######### Higgs mass samples and models ########
################################################

massesAndModelsFile = "massesAndModels.py"
if os.path.exists(massesAndModelsFile) :
    handle = open(massesAndModelsFile,'r')
    exec(handle)
    handle.close()
else:
    print "!!! ERROR file ", massesAndModelsFile, " does not exist."


################################################
################# SKIMS ########################
################################################

mcProduction = 'Fall2017_102X_nAODv7_Full2017v7'

dataReco     = 'Run2017_102X_nAODv7_Full2017v7'

mcSteps      = 'MCl1loose2017v7__MCCorr2017v7__MCCombJJLNu2017'

dataSteps    = 'DATAl1loose2017v7__DATACombJJLNu2017'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  # treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDir = '/eos/user/s/ssiebert/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)

################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
  # ['B','Run2017B-Nano1June2019-v1'] ,
  ['C','Run2017C-02Apr2020-v1'],
  # ['D','Run2017D-Nano1June2019-v1'],
  # ['E','Run2017E-Nano1June2019-v1'],
  # ['F','Run2017F-Nano1June2019-v1']
]

DataSets = [
    'SingleMuon',
    'SingleElectron'
]

DataTrig = {
    'SingleMuon'     : 'Trigger_sngMu' ,
    'SingleElectron' : '!Trigger_sngMu && Trigger_sngEl' ,
}


#########################################
############ MC COMMON ##################
#########################################

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
# mcCommonWeight = mcCommonWeightNoMatch
# mcCommonWeight = 'XSWeight*Lepton_promptgenmatched[0]*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*Lepton_promptgenmatched[0]*METFilter_MC'

###########################################
#############  BACKGROUNDS  ###############
###########################################


###### DY #######
# from high mass (fully leptonic) 2017 config
ptllDYW_NLO = '(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'


files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')
files+= nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50')

samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight + '*(Sum$(GenPart_pdgId == 22 && TMath::Odd(GenPart_statusFlags) && GenPart_pt > 20.) == 0)',
    'FilesPerJob': 8,
}
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)
addSampleWeight(samples,'DY','DYJetsToLL_M-50',ptllDYW_NLO)



# ###### Top #######
#

        # nanoGetSampleFiles(mcDirectory, 'TTWJetsToLNu') + \
        # nanoGetSampleFiles(mcDirectory, 'TTWjets') + \
files = nanoGetSampleFiles(mcDirectory, 'TTToSemiLeptonic') + \
        nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
        nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_PSweights') + \
        nanoGetSampleFiles(mcDirectory, 'ST_tW_top_PSweights')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
}
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')


###### WW ########

files = nanoGetSampleFiles(mcDirectory, 'WWToLNuQQ')

samples['WW'] = {
    'name': files,
    'weight': mcCommonWeight+'*(mjjGen_OTF<100)',
    'FilesPerJob': 12
}

samples['WWewk'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK_noTop'),
    'weight': mcCommonWeight + '*(Sum$(abs(GenPart_pdgId)==6 || GenPart_pdgId==25)==0)',
    #FIXME there are other samples that dont contain top/higgs to begin with
    #filter tops and Higgs
    'FilesPerJob': 12
}


# ############# ggWW semileptonic ##############
# #FIXME: samples for this are being produced
# #FIXME: in the meantime use interference weights?

# samples['ggWW'] = {
#     'name'   : nanoGetSampleFiles(mcDirectory, 'GluGluHToWWToLNuQQ_M125'),
#     'weight' : mcCommonWeight +'*'+model+'_B * ('+model+'_B < 100)',
#     'FilesPerJob': 15
# }


samples['qqWWqq'] = {
    'name'   :   nanoGetSampleFiles(mcDirectory,'WpWmJJ_QCD_noTop') ,
    'weight' : mcCommonWeight+'*(mjjGen_OTF>=100)'+'*(GenLHE)',
    'FilesPerJob': 12
}

samples['WW2J'] = {
    'name'   :   nanoGetSampleFiles(mcDirectory,'WpWmJJ_QCD_noTop') ,
    'weight' : mcCommonWeight +'*(!GenLHE)',
    'FilesPerJob': 12
}



########## W+jets #########

# files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-0J') +\
#         nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-1J') +\
#         nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-2J')

# samples['Wjets'] = {
#     'name'   : files,
#     'weight' : mcCommonWeight +"*EWK_W_correction[0]",
#     'FilesPerJob' : 6,
# }
# # Correction xs used in latinos to the xs given in the pdf file
# # https://github.com/latinos/LatinoAnalysis/blob/master/NanoGardener/python/framework/samples/samplesCrossSections2017.py
# # https://indico.cern.ch/event/673253/contributions/2756806/attachments/1541203/2416962/20171016_VJetsXsecsUpdate_PH-GEN.pdf
# addSampleWeight(samples, 'Wjets', 'WJetsToLNu-0J', '(50131.98/54611.6)')
# addSampleWeight(samples, 'Wjets', 'WJetsToLNu-1J', '(8426.09/8966.2)')
# addSampleWeight(samples, 'Wjets', 'WJetsToLNu-2J', '(3172.96/3643.12)')


# samples['Wjets-0J'] = {
#     'name'   : nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-0J'),
#     'weight' : mcCommonWeight +"*EWK_W_correction[0]",
#     'FilesPerJob' : 9,
# }


files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-1J') +\
        nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-2J')

samples['Wjets-1+2J'] = {
    'name'   : files,
    'weight' : mcCommonWeight +"*EWK_W_correction[0]",
    'FilesPerJob' : 7,
}






####### Vg ########
files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM')
files += nanoGetSampleFiles(mcDirectory, 'ZGToLLG')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*(!(Gen_ZGstar_mass > 0))',
    'FilesPerJob': 8
}


####### VgS ########
files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
        nanoGetSampleFiles(mcDirectory, 'ZGToLLG')
    # nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01') +\

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob': 8,
    'subsamples': {
      'L': 'gstarLow',
      'H': 'gstarHigh'
    }
}
addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
# addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')


############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZ') +\
        nanoGetSampleFiles(mcDirectory, 'WZ') #FIXME double counting of WZTo3LNu

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight, # + '*1.11',
    'FilesPerJob': 8
}

########## VVV #########

files = nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WZZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWZ') + \
    nanoGetSampleFiles(mcDirectory, 'WWW')
    # nanoGetSampleFiles(mcDirectory, 'WWG')
    #FIXME: should WWG be included? or is it already taken into account in the WW sample?

samples['VVV'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 8
}





########### QCD ###########

# files = nanoGetSampleFiles(mcDirectory,'QCD_Pt-15to20_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-20to30_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-30to50_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-50to80_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-80to120_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-120to170_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-170to300_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-300to470_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-470to600_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-600to800_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-800to1000_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-1000toInf_MuEnrichedPt5') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-15to20_EMEnriched') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-20to30_EMEnriched') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-30to50_EMEnriched') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-50to80_EMEnriched') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-80to120_EMEnriched') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-120to170_EMEnriched') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-170to300_EMEnriched') + \
#     nanoGetSampleFiles(mcDirectory,'QCD_Pt-300toInf_EMEnriched')
#
# # files+= nanoGetSampleFiles(mcDirectory, 'QCD_Pt_20to30_bcToE') +\
# files+= nanoGetSampleFiles(mcDirectory, 'QCD_Pt_30to80_bcToE') +\
#         nanoGetSampleFiles(mcDirectory, 'QCD_Pt_80to170_bcToE') +\
#         nanoGetSampleFiles(mcDirectory, 'QCD_Pt_170to250_bcToE') +\
#         nanoGetSampleFiles(mcDirectory, 'QCD_Pt_250toInf_bcToE')
#
#
# samples['QCD_Tight'] = {
#     'name'   :   files,
#     'weight' : mcCommonWeightNoMatch + '*(abs(' + mcCommonWeightNoMatch + ')< 150)'
#                 + '*LepWPCut[0]',
#     'FilesPerJob' : 10,
# }
#
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-15to20_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-20to30_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-30to50_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-50to80_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-80to120_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-120to170_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-170to300_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_Tight', 'QCD_Pt-300toInf_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
#
#
# samples['QCD_NotTight'] = {
#     'name'   :   files,
#     'weight' : mcCommonWeightNoMatch + '*(abs(' + mcCommonWeightNoMatch + ')< 150)'
#                 + '* !LepWPCut[0]',# + '*( (abs(Lepton_pdgId[0])==11)*4440.5/262.0 + (abs(Lepton_pdgId[0])==13)*10333.5/731.0)',
#     'isData': ['all'],
#     'FilesPerJob' : 10,
# }
#
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-15to20_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-20to30_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-30to50_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-50to80_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-80to120_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-120to170_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-170to300_EMEnriched', '(abs(Lepton_pdgId[0])==11)')
# addSampleWeight(samples, 'QCD_NotTight', 'QCD_Pt-300toInf_EMEnriched', '(abs(Lepton_pdgId[0])==11)')



# samples['QCD'] = {}



############## SM Higgs ############
#### ggH -> WW

samples['ggH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWToLNuQQ_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 25,
}

############ VBF H->WW ############
samples['qqH_hww'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWToLNuQQ_M126'),
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}

############ ZH H->WW ############

samples['ZH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HZJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}

# samples['ggZH_hww'] = {
#     'name':   nanoGetSampleFiles(mcDirectory, 'GluGluZH_HToWW_M125'),
#     'weight': mcCommonWeight,
#     'FilesPerJob': 11
# }

############ WH H->WW ############

samples['WH_hww'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToWW_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToWW_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}

############ ttH ############

# samples['ttH_hww'] = {
#     'name':   nanoGetSampleFiles(mcDirectory, 'ttHToNonbb_M125'),
#     'weight': mcCommonWeight,
#     'FilesPerJob': 11
# }

# ############ H->TauTau ############
#
samples['ggH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}

samples['qqH_htt'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'VBFHToTauTau_M125'),
    'weight': mcCommonWeight,
    'FilesPerJob': 25
}

samples['ZH_htt'] = {
   'name': nanoGetSampleFiles(mcDirectory, 'HZJ_HToTauTau_M125'),
   'weight': mcCommonWeight,
   'FilesPerJob': 25
}

samples['WH_htt'] = { #FIXME: HWminusJ_HToTauTau_M125 missing in v6 prod Semilep
   'name':  nanoGetSampleFiles(mcDirectory, 'HWplusJ_HToTauTau_M125') + nanoGetSampleFiles(mcDirectory, 'HWminusJ_HToTauTau_M125'),
   'weight': mcCommonWeight,
   'FilesPerJob': 25
}




# ###########################################
# #############   SIGNALS  ##################
# ###########################################
#
#
# ####### ggH -> WW #################
# for MX in massggh:
#     # Model dependent -> Xsec*BR is applied in later step, so remove "SM"-Xsec*BR
#     SMxsec = HiggsXS.GetHiggsXS4Sample('YR4','13TeV','GluGluHToWWToLNuQQ_M'+MX)['xs']
#     noSMxsec = '(1.0/{})'.format(SMxsec)
#
#     samples['GGH_'+MX+model_name]  = {
#         'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWToLNuQQ_M'+MX),
#         'weight': mcCommonWeight+'*'+noSMxsec+'*( {0} * (abs({0}) < 50) )'.format(model),
#     }
#
#     samples['GGHINT_'+MX+model_name]  = {
#         'name': nanoGetSampleFiles(mcDirectory, 'GluGluHToWWToLNuQQ_M'+MX),
#         'weight': mcCommonWeight+'*'+noSMxsec+'*( {0} * (abs({0}) < 50) )'.format(model_I),
#     }
#
#     if MX in ['4000', '5000']: # Just to be sure, recalculate baseW with new cross sections
#         newbasew = getBaseWnAOD(mcDirectory, mcProduction, ['GluGluHToWWToLNuQQ_M'+MX])
#         addSampleWeight(samples, 'GGH_'+MX+model_name, 'GluGluHToWWToLNuQQ_M'+MX, newbasew+'/baseW')
#         addSampleWeight(samples, 'GGHINT_'+MX+model_name, 'GluGluHToWWToLNuQQ_M'+MX, newbasew+'/baseW')
#
#
#
#
# ############ VBF H->WW ############
# for MX in massvbf:
#     # Model dependent -> Xsec*BR is applied in later step, so remove "SM"-Xsec*BR
#     SMxsec = HiggsXS.GetHiggsXS4Sample('YR4','13TeV','VBFHToWWToLNuQQ_M'+MX)['xs']
#     noSMxsec = '(1.0/{})'.format(SMxsec)
#
#     samples['QQH_'+MX+model_name]  = {
#         'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWToLNuQQ_M'+MX),
#         'weight': mcCommonWeight+'*'+noSMxsec+'*( {0} * (abs({0}) < 50) )'.format(model),
#     }
#
#     samples['QQHINT_'+MX+model_name]  = {
#         'name': nanoGetSampleFiles(mcDirectory, 'VBFHToWWToLNuQQ_M'+MX),
#         'weight': mcCommonWeight+'*'+noSMxsec+'*( {0} * (abs({0}) < 50) )'.format(model_I),
#     }
#
#     if MX in ['4000', '5000']: # Just to be sure, recalculate baseW with new cross sections
#         newbasew = getBaseWnAOD(mcDirectory, mcProduction, ['VBFHToWWToLNuQQ_M'+MX])
#         addSampleWeight(samples, 'QQH_'+MX+model_name, 'VBFHToWWToLNuQQ_M'+MX, newbasew+'/baseW')
#         addSampleWeight(samples, 'QQHINT_'+MX+model_name, 'VBFHToWWToLNuQQ_M'+MX, newbasew+'/baseW')


for key, value in samples.items():
    if key in ['DATA',]: continue
    if 'QQHINT' in key or 'GGHINT' in key: continue
    value['suppressNegative'] = ['all']
    value['suppressNegativeNuisances'] =['all']

###########################################
################## DATA ###################
###########################################

samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 15
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

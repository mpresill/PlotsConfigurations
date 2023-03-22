
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight

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

mcProduction = 'Fall2017_102X_nAODv7_Full2017v7'
dataReco = 'Run2017_102X_nAODv7_Full2017v7'

mcSteps = 'MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7{var}'

fakeReco = 'Run2017_102X_nAODv7_Full2017v7'
fakeSteps = 'DATAl1loose2017v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2017v7__l2loose__l2tightOR2017v7'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'
  treeBaseDirSMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

def makeMCDirectorySMPeos(var=''):
    if var:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDirSMPeos, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
mcDirectorySMPeos = makeMCDirectorySMPeos() #this was added just for signals 

DirectorySMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Fall2017_102X_nAODv7_Full2017v7/MCl1loose2017v7__MCCorr2017v7__l2loose__l2tightOR2017v7'
################################################
############ DATA DECLARATION ##################
################################################

DataRun = [
            ['B','Run2017B-02Apr2020-v1'] ,
            ['C','Run2017C-02Apr2020-v1'] ,
            ['D','Run2017D-02Apr2020-v1'] ,
            ['E','Run2017E-02Apr2020-v1'] ,
            ['F','Run2017F-02Apr2020-v1']
          ]


DataSets = ['MuonEG','DoubleMuon','SingleMuon','DoubleEG','SingleElectron']

DataTrig = {
            'MuonEG'         : 'Trigger_ElMu' ,
            'DoubleMuon'     : '!Trigger_ElMu && Trigger_dblMu' ,
            'SingleMuon'     : '!Trigger_ElMu && !Trigger_dblMu && Trigger_sngMu' ,
            'DoubleEG'       : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && Trigger_dblEl' ,
            'SingleElectron' : '!Trigger_ElMu && !Trigger_dblMu && !Trigger_sngMu && !Trigger_dblEl && Trigger_sngEl' ,
           }


#########################################
############ MC COMMON ##################
#########################################

# SFweight, defined in Alias, does not includ: PUJetIdSF, BoostedWtagSF_nominal.
#About PUJetIdSF: it needs to be added in some "patches" macro
#SFweight      = 'SFweight'
#SFweight += '* PrefireWeight * PUJetIdSF * btagSF * BoostedWtagSF_nominal'

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'



########################################
#######       EFT weights       ########
########################################
sm_cT1 = 'LHEReweightingWeight[0]'
sm_cS0_eboliv2 = 'LHEReweightingWeight[40]'
quadReweight_cS0 = '( 0.5* (1/50) * (1/50) * (LHEReweightingWeight[568] + LHEReweightingWeight[567] - 2*LHEReweightingWeight[526]) )'
quadReweight_cS0_eboliv2 = '( 0.5* (1/30) * (1/30) * (LHEReweightingWeight[0] + LHEReweightingWeight[80] - 2*LHEReweightingWeight[40]) )'




###########################################
#############  SM  SIGNALS  ###############
###########################################
    #************* sm VBS ewk with (old) global recoil option, for EFT limits *******#
samples['sm_global'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 15
}
addSampleWeight(samples,'sm_global','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.03004/0.02982)')
    #************ sm VBS ewk with dipole recoil *********************#
samples['sm_dipole'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 15
}
addSampleWeight(samples,'sm_dipole','WmTo2J_ZTo2L_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.03004/0.02982)')
#************ OLD eboli basis, GLOBAL recoil ************#
samples['sm_aQGC'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + sm_cT1 + '* (0.05862 / 0.2222)', 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_aQGC','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) ')
#************ new eboli basis, dipole recoil ************#
samples['sm_aQGC_eboliv2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2'),
    'weight': mcCommonWeight + '*' + sm_cS0_eboliv2, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) ')



###########################################
#############  EFT QUAD FSO ###############
###########################################
samples['quad_cS0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cS0, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cS0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#************ new eboli basis, dipole recoil ************#
samples['quad_cS0_eboliv2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2'),
    'weight': mcCommonWeight + '*' + quadReweight_cS0_eboliv2, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cS0_eboliv2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)')

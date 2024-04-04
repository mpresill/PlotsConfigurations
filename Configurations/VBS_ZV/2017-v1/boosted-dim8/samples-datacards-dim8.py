
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
### T0
quadReweight_cT0 = '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[870] + LHEReweightingWeight[830] - 2 * LHEReweightingWeight[850]))'
LinReweight_cT0 = '( 0.5* (1/(1)) * ( LHEReweightingWeight[870] - LHEReweightingWeight[830] ))'
sm_cT0 = '( LHEReweightingWeight[850] )'
LinQuadReweight_cT0 = '(' + quadReweight_cT0 + '+' + LinReweight_cT0 + ')'
smLinQuadReweight_cT0 = '(' + sm_cT0 + '+' + quadReweight_cT0 + '+' + LinReweight_cT0 + ')'
### T1
quadReweight_cT1 = '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[951] + LHEReweightingWeight[911] - 2 * LHEReweightingWeight[931]))'
LinReweight_cT1 = '( 0.5* (1/(1)) * ( LHEReweightingWeight[951] - LHEReweightingWeight[911] ))'
sm_cT1 = '( LHEReweightingWeight[931] )'
LinQuadReweight_cT1 = '(' +  quadReweight_cT1 + '+' + LinReweight_cT1 + ')'
smLinQuadReweight_cT1 = '(' + sm_cT0 + '+' +  quadReweight_cT1 + '+' + LinReweight_cT1 + ')'
### T2
quadReweight_cT2 = '( 0.5* (1/(1)) * (1/(1)) * ( LHEReweightingWeight[1022] + LHEReweightingWeight[1002] - 2 * LHEReweightingWeight[1012]))'
LinReweight_cT2 = '( 0.5* (1/(1)) * ( LHEReweightingWeight[1022] - LHEReweightingWeight[1002] ))'
sm_cT2 = '( LHEReweightingWeight[1012] )'
LinQuadReweight_cT2 = '(' + quadReweight_cT2 + '+' + LinReweight_cT2 + ')'
smLinQuadReweight_cT2 = '(' + sm_cT0 + '+' +  quadReweight_cT2 + '+' + LinReweight_cT2 + ')'
 #************ EFT samples ************#
 #*******************#      sm from reweighting
#samples['sm'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm','ZTo2L_ZTo2J_aQGC_eboliv2',                                       sm_cT0)
#addSampleWeight(samples,'sm','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
#addSampleWeight(samples,'sm','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
# #*******************#      sm+linear+quadratic
#samples['sm_lin_quad_cT0'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm_lin_quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2',                                       smLinQuadReweight_cT0)
#addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
#addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
# #*******************#      quadratic only
#samples['quad_cT0'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2',                                       quadReweight_cT0)
#addSampleWeight(samples,'quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
#addSampleWeight(samples,'quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
# #**********************************************************************************#      
# #*******************#      sm+linear+quadratic
#samples['sm_lin_quad_cT1'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm_lin_quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2',                                       smLinQuadReweight_cT1)
#addSampleWeight(samples,'sm_lin_quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
#addSampleWeight(samples,'sm_lin_quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
# #*******************#      quadratic only
#samples['quad_cT1'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2',                                       quadReweight_cT1)
#addSampleWeight(samples,'quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
#addSampleWeight(samples,'quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
# #**********************************************************************************#      
# #*******************#      sm+linear+quadratic
#samples['sm_lin_quad_cT2'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm_lin_quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2',                                       smLinQuadReweight_cT2)
#addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
#addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
# #*******************#      quadratic only
#samples['quad_cT2'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2',                                       quadReweight_cT2)
#addSampleWeight(samples,'quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)
#addSampleWeight(samples,'quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)


##############      centrally produced samples
samples['sm'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}

addSampleWeight(samples,'sm','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       sm_cT0)
addSampleWeight(samples,'sm','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
addSampleWeight(samples,'sm','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
 #*******************#      sm+linear+quadratic
"""
samples['sm_lin_quad_cT0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
addSampleWeight(samples,'sm_lin_quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       smLinQuadReweight_cT0)
addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
 #*******************#      quadratic only
samples['quad_cT0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
addSampleWeight(samples,'quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       quadReweight_cT0)
addSampleWeight(samples,'quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
addSampleWeight(samples,'quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)

#**********************************************************************************#      
 #*******************#      sm+linear+quadratic
samples['sm_lin_quad_cT1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
addSampleWeight(samples,'sm_lin_quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       smLinQuadReweight_cT1)
addSampleWeight(samples,'sm_lin_quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
addSampleWeight(samples,'sm_lin_quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
 #*******************#      quadratic only
samples['quad_cT1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
addSampleWeight(samples,'quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       quadReweight_cT1)
addSampleWeight(samples,'quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
addSampleWeight(samples,'quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
"""
#**********************************************************************************#      
 #*******************#      sm+linear+quadratic
samples['sm_lin_quad_cT2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
addSampleWeight(samples,'sm_lin_quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       smLinQuadReweight_cT2)
addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
 #*******************#      quadratic only
samples['quad_cT2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}

addSampleWeight(samples,'quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       quadReweight_cT2)
addSampleWeight(samples,'quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)
addSampleWeight(samples,'quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)






###########################################
#############  BACKGROUNDS  ###############
###########################################

######## tZq ##########
samples['tZq'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight+'*(Sum$(abs(GenPart_pdgId)==6)!=0)',
    'FilesPerJob': 10
}

########## irreducible VBS QCD 
samples['VBS_VV_QCD'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WpToLNu_ZTo2J_QCD') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpToLNu_WpTo2J_QCD')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_QCD')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_WmToLNu_QCD')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmToLNu_ZTo2J_QCD')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_QCD')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_QCD'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
########VBF-V##########
files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50_newpmx')

samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6
}

########## DY #### 
files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200_newpmx') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600_newpmx') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1') 


samples['DY'] = {
    'name': files,
    'weight': (mcCommonWeight + "*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                        Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )"),#.replace("PUJetIdSF", "1."), ##DY_photons_filter 
    'subsamples' :{
            "Boosted_Z_1" : '(vbs_category == 0) && (Zleppt > 0 && Zleppt <=75)',
            "Boosted_Z_2" : '(vbs_category == 0) && (Zleppt > 75 && Zleppt <=150)',
            "Boosted_Z_3" : '(vbs_category == 0) && (Zleppt > 150 && Zleppt <=250)',
            "Boosted_Z_4" : '(vbs_category == 0) && (Zleppt > 250 && Zleppt <=400)',
            "Boosted_Z_5" : '(vbs_category == 0) && (Zleppt > 400)',	
    },
    'FilesPerJob': 3,
    'EventsPerJob' : 50000,
    #  'suppressNegative' :['all'],
    #  'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext1',                '(LHE_HT < 100)')   
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO_ext1',         '(LHE_HT < 100)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200_newpmx',    '1.000')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400',           '0.999')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600_newpmx',    '0.990')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800',           '0.975')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200',          '0.907')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500',         '0.833')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf',          '1.015')


###### Top #######
files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
    nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic')+ \
    nanoGetSampleFiles(mcDirectory,'TTZjets_ext1') + \
    nanoGetSampleFiles(mcDirectory,'TTWjets_ext1')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
    'EventsPerJob' : 70000,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")

######## Vg ########
samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(mcDirectory,'ZGToLLG'),
                    'weight' : mcCommonWeightNoMatch +'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 6,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }

############ VgS ############
samples['VgS']  =  {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                                 + nanoGetSampleFiles(mcDirectory,'ZGToLLG')
                                 + nanoGetSampleFiles(mcDirectory,'WZTo3LNu_mllmin01'),
                      'weight' : mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
                      'FilesPerJob' : 6,
                      'EventsPerJob' : 70000,
                      'suppressNegative' :['all'],
                      'suppressNegativeNuisances' :['all'],
                   }

addSampleWeight(samples,'VgS','Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') 
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ other backgrounds ############
samples['other'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT70_100') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf') +\
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENEN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENMN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToENTN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNEN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNMN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToMNTN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNEN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNMN') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluToWWToTNTN') + \
            nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop') + \
            nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
            nanoGetSampleFiles(mcDirectory, 'ZZTo4L') + \
            nanoGetSampleFiles(mcDirectory, 'ZZZ') + \
            nanoGetSampleFiles(mcDirectory, 'WZZ') + \
            nanoGetSampleFiles(mcDirectory, 'WWZ') + \
            nanoGetSampleFiles(mcDirectory, 'WWW'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 15,
#    'EventsPerJob' : 70000,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples,'other', 'WJetsToLNu-LO', '(LHE_HT < 70)')
addSampleWeight(samples,'other', 'WJetsToLNu-HT100_200', '0.993') 
addSampleWeight(samples,'other', 'WJetsToLNu-HT200_400', '1.002') 
addSampleWeight(samples,'other', 'WJetsToLNu-HT400_600', '1.009') 
addSampleWeight(samples,'other', 'WJetsToLNu-HT600_800', '1.120') 
addSampleWeight(samples,'other', 'WJetsToLNu-HT800_1200', '1.202') 
addSampleWeight(samples,'other', 'WJetsToLNu-HT1200_2500', '1.332') 
addSampleWeight(samples,'other', 'WJetsToLNu-HT2500_inf', '4.200') 
addSampleWeight(samples,'other','GluGluToWWToENEN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToENMN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToENTN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToMNEN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToMNMN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToMNTN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToTNEN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToTNMN',  "1.53/1.4")
addSampleWeight(samples,'other','GluGluToWWToTNTN',  "1.53/1.4")
addSampleWeight(samples,'other','ZZTo2L2Nu',  "1.11")
addSampleWeight(samples,'other','ZZTo4L',  "1.11")

 
###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 30
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

###########################################
################## DATA ###################
###########################################
samples['DATA'] = {
  'name': [],
  'weight': 'METFilter_DATA*LepWPCut',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 120
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(dataDirectory, pd + '_' + sd)
    samples['DATA']['name'].extend(files)
    samples['DATA']['weights'].extend([DataTrig[pd]] * len(files))

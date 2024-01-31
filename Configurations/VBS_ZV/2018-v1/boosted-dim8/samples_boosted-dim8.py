
import os 
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, getBaseWnAOD, addSampleWeight

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

mcProduction = 'Autumn18_102X_nAODv7_Full2018v7'
dataReco = 'Run2018_102X_nAODv7_Full2018v7'

mcSteps = 'MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7{var}'

fakeReco = 'Run2018_102X_nAODv7_Full2018v7'
fakeSteps = 'DATAl1loose2018v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2018v7__l2loose__l2tightOR2018v7'

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
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
fakeDirectory = os.path.join(treeBaseDir, fakeReco, fakeSteps)
mcDirectorySMPeos = makeMCDirectorySMPeos() #this was added just for signals 

DirectorySMPeos = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

################################################
############ DATA DECLARATION ##################
################################################
DataRun = [
            ['A','Run2018A-02Apr2020-v1'] ,
            ['B','Run2018B-02Apr2020-v1'] ,
            ['C','Run2018C-02Apr2020-v1'] ,
            ['D','Run2018D-02Apr2020-v1'] ,
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

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'
def CombineBaseW(samples, proc, samplelist):
    newbaseW = getBaseWnAOD(mcDirectory, mcProduction, samplelist)
    for s in samplelist:
        addSampleWeight(samples, proc, s, newbaseW+'/baseW')

#def CombineBaseWSMPeos(samples, proc, samplelist):
#    newbaseW = getBaseWnAOD(makeMCDirectorySMPeos, mcProduction, samplelist)
#    for s in samplelist:
#        addSampleWeight(samples, proc, s, newbaseW+'/baseW')


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
#samples['sm-zz-v2'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2'), 
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm-zz-v2','ZTo2L_ZTo2J_aQGC_eboliv2',          '( LHEReweightingWeight[40] )')
#####
#samples['sm-zz'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC'), 
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm-zz','ZTo2L_ZTo2J_aQGC',             '( LHEReweightingWeight[40] )')
#####
#samples['sm-zz-v2-fs1'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2'), 
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm-zz-v2-fs1','ZTo2L_ZTo2J_aQGC_eboliv2',      '( LHEReweightingWeight[121] )')
#####





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
""" 
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




"""











 #*******************#      sm from reweighting
"""samples['sm'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
CombineBaseWSMPeos(samples, 'sm', ['ZTo2L_ZTo2J_aQGC_eboliv2','ZTo2L_ZTo2J_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm', ['WmTo2J_ZTo2L_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm', ['WpTo2J_ZTo2L_aQGC_eboliv2','WpTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive

addSampleWeight(samples,'sm','ZTo2L_ZTo2J_aQGC_eboliv2',                                                sm_cT0)
addSampleWeight(samples,'sm','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       sm_cT0)
addSampleWeight(samples,'sm','WmTo2J_ZTo2L_aQGC_eboliv2',         '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
addSampleWeight(samples,'sm','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
addSampleWeight(samples,'sm','WpTo2J_ZTo2L_aQGC_eboliv2',         '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
addSampleWeight(samples,'sm','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
 #*******************#      sm+linear+quadratic
samples['sm_lin_quad_cT0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT0', ['ZTo2L_ZTo2J_aQGC_eboliv2','ZTo2L_ZTo2J_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT0', ['WmTo2J_ZTo2L_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT0', ['WpTo2J_ZTo2L_aQGC_eboliv2','WpTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive

addSampleWeight(samples,'sm_lin_quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2',                                       smLinQuadReweight_cT0)
addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
addSampleWeight(samples,'sm_lin_quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       smLinQuadReweight_cT0)
addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
 #*******************#      quadratic only
samples['quad_cT0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
CombineBaseWSMPeos(samples, 'quad_cT0', ['ZTo2L_ZTo2J_aQGC_eboliv2','ZTo2L_ZTo2J_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'quad_cT0', ['WmTo2J_ZTo2L_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'quad_cT0', ['WpTo2J_ZTo2L_aQGC_eboliv2','WpTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive

addSampleWeight(samples,'quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2',                                       quadReweight_cT0)
addSampleWeight(samples,'quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
addSampleWeight(samples,'quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
addSampleWeight(samples,'quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       quadReweight_cT0)
addSampleWeight(samples,'quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
addSampleWeight(samples,'quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
 #**********************************************************************************#      
 #*******************#      sm+linear+quadratic
samples['sm_lin_quad_cT1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT1', ['ZTo2L_ZTo2J_aQGC_eboliv2','ZTo2L_ZTo2J_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT1', ['WmTo2J_ZTo2L_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT1', ['WpTo2J_ZTo2L_aQGC_eboliv2','WpTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive

addSampleWeight(samples,'sm_lin_quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2',                                       smLinQuadReweight_cT1)
addSampleWeight(samples,'sm_lin_quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
addSampleWeight(samples,'sm_lin_quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
addSampleWeight(samples,'sm_lin_quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       smLinQuadReweight_cT1)
addSampleWeight(samples,'sm_lin_quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
addSampleWeight(samples,'sm_lin_quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT1)
 #*******************#      quadratic only
samples['quad_cT1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
CombineBaseWSMPeos(samples, 'quad_cT1', ['ZTo2L_ZTo2J_aQGC_eboliv2','ZTo2L_ZTo2J_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'quad_cT1', ['WmTo2J_ZTo2L_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'quad_cT1', ['WpTo2J_ZTo2L_aQGC_eboliv2','WpTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive

addSampleWeight(samples,'quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2',                                       quadReweight_cT1)
addSampleWeight(samples,'quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
addSampleWeight(samples,'quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
addSampleWeight(samples,'quad_cT1','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       quadReweight_cT1)
addSampleWeight(samples,'quad_cT1','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
addSampleWeight(samples,'quad_cT1','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT1)
 #**********************************************************************************#      
 #*******************#      sm+linear+quadratic
samples['sm_lin_quad_cT2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT2', ['ZTo2L_ZTo2J_aQGC_eboliv2','ZTo2L_ZTo2J_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT2', ['WmTo2J_ZTo2L_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'sm_lin_quad_cT2', ['WpTo2J_ZTo2L_aQGC_eboliv2','WpTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive

addSampleWeight(samples,'sm_lin_quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2',                                       smLinQuadReweight_cT2)
addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
addSampleWeight(samples,'sm_lin_quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       smLinQuadReweight_cT2)
addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT2)
 #*******************#      quadratic only
samples['quad_cT2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
}
CombineBaseWSMPeos(samples, 'quad_cT2', ['ZTo2L_ZTo2J_aQGC_eboliv2','ZTo2L_ZTo2J_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'quad_cT2', ['WmTo2J_ZTo2L_aQGC_eboliv2','WmTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive
CombineBaseWSMPeos(samples, 'quad_cT2', ['WpTo2J_ZTo2L_aQGC_eboliv2','WpTo2J_ZTo2L_aQGC_eboliv2_official']) #this is to maximize statistics for this inclusive

addSampleWeight(samples,'quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2',                                       quadReweight_cT2)
addSampleWeight(samples,'quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)
addSampleWeight(samples,'quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)
addSampleWeight(samples,'quad_cT2','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       quadReweight_cT2)
addSampleWeight(samples,'quad_cT2','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)
addSampleWeight(samples,'quad_cT2','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT2)



"""
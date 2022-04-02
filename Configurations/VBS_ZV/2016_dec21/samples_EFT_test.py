
import os
import inspect

configurations = os.path.realpath(inspect.getfile(inspect.currentframe())) # this file
configurations = os.path.dirname(configurations) # ggH2018
configurations = os.path.dirname(configurations) # Differential
configurations = os.path.dirname(configurations) # Configurations
configurations = os.path.dirname(configurations) # Configurations

from LatinoAnalysis.Tools.commonTools import getSampleFiles, getBaseW, addSampleWeight, getBaseWnAOD

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

mcProduction = 'Summer16_102X_nAODv7_Full2016v7'
dataReco = 'Run2016_102X_nAODv7_Full2016v7'

mcSteps = 'MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7{var}'
fakeReco = 'Run2016_102X_nAODv7_Full2016v7'
fakeSteps = 'DATAl1loose2016v7__l2loose__fakeW'

dataSteps = 'DATAl1loose2016v7__l2loose__l2tightOR2016v7'

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
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)
mcDirectorySMPeos = makeMCDirectorySMPeos() #this was added just for signals 

DirectorySMPeos =     '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7'


def CombineBaseW(samples, proc, samplelist):
    newbaseW = getBaseWnAOD(mcDirectory, mcProduction, samplelist)
    for s in samplelist:
        addSampleWeight(samples, proc, s, newbaseW+'/baseW')


################################################
############ DATA DECLARATION ##################
################################################
#THIS NEEDS TO BE UPDATED
DataRun = [
    ['B','Run2016B-02Apr2020_ver1-v1'],
    ['B','Run2016B-02Apr2020_ver2-v1'],
    ['C','Run2016C-02Apr2020-v1'],
    ['D','Run2016D-02Apr2020-v1'],
    ['E','Run2016E-02Apr2020-v1'],
    ['F','Run2016F-02Apr2020-v1'],
    ['G','Run2016G-02Apr2020-v1'],
    ['H','Run2016H-02Apr2020-v1']
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

# SFweight does not include btag weights
mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

###########################################
#############   SIGNALS  ##################
###########################################


########################################
#######       EFT weights       ########
########################################
#####   TRANSVERSE OPERATORS ###########
########################################
sm_cT1 = 'LHEReweightingWeight[0]'
LinReweight_cT1 = '( 0.5* 0.5 * (LHEReweightingWeight[34] - LHEReweightingWeight[33]) )'
quadReweight_cT1 = '( 0.5* 0.5 * 0.5 * (LHEReweightingWeight[34] + LHEReweightingWeight[33] - 2*LHEReweightingWeight[0]) )'
LinQuadReweight_cT1 = '( 0.5* 0.5 * (LHEReweightingWeight[34] - LHEReweightingWeight[33]) ) + ( 0.5* 0.5 * 0.5 * (LHEReweightingWeight[34] + LHEReweightingWeight[33] - 2*LHEReweightingWeight[0]) )'
#####
sm_cT0 = 'LHEReweightingWeight[35]'
LinReweight_cT0 = '(0.5 * 0.5 * (LHEReweightingWeight[69] - LHEReweightingWeight[68]) )'
quadReweight_cT0 = '(0.5 * 0.5 * 0.5 * (LHEReweightingWeight[69] + LHEReweightingWeight[68] - 2*LHEReweightingWeight[35]) )'
LinQuadReweight_cT0 = '(0.5 * 0.5 * (LHEReweightingWeight[69] - LHEReweightingWeight[68]) ) + (0.5 * 0.5 * 0.5 * (LHEReweightingWeight[69] + LHEReweightingWeight[68] - 2*LHEReweightingWeight[35]) )'
### NEW
LinReweight_cT2 = '( 0.5* (1/4.5) * (LHEReweightingWeight[104] - LHEReweightingWeight[103]) )'
quadReweight_cT2 = '( 0.5* (1/4.5) * (1/4.5) * (LHEReweightingWeight[104] + LHEReweightingWeight[103] - 2*LHEReweightingWeight[70]) )'
LinQuadReweight_cT2 = '(' + quadReweight_cT2 + '+' + LinReweight_cT2 + ')'
#### NEW
LinReweight_cT5 = '( 0.5* (1/25) * (LHEReweightingWeight[143] - LHEReweightingWeight[142]) )'
quadReweight_cT5 = '( 0.5* (1/25) * (1/25) * (LHEReweightingWeight[143] + LHEReweightingWeight[142] - 2*LHEReweightingWeight[105]) )'
LinQuadReweight_cT5 = '(' + quadReweight_cT5 + '+' + LinReweight_cT5 + ')'
#### NEW
LinReweight_cT7 = '( 0.5* (1/70) * (LHEReweightingWeight[194] - LHEReweightingWeight[193]) )'
quadReweight_cT7 = '( 0.5* (1/70) * (1/70) * (LHEReweightingWeight[194] + LHEReweightingWeight[193] - 2*LHEReweightingWeight[144]) )'
LinQuadReweight_cT7 = '(' + quadReweight_cT7 + '+' + LinReweight_cT7 + ')'
#### NEW
LinReweight_cT6 = '( 0.5* (1/29) * (LHEReweightingWeight[237] - LHEReweightingWeight[236]) )'
quadReweight_cT6 = '( 0.5* (1/29) * (1/29) * (LHEReweightingWeight[237] + LHEReweightingWeight[236] - 2*LHEReweightingWeight[195]) )'
LinQuadReweight_cT6 = '(' + quadReweight_cT6 + '+' + LinReweight_cT6 + ')'
#### NEW
LinReweight_cT8 = '( 0.5* (1/2) * (LHEReweightingWeight[636] - LHEReweightingWeight[635]) )'
quadReweight_cT8 = '( 0.5* (1/2) * (1/2) * (LHEReweightingWeight[636] + LHEReweightingWeight[635] - 2*LHEReweightingWeight[602]) )'
LinQuadReweight_cT8 = '(' + quadReweight_cT8 + '+' + LinReweight_cT8 + ')'
#### NEW
LinReweight_cT9 = '( 0.5* (1/10) * (LHEReweightingWeight[677] - LHEReweightingWeight[676]) )'
quadReweight_cT9 = '( 0.5* (1/10) * (1/10) * (LHEReweightingWeight[677] + LHEReweightingWeight[676] - 2*LHEReweightingWeight[637]) )'
LinQuadReweight_cT9 = '(' + quadReweight_cT9 + '+' + LinReweight_cT9 + ')'
########################################
#####   M OPERATORS ###########
########################################
LinReweight_cM6 = '( 0.5* (1/20) * (LHEReweightingWeight[272] - LHEReweightingWeight[271]) )'
quadReweight_cM6 = '( 0.5* (1/20) * (1/20) * (LHEReweightingWeight[272] + LHEReweightingWeight[271] - 2*LHEReweightingWeight[238]) )'
LinQuadReweight_cM6 = '(' + quadReweight_cM6 + '+' + LinReweight_cM6 + ')'
#### NEW
LinReweight_cM7 = '( 0.5* (1/40) * (LHEReweightingWeight[303] - LHEReweightingWeight[302]) )'
quadReweight_cM7 = '( 0.5* (1/40) * (1/40) * (LHEReweightingWeight[303] + LHEReweightingWeight[302] - 2*LHEReweightingWeight[273]) )'
LinQuadReweight_cM7 = '(' + quadReweight_cM7 + '+' + LinReweight_cM7 + ')'
#### NEW
LinReweight_cM4 = '( 0.5* (1/130) * (LHEReweightingWeight[340] - LHEReweightingWeight[339]) )'
quadReweight_cM4 = '( 0.5* (1/130) * (1/130) * (LHEReweightingWeight[340] + LHEReweightingWeight[339] - 2*LHEReweightingWeight[304]) )'
LinQuadReweight_cM4 = '(' + quadReweight_cM4 + '+' + LinReweight_cM4 + ')'
#### 
LinReweight_cM5 = '( 0.5* (1/200) * (LHEReweightingWeight[385] - LHEReweightingWeight[384]) )'
quadReweight_cM5 = '( 0.5* (1/200) * (1/200) * (LHEReweightingWeight[385] + LHEReweightingWeight[384] - 2*LHEReweightingWeight[341]) )'
LinQuadReweight_cM5 = '(' + quadReweight_cM5 + '+' + LinReweight_cM5 + ')'
#### 
LinReweight_cM2 = '( 0.5* (1/60) * (LHEReweightingWeight[416] - LHEReweightingWeight[415]) )'
quadReweight_cM2 = '( 0.5* (1/60) * (1/60) * (LHEReweightingWeight[416] + LHEReweightingWeight[415] - 2*LHEReweightingWeight[386]) )'
LinQuadReweight_cM2 = '(' + quadReweight_cM2 + '+' + LinReweight_cM2 + ')'
#### 
LinReweight_cM3 = '( 0.5* (1/105) * (LHEReweightingWeight[447] - LHEReweightingWeight[446]) )'
quadReweight_cM3 = '( 0.5* (1/105) * (1/105) * (LHEReweightingWeight[447] + LHEReweightingWeight[446] - 2*LHEReweightingWeight[386]) )'
LinQuadReweight_cM3 = '(' + quadReweight_cM3 + '+' + LinReweight_cM3 + ')'
#### 
LinReweight_cM0 = '( 0.5* (1/10) * (LHEReweightingWeight[488] - LHEReweightingWeight[487]) )'
quadReweight_cM0 = '( 0.5* (1/10) * (1/10) * (LHEReweightingWeight[488] + LHEReweightingWeight[487] - 2*LHEReweightingWeight[448]) )'
LinQuadReweight_cM0 = '(' + quadReweight_cM0 + '+' + LinReweight_cM0 + ')'
#### 
LinReweight_cM1 = '( 0.5* (1/30) * (LHEReweightingWeight[525] - LHEReweightingWeight[524]) )'
quadReweight_cM1 = '( 0.5* (1/30) * (1/30) * (LHEReweightingWeight[525] + LHEReweightingWeight[524] - 2*LHEReweightingWeight[489]) )'
LinQuadReweight_cM1 = '(' + quadReweight_cM1 + '+' + LinReweight_cM1 + ')'
########################################
#####   S OPERATORS ###########
######################################## 
LinReweight_cS0 = '( 0.5* (1/50) * (LHEReweightingWeight[568] - LHEReweightingWeight[567]) )'
quadReweight_cS0 = '( 0.5* (1/50) * (1/50) * (LHEReweightingWeight[568] + LHEReweightingWeight[567] - 2*LHEReweightingWeight[526]) )'
LinQuadReweight_cS0 = '(' + quadReweight_cS0 + '+' + LinReweight_cS0 + ')'
###
LinReweight_cS1 = '( 0.5* (1/35) * (LHEReweightingWeight[601] - LHEReweightingWeight[600]) )'
quadReweight_cS1 = '( 0.5* (1/35) * (1/35) * (LHEReweightingWeight[601] + LHEReweightingWeight[600] - 2*LHEReweightingWeight[569]) )'
LinQuadReweight_cS1 = '(' + quadReweight_cS1 + '+' + LinReweight_cS1 + ')'
#########################################
#**************************************************************#

"""


######### FT0 ############
#default coupling, quadratic EFT 
samples['quad_cT0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT0, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT0','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cT0','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) * '                                      + LinQuadReweight_cT0 )
addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) * ' + LinQuadReweight_cT0 )
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   * ' + LinQuadReweight_cT0 )
addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')


######### FT1 ############
#default coupling, quadratic EFT 
samples['quad_cT1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT1, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT1','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cT1','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT1 )
addSampleWeight(samples,'sm_lin_quad_cT1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT1 )
addSampleWeight(samples,'sm_lin_quad_cT1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT1 )
addSampleWeight(samples,'sm_lin_quad_cT1','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT1','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
"""
########## FT2 ############
##default coupling, quadratic EFT 
samples['quad_cT2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT2, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT2','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cT2','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT2 )
addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT2 )
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT2 )
addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
"""

########### FT5 ############
###default coupling, quadratic EFT 
#samples['quad_cT5'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cT5, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cT5','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cT5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cT5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cT5'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cT5','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT5 )
#addSampleWeight(samples,'sm_lin_quad_cT5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT5 )
#addSampleWeight(samples,'sm_lin_quad_cT5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT5 )
#addSampleWeight(samples,'sm_lin_quad_cT5','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cT5','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT6 ############
###default coupling, quadratic EFT 
#samples['quad_cT6'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cT6, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cT6','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cT6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cT6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cT6'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cT6','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT6 )
#addSampleWeight(samples,'sm_lin_quad_cT6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT6 )
#addSampleWeight(samples,'sm_lin_quad_cT6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT6 )
#addSampleWeight(samples,'sm_lin_quad_cT6','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cT6','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT7 ############
###default coupling, quadratic EFT 
#samples['quad_cT7'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cT7, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cT7','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cT7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cT7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cT7'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cT7','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT7 )
#addSampleWeight(samples,'sm_lin_quad_cT7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT7 )
#addSampleWeight(samples,'sm_lin_quad_cT7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT7 )
#addSampleWeight(samples,'sm_lin_quad_cT7','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cT7','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT8 ############
###default coupling, quadratic EFT 
#samples['quad_cT8'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cT8, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cT8','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cT8','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cT8','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cT8'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cT8','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT8 )
#addSampleWeight(samples,'sm_lin_quad_cT8','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT8 )
#addSampleWeight(samples,'sm_lin_quad_cT8','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT8 )
#addSampleWeight(samples,'sm_lin_quad_cT8','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cT8','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT9 ############
###default coupling, quadratic EFT 
#samples['quad_cT9'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cT9, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cT9','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cT9','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cT9','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cT9'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cT9','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT9 )
#addSampleWeight(samples,'sm_lin_quad_cT9','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT9 )
#addSampleWeight(samples,'sm_lin_quad_cT9','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT9 )
#addSampleWeight(samples,'sm_lin_quad_cT9','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cT9','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FM6 ############
##default coupling, quadratic EFT 
samples['quad_cM6'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM6, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cM6','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM6'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cM6','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM6 )
addSampleWeight(samples,'sm_lin_quad_cM6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM6 )
addSampleWeight(samples,'sm_lin_quad_cM6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM6 )
addSampleWeight(samples,'sm_lin_quad_cM6','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM6','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FM7 ############
##default coupling, quadratic EFT 
samples['quad_cM7'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM7, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cM7','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM7'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cM7','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM7 )
addSampleWeight(samples,'sm_lin_quad_cM7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM7 )
addSampleWeight(samples,'sm_lin_quad_cM7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM7 )
addSampleWeight(samples,'sm_lin_quad_cM7','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM7','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FM4 ############
###default coupling, quadratic EFT 
#samples['quad_cM4'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cM4, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cM4','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cM4','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cM4','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cM4'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cM4','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM4 )
#addSampleWeight(samples,'sm_lin_quad_cM4','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM4 )
#addSampleWeight(samples,'sm_lin_quad_cM4','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM4 )
#addSampleWeight(samples,'sm_lin_quad_cM4','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cM4','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FM5 ############
###default coupling, quadratic EFT 
#samples['quad_cM5'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cM5, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cM5','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cM5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cM5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cM5'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cM5','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM5 )
#addSampleWeight(samples,'sm_lin_quad_cM5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM5 )
#addSampleWeight(samples,'sm_lin_quad_cM5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM5 )
#addSampleWeight(samples,'sm_lin_quad_cM5','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cM5','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FM2 ############
###default coupling, quadratic EFT 
#samples['quad_cM2'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cM2, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'quad_cM2','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cM2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cM2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cM2'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 1
#}
#addSampleWeight(samples,'sm_lin_quad_cM2','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM2 )
#addSampleWeight(samples,'sm_lin_quad_cM2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM2 )
#addSampleWeight(samples,'sm_lin_quad_cM2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM2 )
#addSampleWeight(samples,'sm_lin_quad_cM2','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cM2','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FM1 ############
##default coupling, quadratic EFT 
samples['quad_cM1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM1, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cM1','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cM1','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM1 )
addSampleWeight(samples,'sm_lin_quad_cM1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM1 )
addSampleWeight(samples,'sm_lin_quad_cM1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM1 )
addSampleWeight(samples,'sm_lin_quad_cM1','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM1','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FM0 ############
##default coupling, quadratic EFT 
samples['quad_cM0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM0, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cM0','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cM0','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM0 )
addSampleWeight(samples,'sm_lin_quad_cM0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM0 )
addSampleWeight(samples,'sm_lin_quad_cM0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM0 )
addSampleWeight(samples,'sm_lin_quad_cM0','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM0','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FS0 ############
##default coupling, quadratic EFT 
samples['quad_cS0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cS0, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cS0','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cS0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cS0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cS0'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cS0','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cS0 )
addSampleWeight(samples,'sm_lin_quad_cS0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cS0 )
addSampleWeight(samples,'sm_lin_quad_cS0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cS0 )
addSampleWeight(samples,'sm_lin_quad_cS0','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cS0','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FS1 ############
##default coupling, quadratic EFT 
samples['quad_cS1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cS1, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cS1','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cS1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cS1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cS1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cS1','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cS1 )
addSampleWeight(samples,'sm_lin_quad_cS1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cS1 )
addSampleWeight(samples,'sm_lin_quad_cS1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cS1 )
addSampleWeight(samples,'sm_lin_quad_cS1','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cS1','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')




"""


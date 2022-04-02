
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


########### FT5 ############
###default coupling, quadratic EFT 
samples['quad_cT5'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT5, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT5','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT5'] = {
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
addSampleWeight(samples,'sm_lin_quad_cT5','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT5 )
addSampleWeight(samples,'sm_lin_quad_cT5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT5 )
addSampleWeight(samples,'sm_lin_quad_cT5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT5 )
addSampleWeight(samples,'sm_lin_quad_cT5','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT5','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT6 ############
###default coupling, quadratic EFT 
samples['quad_cT6'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT6, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT6','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT6'] = {
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
addSampleWeight(samples,'sm_lin_quad_cT6','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT6 )
addSampleWeight(samples,'sm_lin_quad_cT6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT6 )
addSampleWeight(samples,'sm_lin_quad_cT6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT6 )
addSampleWeight(samples,'sm_lin_quad_cT6','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT6','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT7 ############
###default coupling, quadratic EFT 
samples['quad_cT7'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT7, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT7','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT7'] = {
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
addSampleWeight(samples,'sm_lin_quad_cT7','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT7 )
addSampleWeight(samples,'sm_lin_quad_cT7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT7 )
addSampleWeight(samples,'sm_lin_quad_cT7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT7 )
addSampleWeight(samples,'sm_lin_quad_cT7','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT7','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT8 ############
###default coupling, quadratic EFT 
samples['quad_cT8'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT8, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT8','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT8','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT8','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT8'] = {
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
addSampleWeight(samples,'sm_lin_quad_cT8','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT8 )
addSampleWeight(samples,'sm_lin_quad_cT8','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT8 )
addSampleWeight(samples,'sm_lin_quad_cT8','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT8 )
addSampleWeight(samples,'sm_lin_quad_cT8','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT8','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FT9 ############
###default coupling, quadratic EFT 
samples['quad_cT9'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT9, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cT9','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cT9','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cT9','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT9'] = {
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
addSampleWeight(samples,'sm_lin_quad_cT9','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cT9 )
addSampleWeight(samples,'sm_lin_quad_cT9','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cT9 )
addSampleWeight(samples,'sm_lin_quad_cT9','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cT9 )
addSampleWeight(samples,'sm_lin_quad_cT9','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT9','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')


########### FM6 ############ this is redundant, as proportional to M0 https://indico.cern.ch/event/652320/contributions/2699383/attachments/1516308/2366509/Rauch_VBSCAN.pdf 
##default coupling, quadratic EFT 
#samples['quad_cM6'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
#    'weight': mcCommonWeight + '*' + quadReweight_cM6, #do we have to add reweighting for the different Wilson Coeff.?
#    'FilesPerJob': 10,
#    'EventsPerJob' : 70000,
#}
#addSampleWeight(samples,'quad_cM6','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
#addSampleWeight(samples,'quad_cM6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
#addSampleWeight(samples,'quad_cM6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
## SM + lin + quad 
#samples['sm_lin_quad_cM6'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
#    'weight': mcCommonWeight, 
#    'FilesPerJob': 10,
#    'EventsPerJob' : 70000,
#}
#addSampleWeight(samples,'sm_lin_quad_cM6','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM6 )
#addSampleWeight(samples,'sm_lin_quad_cM6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM6 )
#addSampleWeight(samples,'sm_lin_quad_cM6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM6 )
#addSampleWeight(samples,'sm_lin_quad_cM6','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
#addSampleWeight(samples,'sm_lin_quad_cM6','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
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
########### FM5 ############
##default coupling, quadratic EFT 
samples['quad_cM5'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM5, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cM5','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM5'] = {
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
addSampleWeight(samples,'sm_lin_quad_cM5','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM5 )
addSampleWeight(samples,'sm_lin_quad_cM5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM5 )
addSampleWeight(samples,'sm_lin_quad_cM5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM5 )
addSampleWeight(samples,'sm_lin_quad_cM5','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM5','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FM4 ############
##default coupling, quadratic EFT 
samples['quad_cM4'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM4, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cM4','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM4','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM4','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM4'] = {
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
addSampleWeight(samples,'sm_lin_quad_cM4','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM4 )
addSampleWeight(samples,'sm_lin_quad_cM4','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM4 )
addSampleWeight(samples,'sm_lin_quad_cM4','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM4 )
addSampleWeight(samples,'sm_lin_quad_cM4','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM4','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FM3 ############
###default coupling, quadratic EFT 
samples['quad_cM3'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM3, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cM3','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM3','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM3','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM3'] = {
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
addSampleWeight(samples,'sm_lin_quad_cM3','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM3 )
addSampleWeight(samples,'sm_lin_quad_cM3','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM3 )
addSampleWeight(samples,'sm_lin_quad_cM3','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM3 )
addSampleWeight(samples,'sm_lin_quad_cM3','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM3','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########### FM2 ############
###default coupling, quadratic EFT 
samples['quad_cM2'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM2, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'quad_cM2','ZTo2L_ZTo2J_aQGC','0.799 / 3.361 ')
addSampleWeight(samples,'quad_cM2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05862 / 0.2222)')
addSampleWeight(samples,'quad_cM2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1365 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cM2'] = {
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
addSampleWeight(samples,'sm_lin_quad_cM2','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cM2 )
addSampleWeight(samples,'sm_lin_quad_cM2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cM2 )
addSampleWeight(samples,'sm_lin_quad_cM2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cM2 )
addSampleWeight(samples,'sm_lin_quad_cM2','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cM2','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FM1 ############
##default coupling, quadratic EFT 
samples['quad_cM1'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cM1, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm_lin_quad_cS1','ZTo2L_ZTo2J_aQGC', '(0.799 / 3.361) *'                                      + LinQuadReweight_cS1 )
addSampleWeight(samples,'sm_lin_quad_cS1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.05862 / 0.2222) *' + LinQuadReweight_cS1 )
addSampleWeight(samples,'sm_lin_quad_cS1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1365 / 0.569)   *' + LinQuadReweight_cS1 )
addSampleWeight(samples,'sm_lin_quad_cS1','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cS1','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')



















#######VBS EW: only ZV processes 
samples['sm'] = {
    'name':   nanoGetSampleFiles(mcDirectorySMPeos, 'ZTo2L_ZTo2J_dipoleRecoil')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WpTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 15,
    'EventsPerJob' : 70000,
}
addSampleWeight(samples,'sm','WmTo2J_ZTo2_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0')
addSampleWeight(samples,'sm','WpTo2J_ZTo2_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0')


samples['tZq'] = {
	'name' : nanoGetSampleFiles(mcDirectory, 'tZq_ll_4f'),
	'weight' : mcCommonWeight,
    'FilesPerJob': 6,
    'EventsPerJob' : 70000,
}


###########################################
#############  BACKGROUNDS  ###############
###########################################

########## irreducible VBS QCD 
samples['VBS_VV_QCD'] = {
    'name':   nanoGetSampleFiles(mcDirectorySMPeos, 'WpToLNu_ZTo2J_QCD') 
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WpToLNu_WpTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WpToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WpTo2J_ZTo2L_QCD')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WpTo2J_WmToLNu_QCD')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WmToLNu_ZTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WmToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectorySMPeos, 'ZTo2L_ZTo2J_QCD')        
             +nanoGetSampleFiles(mcDirectorySMPeos, 'WmTo2J_ZTo2L_QCD'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 15,
    'EventsPerJob' : 70000,
}

########## DY #### consider using HT binned after Davide's studies.
#Beware! we have to correct the cross section here
###### DY #######

useDYtt = False

ptllDYW_NLO = '(0.876979+gen_ptll*(4.11598e-03)-(2.35520e-05)*gen_ptll*gen_ptll)*(1.10211 * (0.958512 - 0.131835*TMath::Erf((gen_ptll-14.1972)/10.1525)))*(gen_ptll<140)+0.891188*(gen_ptll>=140)'
ptllDYW_LO  = '(8.61313e-01+gen_ptll*4.46807e-03-1.52324e-05*gen_ptll*gen_ptll)*(1.08683 * (0.95 - 0.0657370*TMath::Erf((gen_ptll-11.)/5.51582)))*(gen_ptll<140)+1.141996*(gen_ptll>=140)'



files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-70to100') + \
	nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
	nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-70to100') + \
	nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-100to200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-200to400_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-400to600_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-5to50_HT-600toinf') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO') 


samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + "*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                         Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )",
        'FilesPerJob': 6,
       'EventsPerJob' : 70000,
    }
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext2', '('+ptllDYW_NLO+')*(LHE_HT < 70)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO', '('+ptllDYW_LO+')*(LHE_HT < 70)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-70to100', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600_ext1', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-70to100', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-100to200', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-200to400_ext1', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-400to600_ext1', ptllDYW_LO)
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-5to50_HT-600toinf', ptllDYW_LO)

#BEWARE! SOME CORRECTION IS NEEDED ON THE CROSS SECTION OF THESE SAMPLES

###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
    nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic')

samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
    'EventsPerJob' : 70000,
}

addSampleWeight(samples, 'top', 'TTTo2L2Nu', 'Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")

######WJets#####

files = nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf') 


samples['WJets'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 6
}
"""
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT100_200', '0.993')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT200_400', '1.002')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT400_600', '1.009')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT600_800', '1.120')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT800_1200', '1.202')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT1200_2500', '1.332')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT2500_inf', '4.200')
"""
###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop'),
    'weight': mcCommonWeight, #+ '*nllW',
    'FilesPerJob': 6
}


samples['ggWW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'GluGluWWTo2L2Nu_MCFM'),
    'weight': mcCommonWeight + '*1.53/1.4', # updating k-factor
    'FilesPerJob': 4
}


######## Vg ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'Zg')

samples['Vg'] = {
    'name': files,
    'weight': mcCommonWeightNoMatch + '*!(Gen_ZGstar_mass > 0)',
    'FilesPerJob' : 6,
    'EventsPerJob' : 70000,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

######## VgS ########

files = nanoGetSampleFiles(mcDirectory, 'Wg_MADGRAPHMLM') + \
    nanoGetSampleFiles(mcDirectory, 'Zg') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo3LNu_mllmin01')

samples['VgS'] = {
    'name': files,
    'weight': mcCommonWeight + ' * (gstarLow * 0.94 + gstarHigh * 1.14)',
    'FilesPerJob' : 6,
    'EventsPerJob' : 70000,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples, 'VgS', 'Wg_MADGRAPHMLM', '(Gen_ZGstar_mass > 0 && Gen_ZGstar_mass < 0.1)')
addSampleWeight(samples, 'VgS', 'Zg', '(Gen_ZGstar_mass > 0)')
addSampleWeight(samples, 'VgS', 'WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')
############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 6
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
    'FilesPerJob': 6
}


########VBF-V##########

files =nanoGetSampleFiles(mcDirectory, 'EWK_LLJJ_MLL-50_MJJ-120')

samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
    'EventsPerJob' : 70000,
}

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
  'FilesPerJob': 80
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

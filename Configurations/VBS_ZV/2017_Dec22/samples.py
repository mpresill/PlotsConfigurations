
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
#####   TRANSVERSE OPERATORS ###########
########################################
sm_cT1 = 'LHEReweightingWeight[0]'
LinReweight_cT1 = '( 0.5* 0.5 * (LHEReweightingWeight[34] - LHEReweightingWeight[33]) )'
quadReweight_cT1 = '( 0.5* 0.5 * 0.5 * (LHEReweightingWeight[34] + LHEReweightingWeight[33] - 2*LHEReweightingWeight[0]) )'
LinQuadReweight_cT1 = '(' + quadReweight_cT1 + '+' + LinReweight_cT1 + ')'
#####
sm_cT0 = 'LHEReweightingWeight[35]'
LinReweight_cT0 = '(0.5 * 0.5 * (LHEReweightingWeight[69] - LHEReweightingWeight[68]) )'
quadReweight_cT0 = '(0.5 * 0.5 * 0.5 * (LHEReweightingWeight[69] + LHEReweightingWeight[68] - 2*LHEReweightingWeight[35]) )'
LinQuadReweight_cT0 = '(' + quadReweight_cT0 + '+' + LinReweight_cT0 + ')'
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
addSampleWeight(samples,'quad_cT0','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)')
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
addSampleWeight(samples,'sm_lin_quad_cT0','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) * '                                      + LinQuadReweight_cT0 )
addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) * ' + LinQuadReweight_cT0 )
addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   * ' + LinQuadReweight_cT0 )
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
addSampleWeight(samples,'quad_cT1','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1199 / 0.569)')
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
addSampleWeight(samples,'sm_lin_quad_cT1','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) *'                                      + LinQuadReweight_cT1 )
addSampleWeight(samples,'sm_lin_quad_cT1','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) *' + LinQuadReweight_cT1 )
addSampleWeight(samples,'sm_lin_quad_cT1','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   *' + LinQuadReweight_cT1 )
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
addSampleWeight(samples,'quad_cT2','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1199 / 0.569)')
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
addSampleWeight(samples,'sm_lin_quad_cT2','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) *'                                      + LinQuadReweight_cT2 )
addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) *' + LinQuadReweight_cT2 )
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   *' + LinQuadReweight_cT2 )
addSampleWeight(samples,'sm_lin_quad_cT2','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT2','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')

########## FT5 ############
##default coupling, quadratic EFT 
samples['quad_cT5'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT5, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cT5','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1199 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT5'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cT5','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) *'                                      + LinQuadReweight_cT5 )
addSampleWeight(samples,'sm_lin_quad_cT5','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) *' + LinQuadReweight_cT5 )
addSampleWeight(samples,'sm_lin_quad_cT5','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   *' + LinQuadReweight_cT5 )
addSampleWeight(samples,'sm_lin_quad_cT5','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT5','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FT6 ############
##default coupling, quadratic EFT 
samples['quad_cT6'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT6, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cT6','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1199 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT6'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cT6','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) *'                                      + LinQuadReweight_cT6 )
addSampleWeight(samples,'sm_lin_quad_cT6','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) *' + LinQuadReweight_cT6 )
addSampleWeight(samples,'sm_lin_quad_cT6','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   *' + LinQuadReweight_cT6 )
addSampleWeight(samples,'sm_lin_quad_cT6','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT6','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FT7 ############
##default coupling, quadratic EFT 
samples['quad_cT7'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT7, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cT7','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1199 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT7'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cT7','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) *'                                      + LinQuadReweight_cT7 )
addSampleWeight(samples,'sm_lin_quad_cT7','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) *' + LinQuadReweight_cT7 )
addSampleWeight(samples,'sm_lin_quad_cT7','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   *' + LinQuadReweight_cT7 )
addSampleWeight(samples,'sm_lin_quad_cT7','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT7','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FT8 ############
##default coupling, quadratic EFT 
samples['quad_cT8'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT8, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cT8','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT8','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT8','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1199 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT8'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cT8','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) *'                                      + LinQuadReweight_cT8 )
addSampleWeight(samples,'sm_lin_quad_cT8','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) *' + LinQuadReweight_cT8 )
addSampleWeight(samples,'sm_lin_quad_cT8','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   *' + LinQuadReweight_cT8 )
addSampleWeight(samples,'sm_lin_quad_cT8','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT8','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
########## FT9 ############
##default coupling, quadratic EFT 
samples['quad_cT9'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC'),
    'weight': mcCommonWeight + '*' + quadReweight_cT9, #do we have to add reweighting for the different Wilson Coeff.?
    'FilesPerJob': 1
}
addSampleWeight(samples,'quad_cT9','ZTo2L_ZTo2J_aQGC','0.6361 / 3.361 ')
addSampleWeight(samples,'quad_cT9','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.04146 / 0.2222)')
addSampleWeight(samples,'quad_cT9','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.1199 / 0.569)')
# SM + lin + quad 
samples['sm_lin_quad_cT9'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC')
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight': mcCommonWeight, 
    'FilesPerJob': 1
}
addSampleWeight(samples,'sm_lin_quad_cT9','ZTo2L_ZTo2J_aQGC', '(0.6361 / 3.361) *'                                      + LinQuadReweight_cT9 )
addSampleWeight(samples,'sm_lin_quad_cT9','WmTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.04146 / 0.2222) *' + LinQuadReweight_cT9 )
addSampleWeight(samples,'sm_lin_quad_cT9','WpTo2J_ZTo2L_aQGC','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.1199 / 0.569)   *' + LinQuadReweight_cT9 )
addSampleWeight(samples,'sm_lin_quad_cT9','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')
addSampleWeight(samples,'sm_lin_quad_cT9','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)')




###########################################
#############  SM  SIGNALS  ###############
###########################################
    #************* sm VBS ewk with (old) global recoil option, for EFT limits *******#
samples['sm'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L') 
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 15
}
addSampleWeight(samples,'sm','ZTo2L_ZTo2J','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.01606/0.01589)')
addSampleWeight(samples,'sm','WmTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.03004/0.02982)')
addSampleWeight(samples,'sm','WpTo2J_ZTo2L','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05526/0.05401)')
    #************ sm VBS ewk with dipole recoil *********************#
samples['sm_dipole'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_dipoleRecoil') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil') 
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 15
}
addSampleWeight(samples,'sm_dipole','ZTo2L_ZTo2J_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.01606/0.01589)')
addSampleWeight(samples,'sm_dipole','WmTo2J_ZTo2L_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0) * (0.03004/0.02982)')
addSampleWeight(samples,'sm_dipole','WpTo2J_ZTo2L_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0)* (0.05526/0.05401)')


##########################################################
############   SIGNALS FOR COMBINATION  ##################
##########################################################

samples['ewk_ZZ'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_dipoleRecoil'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 7
}
######
samples['ewk_WmZ'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 7
}
addSampleWeight(samples,'ewk_WmZ','WmTo2J_ZTo2L_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0)')
#####

samples['ewk_WpZ'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 7
}
addSampleWeight(samples,'ewk_WpZ','WpTo2J_ZTo2L_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0)')



###########################################
#############  BACKGROUNDS  ###############
###########################################

######## tZq ##########

samples['tZq'] = {
        'name' : nanoGetSampleFiles(mcDirectory, 'tZq_ll'),
        'weight' : mcCommonWeight,
        'FilesPerJob': 3,
        'EventsPerJob': 50000,
        'suppressNegative' :['all'],
        'suppressNegativeNuisances' :['all'],
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
########## DY #### consider using HT binned LO mainly

ptllDYW_NLO = '(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useDYtt = False

if useDYtt:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
    'EventsPerJob' : 20000,
    }
    addSampleWeight(samples,'DY','DYJetsToTT_MuEle_M-50',ptllDYW_NLO)
    addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO',ptllDYW_LO)


else:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200_newpmx') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600_newpmx') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-100to200_newpmx') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-200to400_newpmx') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-400to600') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-4to50_HT-600toInf') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext1') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1') 


    samples['DY'] = {
        'name': files,
        'weight': (mcCommonWeight + "*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                         Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )"),#.replace("PUJetIdSF", "1."), ##DY_photons_filter 
    	'subsamples' :{
                "Resolved_2d_01" : "fit_2D_bin_Resolved==1",
               "Resolved_2d_02" : "fit_2D_bin_Resolved==2",
               "Resolved_2d_03" : "fit_2D_bin_Resolved==3",
               "Resolved_2d_04" : "fit_2D_bin_Resolved==4",
               "Resolved_2d_05" : "fit_2D_bin_Resolved==5",
               "Resolved_2d_06" : "fit_2D_bin_Resolved==6",
               "Resolved_2d_07" : "fit_2D_bin_Resolved==7",
               "Resolved_2d_08" : "fit_2D_bin_Resolved==8",
               "Resolved_2d_09" : "fit_2D_bin_Resolved==9",
               "Resolved_2d_10" : "fit_2D_bin_Resolved==10",
               "Resolved_2d_11" : "fit_2D_bin_Resolved==11",
               "Resolved_2d_12" : "fit_2D_bin_Resolved==12",
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

    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext1',                'DY_NLO_pTllrw * (LHE_HT < 100)')   
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO_ext1',         'DY_LO_pTllrw * (LHE_HT < 100)')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200_newpmx',    'DY_LO_pTllrw * 1.000')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400',           'DY_LO_pTllrw * 0.999')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600_newpmx',    'DY_LO_pTllrw * 0.990')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800',           'DY_LO_pTllrw * 0.975')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200',          'DY_LO_pTllrw * 0.907')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500',         'DY_LO_pTllrw * 0.833')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf',          'DY_LO_pTllrw * 1.015')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-100to200_newpmx', 'DY_LO_pTllrw')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-200to400_newpmx', 'DY_LO_pTllrw')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-400to600',        'DY_LO_pTllrw')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-600toInf',        'DY_LO_pTllrw')


#NB the weight ptllDYW_LO needs to be updated with DY_LO_pTllrw available in https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/patches/DYrew30.py
#and https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/master/Configurations/VBSWWOS/Full2016_v6/FitDir/samples.py#L160

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
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")

######WJets#####

files =  nanoGetSampleFiles(mcDirectory, 'WJetsToLNu-LO') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT70_100') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') + \
    nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf') 


samples['WJets'] = {
    'name': files,
    'weight': mcCommonWeight, 
    'FilesPerJob': 6,
    'EventsPerJob' : 70000,
}

addSampleWeight(samples,'WJets', 'WJetsToLNu-LO', '(LHE_HT < 70)')
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT100_200', '0.993') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT200_400', '1.002') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT400_600', '1.009') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT600_800', '1.120') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT800_1200', '1.202') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT1200_2500', '1.332') 
addSampleWeight(samples,'WJets', 'WJetsToLNu-HT2500_inf', '4.200') 


###### WW e ggWW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop'),
    'weight': mcCommonWeight, #+ '*nllW',
    'FilesPerJob': 6
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
    'FilesPerJob': 4
}
######## Vg ########

samples['Vg']  = {  'name'   :   nanoGetSampleFiles(mcDirectory,'Wg_MADGRAPHMLM')
                               + nanoGetSampleFiles(mcDirectory,'ZGToLLG'),
                    'weight' : mcCommonWeightNoMatch +'*(Gen_ZGstar_mass <= 0)',
                    'FilesPerJob' : 6,
                    'EventsPerJob' : 70000,
                    'suppressNegative' :['all'],
                    'suppressNegativeNuisances' :['all'],
                  }
#the following baseW correction is needed in v5 and should be removed in v6
#addSampleWeight(samples,'Vg','ZGToLLG','0.448')


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
#0.448 needed in v5 and should be removed in v6
addSampleWeight(samples,'VgS','ZGToLLG', '(Gen_ZGstar_mass > 0)') #*0.448
addSampleWeight(samples,'VgS','WZTo3LNu_mllmin01', '(Gen_ZGstar_mass > 0.1)')

############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 2,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
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
    'FilesPerJob': 4
}


########VBF-V##########

files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50_newpmx')

samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6
}
 
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

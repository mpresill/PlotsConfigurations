
import os 
import inspect

with open('/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/EFT/ReweightFactory/SMEFT_dim6_dictionary.py') as f:
    code = compile(f.read(), 'SMEFT_dim6_dictionary.py', 'exec')
    exec(code)

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


########################################
#######       EFT sample        ########
########################################
smReweight = '( LHEReweightingWeight[0] )'
  #*******************#      sm from reweighting
samples['sm'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 10
} 
addSampleWeight(samples,'sm','ZTo2E_ZTo2J_SMEFT',                                              smReweight)
addSampleWeight(samples,'sm','ZTo2Mu_ZTo2J_SMEFT',                                             smReweight)
addSampleWeight(samples,'sm','ZTo2Tau_ZTo2J_SMEFT',                                            smReweight)
addSampleWeight(samples,'sm','WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
addSampleWeight(samples,'sm','WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)

for operator, expressions in operators.items():
    quadReweight = expressions['quadReweight']
    LinReweight = expressions['LinReweight']
     #*******************#      sm+linear+quadratic
    samples['sm_lin_quad_'+operator] = {
        'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 10
    } 
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2E_ZTo2J_SMEFT',                                              smReweight + '+' + LinReweight + '+' + quadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2Mu_ZTo2J_SMEFT',                                             smReweight + '+' + LinReweight + '+' + quadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2Tau_ZTo2J_SMEFT',                                            smReweight + '+' + LinReweight + '+' + quadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smReweight + '+' + LinReweight + '+' + quadReweight + ')')
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smReweight + '+' + LinReweight + '+' + quadReweight + ')')
     #*******************#      quadratic only
    samples['quad_'+operator] = {
        'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 10
    } 
    addSampleWeight(samples,'quad_'+operator,'ZTo2E_ZTo2J_SMEFT',                                              quadReweight)
    addSampleWeight(samples,'quad_'+operator,'ZTo2Mu_ZTo2J_SMEFT',                                             quadReweight)
    addSampleWeight(samples,'quad_'+operator,'ZTo2Tau_ZTo2J_SMEFT',                                            quadReweight)
    addSampleWeight(samples,'quad_'+operator,'WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
    addSampleWeight(samples,'quad_'+operator,'WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
     #**********************************************************************************#      


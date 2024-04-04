
import os
import inspect
# Import the operators dictionary from EFT_dict.py
# Execute the contents of EFT_dim8_dictionary.py, please update the path according to your exigency 
with open('/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/EFT/EFT_dim8_dictionary.py') as f:
    code = compile(f.read(), 'EFT_dim8_dictionary.py', 'exec')
    exec(code)

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




 #************          EFT samples       ************#
 #++++++ these are the centrally produced samples ++++#
for operator, expressions in operators.items():
    # Adding the quadratic sample for each operator:
    samples['quad_'+operator] = {
        'name':  nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
                 + nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
                 + nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 10
    }
    
    quadReweight = expressions['quadReweight']
    
    addSampleWeight(samples, 'quad_'+operator, 'ZTo2L_ZTo2J_aQGC_eboliv2_official', quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WmTo2J_ZTo2L_aQGC_eboliv2_official', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WpTo2J_ZTo2L_aQGC_eboliv2_official', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)

    # Adding sm_lin_quad sample for each operator:
    smLinQuadReweight = expressions['sm'] + expressions['LinReweight'] + expressions['quadReweight']
    samples['sm_lin_quad_'+operator] = {
        'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
                 + nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
                 + nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 10
    }
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2L_ZTo2J_aQGC_eboliv2_official', smLinQuadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight)




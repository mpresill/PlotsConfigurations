
import os 
import inspect
# Import the operators dictionary from EFT_dict.py
# Execute the contents of EFT_dim8_dictionary.py, please update the path according to your exigency 
with open('/afs/cern.ch/work/m/mpresill/Latino/CMSSW_10_6_4/src/PlotsConfigurations/Configurations/VBS_ZV/EFT/ReweightFactory/EFT_dim8_dictionary_v2.py') as f:
    code = compile(f.read(), 'EFT_dim8_dictionary_v2.py', 'exec')
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

DirectorySMPeos_v2 =     '/eos/cms/store/group/phys_smp/ec/Latinos/HWWNano/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

DirectoryUSEReos = '/eos/user/m/mpresill/www/VBS/nAOD/Autumn18_102X_nAODv7_Full2018v7/MCl1loose2018v7__MCCorr2018v7__l2loose__l2tightOR2018v7'

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

 #************          EFT samples       ************#
 #++++++++ sm from EWK sample ++++++++#
smReweight = operators['cS0']['sm']
samples['sm'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos_v2, 'ZTo2L_ZTo2J_aQGC_Aug2024') 
             +nanoGetSampleFiles(DirectorySMPeos_v2, 'WmTo2J_ZTo2L_aQGC_Aug2024') 
             +nanoGetSampleFiles(DirectorySMPeos_v2, 'WpTo2J_ZTo2L_aQGC_Aug2024'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 12
}

addSampleWeight(samples, 'sm', 'ZTo2L_ZTo2J_aQGC_Aug2024', smReweight)
addSampleWeight(samples, 'sm', 'WmTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
addSampleWeight(samples, 'sm', 'WpTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)

 #************          EFT samples       ************#
 #++++++ these are the centrally produced samples ++++#
for operator, expressions in operators.items():
    # Adding the quadratic sample for each operator:
    samples['quad_'+operator] = {
        'name':  nanoGetSampleFiles(DirectorySMPeos_v2,   'ZTo2L_ZTo2J_aQGC_Aug2024') 
                 + nanoGetSampleFiles(DirectorySMPeos_v2, 'WmTo2J_ZTo2L_aQGC_Aug2024') 
                 + nanoGetSampleFiles(DirectorySMPeos_v2, 'WpTo2J_ZTo2L_aQGC_Aug2024'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 12
        #'EventsPerJob': 100000,
    }
    
    quadReweight = expressions['quadReweight']
    
    addSampleWeight(samples, 'quad_'+operator, 'ZTo2L_ZTo2J_aQGC_Aug2024', quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WmTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WpTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)


    # Adding sm_lin_quad sample for each operator:
    LinReweight = expressions['LinReweight']
    samples['sm_lin_quad_'+operator] = {
        'name':   nanoGetSampleFiles(DirectorySMPeos_v2, 'ZTo2L_ZTo2J_aQGC_Aug2024') 
                 + nanoGetSampleFiles(DirectorySMPeos_v2, 'WmTo2J_ZTo2L_aQGC_Aug2024') 
                 + nanoGetSampleFiles(DirectorySMPeos_v2, 'WpTo2J_ZTo2L_aQGC_Aug2024'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 12
    }
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2L_ZTo2J_aQGC_Aug2024', smReweight + '+' + LinReweight + '+' + quadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WmTo2J_ZTo2L_aQGC_Aug2024','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smReweight + '+' + LinReweight + '+' + quadReweight + ')')
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WpTo2J_ZTo2L_aQGC_Aug2024','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smReweight + '+' + LinReweight + '+' + quadReweight + ')')



#samples['zz_sm'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_dipoleRecoil'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#
# #++++++ these are the centrally produced samples ++++#
#for operator, expressions in operators.items():
#    # Adding the quadratic sample for each operator:
#    samples['zz_quad_'+operator] = {
#        'name':  nanoGetSampleFiles(DirectoryUSEReos, 'ZTo2L_ZTo2J_aQGC_Aug2024'),
#        'weight':  mcCommonWeight,
#        'FilesPerJob': 10
#    }
#    
#    quadReweight = expressions['quadReweight']
#    
#    addSampleWeight(samples, 'zz_quad_'+operator, 'ZTo2L_ZTo2J_aQGC_Aug2024', quadReweight)
#
#
#    # Adding sm sample for each operator:
#    smReweight = expressions['sm']
#    samples['zz_sm_'+operator] = {
#        'name':   nanoGetSampleFiles(DirectoryUSEReos, 'ZTo2L_ZTo2J_aQGC_Aug2024'),
#        'weight':  mcCommonWeight,
#        'FilesPerJob': 10
#    }
#    addSampleWeight(samples,'zz_sm_'+operator,'ZTo2L_ZTo2J_aQGC_Aug2024', smReweight)
#
#
#    # Adding sm_lin_quad sample for each operator:
#    LinReweight = expressions['LinReweight']
#    samples['zz_sm_lin_quad_'+operator] = {
#        'name':   nanoGetSampleFiles(DirectoryUSEReos, 'ZTo2L_ZTo2J_aQGC_Aug2024'),
#        'weight':  mcCommonWeight,
#        'FilesPerJob': 10
#    }
#    addSampleWeight(samples,'zz_sm_lin_quad_'+operator,'ZTo2L_ZTo2J_aQGC_Aug2024', smReweight + '+' + LinReweight + '+' + quadReweight)


##************          EFT samples       ************#
##++++++++ sm from EWK sample ++++++++#
#amples['wp_sm'] = {
#   'name':   nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_dipoleRecoil'),
#   'weight':  mcCommonWeight,
#   'FilesPerJob': 10
#
#ddSampleWeight(samples,'wp_sm','WpTo2J_ZTo2L_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0)')
#
##++++++ these are the centrally produced samples ++++#
#or operator, expressions in operators.items():
#   # Adding the quadratic sample for each operator:
#   samples['wp_quad_'+operator] = {
#       'name':  nanoGetSampleFiles(DirectoryUSEReos, 'WpTo2J_ZTo2L_aQGC_Aug2024'),
#       'weight':  mcCommonWeight,
#       'FilesPerJob': 10
#   }
#   
#   quadReweight = expressions['quadReweight']
#   
#   addSampleWeight(samples, 'wp_quad_'+operator, 'WpTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
#
#
#   # Adding sm sample for each operator:
#   smReweight = expressions['sm']
#   samples['wp_sm_'+operator] = {
#       'name':   nanoGetSampleFiles(DirectoryUSEReos, 'WpTo2J_ZTo2L_aQGC_Aug2024'),
#       'weight':  mcCommonWeight,
#       'FilesPerJob': 10
#   }
#   addSampleWeight(samples,'wp_sm_'+operator,'WpTo2J_ZTo2L_aQGC_Aug2024','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
#
#
#   # Adding sm_lin_quad sample for each operator:
#   LinReweight = expressions['LinReweight']
#   samples['wp_sm_lin_quad_'+operator] = {
#       'name':   nanoGetSampleFiles(DirectoryUSEReos, 'WpTo2J_ZTo2L_aQGC_Aug2024'),
#       'weight':  mcCommonWeight,
#       'FilesPerJob': 10
#   }
#   addSampleWeight(samples,'wp_sm_lin_quad_'+operator,'WpTo2J_ZTo2L_aQGC_Aug2024','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smReweight + '+' + LinReweight + '+' + quadReweight + ')')
#
#
#
##************          EFT samples       ************#
##++++++++ sm from EWK sample ++++++++#
#amples['wm_sm'] = {
#   'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil'),
#   'weight':  mcCommonWeight,
#   'FilesPerJob': 10
#
#ddSampleWeight(samples,'wm_sm','WmTo2J_ZTo2L_dipoleRecoil','(Sum$(abs(GenPart_pdgId)==6)==0)')
#
##++++++ these are the centrally produced samples ++++#
#or operator, expressions in operators.items():
#   # Adding the quadratic sample for each operator:
#   samples['wm_quad_'+operator] = {
#       'name':  nanoGetSampleFiles(DirectoryUSEReos, 'WmTo2J_ZTo2L_aQGC_Aug2024'),
#       'weight':  mcCommonWeight,
#       'FilesPerJob': 10
#   }
#   
#   quadReweight = expressions['quadReweight']
#   
#   addSampleWeight(samples, 'wm_quad_'+operator, 'WmTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
#
#
#   # Adding sm sample for each operator:
#   smReweight = expressions['sm']
#   samples['wm_sm_'+operator] = {
#       'name':   nanoGetSampleFiles(DirectoryUSEReos, 'WmTo2J_ZTo2L_aQGC_Aug2024'),
#       'weight':  mcCommonWeight,
#       'FilesPerJob': 10
#   }
#   addSampleWeight(samples,'wm_sm_'+operator,'WmTo2J_ZTo2L_aQGC_Aug2024','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smReweight)
#
#
#   # Adding sm_lin_quad sample for each operator:
#   LinReweight = expressions['LinReweight']
#   samples['wm_sm_lin_quad_'+operator] = {
#       'name':   nanoGetSampleFiles(DirectoryUSEReos, 'WmTo2J_ZTo2L_aQGC_Aug2024'),
#       'weight':  mcCommonWeight,
#       'FilesPerJob': 10
#   }
#   addSampleWeight(samples,'wm_sm_lin_quad_'+operator,'WmTo2J_ZTo2L_aQGC_Aug2024','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smReweight + '+' + LinReweight + '+' + quadReweight + ')')


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


########################################
#######       EFT weights       ########
########################################
### cW
smRew = '( LHEReweightingWeight[0] )'
######
operators = {
    'cW': {
        'LinReweight': '( 0.5 * (1/(0.2)) * ( LHEReweightingWeight[2] - LHEReweightingWeight[1] ))',
        'quadReweight': '( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0]))'
    },
    'cHWB': {
        'LinReweight': '( 0.5 * (1/(1)) * ( LHEReweightingWeight[4] - LHEReweightingWeight[3] ))',
        'quadReweight': '( 0.5 * (1/(1)) * (1/(1)) * ( LHEReweightingWeight[4] + LHEReweightingWeight[3] - 2 * LHEReweightingWeight[0]))'
    },
    'cHbox': {
        'LinReweight': '( 0.5 * (1/(1)) * ( LHEReweightingWeight[6] - LHEReweightingWeight[5] ))',
        'quadReweight': '( 0.5 * (1/(1)) * (1/(1)) * ( LHEReweightingWeight[6] + LHEReweightingWeight[5] - 2 * LHEReweightingWeight[0]))'
    },
    'cHW': {
        'LinReweight': '( 0.5 * (1/(1)) * ( LHEReweightingWeight[8] - LHEReweightingWeight[7] ))',
        'quadReweight': '( 0.5 * (1/(1)) * (1/(1)) * ( LHEReweightingWeight[8] + LHEReweightingWeight[7] - 2 * LHEReweightingWeight[0]))'
    },
    'cHl1': {
        'LinReweight': '( 0.5 * (1/(1)) * ( LHEReweightingWeight[10] - LHEReweightingWeight[9] ))',
        'quadReweight': '( 0.5 * (1/(1)) * (1/(1)) * ( LHEReweightingWeight[10] + LHEReweightingWeight[9] - 2 * LHEReweightingWeight[0]))'
    },
    'cHB': {
        'LinReweight': '( 0.5 * (1/(1)) * ( LHEReweightingWeight[12] - LHEReweightingWeight[11] ))',
        'quadReweight': '( 0.5 * (1/(1)) * (1/(1)) * ( LHEReweightingWeight[12] + LHEReweightingWeight[11] - 2 * LHEReweightingWeight[0]))'
    },
    'cHQ1': {
        'LinReweight': '( 0.5 * (1/(1)) * ( LHEReweightingWeight[14] - LHEReweightingWeight[13] ))',
        'quadReweight': '( 0.5 * (1/(1)) * (1/(1)) * ( LHEReweightingWeight[14] + LHEReweightingWeight[13] - 2 * LHEReweightingWeight[0]))'
    },
    'cHj1': {
        'LinReweight': '( 0.5 * (1/(1)) * ( LHEReweightingWeight[16] - LHEReweightingWeight[15] ))',
        'quadReweight': '( 0.5 * (1/(1)) * (1/(1)) * ( LHEReweightingWeight[16] + LHEReweightingWeight[15] - 2 * LHEReweightingWeight[0]))'
    }
}

 #************ EFT samples ************#
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
addSampleWeight(samples,'sm','ZTo2E_ZTo2J_SMEFT',                                              smRew)
addSampleWeight(samples,'sm','ZTo2Mu_ZTo2J_SMEFT',                                             smRew)
addSampleWeight(samples,'sm','ZTo2Tau_ZTo2J_SMEFT',                                            smRew)
addSampleWeight(samples,'sm','WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smRew)
addSampleWeight(samples,'sm','WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smRew)

 #**********************************************************************************#      
for operator, expressions in operators.items():
    # Adding the quadratic sample for each operator:
    samples['quad_'+operator] = {
        'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 12
        #'EventsPerJob': 100000,
    }
    
    quadReweight = expressions['quadReweight']

    addSampleWeight(samples,'quad_'+operator,'ZTo2E_ZTo2J_SMEFT',                                              quadReweight)
    addSampleWeight(samples,'quad_'+operator,'ZTo2Mu_ZTo2J_SMEFT',                                             quadReweight)
    addSampleWeight(samples,'quad_'+operator,'ZTo2Tau_ZTo2J_SMEFT',                                            quadReweight)
    addSampleWeight(samples,'quad_'+operator,'WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
    addSampleWeight(samples,'quad_'+operator,'WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
    

    # Adding sm_lin_quad sample for each operator:
    LinReweight = expressions['LinReweight']
    samples['sm_lin_quad_'+operator] = {
        'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
                 +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 12
    }
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2E_ZTo2J_SMEFT',                                              smRew + '+' + LinReweight + '+' + quadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2Mu_ZTo2J_SMEFT',                                             smRew + '+' + LinReweight + '+' + quadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'ZTo2Tau_ZTo2J_SMEFT',                                            smRew + '+' + LinReweight + '+' + quadReweight)
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smRew + '+' + LinReweight + '+' + quadReweight + ')')
    addSampleWeight(samples,'sm_lin_quad_'+operator,'WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ '(' + smRew + '+' + LinReweight + '+' + quadReweight + ')')

###### mixed operators
#Rw_sm_lin_quad_mixed_cW_cHWB = '( LHEReweightingWeight[17] )'
#samples['sm_lin_quad_mixed_cW_cHWB'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT') 
#                +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT') 
#                +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT') 
#                +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT') 
#                +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 12
#}
#addSampleWeight(samples,'sm_lin_quad_mixed_cW_cHWB','ZTo2E_ZTo2J_SMEFT',                                              Rw_sm_lin_quad_mixed_cW_cHWB )
#addSampleWeight(samples,'sm_lin_quad_mixed_cW_cHWB','ZTo2Mu_ZTo2J_SMEFT',                                             Rw_sm_lin_quad_mixed_cW_cHWB )
#addSampleWeight(samples,'sm_lin_quad_mixed_cW_cHWB','ZTo2Tau_ZTo2J_SMEFT',                                            Rw_sm_lin_quad_mixed_cW_cHWB )
#addSampleWeight(samples,'sm_lin_quad_mixed_cW_cHWB','WmTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ Rw_sm_lin_quad_mixed_cW_cHWB)
#addSampleWeight(samples,'sm_lin_quad_mixed_cW_cHWB','WpTo2J_ZTo2L_SMEFT',       '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ Rw_sm_lin_quad_mixed_cW_cHWB)
# Define the reweighting weights
#Rw_sm_lin_quad_mixed_cW_cHWB = '( LHEReweightingWeight[17] )'
#Rw_sm_lin_quad_mixed_cW_cHbox = '( LHEReweightingWeight[18] )'
#Rw_sm_lin_quad_mixed_cW_cHW = '( LHEReweightingWeight[19] )'
#Rw_sm_lin_quad_mixed_cW_cHl1 = '( LHEReweightingWeight[20] )'
#Rw_sm_lin_quad_mixed_cW_cHB = '( LHEReweightingWeight[21] )'
#Rw_sm_lin_quad_mixed_cW_cHQ1 = '( LHEReweightingWeight[22] )'
#Rw_sm_lin_quad_mixed_cW_cHj1 = '( LHEReweightingWeight[23] )'
##### mixed terms for combine when containing cWs (for some reason set to 0.2 in the mixed reweighting cards) are obtained from the following formula:
#####   ( LHEReweightingWeight[mixed] + sm+lin+quad[second operator] * (cW - 1) + quad[cW] * (cW - cW^2) ) / cW
Rw_sm_lin_quad_mixed_cW_cHWB = '( ( LHEReweightingWeight[17] + (0.2 - 1) * ( LHEReweightingWeight[4] )  + (0.2 - (0.2 * 0.2)) * ( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0])) ) * (1/0.2) )'
Rw_sm_lin_quad_mixed_cW_cHbox = '( ( LHEReweightingWeight[18] + (0.2 - 1) * ( LHEReweightingWeight[6] )  + (0.2 - (0.2 * 0.2)) * ( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0])) ) * (1/0.2) )'
Rw_sm_lin_quad_mixed_cW_cHW = '( ( LHEReweightingWeight[19] + (0.2 - 1) * ( LHEReweightingWeight[8] )  + (0.2 - (0.2 * 0.2)) * ( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0])) ) * (1/0.2) )'
Rw_sm_lin_quad_mixed_cW_cHl1 = '( ( LHEReweightingWeight[20] + (0.2 - 1) * ( LHEReweightingWeight[10] )  + (0.2 - (0.2 * 0.2)) * ( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0])) ) * (1/0.2) )'
Rw_sm_lin_quad_mixed_cW_cHB = '( ( LHEReweightingWeight[21] + (0.2 - 1) * ( LHEReweightingWeight[12] )  + (0.2 - (0.2 * 0.2)) * ( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0])) ) * (1/0.2) )'
Rw_sm_lin_quad_mixed_cW_cHQ1 = '( ( LHEReweightingWeight[22] + (0.2 - 1) * ( LHEReweightingWeight[14] )  + (0.2 - (0.2 * 0.2)) * ( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0])) ) * (1/0.2) )'
Rw_sm_lin_quad_mixed_cW_cHj1 = '( ( LHEReweightingWeight[23] + (0.2 - 1) * ( LHEReweightingWeight[16] )  + (0.2 - (0.2 * 0.2)) * ( 0.5 * (1/(0.2)) * (1/(0.2)) * ( LHEReweightingWeight[2] + LHEReweightingWeight[1] - 2 * LHEReweightingWeight[0])) ) * (1/0.2) )'
Rw_sm_lin_quad_mixed_cHWB_cHbox = '( LHEReweightingWeight[24] )'
Rw_sm_lin_quad_mixed_cHWB_cHW = '( LHEReweightingWeight[25] )'
Rw_sm_lin_quad_mixed_cHWB_cHl1 = '( LHEReweightingWeight[26] )'
Rw_sm_lin_quad_mixed_cHWB_cHB = '( LHEReweightingWeight[27] )'
Rw_sm_lin_quad_mixed_cHWB_cHQ1 = '( LHEReweightingWeight[28] )'
Rw_sm_lin_quad_mixed_cHWB_cHj1 = '( LHEReweightingWeight[29] )'
Rw_sm_lin_quad_mixed_cHbox_cHW = '( LHEReweightingWeight[30] )'
Rw_sm_lin_quad_mixed_cHbox_cHl1 = '( LHEReweightingWeight[31] )'
Rw_sm_lin_quad_mixed_cHbox_cHB = '( LHEReweightingWeight[32] )'
Rw_sm_lin_quad_mixed_cHbox_cHQ1 = '( LHEReweightingWeight[33] )'
Rw_sm_lin_quad_mixed_cHbox_cHj1 = '( LHEReweightingWeight[34] )'
Rw_sm_lin_quad_mixed_cHW_cHl1 = '( LHEReweightingWeight[35] )'
Rw_sm_lin_quad_mixed_cHW_cHB = '( LHEReweightingWeight[36] )'
Rw_sm_lin_quad_mixed_cHW_cHQ1 = '( LHEReweightingWeight[37] )'
Rw_sm_lin_quad_mixed_cHW_cHj1 = '( LHEReweightingWeight[38] )'
Rw_sm_lin_quad_mixed_cHl1_cHB = '( LHEReweightingWeight[39] )'
Rw_sm_lin_quad_mixed_cHl1_cHQ1 = '( LHEReweightingWeight[40] )'
Rw_sm_lin_quad_mixed_cHl1_cHj1 = '( LHEReweightingWeight[41] )'
Rw_sm_lin_quad_mixed_cHB_cHQ1 = '( LHEReweightingWeight[42] )'
Rw_sm_lin_quad_mixed_cHB_cHj1 = '( LHEReweightingWeight[43] )'
Rw_sm_lin_quad_mixed_cHQ1_cHj1 = '( LHEReweightingWeight[44] )'

# Loop through the combinations to define samples
weight_map = {
    'sm_lin_quad_mixed_cW_cHWB': Rw_sm_lin_quad_mixed_cW_cHWB,
    'sm_lin_quad_mixed_cW_cHbox': Rw_sm_lin_quad_mixed_cW_cHbox,
    'sm_lin_quad_mixed_cW_cHW': Rw_sm_lin_quad_mixed_cW_cHW,
    'sm_lin_quad_mixed_cW_cHl1': Rw_sm_lin_quad_mixed_cW_cHl1,
    'sm_lin_quad_mixed_cW_cHB': Rw_sm_lin_quad_mixed_cW_cHB,
    'sm_lin_quad_mixed_cW_cHQ1': Rw_sm_lin_quad_mixed_cW_cHQ1,
    'sm_lin_quad_mixed_cW_cHj1': Rw_sm_lin_quad_mixed_cW_cHj1,
    'sm_lin_quad_mixed_cHWB_cHbox': Rw_sm_lin_quad_mixed_cHWB_cHbox,
    'sm_lin_quad_mixed_cHWB_cHW': Rw_sm_lin_quad_mixed_cHWB_cHW,
    'sm_lin_quad_mixed_cHWB_cHl1': Rw_sm_lin_quad_mixed_cHWB_cHl1,
    'sm_lin_quad_mixed_cHWB_cHB': Rw_sm_lin_quad_mixed_cHWB_cHB,
    'sm_lin_quad_mixed_cHWB_cHQ1': Rw_sm_lin_quad_mixed_cHWB_cHQ1,
    'sm_lin_quad_mixed_cHWB_cHj1': Rw_sm_lin_quad_mixed_cHWB_cHj1,
    'sm_lin_quad_mixed_cHbox_cHW': Rw_sm_lin_quad_mixed_cHbox_cHW,
    'sm_lin_quad_mixed_cHbox_cHl1': Rw_sm_lin_quad_mixed_cHbox_cHl1,
    'sm_lin_quad_mixed_cHbox_cHB': Rw_sm_lin_quad_mixed_cHbox_cHB,
    'sm_lin_quad_mixed_cHbox_cHQ1': Rw_sm_lin_quad_mixed_cHbox_cHQ1,
    'sm_lin_quad_mixed_cHbox_cHj1': Rw_sm_lin_quad_mixed_cHbox_cHj1,
    'sm_lin_quad_mixed_cHW_cHl1': Rw_sm_lin_quad_mixed_cHW_cHl1,
    'sm_lin_quad_mixed_cHW_cHB': Rw_sm_lin_quad_mixed_cHW_cHB,
    'sm_lin_quad_mixed_cHW_cHQ1': Rw_sm_lin_quad_mixed_cHW_cHQ1,
    'sm_lin_quad_mixed_cHW_cHj1': Rw_sm_lin_quad_mixed_cHW_cHj1,
    'sm_lin_quad_mixed_cHl1_cHB': Rw_sm_lin_quad_mixed_cHl1_cHB,
    'sm_lin_quad_mixed_cHl1_cHQ1': Rw_sm_lin_quad_mixed_cHl1_cHQ1,
    'sm_lin_quad_mixed_cHl1_cHj1': Rw_sm_lin_quad_mixed_cHl1_cHj1,
    'sm_lin_quad_mixed_cHB_cHQ1': Rw_sm_lin_quad_mixed_cHB_cHQ1,
    'sm_lin_quad_mixed_cHB_cHj1': Rw_sm_lin_quad_mixed_cHB_cHj1,
    'sm_lin_quad_mixed_cHQ1_cHj1': Rw_sm_lin_quad_mixed_cHQ1_cHj1
}

for sample_name, reweighting_weight in weight_map.items():
    samples[sample_name] = {
        'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2E_ZTo2J_SMEFT')
                    +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Mu_ZTo2J_SMEFT')
                    +nanoGetSampleFiles(DirectorySMPeos, 'ZTo2Tau_ZTo2J_SMEFT')
                    +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_SMEFT')
                    +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_SMEFT'),
        'weight':  mcCommonWeight,
        'FilesPerJob': 12
    }

    addSampleWeight(samples, sample_name, 'ZTo2E_ZTo2J_SMEFT', reweighting_weight)
    addSampleWeight(samples, sample_name, 'ZTo2Mu_ZTo2J_SMEFT', reweighting_weight)
    addSampleWeight(samples, sample_name, 'ZTo2Tau_ZTo2J_SMEFT', reweighting_weight)
    addSampleWeight(samples, sample_name, 'WmTo2J_ZTo2L_SMEFT', '(Sum$(abs(GenPart_pdgId)==6)==0) *' + reweighting_weight)
    addSampleWeight(samples, sample_name, 'WpTo2J_ZTo2L_SMEFT', '(Sum$(abs(GenPart_pdgId)==6)==0) *' + reweighting_weight)

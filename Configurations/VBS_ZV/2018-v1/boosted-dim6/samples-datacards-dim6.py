
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
#######       EFT samples       ########
########################################
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
 #**********************************************************************************#      



###########################################
#############  BACKGROUNDS  ###############
###########################################

############## tZq  
#changed tZq to specific bkg

#tZq from sm ewk sample
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
#    'EventsPerJob' : 70000,
}

########VBF-V##########

files =nanoGetSampleFiles(mcDirectory, 'WLNuJJ_EWK') + \
    nanoGetSampleFiles(mcDirectory, 'EWKZ2Jets_ZToLL_M-50')

samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6
}

###### DY #######

files = nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-100to200') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-200to400') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-400to600') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-600to800') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-800to1200') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-1200to2500') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_HT-2500toInf') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50_ext2') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO') + \
    nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1')


samples['DY'] = {
    'name': files,
    'weight': mcCommonWeight + "*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                        Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )",
    'FilesPerJob': 1,
    'subsamples' :{
        "Boosted_Z_1":'fit_Z_bin_Boosted==1',
        "Boosted_Z_2":'fit_Z_bin_Boosted==2',
        "Boosted_Z_3":'fit_Z_bin_Boosted==3',
        "Boosted_Z_4":'fit_Z_bin_Boosted==4',
        "Boosted_Z_5":'fit_Z_bin_Boosted==5',
        #"Resolved_2d_01" : "fit_2D_bin_Resolved==1",
        #"Resolved_2d_02" : "fit_2D_bin_Resolved==2",
        #"Resolved_2d_03" : "fit_2D_bin_Resolved==3",
        #"Resolved_2d_04" : "fit_2D_bin_Resolved==4",
        #"Resolved_2d_05" : "fit_2D_bin_Resolved==5",
        #"Resolved_2d_06" : "fit_2D_bin_Resolved==6",
        #"Resolved_2d_07" : "fit_2D_bin_Resolved==7",
        #"Resolved_2d_08" : "fit_2D_bin_Resolved==8",
        #"Resolved_2d_09" : "fit_2D_bin_Resolved==9",
        #"Resolved_2d_10" : "fit_2D_bin_Resolved==10",
        #"Resolved_2d_11" : "fit_2D_bin_Resolved==11",
        #"Resolved_2d_12" : "fit_2D_bin_Resolved==12",
    },
    'FilesPerJob': 3,
    'EventsPerJob' : 50000,
}
CombineBaseW(samples, 'DY', ['DYJetsToLL_M-10to50-LO','DYJetsToLL_M-10to50-LO_ext1']) #this is to maximize statistics for this inclusive

addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext2', '(LHE_HT < 100)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO', '(LHE_HT < 100)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO_ext1', '(LHE_HT < 100)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200',  '1.000')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400',  '0.999')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600',  '0.990')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800',  '0.975')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200',  '0.907')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500',  '0.833')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf',  '1.015')



###### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop_ext1') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top_ext1') + \
    nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic') + \
    nanoGetSampleFiles(mcDirectory,'TTZjets') + \
    nanoGetSampleFiles(mcDirectory,'TTWjets')


samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
    'EventsPerJob' : 50000,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
}

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','ST_t-channel_top_ext1',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
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

############ other backgrounds ############
samples['other'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT70_100') + \
        	nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf') + \
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
            nanoGetSampleFiles(mcDirectory, 'WpWmJJ_EWK') + \
            nanoGetSampleFiles(mcDirectory, 'WpWpJJ_QCD') + \
            nanoGetSampleFiles(mcDirectory, 'WpWpJJ_EWK') + \
            nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu_ext2') + \
            nanoGetSampleFiles(mcDirectory, 'ZZTo4L_ext2') + \
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

#addSampleWeight(samples,'other', 'WJetsToLNu-LO', '(LHE_HT < 70)') #not present in 2018
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
addSampleWeight(samples,'other','ZZTo2L2Nu_ext2',  "1.11")
addSampleWeight(samples,'other','ZZTo4L_ext2',  "1.11")



###########################################
################## FAKE ###################
###########################################

samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 50
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))



##########################################
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




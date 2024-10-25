
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
DirectorySMPeos_v2 =     '/eos/cms/store/group/phys_smp/ec/Latinos/HWWNano/Summer16_102X_nAODv7_Full2016v7/MCl1loose2016v7__MCCorr2016v7__l2loose__l2tightOR2016v7'


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


##############      centrally produced samples
#samples['sm'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#
#addSampleWeight(samples,'sm','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       sm_cT0)
#addSampleWeight(samples,'sm','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
#addSampleWeight(samples,'sm','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ sm_cT0)
# #*******************#      sm+linear+quadratic
#
#samples['sm_lin_quad_cT0'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'sm_lin_quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       smLinQuadReweight_cT0)
#addSampleWeight(samples,'sm_lin_quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
#addSampleWeight(samples,'sm_lin_quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ smLinQuadReweight_cT0)
# #*******************#      quadratic only
#samples['quad_cT0'] = {
#    'name':   nanoGetSampleFiles(DirectorySMPeos, 'ZTo2L_ZTo2J_aQGC_eboliv2_official') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_aQGC_eboliv2_official') 
#             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_aQGC_eboliv2_official'),
#    'weight':  mcCommonWeight,
#    'FilesPerJob': 10
#}
#addSampleWeight(samples,'quad_cT0','ZTo2L_ZTo2J_aQGC_eboliv2_official',                                       quadReweight_cT0)
#addSampleWeight(samples,'quad_cT0','WmTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
#addSampleWeight(samples,'quad_cT0','WpTo2J_ZTo2L_aQGC_eboliv2_official','(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight_cT0)
 #************          EFT samples       ************#
 #++++++++ sm from EWK sample ++++++++#
smReweight = operators['cS0']['sm']
samples['sm'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos_v2, 'ZTo2L_ZTo2J_aQGC_Aug2024') 
             +nanoGetSampleFiles(DirectorySMPeos_v2, 'WmTo2J_ZTo2L_aQGC_Aug2024') 
             +nanoGetSampleFiles(DirectorySMPeos_v2, 'WpTo2J_ZTo2L_aQGC_Aug2024'),
    'weight':  mcCommonWeight,
    #'EventsPerJob': 100000,
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
    }
    
    quadReweight = expressions['quadReweight']
    
    addSampleWeight(samples, 'quad_'+operator, 'ZTo2L_ZTo2J_aQGC_Aug2024', quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WmTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)
    addSampleWeight(samples, 'quad_'+operator, 'WpTo2J_ZTo2L_aQGC_Aug2024', '(Sum$(abs(GenPart_pdgId)==6)==0) *'+ quadReweight)


    # Adding sm_lin_quad sample for each operator:
    #smReweight = expressions['sm']
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




###########################################
#############  BACKGROUNDS  ###############
###########################################
######## irreducible VBS QCD  #####
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
    'FilesPerJob': 10,
    'EventsPerJob': 70000
}

########VBF-V##########
files =nanoGetSampleFiles(mcDirectory, 'EWK_LLJJ_MLL-50_MJJ-120')

samples['VBF-V'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 6,
    'EventsPerJob' : 70000,
}

######## tZq ##########
#tZq from sm ewk sample
samples['tZq'] = {
    'name':   nanoGetSampleFiles(DirectorySMPeos, 'WmTo2J_ZTo2L_dipoleRecoil') 
             +nanoGetSampleFiles(DirectorySMPeos, 'WpTo2J_ZTo2L_dipoleRecoil'),
    'weight':  mcCommonWeight+'*(Sum$(abs(GenPart_pdgId)==6)!=0)',
    'FilesPerJob': 10
}


###### DY #######

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
        'FilesPerJob': 5,
	    'subsamples' : {
	    	"bin1" :  '(Zleppt > 0 && Zleppt <=75)',
	    	"bin2" :  '(Zleppt > 75 && Zleppt <= 150)',
	    	"bin3" :  '(Zleppt > 150 && Zleppt <= 250)',
	    	"bin4" :  '(Zleppt > 250 && Zleppt <= 400)',
	    	"bin5" :  '(Zleppt > 400)',
	    }
    }
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_ext2', '(LHE_HT < 70)')
addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO', '(LHE_HT < 70)')

##### Top #######

files = nanoGetSampleFiles(mcDirectory, 'TTTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ST_s-channel') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_t-channel_top') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_antitop') + \
    nanoGetSampleFiles(mcDirectory, 'ST_tW_top') + \
    nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic')
#TTWjets is not generated, but TTZjets actually yes... neglecting for the moment
samples['top'] = {
    'name': files,
    'weight': mcCommonWeight,
    'FilesPerJob': 10,
    'EventsPerJob' : 70000,
    'suppressNegative' :['all'],
    'suppressNegativeNuisances' :['all'],
    
}

addSampleWeight(samples, 'top', 'TTTo2L2Nu', 'Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
addSampleWeight(samples,'top','ST_t-channel_top',  "100. / 32.4 ") # N.B We are using inclusive sample with leptonic-only XS
addSampleWeight(samples,'top','ST_t-channel_antitop',  "100. / 32.4")

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

############ other backgrounds ############
samples['other'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT100_200') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT200_400') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT400_600') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT600_800') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT800_1200') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT1200_2500') + \
            nanoGetSampleFiles(mcDirectory, 'WJetsToLNu_HT2500_inf') + \
            nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop') + \
            nanoGetSampleFiles(mcDirectory, 'GluGluWWTo2L2Nu_MCFM') + \
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
addSampleWeight(samples,'other','GluGluWWTo2L2Nu_MCFM',  "1.53/1.4")
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


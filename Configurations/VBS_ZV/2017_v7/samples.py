
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

fakeSteps = 'DATAl1loose2018v6__l2loose__fakeW'

dataSteps = 'DATAl1loose2017v7__l2loose__l2tightOR2017v7'

##############################################
###### Tree base directory for the site ######
##############################################

SITE=os.uname()[1]
if    'iihe' in SITE:
  treeBaseDir = '/pnfs/iihe/cms/store/user/xjanssen/HWW2015'
elif  'cern' in SITE:
  treeBaseDir = '/eos/cms/store/group/phys_higgs/cmshww/amassiro/HWWNano'

def makeMCDirectory(var=''):
    if var:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var='__' + var))
    else:
        return os.path.join(treeBaseDir, mcProduction, mcSteps.format(var=''))

mcDirectory = makeMCDirectory()
fakeDirectory = os.path.join(treeBaseDir, dataReco, fakeSteps)
dataDirectory = os.path.join(treeBaseDir, dataReco, dataSteps)


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
XSWeight   = 'XSWeight'

#SFweight      = 'SFweight'
#SFweight += '* PrefireWeight * PUJetIdSF * btagSF * BoostedWtagSF_nominal'

METFilter_MC   = 'METFilter_MC'

PromptGenLepMatch2l = 'PromptGenLepMatch2l'

mcCommonWeightNoMatch = 'XSWeight*SFweight*METFilter_MC'
mcCommonWeight = 'XSWeight*SFweight*PromptGenLepMatch2l*METFilter_MC'

#########################################
############# EFT SIGNALS ###################
########VBS aQGC - SMP-18-006 model: all signals givin aQGC with Z to 2L and V to 2J
# WpTo2J_ZTo2L_aQGC
# WmTo2J_ZTo2L_aQGC
# ZTo2L_ZTo2J_aQGC
#N.B. no processing campaign v6 is present for aQGC samples
########################################

#samples['VBS_ZV_aQGC'] = {
#    'name':   nanoGetSampleFiles(mcDirectorySig, 'ZTo2L_ZTo2J_aQGC')
#             +nanoGetSampleFiles(mcDirectorySig, 'WpTo2J_ZTo2L_aQGC')
#             +nanoGetSampleFiles(mcDirectorySig, 'WmTo2J_ZTo2L_aQGC'),
#    'weight':  XSWeight+'*'+SFweight+'*'+GenLepMatch+'*'+METFilter_MC ,
#    'FilesPerJob': 1
#}


###########################################
#############   SIGNALS  ##################
###########################################

#######VBS EW: only ZV processes

samples['VBS_ZV'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'ZTo2L_ZTo2J') 
             +nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L') 
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J')
             #+nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_ZTo2L'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 1
}


###########################################
#############  BACKGROUNDS  ###############
###########################################

########## irreducible VBS QCD 

samples['VBS_VV_QCD'] = {
    'name':   nanoGetSampleFiles(mcDirectory, 'WpToLNu_ZTo2J_QCD') 
             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WpTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpToLNu_WmTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_ZTo2L_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WpTo2J_WmToLNu_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_ZTo2J_QCD')
             +nanoGetSampleFiles(mcDirectory, 'WmToLNu_WmTo2J_QCD')
             #+nanoGetSampleFiles(mcDirectory, 'ZTo2L_ZTo2J_QCD')                <----BEWARE! THIS ONE NEEDS TO BE POST-PROCESSED 
             +nanoGetSampleFiles(mcDirectory, 'WmTo2J_ZTo2L_QCD'),
    'weight':  mcCommonWeight,
    'FilesPerJob': 1
}

########## DY #### consider using HT binned after Davide's studies.
#Beware! we have to correct the cross section here
###### DY #######


ptllDYW_NLO = '(((0.623108 + 0.0722934*gen_ptll - 0.00364918*gen_ptll*gen_ptll + 6.97227e-05*gen_ptll*gen_ptll*gen_ptll - 4.52903e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll<45)*(gen_ptll>0) + 1*(gen_ptll>=45))*(abs(gen_mll-90)<3) + (abs(gen_mll-90)>3))'
ptllDYW_LO = '((0.632927+0.0456956*gen_ptll-0.00154485*gen_ptll*gen_ptll+2.64397e-05*gen_ptll*gen_ptll*gen_ptll-2.19374e-07*gen_ptll*gen_ptll*gen_ptll*gen_ptll+6.99751e-10*gen_ptll*gen_ptll*gen_ptll*gen_ptll*gen_ptll)*(gen_ptll>0)*(gen_ptll<100)+(1.41713-0.00165342*gen_ptll)*(gen_ptll>=100)*(gen_ptll<300)+1*(gen_ptll>=300))'

useDYtt = False

if useDYtt:
    files = nanoGetSampleFiles(mcDirectory, 'DYJetsToTT_MuEle_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO')

    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + '*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0))',
        'FilesPerJob': 4,
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
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-50') + \
        nanoGetSampleFiles(mcDirectory, 'DYJetsToLL_M-10to50-LO_ext1') 


    samples['DY'] = {
        'name': files,
        'weight': mcCommonWeight + "*( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>15 && abs(PhotonGen_eta)<2.6) > 0 &&\
                                         Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )", ##DY_photons_filter 
        'FilesPerJob': 4,
        'EventsPerJob' : 70000,
        #  'suppressNegative' :['all'],
        #  'suppressNegativeNuisances' :['all'],
    }



    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50', '('+ptllDYW_NLO+')*(LHE_HT < 100)')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-10to50-LO_ext1', '('+ptllDYW_LO+')*(LHE_HT < 100)')
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-100to200_newpmx', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-200to400', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-400to600_newpmx', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-600to800', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-800to1200', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-1200to2500', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-50_HT-2500toInf', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-100to200_newpmx', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-200to400_newpmx', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-400to600', ptllDYW_LO)
    addSampleWeight(samples, 'DY', 'DYJetsToLL_M-4to50_HT-600toInf', ptllDYW_LO)


#Q: the ptllDYW_LO is needed in HT binned samples!?
#BEWARE! SOME CORRECTION IS NEEDED ON THE CROSS SECTION OF THESE SAMPLES

"""
DY_photons_filter = '( !(Sum$(PhotonGen_isPrompt==1 && PhotonGen_pt>10 && abs(PhotonGen_eta)<2.6) > 0 && Sum$(LeptonGen_isPrompt==1 && LeptonGen_pt>15)>=2) )'

samples['DY'] = {    'name'   :   nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50') 
                                  #+ nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-10to50-LO_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-100to200_newpmx') 
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400')
                                  #+ nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-200to400_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-400to600_newpmx') 
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-600to800')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-800to1200')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-1200to2500')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-50_HT-2500toInf')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-100to200_newpmx')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-200to400_newpmx')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-400to600')
                                  #+ nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-400to600_ext1')
                                  + nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-600toInf'),
                                  #+ nanoGetSampleFiles(mcDirectory,'DYJetsToLL_M-4to50_HT-600toInf_ext1') ,
                       'weight' :(XSWeight+'*'+SFweight+'*'+PromptGenLepMatch2l+'*'+METFilter_MC+"*"+DY_photons_filter),#.replace("PUJetIdSF", "1.") ,
                       'FilesPerJob' : 4,
                       'EventsPerJob' : 70000,
                      #  'suppressNegative' :['all'],
                      #  'suppressNegativeNuisances' :['all'],
                   }
                   
                   
#CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50', 'DYJetsToLL_M-50_ext1'])  
addSampleWeight(samples,'DY','DYJetsToLL_M-50','ptllDYW_LO')
#addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext1','DY_NLO_pTllrw')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1','ptllDYW_LO')

#CombineBaseW(samples, 'DY', ['DYJetsToLL_M-50_HT-200to400', 'DYJetsToLL_M-50_HT-200to400_ext1'])
#CombineBaseW(samples, 'DY', ['DYJetsToLL_M-4to50_HT-400to600', 'DYJetsToLL_M-4to50_HT-400to600_ext1'])
#CombineBaseW(samples, 'DY', ['DYJetsToLL_M-4to50_HT-600toInf', 'DYJetsToLL_M-4to50_HT-600toInf_ext1'])
addSampleWeight(samples,'DY','DYJetsToLL_M-50',                      '('+ptllDYW_NLO+')*(LHE_HT < 100)')
#addSampleWeight(samples,'DY','DYJetsToLL_M-50_ext1',                 '(LHE_HT < 100)')
addSampleWeight(samples,'DY','DYJetsToLL_M-10to50-LO_ext1',               '('+ptllDYW_NLO+')*(LHE_HT < 100)')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-100to200_newpmx',          'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400',          'ptllDYW_LO')
#ddSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-200to400_ext1',     'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-400to600_newpmx',     'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-600to800',          'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-800to1200',         'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-1200to2500',        'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-50_HT-2500toInf',         'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-100to200_newpmx',       'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-200to400_newpmx',       'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600',       'ptllDYW_LO')
#addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-400to600_ext1',  'ptllDYW_LO')
addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf',       'ptllDYW_LO')
#addSampleWeight(samples,'DY','DYJetsToLL_M-4to50_HT-600toInf_ext1',  'ptllDYW_LO')

"""
#NB the weight ptllDYW_LO needs to be updated with DY_LO_pTllrw available in https://github.com/latinos/PlotsConfigurations/blob/master/Configurations/patches/DYrew30.py
#and https://github.com/UniMiBAnalyses/PlotsConfigurations/blob/master/Configurations/VBSWWOS/Full2016_v6/FitDir/samples.py#L160
###### Top #######

samples['top'] = {    'name'   :   nanoGetSampleFiles(mcDirectory,'TTTo2L2Nu') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_s-channel') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_antitop') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_t-channel_top') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_antitop') 
                                 + nanoGetSampleFiles(mcDirectory,'ST_tW_top') 
                                 + nanoGetSampleFiles(mcDirectory,'TTToSemiLeptonic') 
                                 + nanoGetSampleFiles(mcDirectory,'TTZjets')
#                                 + nanoGetSampleFiles(mcDirectory,'TTZjets_ext1')
                                 + nanoGetSampleFiles(mcDirectory,'TTWjets'),
#                                 + nanoGetSampleFiles(mcDirectory,'TTWjets_ext1'),
                     'weight' : mcCommonWeight ,
                     'FilesPerJob' : 5,
                     'EventsPerJob' : 70000,
#                     'suppressNegative' :['all'],
#                     'suppressNegativeNuisances' :['all'],
                 }

#CombineBaseW(samples, 'top', ['TTZjets', 'TTZjets_ext1'])
#CombineBaseW(samples, 'top', ['TTWjets', 'TTWjets_ext1'])

addSampleWeight(samples,'top','TTTo2L2Nu','Top_pTrw')
addSampleWeight(samples,'top','TTToSemiLeptonic','Top_pTrw')
#addSampleWeight(samples,'top','TTZjets','Top_pTrw')
#addSampleWeight(samples,'top','TTWjets','Top_pTrw')
#addSampleWeight(samples,'top','TTZjets_ext1','Top_pTrw')
#addSampleWeight(samples,'top','TTWjets_ext1','Top_pTrw')

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
    'FilesPerJob': 2
}

###### WW ########

samples['WW'] = {
    'name': nanoGetSampleFiles(mcDirectory, 'WpWmJJ_QCD_noTop'),
    'weight': mcCommonWeight, #+ '*nllW',
    'FilesPerJob': 3
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
    'FilesPerJob': 2
}
######## Vg ########
"""
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
"""
############ VZ ############

files = nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Nu') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo2L2Q') + \
    nanoGetSampleFiles(mcDirectory, 'ZZTo4L') + \
    nanoGetSampleFiles(mcDirectory, 'WZTo2L2Q')

samples['VZ'] = {
    'name': files,
    'weight': mcCommonWeight + '*1.11',
    'FilesPerJob': 2
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
    'FilesPerJob': 2
}

###########################################
################## FAKE ###################
###########################################
"""
samples['Fake'] = {
  'name': [],
  'weight': 'METFilter_DATA*fakeW',
  'weights': [],
  'isData': ['all'],
  'FilesPerJob': 80
}

for _, sd in DataRun:
  for pd in DataSets:
    files = nanoGetSampleFiles(fakeDirectory, pd + '_' + sd)
    samples['Fake']['name'].extend(files)
    samples['Fake']['weights'].extend([DataTrig[pd]] * len(files))

samples['Fake']['subsamples'] = {
  'em': 'abs(Lepton_pdgId[0]) == 11',
  'me': 'abs(Lepton_pdgId[0]) == 13'
}
"""
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


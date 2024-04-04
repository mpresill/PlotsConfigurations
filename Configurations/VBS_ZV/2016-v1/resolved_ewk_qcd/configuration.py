# example of configuration file
treeName= 'Events'


date='_16Mar2024_2016_ewk_qcd'

categ = 'resolved'
#operator = 'T0' #uncomment for EFT launching process.


#tag = 'VBS_ZV'+date             #after adding
tag = 'VBS_ZV'+date+'_'+categ


# used by mkShape to define output directory for root files
#outputDir = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile'+date #+tag
outputDir = '/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile'+date #+tag
#outputDir = date #+tag

# file with TTree aliases
aliasesFile = '../aliases.py'

# file with list of variables
variablesFile = '../variables.py'
#variablesFile = '../variables_njet.py'

# file with list of cuts
cutsFile = 'cuts_'+categ+'.py'  #when launching
#cutsFile = 'cuts.py'           #after adding the categories

# file with list of samples
samplesFile = '../samples_ewk_qcd.py'


# file with list of samples
plotFile = '../plot.py'
#plotFile = 'plot_test.py'


# luminosity to normalize to (in 1/fb)
lumi = 35.87

# used by mkPlot to define output directory for plots
# different from "outputDir" to do things more tidy
outputDirPlots = '/eos/user/m/mpresill/www/VBS/2016_v7/Plots'+date


# used by mkDatacards to define output directory for datacards: common vbs-italia github folder : /afs/cern.ch/work/m/mpresill/Combine_limits/CMSSW_10_2_13/src/HiggsAnalysis/CombinedLimit/VBS/2017_v7/
outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards'+date
#outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/Datacards'+date+'_c'+operator
#outputDirDatacard = '/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/VBScomb_Datacards'+date    

# structure file for datacard
structureFile = '../structure_ewk_qcd.py'

# nuisances file for mkDatacards and for mkShape
nuisancesFile = '../nuisances_ewk_qcd.py'
#nuisancesFile = '../2016_v7_Jan22/nuisances_StatOnly.py'


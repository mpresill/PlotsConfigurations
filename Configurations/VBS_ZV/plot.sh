#! /bin/bash
DATE=16Mar2024_2018_ewk_qcd-v2 #change date 
category=resolved #_QCDscaleDY_corr
#eosPATH=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/
#eosPATH=/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/

estetica='--minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --logOnly' #--plotNormalizedDistributions
inputFile=/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd-v2/plots_VBS_ZV_16Mar2024_2018_ewk_qcd-v2_resolved.root
#/eos/cms/store/group/phys_smp/VJets_NLO_VBSanalyses/ZV_analysis/histograms/rootFile_16Mar2024_2018_ewk_qcd/corrections/plots_VBS_ZV_16Mar2024_2018_ewk_qcd_resolved_wBkg.root
outputFolder=/eos/user/m/mpresill/www/VBS/2018_v7/PlotsVBS_ZV_${DATE}_${category}/


cd 2018-v1/resolved_ewk_qcd
mkPlot.py --pycfg=configuration.py --inputFile=${inputFile} --outputDirPlots=${outputFolder} ${estetica} 

cp /eos/user/m/mpresill/www/VBS/2018_v7/index.php ${outputFolder}
cp -r *.py ${outputFolder}

cd ../..

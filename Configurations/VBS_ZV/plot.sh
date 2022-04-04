#! /bin/bash
VERS=2016_Feb22 #2017_sep21
DATE=29Mar2022_2016 #change date 
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch  #espresso #longlunch #--dry-run

##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files
cd ${VERS}

#mkPlot.py --pycfg=configuration.py --inputFile=/eos/home-a/ahakimi/www/ZV_analysis/rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --onlyPlot=cratio --logOnly --plotFile=plot_res.py --cutsFile=cuts_res.py #--fileFormats=png,eps
mkPlot.py --pycfg=configuration.py --inputFile=/eos/home-a/ahakimi/www/ZV_analysis/rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --onlyPlot=cratio --logOnly --plotFile=plot.py --cutsFile=cuts.py #--fileFormats=png,eps
#--showNormalizedDistributions
#mkPlot.py --pycfg=configuration.py --inputFile=/eos/home-a/ahakimi/www/ZV_analysis/rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --onlyPlot=cratio --logOnly --plotFile=plot.py --cutsFile=cuts.py #--fileFormats=png,eps

#cp *.py /eos/home-a/ahakimi/www/ZV_analysis/Plots_${DATE}_test/
#cp /eos/home-a/ahakimi/www/ZV_analysis/index.php /eos/home-a/ahakimi/www/ZV_analysis/Plots_${DATE}_test/
#rm -rf /eos/user/m/mpresill/www/VBS/2018_v7/PlotsVBS_ZV_${DATE}*root

cd ..
#to resubmit jobs:
#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

#to make datacard:
#mkDatacards.py --pycfg configuration.py --inputFile rootFile_${DATE}/plots_VBS_ZV_${DATE}.root

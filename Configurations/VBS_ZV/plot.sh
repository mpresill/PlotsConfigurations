#! /bin/bash
DATE=18Feb2021_2016_btag #change date 
#mkShapesMulti.py --pycfg=configuration.py --batchSplit=Samples,Files

#mkShapesMulti.py --pycfg=configuration.py --doBatch=1 --batchSplit=Samples,Files --batchQueue=longlunch  #espresso #longlunch #--dry-run

##mkShapesMulti.py --pycfg=configuration.py --doHadd=1 --batchSplit=Samples,Files --doNotCleanup --nThreads=10 #to hadd files
cd 2016_v7_Jan21

mkPlot.py --pycfg=configuration.py --inputFile=rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 #--plotNormalizedDistributions #--fileFormats=png,eps
#--showNormalizedDistributions

#mkPlot.py --pycfg=configuration.py --inputFile=rootFile_28Jan2021_2016_nobtag.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --plotNormalizedDistributions #--fileFormats=png,eps

#mkPlot.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/www/VBS/2016_v7_Jan21/rootFile_${DATE}/plots_VBS_ZV_${DATE}.root --minLogC=0.01 --minLogCratio=0.01 --maxLogC=10000 --maxLogCratio=10000  --showIntegralLegend=1 --plotNormalizedDistributions #--fileFormats=png,eps
#--showNormalizedDistributions


cp /eos/user/m/mpresill/www/VBS/2016_v7/index.php /eos/user/m/mpresill/www/VBS/2016_v7/PlotsVBS_ZV_${DATE}/.
#rm -rf /eos/user/m/mpresill/www/VBS/2016_v7_Jan21/PlotsVBS_ZV_${DATE}*root
#rm -rf /eos/user/m/mpresill/www/VBS/2016_v7_Jan21/PlotsVBS_ZV_${DATE}/*SR*   #blind SR!
cp -r *.py /eos/user/m/mpresill/www/VBS/2016_v7/PlotsVBS_ZV_${DATE}/.


cd ..
#to resubmit jobs:
#for i in *jid; do sed -i "s/longlunch/microcentury/g" ${i/jid/jds}; condor_submit ${i/jid/jds}; done

#to make datacard:
#mkDatacards.py --pycfg configuration.py --inputFile rootFile_${DATE}/plots_VBS_ZV_${DATE}.root

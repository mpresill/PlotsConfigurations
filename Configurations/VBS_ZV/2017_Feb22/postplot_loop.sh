#!/bin/bash
folder=2017_Feb22
date=01Mar2022_2017
FITVAR=DNNoutput_pruned_bReq
CUT=Boosted_DYcr_bTag
CAT=Boosted
PLOTFILE=plot_boost.py
DATACARD_NAME=Datacards_${date}/${CUT}/${PLOTVAR}/datacard_${CAT}

rm -rf Workspace/${CUT}
mkdir -p Workspace
mkdir Workspace/${CUT}
cardName=${CUT}
for PLOTVAR in VBS_jet_pt1 VBS_jet_pt2 V_jet_pt1 V_jet_pt2 Zleppt DYfit_Z_bin_Boosted detajj_mjjmax mjj_max VBS_jet_qgl1_morphed VBS_jet_qgl2_morphed V_jet_qgl1_morphed V_jet_qgl2_morphed DNNoutput_full_bVeto DNNoutput_pruned_bVeto DYfit_2D_bin_Resolved DYfit_Z_bin_Boosted DNNoutput_pruned_bReq
do
	echo "plotting ${PLOTVAR}"
	DATACARD_NAME=Datacards_${date}/${CUT}/${PLOTVAR}/datacard
	cardNameWorkspace=Workspace/${CUT}/${PLOTVAR}
	outputFolder=Workspace/${CUT}

	text2workspace.py ${DATACARD_NAME}.txt -o ${cardNameWorkspace}.root

	PostFitShapesFromWorkspace \
    	-w ${cardNameWorkspace}.root \
    	-d ${DATACARD_NAME}.txt \
    	-o output_${PLOTVAR}.root \
    	--postfit --sampling \
    	-f fit/${CAT}/${FITVAR}/fitDiagnostics.root:fit_s \
    	--total-shapes


	mkPostFitCombinedPlot.py \
    	--inputFilePostFitShapesFromWorkspace output_${PLOTVAR}.root \
    	--outputFile postfit.root \
    	--kind P \
    	--cutName ${CUT} \
    	--variable ${PLOTVAR} \
    	--structureFile structure.py \
    	--plotFile ${PLOTFILE} \
    	--lumiText '41.53/fb' \
   
    

	mkPlot.py --pycfg=configuration_combined.py --inputFile postfit.root --onlyPlot=cratio --logOnly --showIntegralLegend=1 --minLogCratio=0.01 --maxLogCratio=10000

done
rm -r postfit_${CUT}_${FITVAR}fit
mv plot_combined postfit_${CUT}_${FITVAR}fit

python $CMSSW_BASE/src/HiggsAnalysis/CombinedLimit/test/diffNuisances.py --all --abs --format html fit/${CAT}/${FITVAR}/fitDiagnostics.root > postfit_${CUT}_${FITVAR}fit/fit.html
cp ../index.php postfit_${CUT}_${FITVAR}fit
cp -r postfit_${CUT}_${FITVAR}fit /eos/home-a/ahakimi/www/ZV_analysis/Plots_${date}



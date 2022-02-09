t
date=31Mar2021_2018bintest
DATACARD_NAME=combined_card_all
VAR=Zleppt

cd ${folder}

#echo "RUNNING WITH TOP CR FIT"
rm -rf Fit/${DATACARD_NAME}
mkdir -p Fit
mkdir Fit/${DATACARD_NAME}
cardName=${DATACARD_NAME}
cardNameWorkspace=Fit/${DATACARD_NAME}
outputFolder=Fit/${DATACARD_NAME}



text2workspace.py Datacards_${date}/${cardName}.txt -o ${cardNameWorkspace}.root
mkdir fitDiagnosticsCombined

combine -M FitDiagnostics ${cardNameWorkspace}.root --out fitDiagnosticsCombined

cd Datacards_${date}
PostFitShapesFromWorkspace \
    -w ../${cardNameWorkspace}.root \
    -d ${DATACARD_NAME}.txt \
    -o ../output_histograms.root \
    --postfit --sampling \
    -f ../fitDiagnosticsCombined/fitDiagnostics.root:fit_s \
    --total-shapes
cd .. 

#kind P = postfit, p=prefit 
mkPostFitCombinedPlot.py \
    --inputFilePostFitShapesFromWorkspace output_histograms.root \
    --outputFile postfit.root \
    --kind P \
    --cutName combined \
    --variable ${VAR} \
    --structureFile structure.py \
    --plotFile plot.py \
    --lumiText '59.74/fb'

mkPlot.py --pycfg=configuration_combined.py --inputFile postfit.root --onlyPlot=cratio --linearOnly --showIntegralLegend=1


cd ..

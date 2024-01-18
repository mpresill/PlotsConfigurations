# List of changes wrt older configs
# LIST OF UPDATES WRT TO CONFIG 2018_may23:

> This is the release started on 21 august 2023 - when unblinding procedure was starting.


## LIST OF UPDATES WRT TO CONFIG 2018-v0:
- minor backgrounds are gathered in the datacards
- PS weights for DY, Vg, VgS, top are computed with the old method 
    - we added PS_DY and PS_top nuisances computed with the latinos method to cross-check the validity of their extrapolation for these backgrounds
    [x] add link here to validation plots: https://mpresill.web.cern.ch/mpresill/VBS/nuisances/PS_ISR_comparison/6Dec2023_2018/?match=latinos  https://mpresill.web.cern.ch/mpresill/VBS/nuisances/PS_FSR_comparison/6Dec2023_2018/?match=latinos 
    Afterall the extraction method from latinos group seems to interpolate well up and down fluctuations, with the pro of being less subject to statistical fluctuations. We could use those ones and simply rename `PS_ISR_latinos`->`PS_ISR`, `PS_FSR_latinos`->`PS_FSR` in the datacards.
    [x] add here link to validate "other" PS unceratainties: https://mpresill.web.cern.ch/mpresill/VBS/nuisances/PS_ISR/6Dec2023_2018/ https://mpresill.web.cern.ch/mpresill/VBS/nuisances/PS_FSR/6Dec2023_2018/ : some fluctuations, but overall OK!
    [x] add here link to validate "other" QCDscale uncertainties: https://mpresill.web.cern.ch/mpresill/VBS/nuisances/QCDscale/6Dec2023_2018/ OK!
- JES/JER are not log normal anymore (and they are included for all processes)
- b-tagging nuisances are shape


__________________________________________________
# list of commands to make it work:
1. run mkShape, get to end, and hadd
2. backup the file produced
```sh
cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted_copy.root

cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved_copy.root
```
Corrected samples will be stored at this path (if does not exists, mkdir): `/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections`

3. a. (ONLY ONCE) 
    extract PS weights 
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/PS-plots_VBS_ZV_6Dec2023_2018_resolved.root -sf samples_PS_extraction.txt -cf cuts_PS_extraction.txt -v ALL -n PS_ISR PS_FSR
```
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/PS-plots_VBS_ZV_6Dec2023_2018_boosted.root -sf samples_PS_extraction.txt -cf cuts_PS_extraction.txt -v ALL -n PS_ISR PS_FSR
```
    extract QCDscale_VBS_VV_QCD
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/QCDscale-plots_VBS_ZV_6Dec2023_2018_resolved.root -s VBS_VV_QCD -cf cuts_PS_extraction.txt -v ALL -n QCDscale_VBS_VV_QCD
```
```sh
python ../../scripts/Utilities_nuisances/extract_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/QCDscale-plots_VBS_ZV_6Dec2023_2018_boosted.root -s VBS_VV_QCD -cf cuts_PS_extraction.txt -v ALL -n QCDscale_VBS_VV_QCD
```

3. b. patch for QCD scale DY process:
```sh
sh QCDnorm_datacards.sh _6Dec2023_2018 resolved 2018-v1
sh QCDnorm_datacards.sh _6Dec2023_2018 boosted 2018-v1
```


4. make datacards (N.B.: use `nuisances_datacards.py` as input since I realized that when there are two nuisances entries with same name, the combineCards.py keeps only one of the two, i.e. in the case of `nuisances.py` would suppress all nuisances for backgrougs in JES, etc etc):
```sh
###without QCD corrections
cd 2018-v1/resolved/
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_resolved.root --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py 
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/plots_VBS_ZV_6Dec2023_2018_boosted.root --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
###with QCD corrections
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/plots_VBS_ZV_6Dec2023_2018_resolved.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2018_QCDscaleDY_corr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py 
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/plots_VBS_ZV_6Dec2023_2018_boosted.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2018_QCDscaleDY_corr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
###with QCD corrections and DY ln (for this need to update nuisances.py before)
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/plots_VBS_ZV_6Dec2023_2018_resolved.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2018_QCDscaleDY_corr_ln/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py 
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2018/corrections/plots_VBS_ZV_6Dec2023_2018_boosted.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2018_QCDscaleDY_corr_ln/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
```

5. do the statistical analysis (check combine2018 or combineRun2 folder)

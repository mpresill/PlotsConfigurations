# List of changes wrt older configs
## LIST OF UPDATES WRT TO CONFIG 2017_may23:

> This is the release started on 22 August 23 - when unblinding was proposed.
> Changes wrt may23 release:
    > removed PS nuisances modeling and tried to use the standard weights
    > eventually will extrapolate it from 2017 for buggy samples

## LIST OF UPDATES WRT TO CONFIG 2017-v0:
- minor backgrounds are gathered in the datacards
- PS weights for DY, Vg, VgS, top are computed with the old method (latinos way)
- JES/JER are not log normal anymore (and they are included for all processes)
- b-tagging nuisances are shape


__________________________________________________
# list of commands to make it work (SM EWK):
1. run mkShape, get to end, and hadd
2. backup the file produced
```sh
cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_boosted.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_boosted_copy.root

cp /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_resolved.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_resolved_copy.root
```
Corrected samples will be stored at this path (if does not exists, mkdir): `/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections`

4. patch for PS weights: 
(N.b. ho dovuto togliere i fondi migliori per l'estrapolazione perché "other" non è ancora definito mentre scrivo nel 2018)
```sh
python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_resolved.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_PSvar.root --nuisance-effect ../../2018-v1/resolved/PS-plots_VBS_ZV_6Dec2023_2018_resolved.root -sf ../../2018-v1/resolved/samples_PS_extraction.txt -n PS_FSR PS_ISR

python ../../scripts/Utilities_nuisances/apply_nuisances_effect.py -i /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_boosted.root -o /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_PSvar.root --nuisance-effect ../../2018-v1/boosted/PS-plots_VBS_ZV_6Dec2023_2018_boosted.root -sf ../../2018-v1/boosted/samples_PS_extraction.txt -n PS_FSR PS_ISR
```
and uncomment the corresponding nuisance from `nuisances.py` so can be included in the datacard

5. patch for QCD scale DY process
```sh
sh QCDnorm_datacards.sh _6Dec2023_2017 resolved 2017-v1
sh QCDnorm_datacards.sh _6Dec2023_2017 boosted 2017-v1
```

6. hadd files with the corrected ones

a.  WITH QCD scale DY corrections
```sh
hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS_QCDscaleDY_corr.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved.root 

hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS_QCDscaleDY_corr.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted.root 
```
b.  WITHOUT QCD scale DY corrections
```sh
hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_resolved.root 

hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_PSvar.root \
/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/plots_VBS_ZV_6Dec2023_2017_boosted.root 
```



7. make datacards(N.B.: use `nuisances_datacards.py` as input since I realized that when there are two nuisances entries with same name, the combineCards.py keeps only one of the two, i.e. in the case of `nuisances.py` would suppress all nuisances for backgrougs in JES, etc etc):
```sh
###without QCD corrections
cd 2017-v1/resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
###with QCD corrections
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py 
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
###with QCD corrections and DY ln (for this need to update nuisances.py before)
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr_ln/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py 
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr_ln/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards.py
```

To avoid unpleasant statistical fluctuations for nuisances of minor backgrouds in top cr (since those crs are very very pure), I am removing all nuisances from minor backgrouds in datacards for top cr. To try this out, please run again `mkDatacards.py` as follows (for the case of QCD corr+ln DY for instance)
```sh
cd ../resolved
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr_ln_topcr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_topcr.py --cutsFile=cuts_resolved_topcr.py 
cd ../boosted
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr_ln_topcr/ --skipMissingNuisance --nuisancesFile=../nuisances_datacards_topcr.py --cutsFile=cuts_boosted_topcr.py
```



__________________________________________________
# list of commands to make it work (EFT):
1. complete the list above for the SM EWK measurement and be sure to have the correct `variables.py` for both EWk and EFT processing
2. hadd EFT outputs, and the manually hadd EFT and EWK outputs:
```sh
hadd /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017-dim8/plots_VBS_ZV_6Dec2023_2017-dim8_boosted_wBkg.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017-dim8/plots_VBS_ZV_6Dec2023_2017-dim8_boosted.root /eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS_QCDscaleDY_corr.root
```
In the example I merged the boosted dim-8 signals root file with the QCDscaleDY corrected smaples.
3. prepare datacards (picking up the desired EFT signals in the `structure-dim8.py` and in the `samples_boosted-dim8.py`) and using the `nuisances_datacards-dim8.py`:
```sh
cd 2017-v1/boosted-dim8
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017-dim8/plots_VBS_ZV_6Dec2023_2017-dim8_boosted_wBkg.root --skipMissingNuisance --nuisancesFile=../nuisances_datacards-dim8.py --samplesFile=samples-datacards-dim8.py
```
You need to prepare one set of datacards per EFT operator, modifying samples, structure and configuration every time.

4. use the `EFT/datacards_categories_2017_EFT.sh` macro to combine categories (here for the single-here example)
5. launch the `EFT/eft.sh` script as follows:
```sh
sh eft.sh /eos/user/m/mpresill/CMS/VBS/VBS_ZV/DatacardsEFT/YearsCombination_8June2022/combined_boosted_bVeto.txt cT1 boosted_bVeto 
```
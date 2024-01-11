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
# list of commands to make it work:
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



7. make datacards:
```sh
###without QCD corrections
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017/ --skipMissingNuisance 
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017/ --skipMissingNuisance
###with QCD corrections
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr/ --skipMissingNuisance 
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr/ --skipMissingNuisance
###with QCD corrections and DY ln (for this need to update nuisances.py before)
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_resolved_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr_ln/ --skipMissingNuisance 
mkDatacards.py --pycfg=configuration.py --inputFile=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/histograms/rootFile_6Dec2023_2017/corrections/plots_VBS_ZV_6Dec2023_2017_boosted_wPS_QCDscaleDY_corr.root  --outputDirDatacard=/eos/user/m/mpresill/CMS/VBS/VBS_ZV/Datacards/Datacards_6Dec2023_2017_QCDscaleDY_corr_ln/ --skipMissingNuisance
```